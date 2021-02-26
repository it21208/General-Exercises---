from datetime import datetime, timedelta

from airflow import DAG
from airflow.hooks.mysql_hook import MySqlHook
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

    default_args = {
    'owner': 'airflow',
    'depend_on_past': False,
    'start_date': datetime(2020, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

# Read the table sources to fetch the data and return the name of
# first source having its column "activated" sets to true.
# No need to call xcom_push here since we use the keyword "return"
# which has the same effect.
def get_activated_sources(**kwargs):
    ti = kwargs['ti'] # kwargs is a dictionary so we use a specific key to get a certain value. 
    request = "SELECT * FROM sources"
    mysql_hook = MySqlHook(mysql_conn_id="mysql", schema="airflow_mdb")
    connection = mysql_hook.get_conn()
    cursor = connection.cursor()
    cursor.execute(request)
    sources = cursor.fetchall()
    for source in sources:
        if source[1]:
            ti.xcom_push(key='activated_source', value=source[0])
            # return source[0]
            return None
        
    return None

def source_to_use(**kwargs):
    '''  **kwargs special argument to pass any number of keyword arguments
         basically a dictionary where you can find different information about
         the current DAG as well the running TaskInstance xxcom_task .
    '''
    ti = kwargs['ti']
    source = ti.xcom_pull(task_ids='hook_task')
    print("source fetch from XCOM: {}".format(source))

with DAG('xcom_dag', default_args=default_args, schedule_interval='@once', catchup=False) as dag:
    start_task = DummyOperator(task_id='start_task')
    hook_task = PythonOperator(task_id='hook_task', python_callable=get_activated_sources,
                               provide_context=True)
    xcom_task = PythonOperator(task_id='xcom_task', python_callable=source_to_use, provide_context=True)
    start_task >> hook_task >> xcom_task
    

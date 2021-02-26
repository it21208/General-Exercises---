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

def get_activated_sources():
    ''' Hooks are nothing more than objects allowing you to interact with external tools. '''
    request = "SELECT * FROM sources"
    # This connection must be set from the Connection view in Airflow UI.
    mysql_hook = MySqlHook(mysql_conn_id="mysql", schema="airflow_mdb")
    connection = mysql_hook.get_conn() # Gets the connection from MySqlHook.
    cursor = connection.cursor()       # Gets a cursor.
    cursor.execute(request)            # Executes the request.
    sources = cursor.fetchall()        # Fetches all the data from the executed request.
    for source in sources:
        ''' Does a simple print of each source to show that the hook works well. '''
        print("Source: {0} - activated: {1}".format(sourcep[0], source[1]))
    return sources

with DAG('hook_dag', default_args=default_args, schedule_interval='@once', catchup=False) as dag:
    start_task = DummyOperator(task_id='start_task')
    hook_task = PythonOperator(task_id='hook_task', python_callable=get_activated_sources)
    start_task >> hook_task

# the contents of the table Sources
# from the terminal run the following:
''' $> mysql -u airflow -P 3306 -pairflow -D airflow_mdb '''
''' mysql> select * from sources; '''

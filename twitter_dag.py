from airflow import DAG
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.hive_operator import HiveOperator
from datetime import datetime

import fetching_tweet
import cleaning_tweet

default_args = {
    "start_date": datetime(2020, 1, 1),
    "owner": "airflow"
}


with DAG(dag_id="twitter_dag", schedule_interval="@daily", default_args=default_args, catchup=False) as dag:
    
    # checking if tweets are available - FileSensor
    waiting_for_tweets = FileSensor(task_id="waiting_for_tweets", fs_conn_id="fs_tweet", filepath="data.csv", poke_interval=5)
    
    # fetching tweets
    fetching_tweets = PythonOperator(task_id="fetching_tweets", python_callable=fetching_tweet.main)
    
    # cleaning tweets
    cleaning_tweets = PythonOperator(task_id="cleaning_tweets", python_callable=cleaning_tweet.main)
    
    # storing tweets into hdfs
    storing_tweets = BashOperator(task_id="storing_tweets", bash_command="hadoop fs -put -f /tmp/data_cleaned.csv /tmp/")
    
    # load tweets into a hive table -> hive data warehouse tool
    loading_tweets = HiveOperator(task_id="loading_tweets", hql="LOAD DATA INPATH '/tmp/data_cleaned.csv' INTO TABLE tweets")
    # in the terminal enter hive to start hive
    # show tables;
    # we should see the empty table tweets
    
    # notice how we add the dependencies betwees tasks
    # t4 << t3 ( = t4.set_upstream(t3) )
    # t1 >> t2 ( = t1.set_downstream(t2) )
    waiting_for_tweets >>  fetching_tweets >> cleaning_tweets >> storing_tweets >> loading_tweets
    
    
# to test it run in the following in a python .sandbox environment
# $  airflow test twitter_dag storing_tweets 2020-01-01

# to test the loading of tweets we enter the following command
# $  airflow test twitter_dag loading_tweets 2020-01-01
   
# after setting the dependencies these should reflect on the graph view of the twitter_dag
   
# verify if the file has been uploaded 
# $ hadoop fs -ls /tmp
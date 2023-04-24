import os


"""
executes hive Query
"""

"""Usage
#Create an Internal Table
table_query = ""CREATE DATABASE IF NOT EXISTS {database_name};
            CREATE TABLE IF NOT EXISTS {database_name}.{table_name} (
              year int,make String ,model String) 
              ROW FORMAT DELIMITED 
              FIELDS TERMINATED BY ','
              LINES TERMINATED BY '\n'
              STORED AS TEXTFILE;
              "".format(**locals())

database_name="test_db"
table_name="car_table"

execute_hive_query(table_name)
"""

def execute_hive_query(query):
    command = "hive -e \"{0}\"".format(query)
    return_code = os.system(command)
    return return_code














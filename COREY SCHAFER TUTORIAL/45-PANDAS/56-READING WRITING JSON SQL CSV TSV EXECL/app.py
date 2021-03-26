import mysql.connector
from mysql import connector
import pandas as pd
from sqlalchemy import create_engine
import mysql
# Connecting from the server
# conn = mysql.connector.connect(user='root',
#                                host='localhost',
#                                passwd = 'password',
#                                database='giraffe')
# conn=create_engine('mysql://root:password@localhost/giraffe')
conn = create_engine('mysql+mysqlconnector://root:password@localhost/giraffe')  ##this works for mysql
# conn = create_engine('sqlite:///giraffe.db')
print(conn)
df=pd.read_sql_query('show tables from giraffe',conn)
print(df)
# Disconnecting from the server
# conn.close()
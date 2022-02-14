'''
Module Description: ingest data from SQL then created dataframe through tuples.
File Name:createjsoninfo.py
Created by:Dhivyakrishnaraj
created Date:02/13/2022
'''

#Create a function list of tuples, tuples should be paired in a list.Take the list in the for loop and print it in the form of (Parent1/Child1 to 5 pair.)


#[(p1,c1),(p2,c2)]
def pc():
    v = [('p1','c1'),('p2','c2'),('p3','c3'),('p4','c4'),('p5','c5')]
    for i in v:
        print(i[0])

pc()

#list the file from the folder and create the list of files in a variable.

import os
import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import psycopg2.extras as extras
my_list = os.listdir('C:\Dhivya\Project-1_File_Status\Data') 
x = map(lambda a: (a[4],'testmsg',a,a[4],'N',a.split('.')[0][-3:]),  my_list)
#x = lambda a: (1,a)

#Create dataframe with list of tuples
v = list(x)
print(v)
df  = pd.DataFrame(v)
print(df)

conn = psycopg2.connect("dbname=suppliers user=postgres password=0321")
#db = create_engine(conn)
#conn1 = db.connect()


# load data from dataframe directly into database.
#df.to_sql('dhivya.ingest_status',con=conn,if_exists='append', index = False)
cursor = conn.cursor()
table = 'dhivya.ingest_stats'
cols = 'batch_id,service_msg,filename,seq_no,is_processed,ingest_batch_id'
query = "INSERT INTO %s(%s) VALUES %%s" % (table,cols)

#sql1 = 'select * From dhivya.ingest_stats;'
extras.execute_values(cursor,query,v)
conn.commit()
#print(cursor.fetchone()[0])
conn.close()


# read from database table and create dataframe

#with help of tuples create dataframe modification
#dataframe transformation and actions(filter, null)


    
data = [('peter',18,7),('riff',15,6),('john',17,8),('michel',18,7),('sheli',17,5)]
df = pd.DataFrame(data,columns = ['Name','Age','Score'])
df['Country']=[('Europe'),('Asia'),('France'),('Sweden'),('Italy')]

print(df)












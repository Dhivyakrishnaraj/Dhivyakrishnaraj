#get table info from database table and create a list of  tuples.

import os
import psycopg2
import pandas as pd
import json
import glob
#select batch_id,service_msg,filename,seq_no,is_processed from ingest_status
conn = psycopg2.connect("dbname=suppliers user=postgres password=0321")
cursor = conn.cursor()
cursor.execute("select batch_id,service_msg,filename,seq_no,is_processed from dhivya.ingest_stats")
s = (cursor.fetchall())   
cursor.close()
conn.close()

try:
    temp = pd.DataFrame()
    array_json = []
    
    for items in s:
        filename = items[2]
        print(filename)
        path = "C:\\Dhivya\\Project-1_File_Status\\Data\\"+filename
        f = open(path)
        v_json = json.load(f)             
        array_json.append(v_json)
        #temp = pd.DataFrame.from_dict(v_json, orient = 'index')
        #temp = temp.transpose()
        f.close()
    
        '''v_json["Seq_no"] = filename[4]
        g = open(path,'w')
        json.dump(v_json,g,indent = 6)
        g.close()
        print(g)
        
    json_pattern = os.path.join("C:\\Dhivya\\Project-1_File_Status\\Data\\",'*.json.*')
    file_list = glob.glob(json_pattern)
    dfs = []
    
        for v_json in file_list:
        print(v_json)
        df = pd.read_json(v_json)
        dfs.append(df, ignore_index = True)'''
              
        
    print(array_json)
    df = pd.DataFrame(array_json)
    print(df)
    c = df.explode('children')
    print(c)
    t =df.join(pd.DataFrame(df.explode('children').to_dict()).T)
    
    print(t)
    
    
    
    
except Exception as e:
    raise(e)





        
        
    


           

           
           



    

import pyodbc
import streamlit as st

server = 'techitoutserver.database.windows.net'
database = 'techitoutdb'
username = 'techitoutadmin'
password = '{Cloudmoyo@123}'
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("select tab.name as TabName,col.name,t.name as data_type from sys.tables as tab inner join sys.columns as col on tab.object_id = col.object_id left join sys.types as t on col.user_type_id = t.user_type_id")
        row = cursor.fetchone()
        while row:
            #print (row)
            st.write(row)
            row = cursor.fetchone()

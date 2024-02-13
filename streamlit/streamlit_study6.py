import streamlit as st
import os
from dotenv import load_dotenv


load_dotenv(override=True)
host = os.getenv('HOST')
database = os.getenv('DB_NAME')
port = os.getenv('PORT')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
    
conn=st.connection('mysql', type='sql', dialect='mysql', host=host, port=port
                   , username=username, password=password, database=database)

df=conn.query('SELECT * FROM customer LIMIT 10')

st.header("Database connection")
st.write('SELECT * FROM customer LIMIT 10 의 결과입니다.')
for row in df.itertuples():
    st.write(f".{row.last_name}'s email is {row.email}")
#! /bin/python3

#! pip install langchain langchain-experimental openai
#!pip install sqlalchemy==2.0.23 ipython-sql
#!pip install PyMySQL



from langchain.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql.base import SQLDatabaseChain
import apikey
apikey.getOpenai()

#dburi="sqlite:////content/dirve/MyDrive/Chinook.db"
dburi = f"mysql+pymysql://root:9080@imcmaster.iptime.org:3336/sakila"
db = SQLDatabase.from_uri(dburi, include_tables=['customer', 'payment'])
llm = OpenAI(temperature=0, verbose=True)
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)

#db_chain.run("How many employees are there?")
exequery=db_chain.run("How much money Mary Smith has spent ?")
#db_chain.run("How may products in Classic Cars productline ?")
print("execute result: ", exequery)

from langchain.chains import create_sql_query_chain
from langchain.chat_models import ChatOpenAI

chain = create_sql_query_chain(ChatOpenAI(temperature=0), db)
query = chain.invoke({"question": "How many customers are there"})
print("created query: ",query)
exequery=db.run(query)
print("execute result: ", exequery)


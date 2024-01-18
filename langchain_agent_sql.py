import apikey
apikey.getOpenai()

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.utilities import SQLDatabase
from langchain.agents.agent_types import AgentType
from langchain.llms import OpenAI

#dburi = "sqlite:////home/yknam/ipykernel/data/chinook.db"
dburi = f"mysql+pymysql://root:9080@imcmaster.iptime.org:3336/sakila"
db=SQLDatabase.from_uri(dburi, include_tables=['customer', 'payment'])
agent_executor =create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=SQLDatabaseToolkit(db=db,llm=OpenAI(temperature=0)),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

# agent_executor.run("고객 중 가장 많이 지불한 사람과 금액을 알려줘?")
agent_executor.run("payment 테이블을 설명해줘")

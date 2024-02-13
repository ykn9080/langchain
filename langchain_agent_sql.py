from langchain.load.dump import dumps
from langchain.llms import OpenAI
from langchain.agents.agent_types import AgentType
from langchain.utilities import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
import apikey
apikey.getOpenai()


# dburi = "sqlite:////home/yknam/ipykernel/data/chinook.db"
dburi = f"mysql+pymysql://root:9080@imcmaster.iptime.org:3336/sakila"
db = SQLDatabase.from_uri(dburi, include_tables=['customer', 'payment'])
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0)),
    verbose=True,
    return_intermediate_steps=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION

)

# agent_executor.run("고객 중 가장 많이 지불한 사람과 금액을 알려줘?")
# agent_executor.run("payment 테이블을 설명해줘")
response = agent_executor({"input": "payment 테이블을 설명해줘"})
print(dumps(response["intermediate_steps"], pretty=True))
print(response["output"])

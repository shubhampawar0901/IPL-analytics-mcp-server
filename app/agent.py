# we will build agent and tools using langgraph and langchain with system prompt, user prompt and agent prompt keeping conditoins for sql precautions

from langchain.chat_models import init_chat_model
from langchain_community.agent_toolkits import SQLDatabaseToolkit
#prebuilt langgraph agent
from langgraph.prebuilt import create_react_agent
import os
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
db_path = "sqlite:///" + os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "database.sqlite") 
db = SQLDatabase.from_uri(db_path)


def build_agent_and_tools():

    llm = init_chat_model("openai:gpt-3.5-turbo")

    #tools
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    tools = toolkit.get_tools()

    system_prompt = """
    You are an agent designed to interact with a SQL database.
    Given an input question, create a syntactically correct {dialect} query to run,
    then look at the results of the query and return the answer. Unless the user
    specifies a specific number of examples they wish to obtain, always limit your
    query to at most {top_k} results.

    You can order the results by a relevant column to return the most interesting
    examples in the database. Never query for all the columns from a specific table,
    only ask for the relevant columns given the question.

    You MUST double check your query before executing it. If you get an error while
    executing a query, rewrite the query and try again.

    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the
    database.

    To start you should ALWAYS look at the tables in the database to see what you
    can query. Do NOT skip this step.

    Then you should query the schema of the most relevant tables.
    """.format(
        dialect=db.dialect,
        top_k=5,
    )

    agent = create_react_agent(
        llm,
        tools,
        prompt=system_prompt,
    )

    return agent, tools, toolkit

def main():
    agent, tools, toolkit = build_agent_and_tools()
    # agent.run("What is the total number of orders?")

    print(agent, tools, toolkit)

if __name__ == "__main__":
    main()
from langchain_community.utilities import SQLDatabase
import os
from langchain_community.agent_toolkits import SQLDatabaseToolkit
#sql file  is present in IPL-analytics-mcp-server\data\database.sqlite we are in app folder. build db_path without .env
db_path = "sqlite:///" + os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "database.sqlite") 
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llm = init_chat_model("openai:gpt-4.1")
def create_db():
    db = SQLDatabase.from_uri(db_path)
    print(db.dialect)



    return db

def get_schema_text(db):
    print(db.get_usable_table_names())
    # print(db.run("SELECT * FROM Artist LIMIT 10;"))
    # get schema of all tables
    print(db.get_table_info())
    tables = db.get_usable_table_names()
    print(tables)
    
    schema_text = ""
    for table in tables:
        #get schema of table
        schema_text += db.get_table_info(table) + "\n"
    return schema_text


#run file config
if __name__ == "__main__":
    create_db()
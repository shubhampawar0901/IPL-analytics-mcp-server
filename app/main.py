# We will buld fastMCP 

import os
from fastmcp import FastMCP
from db_utils import create_db, get_schema_text
from agent import build_agent_and_tools
from sql_safety import is_sql_safe, extract_first_select
from tools import prompt_head_to_head, prompt_query_player_stats, prompt_season_comparisons, prompt_team_performance
import sqlite3

db_path = "sqlite:///" + os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "database.sqlite") 

sql_db = create_db(db_path)
schema_text = get_schema_text(sql_db)

agent, tools = build_agent_and_tools(sql_db, schema_text)

mcp = FastMCP("ipl-analytics", agent, tools)

def run_sql(sql):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results

@mcp.tool(name="head_to_head", description="Compare the performance of two players head to head")
def head_to_head_tool(player1, player2):
    prompt = prompt_head_to_head(player1, player2)
    sql = agent.run(prompt)
    if not is_sql_safe(sql):
        return "SQL is not safe"
    results = run_sql(sql)
    return results

@mcp.tool(name="query_player_stats", description="Query the stats of a player")
def query_player_stats_tool(player):
    prompt = prompt_query_player_stats(player)
    sql = agent.run(prompt)
    if not is_sql_safe(sql):
        return "SQL is not safe"
    results = run_sql(sql)
    return results

@mcp.tool(name="season_comparisons", description="Compare the performance of a player in two different seasons")
def season_comparisons_tool(player, season1, season2):
    prompt = prompt_season_comparisons(player, season1, season2)
    sql = agent.run(prompt)
    if not is_sql_safe(sql):
        return "SQL is not safe"
    results = run_sql(sql)
    return results

@mcp.tool(name="team_performance", description="Query the performance of a team")
def team_performance_tool(team):
    prompt = prompt_team_performance(team)
    sql = agent.run(prompt)
    if not is_sql_safe(sql):
        return "SQL is not safe"
    results = run_sql(sql)
    return results

mcp.run(host="0.0.0.0", port=8000)
   
# here we will write all the tools that we will use in the project which will include prompt domain specific questions and get the answers from the user

def prompt_head_tohead(schema_text,team1, team2):
    return(
        f"Schema: {schema_text} \n\n"
        f"Instruction: Generate only and only one valid sqlite select statement to answer the following question. Strictly follow\n\n "
        f"Question: What is the head to head record between {team1} and {team2}? \n\n"
    )

def prompt_query_player_stats(schema_text,player_name):
    return(
        f"Schema: {schema_text} \n\n"
        f"Instruction: Generate only and only one valid sqlite select statement to answer the following question. Strictly follow\n\n "
        f"Question: What are the stats of {player_name}? \n\n"
    )

# team_performance: Team statistics and trends
# season_comparisons: Cross-season analysis
# head_to_head: Team vs team historical data

def prompt_team_performance(schema_text,team_name):
    return(
        f"Schema: {schema_text} \n\n"
        f"Instruction: Generate only and only one valid sqlite select statement to answer the following question. Strictly follow\n\n "
        f"Question: What is the performance of {team_name}? \n\n"
    )

def prompt_season_comparisons(schema_text,team_name,season1,season2):
    return(
        f"Schema: {schema_text} \n\n"
        f"Instruction: Generate only and only one valid sqlite select statement to answer the following question. Strictly follow\n\n "
        f"Question: How did {team_name} perform in {season1} compared to {season2}? \n\n"
    )

def prompt_head_to_head(schema_text,team1,team2):
    return(
        f"Schema: {schema_text} \n\n"
        f"Instruction: Generate only and only one valid sqlite select statement to answer the following question. Strictly follow\n\n "
        f"Question: What is the head to head record between {team1} and {team2}? \n\n"
    )


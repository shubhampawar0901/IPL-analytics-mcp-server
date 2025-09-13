# this will protect from sql injection attacks
import re

select_only = re.compile(r'^SELECT\s+.*\s+FROM\s+.*$')
forbidden = ['INSERT', 'UPDATE', 'DELETE', 'DROP', 'TRUNCATE', 'ALTER', 'CREATE', 'GRANT', 'REVOKE', 'EXECUTE', 'CALL']

def is_select_only(query):

    if not query or not select_only.match(query):
        return False

    for f in forbidden:
        if f in query:
            return False

    return True

def extract_first_select(input):
    # we will extract the first select statement from the query

    if not input or not select_only.match(input):
        return False

    input_upper = input.upper()
    for f in forbidden:
        if f in input_upper:
            return False

    first_select = re.search(r'SELECT\s+.*\s+FROM\s+.*', input_upper)
    if first_select:
        return first_select.group(1).strip()
    else:
        return ""
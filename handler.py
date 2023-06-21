import sys
import logging
import json
from sqlalchemy import create_engine, text

rds_host = "database-mastere.cqomuy5p6jjk.ap-northeast-2.rds.amazonaws.com"
user_name = "admin"
user_password = "qkrwjdgus"
db_name = "mastere"

engine = create_engine(f"mysql+pymysql://{user_name}:{user_password}@{rds_host}/{db_name}")

try:
    conn = engine.connect()
except Exception as e:
    logging.error("ERROR: Could not connect to DB")
    logging.error(e)
    sys.exit()

def hello(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def lambda_handler(event, context):
    query = "SELECT * FROM vocas"

    result = conn.execute(text(query)).fetchall()
    results = [dict(row) for row in result]
    
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
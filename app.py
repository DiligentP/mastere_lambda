import json
from sqlalchemy import create_engine, text

# RDS 정보
rds_host = "database-mastere.cqomuy5p6jjk.ap-northeast-2.rds.amazonaws.com"
user_name = "admin"
user_password = "qkrwjdgus"
db_name = "mastere"

# SQLAlchemy 연결
db_uri = f"mysql+pymysql://{user_name}:{user_password}@{rds_host}/{db_name}"
engine = create_engine(db_uri)

def hello(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello, Lambda!'
    }

def test(event, context):
    try:
        # 데이터베이스에 연결
        with engine.connect() as conn:
            # 쿼리 실행
            result = conn.execute(text("SELECT * FROM vocas;"))

            # 결과를 리스트 형태로 변환
            rows = [dict(row) for row in result]

        # 결과를 JSON 형태로 반환
        return {
            'statusCode': 200,
            'body': json.dumps(rows)
        }
    except Exception as e:
        # 예외 처리
        return {
            'statusCode': 500,
            'body': str(e)
        }

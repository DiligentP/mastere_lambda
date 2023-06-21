import json
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# RDS 정보
rds_host = "database-mastere.cqomuy5p6jjk.ap-northeast-2.rds.amazonaws.com"
user_name = "admin"
user_password = "qkrwjdgus"
db_name = "mastere"

# SQLAlchemy 연결 문자열 생성
db_uri = f"mysql+pymysql://{user_name}:{user_password}@{rds_host}/{db_name}"

# SQLAlchemy 엔진 생성
engine = create_engine(db_uri)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Voca(Base):
    __tablename__ = 'vocas'

    id = Column(Integer, primary_key=True)
    word = Column(String(255), nullable=True)
    mean = Column(String(255), nullable=True)
    source = Column(String(255), nullable=True)


def lambda_handler(event, context):
    try:
        # 이벤트에서 단어, 의미, 소스 추출
        body = json.loads(event['body'])
        word = body['word']
        mean = body['mean']
        source = body['source']
        dbcommit = body.get('dbcommit', 'False')

        # 단어 생성 후 세션추가
        voca = Voca(word=word, mean=mean, source=source)
        session.add(voca)
        
        # dbcommit 값이 정확히 "true"인 경우에만 커밋
        if dbcommit.lower() == 'true':
            session.commit()

        # 결과 반환
        return {
            'statusCode': 200,
            'body': json.dumps({'voca_id': voca.id}),
            'status': "Succsessful",
            'dbcommit': dbcommit
        }
    except Exception as e:
        # 예외 처리
        return {
            'statusCode': 500,
            'error': str(e)
        }
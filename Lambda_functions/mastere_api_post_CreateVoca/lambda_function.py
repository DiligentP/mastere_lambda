import json
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# RDS 정보
rds_host = "db.diligentp.com"
user_name = "park"
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
    word = Column(String(255), nullable=False)
    mean = Column(String(255), nullable=False)
    content = Column(Text, nullable=True)


def lambda_handler(event, context):
    try:
        # 이벤트에서 단어, 의미, 소스 추출
        word = event['word']
        mean = event['mean']
        content = event['content']

        # 단어 생성 후 세션추가
        voca = Voca(word=word, mean=mean, content=content)
        session.add(voca)
        session.commit()

        # 결과 반환
        return {
            'statusCode': 200,
            'body': "Succsessful"
        }
    except Exception as e:
        # 예외 처리
        return {
            'statusCode': 500,
            'error': str(e)
        }
import json
import jwt
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

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


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


def lambda_handler(event, context):
    username = event['username']
    password = event['password']
    user = session.query(Users).filter_by(username=username, password=password).first()

    # JWT 생성
    payload = {'username': username}  # 필요한 클레임 정보 추가
    secret_key = 'mastere'  # JWT 서명에 사용할 비밀 키
    algorithm = 'HS256'  # 사용할 알고리즘 지정

    jwt_token = jwt.encode(payload, secret_key, algorithm=algorithm)

    if user:
        return {
            'statusCode': 200,
            'body': 'true',
            'token': jwt_token
        }
    else:
        return {
            'statusCode': 400,
            'body': 'false'
        }


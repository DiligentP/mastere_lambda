import json
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


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


def lambda_handler(event, context):
    try:
        # JSON 데이터에서 필요한 정보 추출
        username = event['username']

        # 사용자 이름 조회
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            return {
                'statusCode': 200,
                'body': 'true'
            }
        else:
            return {
                'statusCode': 400,
                'body': 'false'
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error: {str(e)}'
        }
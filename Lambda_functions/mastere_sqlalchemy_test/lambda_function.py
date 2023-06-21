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
        # 'vocas' 테이블에서 데이터 조회
        vocas = session.query(Voca).all()

        # 결과를 리스트 형태로 변환
        rows = []
        for voca in vocas:
            rows.append({
                'id': voca.id,
                'word': voca.word,
                'mean': voca.mean,
                'source': voca.source
            })

        # 결과를 JSON 형태로 반환
        return {
            'statusCode': 200,
            'body': rows
        }
    except Exception as e:
        # 예외 처리
        return {
            'statusCode': 500,
            'body': str(e)
        }
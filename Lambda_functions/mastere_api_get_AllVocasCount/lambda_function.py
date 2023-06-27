# vocas 테이블의 총 데이터 갯수를 반환하는 함수

import json
import pymysql

# RDS 정보
rds_host = "db.diligentp.com"
user_name = "park"
user_password = "qkrwjdgus"
db_name = "mastere"

def lambda_handler(event, context):
    # 데이터베이스 연결 설정
    conn = pymysql.connect(host=rds_host, user=user_name, password=user_password, database=db_name)
    
    try:
        # 커서 생성
        with conn.cursor() as cursor:
            # vocas 테이블의 총 데이터 개수 조회
            query = "SELECT COUNT(*) FROM vocas"
            cursor.execute(query)
            
            # 결과 가져오기
            result = cursor.fetchone()
            
            # 총 데이터 개수 반환
            total_count = result[0]
            
            return {
                'statusCode': 200,
                'body': json.dumps(total_count)
            }
    
    finally:
        # 연결 종료
        conn.close()
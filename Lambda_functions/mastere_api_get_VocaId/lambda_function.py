# vocaid 를 조회하여 일치하는 단어정보를 반환

# 데이터 형식 
# {
#   "voca_id" : "1"   
# }

import json
import pymysql

# RDS 정보
rds_host = "db.diligentp.com"
user_name = "park"
user_password = "qkrwjdgus"
db_name = "mastere"

def lambda_handler(event, context):
    # 입력된 "voca_id" 값을 가져옴
    voca_id = event['voca_id']
    
    # 데이터베이스 연결 설정
    conn = pymysql.connect(host=rds_host, user=user_name, password=user_password, database=db_name)
    
    try:
        # 커서 생성
        with conn.cursor() as cursor:
            # 입력된 "voca_id" 값과 일치하는 데이터 조회
            query = "SELECT * FROM vocas WHERE id = %s"
            cursor.execute(query, (voca_id,))
            
            # 조회된 데이터 가져오기
            result = cursor.fetchone()
            
            # 결과가 없으면 None을 반환
            if result is None:
                return {
                    'statusCode': 200,
                    'body': json.dumps(None)
                }
            
            # 조회된 데이터를 JSON 형식으로 변환하여 반환
            data = {
                'id': result[0],
                'word': result[1],
                'mean': result[2],
                'source': result[3]
            }
            
            return {
                'statusCode': 200,
                'body': json.dumps(data)
            }
    
    finally:
        # 연결 종료
        conn.close()
import json
import random
import pymysql

# RDS 정보
rds_host = "db.diligentp.com"
user_name = "park"
user_password = "qkrwjdgus"
db_name = "mastere"

def get_unique_quiz(count):
    # 데이터베이스 연결 설정
    conn = pymysql.connect(host=rds_host, user=user_name, password=user_password, database=db_name)

    try:
        # 커서 생성
        with conn.cursor() as cursor:
            # 데이터베이스에서 랜덤한 10개의 데이터를 가져옴
            query = f"SELECT * FROM vocas ORDER BY RAND() LIMIT {count}"
            
            cursor.execute(query)
            result = cursor.fetchall()

            # 결과가 없으면 None을 반환
            if not result:
                return None

            # 조회된 데이터를 리스트 형식으로 변환
            data = []
            for row in result:
                # 보기를 가져올 쿼리 작성
                query2 = f"SELECT mean FROM vocas WHERE id <> {int(row[0])} LIMIT 3;"
                cursor.execute(query2)
                result2 = cursor.fetchall()
                
                # 보기 리스트 초기화
                options = []
                options.append(row[2])

                # 보기 데이터를 리스트에 추가
                for row2 in result2:
                    options.append(row2[0])
                
                print("options : ", options)
                random.shuffle(options)
                print("mixeddd : ", options)
                
                # 문제 데이터 생성
                quiz = {
                    'id': row[0],
                    'word': row[1],
                    'mean': row[2],
                    'source': row[3],
                    'q1': options[0],
                    'q2': options[1],
                    'q3': options[2],
                    'q4': options[3]	
                }
                
                # 문제 리스트에 추가
                data.append(quiz)

            return data

    finally:
        # 연결 종료
        conn.close()

def lambda_handler(event, context):
    # 입력된 "quiz_count" 값을 가져옴
    quiz_count = int(event['quiz_count'])

    # 겹치지 않는 10개의 데이터를 가져옴
    quiz_data = get_unique_quiz(quiz_count)

    # 반환할 데이터 형식
    response = {
        'statusCode': 200,
        'body': json.dumps(quiz_data)
    }

    return response

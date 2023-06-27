import json
import pymysql

# RDS 정보
rds_host = "db.diligentp.com"
user_name = "park"
user_password = "qkrwjdgus"
db_name = "mastere"

def lambda_handler(event, context):
    user_id = int(event['user_id'])

    # RDS에 연결
    conn = pymysql.connect(
        host=rds_host,
        user=user_name,
        password=user_password,
        database=db_name
    )
    
    data = []
    try:
        # user_vocabulary 테이블에서 해당 user_id의 모든 행 검색
        with conn.cursor() as cursor:
            sql = "SELECT * FROM user_vocabulary WHERE user_id = %s"
            cursor.execute(sql, (user_id,))
            rows = cursor.fetchall()
            
            for row in rows:
                word_id = row[1]
                per = row[2]
                
                sql = "SELECT * FROM vocas WHERE id= %s"
                cursor.execute(sql, (word_id,))
                voca = cursor.fetchone()
                
                # 사용자가 외운 voca 데이터 생성
                vocadata = {
                    "id": voca[0],
                    "word": voca[1],
                    "mean": voca[2],
                    "source": voca[3],
                    "per": per
                }
                data.append(vocadata)

        # 결과 반환
        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Failed to fetch user vocabulary: {}'.format(str(e)))
        }
    finally:
        # 연결 종료
        conn.close()

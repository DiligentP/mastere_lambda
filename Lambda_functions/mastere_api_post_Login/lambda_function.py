import pymysql
import jwt

def lambda_handler(event, context):
    # RDS 정보
    rds_host = "db.diligentp.com"
    user_name = "park"
    user_password = "qkrwjdgus"
    db_name = "mastere"

    # Post로 전달받은 데이터
    username = event["username"]
    password = event["password"]

    # 데이터베이스 연결
    conn = pymysql.connect(
        host=rds_host,
        user=user_name,
        password=user_password,
        database=db_name,
        connect_timeout=5,
        cursorclass=pymysql.cursors.DictCursor
    )
    
    payload = {'username': username}  # 필요한 클레임 정보 추가
    secret_key = 'mastere'  # JWT 서명에 사용할 비밀 키
    algorithm = 'HS256'  # 사용할 알고리즘 지정

    jwt_token = jwt.encode(payload, secret_key, algorithm=algorithm)

    try:
        # 데이터베이스 쿼리 실행
        with conn.cursor() as cursor:
            sql = "SELECT * FROM users WHERE username=%s AND password=%s"
            cursor.execute(sql, (username, password))
            result = cursor.fetchone()
            
            if result:
                return {
                    'statusCode': 200,
                    'body': 'true',
                    'token': jwt_token,
                    'user_id': result['user_id']
                }
            else:
                return {
                    'statusCode': 400,
                    'body': 'false'
                }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': 'error'
        }
    finally:
        conn.close()

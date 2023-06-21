## 패키지 설치
```
pip install -r requirement.txt --target .
```

## Serverless 명령어
```
# 작성한 코드를 Lamda로 배포
serverless deploy

# 함수만 업데이트
serverless deploy function -f hello

# 함수 호출
serverless invoke -f [FUNCTION]
serverless invoke -f hello --data "{'name':'park'}"

# 함수 로그 확인
serverless log -f [FUNCTION]
serverless logs -f hello

# 함수 삭제
serverless remove
```
from fastapi import FastAPI

app = FastAPI()

rds_host = "database-mastere.cqomuy5p6jjk.ap-northeast-2.rds.amazonaws.com"
user_name = "admin"
user_password = "qkrwjdgus"
db_name = "mastere"


@app.get("/")
def hello():
    return {"Hello": "World"}

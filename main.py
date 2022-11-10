from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 注册账号
@app.post("/register")
async def register(username: str, password: str):
    # TODO 写入{user} {pass}到数据库
    return {"message": f"register {username} {password}"}


# 登录
@app.get("/login")
async def login(username: str, password: str):
    token = ""
    # TODO 从数据库中读取{user} {pass}，如果匹配成功，生成token
    return token


# 修改密码
@app.post("/change_password")
async def change_password(token: str, old_password: str, new_password: str):
    # TODO 从数据库中读取{token}，如果匹配成功，修改密码
    return {"message": f"change password {old_password} to {new_password}"}


# 发帖
@app.post("/post")
async def post(token: str, title: str, content: str):
    # TODO 从数据库中读取{token}，如果匹配成功，写入{title} {content}到数据库
    return {"message": f"post {title} {content}"}


# 评论
@app.post("/comment")
async def comment(token: str, post_id: int, content: str):
    # TODO 从数据库中读取{token}，如果匹配成功，写入{post_id} {content}到数据库
    return {"message": f"comment {post_id} {content}"}


# 读取所有帖子（时间排序）
@app.get("/posts")
async def posts():
    # TODO 从数据库中读取所有帖子，按时间排序
    return []

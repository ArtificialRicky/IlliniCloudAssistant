import motor.motor_asyncio
from fastapi import FastAPI
from fastapi import status
from starlette.responses import JSONResponse

MONGODB_URL = "mongodb+srv://root:IlliniCloudAssistant@cluster0.7oprx89.mongodb.net/test"

app = FastAPI()

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = client.IlliniCloudAssistant


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# 注册账号
@app.api_route("/register", methods=["GET", "POST"])
async def register(username: str, password: str):
    """
    写入 username, password 到数据库
    :param username:
    :param password:
    :return:
    """

    user = {
        "username": username,
        "password": password,
    }
    new_user = await db["User"].insert_one(user)
    created_user = await db["User"].find_one({
        "_id": new_user.inserted_id,
    })
    # return {"message": f"register {username} {password}"}
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_user)


# 登录
@app.get("/login")
async def login(username: str, password: str):
    # TODO 从数据库中读取{user} {pass}，如果匹配成功，生成token
    token = "I'm token"

    if not username or not password:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                            content={"message": "username or password is empty"})

    user = await db["User"].find_one({
        "username": username,
        "password": password,
    })

    if user is not None:
        return JSONResponse(status_code=status.HTTP_200_OK, content={"token": token})
    else:
        # user is None
        return JSONResponse(status_code=status.HTTP_403_FORBIDDEN,
                            content={"message": "Invalid username or password"})


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

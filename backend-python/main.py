from fastapi import FastAPI
import json
from pydantic import BaseModel
import bcrypt
from fastapi.responses import PlainTextResponse

app = FastAPI()
#TODO: add encryption

class LoginInfo(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    value: str


class RegistrationInfo(BaseModel):
    username: str
    password: str


@app.get("/mock/receipts/list")
async def get_all_receipts():
    with open('./mock-files/mock-receipts-list.json', encoding='utf-8') as file:
        data = json.load(file)
        return data


@app.get("/mock/receipt")
async def get_receipt_by_id(receipt_id: int = 1):
    with open('./mock-files/mock-receipt.json', encoding='utf-8') as file:
        if receipt_id not in [1, 2, 3]:
            return 'error'
        data = json.load(file)
        return data[receipt_id]


auth_token = "token"


@app.post('/login', response_class=PlainTextResponse)
async def try_login(request_login_info: LoginInfo):
    login_info = LoginInfo(**{'username': 'user', 'password': bcrypt.hashpw(b'password', bcrypt.gensalt())})
    if login_info.username == request_login_info.username:
        return login_info.password
    else:
        return 'error'


@app.post('/updateToken', response_class=PlainTextResponse)
async def update_token(token: Token):
    auth_token = token.value
    return 'ok'


@app.post('/authenticate')
async def authenticate(token: Token):
    if token.value == auth_token:
        return LoginInfo('user', 'password')
    else:
        return LoginInfo('error', 'error')


@app.post('/register', response_class=PlainTextResponse)
async def authenticate(registration_info: RegistrationInfo):
    if registration_info.username != 'user':
        return 'ok'
    else:
        return 'error'

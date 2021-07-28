from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from tortoise.contrib.pydantic import pydantic_model_creator
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt

from cipherFunc import Cipher

cipher = Cipher()
app = FastAPI()

JWT_SECRET = 'secret'

""" User model """


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(50, unique=True)
    password = fields.CharField(128)


""" Register database """

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['cipherAPI']},
    generate_schemas=True,
    add_exception_handlers=True
)

User_Pydantic = pydantic_model_creator(User, name='User')
UserIn_Pydantic = pydantic_model_creator(User, name='UserIn', exclude_readonly=True)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


async def authenticate_user(username: str, password: str):
    user = await User.get(username=username, password=password)
    if not user:
        return False
    else:
        return user


""" Create user endpoint """


@app.post('/users', response_model=User_Pydantic)
async def create_user(user: UserIn_Pydantic):
    user_obj = User(username=user.username, password=user.password)
    await user_obj.save()
    return await User_Pydantic.from_tortoise_orm(user_obj)


""" Create token endpoint """


@app.post('/token')
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)

    if not user:
        return {'error': 'invalid credentials'}

    user_obj = await User_Pydantic.from_tortoise_orm(user)

    token = jwt.encode(user_obj.dict(), JWT_SECRET)

    return {'token': token, 'token_type': 'bearer'}


""" Encrypt string endpoint """


@app.post('/encrypt')
async def decrypt_string(string: str, key: int):
    return {'encrypted ': cipher.cipher_algorithm(string, key)}


""" Decrypt string endpoint """


@app.post('/decrypt')
async def decrypt_string(string: str, key: int):
    return {'Decrypted ': cipher.cipher_algorithm(string, key, decrypt=True),
            'The key is: ': key}

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)

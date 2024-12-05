from fastapi import FastAPI, Path
from typing import Annotated

from fastapi import FastAPI

app=FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}

@app.get('/users')
async def get_user_page() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def user_register(username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='UrbanUser')]
        , age: int) -> str:
    user_id= str(int(max(users, key=int))+1)
    users[user_id]=f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(ge=1, le=100, description='Enter your age', example='24')
                      , username: str = Path(min_length=3, max_length=20, description='Enter username',
                                             example='UrbanUser')
                      , age: int = 30) -> str:
    users[user_id]=f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is registered'

@app.delete('/user/{user_id}')
async def delete_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'

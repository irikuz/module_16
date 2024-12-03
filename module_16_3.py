from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=3, max_length=15, description='Enter username', example='UrbanUser')]
        , age: int) -> str:
    current_index = str(int(max(users, key=int)) + 1)
    users[current_index] = username, age
    return f'User {current_index} is registered!'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str = Path(ge=1, le=100, description='Enter your age', example='24')
                      , username: str = Path(min_length=3, max_length=20, description='Enter username',
                                             example='UrbanUser')
                      , age: int = 30) -> str:
    users[user_id] = user_id, username, age
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def delite_user(user_id: str) -> str:
    users.pop(user_id)
    return f'User {user_id} has been deleted'

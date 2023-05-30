from fastapi import APIRouter

from .endpoints import auth, todo, users, chats

api_router = APIRouter()

# fmt: off
api_router.include_router(auth.router, prefix='', tags=['Auth'])
api_router.include_router(users.router, prefix='/users', tags=['Users'])
api_router.include_router(chats.router, prefix='/chats', tags=['Chats'])
api_router.include_router(todo.router, prefix='/todos', tags=['Todos'])
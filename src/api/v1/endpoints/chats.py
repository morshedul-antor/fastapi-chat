from fastapi import Depends, APIRouter
from schemas import ChatIn, ChatOut
from services import chats_service
from db import get_db
from exceptions import handle_result
from typing import List
from sqlalchemy.orm import Session

router = APIRouter()


@router.post('/', response_model=ChatOut)
def create_chat(chat_in: ChatIn, db: Session = Depends(get_db)):
    create = chats_service.create(db=db, data_in=chat_in)
    return handle_result(create)


@router.get('/{sender_id}/{receiver_id}', response_model=List[ChatOut])
def get_messages(sender_id: int, receiver_id: int, db: Session = Depends(get_db)):
    data = chats_service.get_message(
        db=db, sender_id=sender_id, receiver_id=receiver_id)
    return handle_result(data)

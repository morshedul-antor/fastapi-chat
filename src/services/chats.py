from models import Chat
from schemas import ChatIn, ChatUpdate
from repositories import chats_repo
from services import BaseService
from sqlalchemy.orm import Session
from fastapi import status
from exceptions import ServiceResult, AppException


class ChatService(BaseService[Chat, ChatIn, ChatUpdate]):

    def get_message(self, db: Session, sender_id: int, receiver_id: int):
        data = chats_repo.get_message(
            db=db, sender_id=sender_id, receiver_id=receiver_id)

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_200_OK)


chats_service = ChatService(Chat, chats_repo)

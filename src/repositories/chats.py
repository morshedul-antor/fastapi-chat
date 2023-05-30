from operator import or_
from models import Chat
from schemas import ChatIn, ChatUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc


class ChatRepo(BaseRepo[Chat, ChatIn, ChatUpdate]):

    def get_message(self, db: Session, sender_id: int, receiver_id: int):
        return db.query(Chat).order_by((Chat.created_at)).filter(or_(Chat.sender_id == sender_id, Chat.sender_id == receiver_id)).filter(or_(Chat.receiver_id == receiver_id,  Chat.receiver_id == sender_id)).all()


chats_repo = ChatRepo(Chat)

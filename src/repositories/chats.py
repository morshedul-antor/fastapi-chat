from operator import or_
from models import Chat, User
from schemas import ChatIn, ChatUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy import or_, desc, func


class ChatRepo(BaseRepo[Chat, ChatIn, ChatUpdate]):

    def get_message(self, db: Session, sender_id: int, receiver_id: int):
        return db.query(Chat).order_by(desc(Chat.created_at)).filter(or_(Chat.sender_id == sender_id, Chat.sender_id == receiver_id)).filter(or_(Chat.receiver_id == receiver_id,  Chat.receiver_id == sender_id)).all()

    def get_users(self, db: Session):

        user_id = 1
        data = db.query(Chat.sender_id, Chat.receiver_id).distinct().filter(
            or_(Chat.sender_id == user_id, Chat.receiver_id == user_id)).all()

        data = [user[0] for user in data]
        data = db.query(User).filter(User.id.in_(data)).distinct().all()

        return data


chats_repo = ChatRepo(Chat)

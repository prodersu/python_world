import uuid
import hashlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Users, Posts, Likes, Comments

engine = create_engine("mysql+mysqlconnector://root:@localhost/flask_api", echo=False)
session = sessionmaker(bind=engine)

s = session()


def ins_user(nick, email, password):
    new_user = Users(nickname=nick, email=email, password=password)
    s.add(new_user)
    s.commit()


def ins_post(title, text, user_id):
    new_post = Posts(title=title, description=text, user_id=user_id)
    s.add(new_post)
    s.commit()


def ins_comment(text, user_id, post_id):
    new_comment = Comments(text=text, user_id=user_id, post_id=post_id)
    s.add(new_comment)
    s.commit()


def to_like(user_id, post_id):
    like = Likes(user_id=user_id, post_id=post_id)
    s.add(like)
    s.commit()


def get_users():
    users = s.query(Users).all().first()
    return users


def hash_password(password):
    # uuid используется для генерации случайного числа
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

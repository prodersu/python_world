from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Posts(Base):
    __tablename__ = 'Posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)
    created_time = Column(DateTime(timezone=True), server_default=func.utc.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('Users.id'))
    Users = relationship('Users')


class Likes(Base):
    __tablename__ = 'Likes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    post_id = Column(Integer, ForeignKey('Posts.id'))
    Users = relationship('Users')
    Posts = relationship('Posts')


class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


class Comments(Base):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)
    created_time = Column(DateTime(timezone=True), server_default=func.utc.now())
    updated_time = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey('Users.id'))
    post_id = Column(Integer, ForeignKey('Posts.id'))
    Users = relationship('Users')
    Posts = relationship('Posts')

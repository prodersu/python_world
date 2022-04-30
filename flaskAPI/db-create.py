
from sqlalchemy import create_engine, Table, Column, Integer, String, DateTime, func, MetaData, ForeignKey

meta = MetaData()

users = Table('Users', meta,
              Column('id', Integer, primary_key=True),
              Column('nickname', String(250), nullable=False),
              Column('email', String(250), nullable=False),
              Column('password', String(250), nullable=False)
              )

posts = Table('Posts', meta,
              Column('id', Integer, primary_key=True),
              Column('title', String(250), nullable=False),
              Column('description', String(250), nullable=False),
              Column('created_time', DateTime(timezone=True), server_default=func.now()),
              Column('updated_time', DateTime(timezone=True), onupdate=func.now()),
              Column('user_id', Integer, ForeignKey('Users.id'))
              )

comments = Table('Comments', meta,
                 Column('id', Integer, primary_key=True),
                 Column('text', String(250), nullable=False),
                 Column('created_time', DateTime(timezone=True), server_default=func.now()),
                 Column('updated_time', DateTime(timezone=True), onupdate=func.now()),
                 Column('post_id', Integer, ForeignKey('Posts.id')),
                 Column('user_id', Integer, ForeignKey('Users.id'))
                 )

likes = Table('Likes', meta,
              Column('id', Integer, primary_key=True),
              Column('post_id', Integer, ForeignKey('Posts.id')),
              Column('user_id', Integer, ForeignKey('Users.id'))
              )

engine = create_engine("mysql+mysqlconnector://root:@localhost/flask_api", echo=True)
meta.create_all(engine)



# ins_user('Dersu', 'dersu@dragun.ru', 'dersu345')
# ins_post('First post', 'Hello world', 1)
#
# print(users.c.nickname)
# print(posts.c)
# s = select([users, posts]).where(users.c.id == posts.c.user_id)

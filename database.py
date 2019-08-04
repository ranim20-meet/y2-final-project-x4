from model import Base, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///posts.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_post(author_name, title, content):
	new_post = Post(author_name = author_name, title = title, content = content)
	session.add(new_post)
	session.commit()


def query_all_posts():
	return session.query(Post).all()

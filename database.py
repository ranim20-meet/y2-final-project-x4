from model import Base, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine1 = create_engine('sqlite:///posts.db?check_same_thread=False')
Base.metadata.create_all(engine1)
DBSession1 = sessionmaker(bind=engine1)
session1 = DBSession1()


from model import Admin
engine2 = create_engine('sqlite:///admins.db?check_same_thread=False')
Base.metadata.create_all(engine2)
DBSession2 = sessionmaker(bind=engine2)
session2 = DBSession2()

def add_post(author_name, title, content):
	new_post = Post(author_name = author_name, title = title, content = content)
	session1.add(new_post)
	session1.commit()


def query_all_posts():
	return session1.query(Post).all()

def add_admin(username, password):
	new_admin = Admin(username = username)
	new_admin.hash_password(password)
	session2.add(new_admin)
	session2.commit()

def get_admin(username):
	return session2.query(Admin).filter_by(username = username).first()
add_admin("greenwall", "funwithmeet20")
print(get_admin("greenwall"))
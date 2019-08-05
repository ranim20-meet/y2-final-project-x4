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

def query_post_by_id(post_id):
	return session1.query(Post).filter_by(post_id = post_id).first()

def delete_post_by_id(post_id):
	session1.query(Post).filter_by(post_id = post_id).delete()
	session1.commit()

# Admin code
def add_admin(username, password):
	new_admin = Admin(username = username)
	new_admin.hash_password(password)
	session2.add(new_admin)
	session2.commit()

def get_admin(username):
	return session2.query(Admin).filter_by(username = username).first()

def query_all_admins():
	return session2.query(Admin).all()


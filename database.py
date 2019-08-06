from model import Base, Post

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# START POST CODE
# Create session for Post database
engine1 = create_engine('sqlite:///posts.db?check_same_thread=False')
Base.metadata.create_all(engine1)
DBSession1 = sessionmaker(bind=engine1)
session1 = DBSession1()

# Post functions: use 
def add_post(author_name, title, content):
	"""
	Add new post to posts.db
	"""
	new_post = Post(author_name = author_name, title = title, content = content)
	session1.add(new_post)
	session1.commit()


def query_all_posts():
	"""
	Get all posts
	"""
	return session1.query(Post).all()

def query_post_by_id(post_id):
	"""
	Get post by ID
	"""
	return session1.query(Post).filter_by(post_id = post_id).first()

def delete_post_by_id(post_id):
	"""
	Delete post by its's ID
	"""
	session1.query(Post).filter_by(post_id = post_id).delete()
	session1.commit()
# END OF POST CODE
#------------------
# START ADMIN CODE
from model import Admin

# Create session for Admin database
engine2 = create_engine('sqlite:///admins.db?check_same_thread=False')
Base.metadata.create_all(engine2)
DBSession2 = sessionmaker(bind=engine2)
session2 = DBSession2()

# Post functions: use session2!
def add_admin(username, password):
	"""
	Add new admin to 
	"""
	new_admin = Admin(username = username)
	new_admin.hash_password(password)
	session2.add(new_admin)
	session2.commit()

def get_admin(username):
	return session2.query(Admin).filter_by(username = username).first()

def query_all_admins():
	return session2.query(Admin).all()

# END ADMIN CODE

add_admin("hello", "hello")
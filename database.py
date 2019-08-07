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
def add_post(author_name, title, content, author_email):
	"""
	Add new post to posts.db
	"""
	new_post = Post(author_name = author_name, title = title, content = content, author_email = author_email)
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

# Admin functions: use session2!
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


# END OF ADMIN CODE
#------------------
# START REPLY CODE
from model import Reply
# Create session for Reply database
engine3 = create_engine('sqlite:///replies.db?check_same_thread=False')
Base.metadata.create_all(engine3)
DBSession3 = sessionmaker(bind=engine3)
session3 = DBSession3()

# Reply functions: use session3!
def add_reply(parent_id, reply_author_name, reply_title, reply_content):
	"""
	Add new reply to 
	"""
	new_reply = Reply(parent_id = parent_id, reply_author_name = reply_author_name, reply_title = reply_title, reply_content = reply_content)
	session3.add(new_reply)
	session3.commit()

def delete_reply_by_parent(parent_id):
	session3.query(Reply).filter_by(parent_id = parent_id).delete()		
	session3.commit()

def query_all_replies():
	return session3.query(Reply).all()

#END OF REPLY CODE


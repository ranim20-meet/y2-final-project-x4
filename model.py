from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from passlib.apps import custom_app_context as pwd_security

Base = declarative_base()

class Post(Base):
	
	__tablename__ = 'posts'
	post_id = Column(Integer, primary_key=True)
	author_name = Column(String)
	title = Column(String)
	content = Column(String)
	author_email = Column(String)

	def __repr__(self):
		return ("Author: {}\n"
				"Title: {} \n"
				"Comment: {}").format(
					self.author_name,
					self.title,
					self.content)

class Admin(Base):
	__tablename__ = 'admins'
	admin_id = Column(Integer, primary_key=True)
	username = Column(String)
	password_hash = Column(String)

	def hash_password(self, password):
		self.password_hash = pwd_security.encrypt(password)

	def verify_password(self, password):
		return pwd_security.verify(password, self.password_hash)

	def __repr__(self):
		return ("username: {} \n"
				"password: {} \n").format(
				self.username, 
				self.password_hash)

class Reply(Base):
	__tablename__ = 'replies'
	reply_id = Column(Integer, primary_key = True)
	parent_id = Column(Integer)
	reply_author_name = Column(String)
	reply_title = Column(String)
	reply_content = Column(String)

	def __repr__(self):
		return ("Author: {}\n"
				"Title: {} \n"
				"Reply: {}").format(
					self.reply_author_name,
					self.reply_title,
					self.reply_content)

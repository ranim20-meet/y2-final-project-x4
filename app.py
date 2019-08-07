from database import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'greenwallx4@gmail.com'
app.config['MAIL_PASSWORD'] = 'funwithmeet19'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
	if request.method == 'GET':
		all_posts = query_all_posts()
		all_posts = all_posts[::-1]
		all_replies = query_all_replies()
		return render_template('chatroom.html', all_posts = all_posts, login_session = login_session, all_replies = all_replies)

	else:
		author_name = request.form['author_name']
		title = request.form['title']
		content = request.form['content']
		author_email = request.form['author_email']

		add_post(author_name = author_name, title = title, content = content, author_email = author_email)
		all_posts = query_all_posts()
		all_posts = all_posts[::-1]
		all_replies = query_all_replies()
		return render_template('chatroom.html', all_posts = all_posts, login_session  = login_session, all_replies = all_replies)

@app.route("/tips")
def tips():
	return render_template('tips.html')

@app.route('/admin-login', methods=['POST'])
def admin_login():
	admin = get_admin(request.form['username'])
	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	all_replies = query_all_replies()
	if admin != None and admin.verify_password(request.form["password"]):
		login_session['name'] = admin.username
		login_session['logged_in'] = True
		return render_template('chatroom.html', login_session = login_session, all_posts = all_posts, all_replies = all_replies)
	else:
		return home()

@app.route('/admin-logout', methods = ['GET'])
def admin_logout():
	login_session['username'] = None
	login_session['logged_in'] = False
	return redirect(url_for("home"))

@app.route('/delete/<int:post_id>', methods = ['POST'])
def delete_post(post_id):
	delete_post_by_id(post_id)
	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	all_replies = query_all_replies()
	return render_template('chatroom.html', all_posts = all_posts, login_session = login_session, all_replies = all_replies)

@app.route('/admin_reply/<int:post_id>', methods = ['POST'])
def admin_reply(post_id):
	post_to_reply = query_post_by_id(post_id)
	msg_to_send = request.form['msg']
	email_to_send_to = post_to_reply.author_email
	email_sub = "GreenWall Reply: "+post_to_reply.title
	msg = Message(email_sub, sender = 'greenwallx4@gmail.com', recipients = [email_to_send_to])
	msg.body =  request.form['msg']
	mail.send(msg)
	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	all_replies = query_all_replies()
	return render_template('chatroom.html', all_posts = all_posts, login_session = login_session, all_replies = all_replies)

@app.route("/reg_reply/<int:post_id>", methods = ['POST'])
def reg_reply(post_id):
	parent_id = post_id
	reply_author_name = request.form['reply_author']
	reply_title = request.form['reply_title']
	reply_content = request.form['reply_content']

	add_reply(parent_id, reply_author_name, reply_title, reply_content)
	
	all_replies = query_all_replies()

	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	return render_template('chatroom.html', all_posts = all_posts, login_session = login_session, all_replies = all_replies)


if __name__ == '__main__':
    app.run(debug=True)


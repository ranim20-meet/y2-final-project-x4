from database import *
from flask import Flask, render_template, url_for, request, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/chat', methods=['GET', 'POST'])
def chat():
	if request.method == 'GET':
		all_posts = query_all_posts()
		all_posts = all_posts[::-1]
		return render_template('chatroom.html', all_posts = all_posts, login_session = login_session)

	else:
		author_name = request.form['author_name']
		title = request.form['title']
		content = request.form['content']

		add_post(author_name = author_name, title = title, content = content)
		all_posts = query_all_posts()
		all_posts = all_posts[::-1]
		return render_template('chatroom.html', all_posts = all_posts, login_session  = login_session)

@app.route("/tips")
def tips():
	return render_template('tips.html')

@app.route('/admin-login', methods=['POST'])
def admin_login():
	admin = get_admin(request.form['username'])
	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	if admin != None and admin.verify_password(request.form["password"]):
		login_session['name'] = admin.username
		login_session['logged_in'] = True
<<<<<<< HEAD
		return render_template('chatroom.html', login_session = login_session)
=======
		return render_template('chatroom.html', login_session = login_session, all_posts = all_posts)
>>>>>>> 98ee279424e53ee3160438f2839666f7c048c536
	else:
		return home()

@app.route('/admin-logout', methods = ['POST'])
def admin_logout():
	login_session['username'] = None
	return home()

@app.route('/delete/<int:post_id>', methods = ['POST'])
def delete_post(post_id):
	delete_post_by_id(post_id)
	all_posts = query_all_posts()
	all_posts = all_posts[::-1]
	return render_template('chatroom.html', all_posts = all_posts, login_session = login_session)

if __name__ == '__main__':
    app.run(debug=True)


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
		return render_template('chatroom.html', all_posts = all_posts)

	else:
		author_name = request.form['author_name']
		title = request.form['title']
		content = request.form['content']

		add_post(author_name = author_name, title = title, content = content)
		all_posts = query_all_posts()
		return render_template('chatroom.html', all_posts = all_posts)

@app.route("/tips")
def tips():
	return render_template('tips.html')

@app.route('/admin-login', methods=['POST'])
def admin_login():
	admin = get_admin(request.form['username'])
    if admin != None and admin.verify_password(request.form["password"]):
        login_session['name'] = user.username
        login_session['logged_in'] = True
        return render_template('chatroom.html', login_session = login_session)
    else:
        return home()


if __name__ == '__main__':
    app.run(debug=True)


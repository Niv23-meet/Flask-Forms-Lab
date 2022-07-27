from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)
app.config['T#%435']='NL^adLJW$y0'

username = "nivcaspi"
password = "111"
facebook_friends=["Tal","Noa","Roei", "Yuval", "Lia", "Avigail", "cindy", "adan"]


@app.route('/', methods = ['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		username_in = request.form['username']
		password_in = request.form['password']
		if username_in == username and password_in == password:
			return redirect(url_for('home'))
	return render_template('login.html')
  


@app.route('/home')
def home():
	return render_template('home.html', facebook_friends = facebook_friends)

@app.route('/friend/<string:f_name>', methods = ['GET', 'POST'])
def friends_exists(f_name):
	flag = False
	if f_name in facebook_friends:
		flag = True
	return render_template('friend_exists.html', f_name = f_name, flag = flag)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
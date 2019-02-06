from flask import *
from model import sum

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.php')

@app.route('/result', methods = ['GET','POST'])
def result():
	a = request.form['a']
	b = request.form['b']
	r = sum(int(a),int(b))
	return render_template("index.php",result = str(r))

# ==================== FOR GET

# from flask import *
# from model import sum
# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return render_template('index.php')

# @app.route('/result')
# def result():
# 	a = request.args.get('a')
# 	b = request.args.get('b')
# 	r = sum(int(a),int(b))
# 	return render_template("index.php",result = str(r))



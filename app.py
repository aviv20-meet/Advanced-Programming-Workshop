from database import *
from flask import *
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


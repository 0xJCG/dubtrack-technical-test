from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', method='POST')
def index():
    if request.method == 'POST':
        return render_template('search.html')
    return render_template('index.html')

@app.route('/channel/<int:ch_id>')
def index():
    return render_template('channel.html')

if __name__ == '__main__':
    app.run()

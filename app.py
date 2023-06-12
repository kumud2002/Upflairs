from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return 'HI'

@app.route('/chat')
def response():
    return render_template('mypage.html')

app.run(debug = True)
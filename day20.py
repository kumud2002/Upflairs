from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def some_function():
    return 'some message from string'

@app.route('/home/<name>')
def some_function2(name):
    print(name)
    return render_template('home.html', name_value = name)


app.run(debug = True)


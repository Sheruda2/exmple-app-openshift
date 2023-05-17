from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    age = request.form['age']
    address = request.form['address']
    return render_template('greeting.html', name=name, age=age, address=address)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

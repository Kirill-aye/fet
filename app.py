# pip install flask
# python -m pip install flask
# python -m pip install flask --user


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form['name'])
        return 'Form was sent'
    return render_template('index.html')

@app.route('/users/<name>')
def user_page(name):
    return render_template('user.html', name=name)


# @app.route('/users/milena')
# def user_milena():
#     return 'Hello, Milena!'



app.run(debug=True) # app.run('0.0.0.0', '3000', debug=True)

from flask import Flask,jsonify, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/home')
def home():
    """
    testing route
    :return: str
    """
    return jsonify(message='listen to me we will do this'), 200


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + " you are not old enough."), 401
    else:
        return jsonify(message="Welcome " + name + " You're old enough to visit the site")


@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + " You're not old enough!"), 401
    else:
        return jsonify(message="Welcome " + name + " You're in.")


@app.route('/not_found')
def not_found():
    return jsonify(message="Error page not found"), 404


if __name__ == '__main__':
    app.run()

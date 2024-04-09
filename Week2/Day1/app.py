from flask import Flask, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def hello():
    if request.method == 'POST':
        return 'Received a POST request!'
    elif request.method == 'PUT':
        return 'Received a PUT request!'
    elif request.method == 'DELETE':
        return 'Received a DELETE request!'
    else:
        return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)







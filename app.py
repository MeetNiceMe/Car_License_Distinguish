from flask import Flask,render_template, request,Response
import test1
import json

app = Flask(__name__)

def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/distinguish', methods=['POST'])
def distinguish():
    base64=request.form['base64']
    jsondata=test1.Distinguish(base64)
    print(jsondata)
    return Response_headers(jsondata['plate'])


if __name__ == '__main__':
    app.run()

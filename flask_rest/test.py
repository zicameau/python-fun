#!flask/bin/python
from flask import Flask,request

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index():
    return "Moved to /name.",301

@app.route('/name',methods = ['GET','POST'])
def name():
    if request.method !='POST':
        return "Only POST allowed."
    
    data = request.get_data()
    return "hello " + str(data)

if __name__ == '__main__':
    app.run(port=5000,debug=True)

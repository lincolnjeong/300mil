from flask import Flask
app = Flask (__name__)
 
@app.route('/')
def hello_world():
    return 'Hello, World!'
 
@app.route('/user/<userName>') # URL뒤에 <>을 이용해 가변 경로를 적는다
def hello_user(userName):
    return 'Hello, %s'%(userName)
 
if __name__ == "__main__":
    app.run()
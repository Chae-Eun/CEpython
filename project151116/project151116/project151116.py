from flask import Flask, redirect, url_for
#the name of the application package
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('./header.html')

@app.route('/hello/<username>')
def hello_world(username):
    #return 'Hello World!'+username
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return 'log in'

if __name__ == '__main__':
    #app.run()

    #debug를 True로 하면 볼 수 있음
    #배포할 때는 False로 해야함
    app.debug=True #소스 변경과 디버거 제공
    app.run(host="172.16.46.104")
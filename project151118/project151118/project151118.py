from flask import Flask, redirect, url_for, render_template
#the name of the application package
app = Flask(__name__)

@app.route('/')
def mainpage():
    return render_template('header.html')
    #return 'Hello World!'

#@app.route('/hello/')
#def hello():
#    return render_template('hello.html')    

@app.route('/hello/')
@app.route('/hello/<username>')
def hello_world(username=None):
    #data={
    #    'title' : 'Chaeeun\'s Server',
    #    'name' : username
    #}
    data=[dict(href="http://www.naver.com", caption="네이버"), dict(href="http://www.google.com", caption="구글")]
    return render_template('main.html', item=data)    

@app.route('/login')
def login():
    return 'log in'

if __name__ == '__main__':
    app.debug=True
    app.run(host="172.16.47.184")
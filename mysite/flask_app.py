from flask import Flask
from flask import render_template, redirect, url_for, request
import requests
import pymysql
import time

app = Flask(__name__)

def connectsql():
    #dev 환경
    if request.host == "localhost:5000" :
        conn = pymysql.connect(host='localhost', user = 'root', passwd = 'wndnjsWkd!2', db = 'userlist', charset='utf8')
    else :
        conn = pymysql.connect(host='iameeo.mysql.pythonanywhere-services.com', user = 'iameeo', passwd = 'wndnjsWkd!2', db = 'iameeo$iameeo_db', charset='utf8')
    return conn

@app.route('/')
def Index():
    path = 'Index'
    return render_template('Index.html', path=path)
    
@app.route('/Intro')
def Intro():
    path = 'Intro'
    return render_template('Intro.html', path=path)
    
@app.route('/Skill')
def Skill():
    path = 'Skill'
    return render_template('Skill.html', path=path)
    
@app.route('/Project')
def Project():
    path = 'Project'
    return render_template('Project.html', path=path)
    
@app.route('/Certification')
def Certification():
    path = 'Certification'
    return render_template('Certification.html', path=path)

#연락처 GET
@app.route('/Contact', methods=['GET'])
def Contact():
    path = 'Contact'
    return render_template('Contact.html', path=path)

#연락처 POST
@app.route('/Contact', methods=['POST'])
def Contact_Post():
    username = request.form['name']
    usertitle = request.form['title']
    usercontent = request.form['content']

    conn = connectsql()
    cursor = conn.cursor() 
    query = "INSERT INTO board (name, title, content, regdate) values (%s, %s, %s, now())"
    value = (username, usertitle, usercontent)
    cursor.execute(query, value)
    conn.commit()
    cursor.close()
    conn.close()

    slackMessage(username + "- " + usertitle)

    return redirect(url_for('Contact'))

def current_milli_time():
    return round(time.time() * 1000)
    
def slackMessage(text):
    url = 'https://hooks.slack.com/services/TMGE25VGT/B05GZRKLRU1/'
    url = url + '78IBMFJojDSDx6ON7wEXiOe7'
    payload = { "text" : text }

    requests.post(url, json=payload)

#@app.before_first_request
#def before_first_request():
#	print("앱 기동 후 첫번째 http 요청에 대한 응답")

#@app.before_request
#def before_request():
	#slackMessage()

#@app.after_request
#def after_request(response):		
#	print("http 요청이 처리된 뒤 실행")

#@app.teardown_request
#def teardown_request(exception):
#	print("http 요청의 결과가 브라우저에 응답된 뒤 호출")

#@app.teardown_appcontext
#def teardown_request(exception):
#	print("http 요청의 애플리케이션 컨택스트가 종료될 때 실행")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

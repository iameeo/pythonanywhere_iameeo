from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def Index():
    path = 'Index';
    return render_template('Index.html', path=path)
    
@app.route('/Intro')
def Intro():
    path = 'Intro';
    return render_template('Intro.html', path=path)
    
@app.route('/Skill')
def Skill():
    path = 'Skill';
    return render_template('Skill.html', path=path)
    
@app.route('/Project')
def Project():
    path = 'Project';
    return render_template('Project.html', path=path)
    
@app.route('/Certification')
def Certification():
    path = 'Certification';
    return render_template('Certification.html', path=path)
    
@app.route('/Contact')
def Contact():
    path = 'Contact';
    return render_template('Contact.html', path=path)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
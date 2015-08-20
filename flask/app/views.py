from flask import render_template
from app import app

import subprocess

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    return render_template('index.html',
                           user=user)




## Include scripts

# helloworld.py
@app.route('/scripts/helloworld')
def helloworld():
    cmd = ["ls","-l"]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              stdin=subprocess.PIPE)
    out, err = p.communicate()
    print(type(out))
    out = out.decode('utf-8')
    err = err.decode('utf-8')
    return render_template('index.html', out=out, err=err)
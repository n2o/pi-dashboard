from flask import render_template
from app import app

from pygments import highlight
from pygments.lexers import BashLexer
from pygments.formatters import HtmlFormatter

import subprocess


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


## Include scripts

# helloworld.py
@app.route('/scripts')
@app.route('/scripts/')
@app.route('/scripts/<script>')
def execute(script=None):
    """ Executes given script """
    if script:
        path = "app/scripts/"
        cmd = ["python3", path + script + ".py"]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        out, err = p.communicate()

        # If there is any response, format it for HTML
        if out:
            out = highlight(out.decode('utf-8'), BashLexer(), HtmlFormatter())
        if err:
            err = highlight(err.decode('utf-8'), BashLexer(), HtmlFormatter())

    else:
        out = None
        err = "Es wurde kein Skript angegeben."

    return render_template('index.html', out=out, err=err)
from flask import render_template, request, jsonify
from app import app

from pygments import highlight
from pygments.lexers import BashLexer
from pygments.formatters import HtmlFormatter

import subprocess


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


## Include scripts with AJAX
@app.route('/_exec')
def exec():
    """ Executes given script """
    script = request.args.get('script', None, type=str)

    if script:
        path = "app/scripts/"
        cmd = ["python3", path + script]
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  stdin=subprocess.PIPE)
        out, err = p.communicate()

        # If there is any response, format it for HTML
        if out:
            out = highlight(out, BashLexer(), HtmlFormatter())
        if err:
            err = highlight(err, BashLexer(), HtmlFormatter())

    else:
        out = None
        err = "Es wurde kein Skript angegeben."

    return jsonify(out=str(out), err=str(err))
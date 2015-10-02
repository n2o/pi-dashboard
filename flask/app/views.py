from flask import render_template, Response
from jinja2 import Environment, FileSystemLoader
from app import app
import re

from pygments import highlight
from pygments.lexers import BashLexer
from pygments.formatters import HtmlFormatter

import subprocess


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/stream/<script>')
def execute(script):
    def inner():
        assert re.match(r'^[a-zA-Z._-]+$', script)
        exec_path = "scripts/" + script + ".py"
        cmd = ["python3", "-u", exec_path]  # -u: don't buffer output

        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
        )

        for line in proc.stdout:
            yield highlight(line, BashLexer(), HtmlFormatter())

        yield "<script>parent.stream_finished()</script>"

    env = Environment(loader=FileSystemLoader('app/templates'))
    tmpl = env.get_template('stream.html')
    return Response(tmpl.generate(result=inner()))
from flask import render_template, Response
from jinja2 import Environment, FileSystemLoader
from app import app

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
        exec_path = "scripts/" + script + ".py"
        cmd = ["/usr/bin/env", "python3", "-u", exec_path]  # -u: don't buffer output

        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
        )

        for line in iter(proc.stdout.readline, ''):
            yield highlight(line, BashLexer(), HtmlFormatter())
            # If process is done, break loop
   #         if proc.poll() == 0:
   #             yield "<span id='stream_finished'></span>"
   #             break

    env = Environment(loader=FileSystemLoader('app/templates'))
    tmpl = env.get_template('stream.html')
    return Response(tmpl.generate(result=inner()))
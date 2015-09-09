from flask import render_template, stream_with_context, Response
from app import app

from pygments import highlight
from pygments.lexers import BashLexer
from pygments.formatters import HtmlFormatter

import subprocess
import psutil


pid = None


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/stream/<script>')
def execute(script):
    def inner():
        global pid

        path = "scripts/"
        exec_path = path + script + ".py"
        cmd = ["/usr/bin/env", "python3", "-u", exec_path]

        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
        )
        pid = proc.pid

        for line in iter(proc.stdout.readline, ''):
            # If process is done, break loop
            if not proc.poll() == 0:
                yield highlight(line, BashLexer(), HtmlFormatter())
            else:
                pid = None
                break

    return Response(stream_with_context(inner()), mimetype='text/html')  # text/html is required for most browsers to show the partial page immediately

@app.route('/kill-pid')
def kill_pid():
    global pid

    if pid:
        process = psutil.Process(pid)
        for proc in process.children(recursive=True):
            proc.kill()
        process.kill()
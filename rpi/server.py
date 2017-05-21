import subprocess

from flask import Flask
app = Flask(__name__)

IRSEND_COMMAND = ['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG']

@app.route("/")
def hello():
    return "Hi my name is LG!"

@app.route("/<command>")
def get_command(command):
    subprocess.call(['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG', command])
    return command

def switch_source(source):
    # not implemented

def send_command(command):
    IRSEND_COMMAND.append(command)
    subprocess.call(IRSEND_COMMAND)

if __name__ == "__main__":
    app.run(host='192.168.1.27',debug = False)

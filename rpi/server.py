from irChiefCommander import IrChiefCommander

import subprocess
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi my name is LG!"

@app.route("/tv/<command>")
def run_tv_command(command):
    IrChiefCommander.blast(command)
    return command

if __name__ == "__main__":
    app.run(host='192.168.1.27',debug = False)

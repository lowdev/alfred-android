from irChiefCommander import IrChiefCommander
from tvCommandInterpreter import TvCommandInterpreter

import subprocess
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi my name is LG!"

@app.route("/tv/<command>")
def run_tv_command(command):
    intent = TvCommandInterpreter.interpret(command)
    IrChiefCommander.blast(intent)
    return command

if __name__ == "__main__":
    app.run(host='192.168.1.27',debug = False)

import subprocess

class IrChiefCommander(object):
    "Blast ir command"

    @staticmethod
    def blast(command):
        subprocess.call(['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG', command])

    def blast(commands):
        for command in commands:
            blast(command)

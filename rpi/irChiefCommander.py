import subprocess

class IrChiefCommander(object):
    "Blast ir command"

    BASE_COMMAND = ['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG']

    @staticmethod
    def blast(command):
        subprocess.call(['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG', command])

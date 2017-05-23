import subprocess
import time

class IrChiefCommander(object):
    "Blast ir command"

    @staticmethod
    def oneBlast(command):
        subprocess.call(['irsend', '-d', '/run/lirc/lircd-lirc0', 'SEND_ONCE', 'LG', command])

    @staticmethod
    def blast(commands):
        for command in commands:
            print 'command:' + command
            if 'time' in command:
                print 'time: ' + command[4:]
                time.sleep(int(command[4:]))
                continue

            time.sleep(0.3)
            IrChiefCommander.oneBlast(command)

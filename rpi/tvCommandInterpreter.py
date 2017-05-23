class TvCommandInterpreter:
    "Try to know what you really want"

    @staticmethod
    def interpret(text):
        if text == 'av1':
            return ['tvrad', 'time1', 'input', 'input', 'KEY_OK']           

        if text == 'hdmi1':
            return ['tvrad', 'time1', 'input', 'input', 'input', 'KEY_OK']

        if text == 'hdmi2':
            return ['tvrad', 'time1', 'input', 'input', 'input', 'input', 'KEY_OK']

        return [text]

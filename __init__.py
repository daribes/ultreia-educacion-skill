from mycroft import MycroftSkill, intent_file_handler


class UltreiaEducacion(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('educacion.ultreia.intent')
    def handle_educacion_ultreia(self, message):
        self.speak_dialog('educacion.ultreia')


def create_skill():
    return UltreiaEducacion()


from behavioral_patterns.mediator.controllers.chat_room import ChatRoom


class User:

    def __init__(self, name):
        self.name = name
        self.chat_room = ChatRoom()

    def send_message(self, message):
        return self.chat_room.display_message(self.name, message)

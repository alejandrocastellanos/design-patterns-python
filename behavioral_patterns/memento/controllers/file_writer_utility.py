from behavioral_patterns.memento.controllers.memento import Memento


class FileWriterUtility:

    def __init__(self, file):
        self.file = file
        self.content = ''

    def write(self, string):
        self.content += string

    def save(self):
        return Memento(self.file, self.content)

    def undo(self, memento):
        self.file = memento.file
        self.content = memento.content

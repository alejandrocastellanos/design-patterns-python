class FileWriterCaretaker:

    def __init__(self):
        self.obj = ''

    def save(self, writer):
        self.obj = writer.save()

    def undo(self, writer):
        writer.undo(self.obj)

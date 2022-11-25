from behavioral_patterns.memento.controllers.file_writer_caretaker import FileWriterCaretaker
from behavioral_patterns.memento.controllers.file_writer_utility import FileWriterUtility


def test_memento():
    caretaker = FileWriterCaretaker()
    writer = FileWriterUtility("myfile.txt")

    writer.write("First comment in file")
    content_1 = writer.content
    caretaker.save(writer)
    writer.write("Second comment in file")
    caretaker.undo(writer)
    content_2 = writer.content

    assert content_1 == "First comment in file"
    assert content_2 == "First comment in file"

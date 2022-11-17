from structural_patterns.composite.controllers.file_component import FileComponent
from structural_patterns.composite.controllers.folder_component import FolderComponent


def test_folder_component():
    photo_file = FileComponent('my_photos.jpg', 10)
    report_file = FileComponent('reports.xlsx', 45)

    elements = FolderComponent('My elements', [photo_file, report_file])

    total_size = elements.get_size()

    assert total_size == 55
    assert photo_file.get_size() == 10
    assert report_file.get_size() == 45

from abstract_factory.controller import Instrumentalist


def test_instrumentalist_jungle_location():
    instrumentalist = Instrumentalist('jungle')
    instrumentalist.select_tools()

    assert instrumentalist.cutting_tool == 'Knife'
    assert instrumentalist.drying_tool == 'Rag'


def test_instrumentalist_operating_room_location():
    instrumentalist = Instrumentalist('operating room')
    instrumentalist.select_tools()

    assert instrumentalist.cutting_tool == 'Scalpel'
    assert instrumentalist.drying_tool == 'Compress'


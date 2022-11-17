from creational_patterns.abstract_factory.controller import Instrumentalist, Surgeon


def test_surgeon_in_operating_room():
    instrumentalist = Instrumentalist('operating room')
    instrumentalist.select_tools()

    surgeon = Surgeon(instrumentalist)

    assert instrumentalist.cutting_tool == 'Scalpel'
    assert instrumentalist.drying_tool == 'Compress'
    assert surgeon.operate() == 'Operating with Scalpel and Compress'


def test_surgeon_in_jungle():
    instrumentalist = Instrumentalist('jungle')
    instrumentalist.select_tools()

    surgeon = Surgeon(instrumentalist)

    assert instrumentalist.cutting_tool == 'Knife'
    assert instrumentalist.drying_tool == 'Rag'
    assert surgeon.operate() == 'Operating with Knife and Rag'

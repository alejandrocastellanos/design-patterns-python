from adapter.controllers.plug_description.europa_plug_description import EuropaPlugDescription


def test_europa_plug_ok():
    europa_plug_description = EuropaPlugDescription()
    name, type = europa_plug_description.description()
    assert name == 'Europa'
    assert type == 'Plug b type'


def test_europa_plug_ok():
    europa_plug_description = EuropaPlugDescription()
    name, type = europa_plug_description.description()
    assert name != 'America'

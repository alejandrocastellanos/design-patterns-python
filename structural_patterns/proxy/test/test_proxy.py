from structural_patterns.proxy.controller.secured_door import SecuredDoor


def test_proxy():
    secured_door = SecuredDoor()
    open_door = secured_door.open_door()

    assert open_door == 'Open door from Door class'

from structural_patterns.bridge.controllers.implementer.linux_implementer import LinuxImplementer
from structural_patterns.bridge.controllers.implementer.windows_implementer import WindowsImplementer
from structural_patterns.bridge.controllers.interface.linux_interface import Linux
from structural_patterns.bridge.controllers.interface.windows_interface import Windows


def test_bridge_windows():
    w = Windows(WindowsImplementer())
    io_windows = w.operate()

    assert io_windows == 'Windows IOS implementer!'


def test_bridge_linux():
    w = Linux(LinuxImplementer())
    io_linux = w.operate()

    assert io_linux == 'Linux IOS implementer!'

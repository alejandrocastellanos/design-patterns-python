from structural_patterns.facade.controllers.washing_machine import WashingMachine


def test_facade():
    washing_machine = WashingMachine()
    wash, rinse, spin = washing_machine.start_washing()

    assert wash == 'Washing...'
    assert rinse == 'Rinsing...'
    assert spin == 'Spinning...'

from structural_patterns.facade.controllers.rinsing import Rinsing
from structural_patterns.facade.controllers.spinning import Spinning
from structural_patterns.facade.controllers.washing import Washing


class WashingMachine:
    ''' Facade '''

    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()

    def start_washing(self):
        wash = self.washing.wash()
        rinse = self.rinsing.rinse()
        spin = self.spinning.spin()
        return wash, rinse, spin


class BaseFactory:

    def __init__(self):
        self.name = None

    def add_tires(self):
        # add tires
        pass

    def add_frame(self):
        # add frame
        pass

    def description(self):
        tires = self.add_tires()
        frame = self.add_frame()
        return self.name, tires, frame

from behavioral_patterns.template_method.controllers.make_meal import MakeMeal


class MakeSoup(MakeMeal):

    def prepare(self):
        return 'Prepare Soup'

    def cook(self):
        return 'Cook Soup'

    def eat(self):
        return 'Eat Soup'

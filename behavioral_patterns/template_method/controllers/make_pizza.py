from behavioral_patterns.template_method.controllers.make_meal import MakeMeal


class MakePizza(MakeMeal):

    def prepare(self):
        return 'Prepare Pizza'

    def cook(self):
        return 'Cook Pizza'

    def eat(self):
        return 'Eat Pizza'

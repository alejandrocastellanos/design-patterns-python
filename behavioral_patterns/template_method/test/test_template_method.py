from behavioral_patterns.template_method.controllers.make_pizza import MakePizza


def test_template_method():
    make_pizza = MakePizza()

    prepare, cook, eat = make_pizza.go()
    assert prepare == 'Prepare Pizza'
    assert cook == 'Cook Pizza'
    assert eat == 'Eat Pizza'

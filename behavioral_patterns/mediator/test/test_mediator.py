from behavioral_patterns.mediator.controllers.user import User


def test_mediator():
    molly = User("Molly")
    mark = User("Mark")
    ethan = User("Ethan")

    message_1 = molly.send_message("Hi team! Meeting at 3 PM today")
    message_2 = mark.send_message("Roger that!")
    message_3 = ethan.send_message("Alright!")

    assert message_1 == "[Molly says]: Hi team! Meeting at 3 PM today"
    assert message_2 == "[Mark says]: Roger that!"
    assert message_3 == "[Ethan says]: Alright!"

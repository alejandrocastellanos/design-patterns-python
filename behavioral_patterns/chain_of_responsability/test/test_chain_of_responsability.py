from behavioral_patterns.chain_of_responsability.controllers.payment import Payment


def test_chain_of_responsability():
    payment = Payment(payment=55)
    apply_payment = payment.apply_payment()

    assert apply_payment == 15


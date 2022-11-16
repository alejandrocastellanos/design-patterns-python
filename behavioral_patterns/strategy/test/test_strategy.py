from strategy.controllers.on_sale_discount import on_sale_discount
from strategy.controllers.item import Item
from strategy.controllers.twenty_percentaje_discount import twenty_percentaje_discount


def test_strategy():
    price = 2000

    result_item_without_discount = Item(price).price_after_discount()
    result_twenty_percentaje_discount = Item(price, discount_strategy=twenty_percentaje_discount).price_after_discount()
    result_on_sale_discount = Item(price, discount_strategy=on_sale_discount).price_after_discount()

    assert result_item_without_discount == 2000
    assert result_twenty_percentaje_discount == 1600
    assert result_on_sale_discount == 1480
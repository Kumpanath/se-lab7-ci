from order import total_price


def test_normal_order():
    items = [("ข้าวกะเพรา", 50), ("ชาเย็น", 30)]
    assert total_price(items, 10) == 90


def test_empty_cart():
    assert total_price([], 10) == 10


def test_zero_delivery_fee():
    items = [("ข้าวกะเพรา", 50)]
    assert total_price(items, 0) == 50

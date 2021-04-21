from views.products import get_default_products


def test_get_default_products():
    products = get_default_products()
    assert all(map(lambda k: isinstance(k, int), products))

import pytest
from Invoice import Invoice


@pytest.fixture()
def products():
    products = {'Pen': {'qnt': 10, 'unit_price': 3.75, 'discount': 5},
                'Notebook': {'qnt': 5, 'unit_price': 7.5, 'discount': 10}}
    return products

@pytest.fixture()
def invoice():
    invoice = Invoice()
    return invoice

def test_CanCalucateTotalRoughImpurePrice(invoice, products):
    invoice.totalRoughImpurePrice(products)
    assert invoice.totalRoughImpurePrice(products) == 75.00

def test_CanCalucateTotalRoundImpurePrice(invoice, products):
    invoice.totalRoundImpurePrice(products)
    assert invoice.totalRoundImpurePrice(products) == 75

#def test_CanCalucateTotalImpurePrice(invoice, products):
#    invoice.totalImpurePrice(products)
#    assert invoice.totalImpurePrice(products) == 75

def test_CanCalucateTotalRoundDiscount(invoice, products):
    invoice.totalRoundDiscount(products)
    assert invoice.totalRoundDiscount(products) == 1.88

def test_CanCalucateTotalRoughDiscount(invoice, products):
    invoice.totalRoughDiscount(products)
    assert invoice.totalRoughDiscount(products) == 1.875

#def test_CanCalucateTotalDiscount(invoice, products):
#    invoice.totalDiscount(products)
#    assert invoice.totalDiscount(products) == 1.88

def test_CanCalucateTotalPurePrice(invoice, products):
    invoice.totalPurePrice(products)
    assert invoice.totalPurePrice(products) == 73.12

def test_CanCalculateTotalCount(invoice, products):
    invoice.totalCount(products)
    assert invoice.totalCount(products) == 15.00

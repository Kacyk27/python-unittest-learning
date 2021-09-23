import unittest
from product import Product


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("milk",3.0)


    def test_get_product_name(self):
        self.assertEqual(self.product.name,"milk")

    def test_get_product_price(self):
        self.assertEqual(self.product.price,3.0)

    def test_get_quantity(self):
        self.assertEqual(self.product.quantity,1)
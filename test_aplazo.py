import unittest
from data.base.webdriver import WebdriverHandler
from page_object.add_products_to_carts import add_items
from helpers.generate_number_product_random import generate_numbert_random
from page_object.cart import cart
from page_object.checkout import checkout

class MyTestCase(unittest.TestCase, WebdriverHandler):

    def setUp(self):
        self.my_class_instance = MyTestCase()
        # Inicia  el navegador.
        WebdriverHandler.__init__(self)
        self.driver.get("https://www.demoblaze.com/")




    def tearDown(self):
        # Este método se ejecuta después de cada prueba
        self.driver.quit()



    # def test_add_products_to_cart(self):
    #     number_produtcs = generate_numbert_random()
    #     add_items(self.driver, self.wait, number_produtcs)
    #     number_produtcs_in_cart = cart(self.driver, self.wait)
    #     self.assertEqual(number_produtcs, number_produtcs_in_cart, "Error la cantidad de productos no coincide")

    def test_buy_one_item_complete(self):
        number_produtcs = 1
        add_items(self.driver, self.wait, number_produtcs)
        number_produtcs_in_cart = cart(self.driver, self.wait)
        self.assertEqual(number_produtcs, number_produtcs_in_cart, "Error la cantidad de productos no coincide")
        number_order = checkout(self.driver, self.wait)
        self.assertIsNotNone(number_order, "Error: No se ha generado la compra ")


MyTestCase()
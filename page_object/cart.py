import time
def cart(driver, wait):
    time.sleep(2)
    cart_nav_bar = wait.waitForElement(locator="//a[contains(text(), 'Cart')]", locatorType='xpath')
    driver.get("https://www.demoblaze.com/cart.html")
    time.sleep(2)
    for n in range(1,16):
        product = wait.waitForElement(locator=f'//*[@id="tbodyid"]/tr[{n}]/td[2]', locatorType='xpath')
        if product is None:
            products_in_cart = n-1
            print(f"Pruductos in cat {products_in_cart}")
            return products_in_cart # Devuelve la cantidad de productos en el carrito

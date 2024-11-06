import time

def add_items(driver, wait,number_products):
    total_page = (number_products//9)+1
    time.sleep(2)
    print(f"total de paginas {total_page}")
    p = None
    for _ in range(total_page):
        for n in range(1, number_products+1):
            if n > 9:
                next_page = wait.waitForElement(locator="//button[contains(text(), 'Next')]", locatorType='xpath')
                wait.click(next_page)
                time.sleep(4)
                driver.execute_script("window.scrollBy(0,	-300);	")
                print(f"numero n:{n}")
                p = 1
            if p is not None:
                product = wait.waitForElement(locator=f'//*[@id="tbodyid"]/div[{p}]/div/a/img', locatorType='xpath')
                wait.click(product)
                time.sleep(1)
                p = p +1
            else:
                product = wait.waitForElement(locator=f'//*[@id="tbodyid"]/div[{n}]/div/a/img', locatorType='xpath')
                wait.click(product)
                time.sleep(1)
            add_to_cart_buttom = wait.waitForElement(locator="//a[contains(text(), 'Add to cart')]", locatorType='xpath')
            wait.click(add_to_cart_buttom)
            time.sleep(1)
            try:
                alert = driver.switch_to.alert
                # Acepta la alerta (haz clic en el botón "Aceptar")
                alert.accept()
                time.sleep(1)
                driver.back()
                driver.back()
            except:
                pass



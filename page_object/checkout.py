import time

def checkout(driver, wait):
    buttom_placer_order = wait.waitForElement(locator="//button[contains(text(), 'Place Order')]", locatorType='xpath')
    wait.click(buttom_placer_order)
    name_input = wait.waitForElement(locator="name")
    wait.sendKeys("Test", name_input)
    country_input = wait.waitForElement(locator="country")
    wait.sendKeys("country", country_input)
    city_input = wait.waitForElement(locator="city")
    wait.sendKeys("Ciudad de Mexico", city_input)
    card_input = wait.waitForElement(locator="card")
    wait.sendKeys("4111-1111-1111-1111", card_input)
    month_input = wait.waitForElement(locator="month")
    wait.sendKeys("12", month_input)
    year_input = wait.waitForElement(locator="year")
    wait.sendKeys("2025", year_input)
    buttom_purchase = wait.waitForElement(locator="//button[contains(text(), 'Purchase')]", locatorType='xpath')
    wait.click(buttom_purchase)
    time.sleep(2)
    code_success = wait.waitForElement(locator="//h2[contains(text(), 'Thank you for your purchase!')]", locatorType='xpath')
    return code_success


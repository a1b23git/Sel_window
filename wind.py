from selenium import webdriver
import time
import os
import math

link = "http://suninjuly.github.io/redirect_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
   
    x = x_element.text

    y = calc(x)

    input4 = browser.find_element_by_id('answer')
    input4.send_keys(y)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

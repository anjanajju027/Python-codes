import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
radios=driver.find_elements(By.XPATH,"//input[@type='radio']")
time.sleep(3)
for radio in radios:
    if radio.get_attribute("class")=="radioButton":
        radio.click()
        radio.is_selected()
    break

# 2 way to do it for the click of radio button
radiobuttons=driver.find_elements(By.CSS_SELECTOR,".radioButton")
radiobuttons[1].click()
assert radiobuttons[1].is_selected()

#hide button
driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
assert not driver.find_element(By.ID,"displayed-text").is_displayed()# assert not is used to that it is not working



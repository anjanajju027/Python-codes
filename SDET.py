from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()

driver.get("https://www.countries-ofthe-world.com/capitals-of-the-world.html")
wait=WebDriverWait (driver,10)
driver.switch_to.frame("cf-chl-widget-ulbs0")
wait.until((expected_conditions.presence_of_element_located(By.XPATH,"//input[@type='checkbox']"))).click()
driver.find_element(By.XPATH,"//td[contains(text(),'Afghanistan')]/following-sibling::*").get_attribute()
input("Press Enter to close the browser...")

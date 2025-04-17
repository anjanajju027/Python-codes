from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.XPATH,"//div[text()='Apple']")
colum=driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
fruit=driver.find_element(By.XPATH,"//div[text()='Fruit Name']").get_attribute("cell-2-undefined")
print(colum)
print(fruit)
driver.close()
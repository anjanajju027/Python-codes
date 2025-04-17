from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,".radioButton").click()
driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1").is_selected()
checkboxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
wait=WebDriverWait (driver,5)
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        checkbox.is_selected()
    break

driver.close()


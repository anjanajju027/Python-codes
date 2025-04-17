
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce")
driver.find_element(By.ID,"tinymce").send_keys("able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"#content > div > h3"))
driver.close()


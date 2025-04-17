import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
from selenium.webdriver import ActionChains
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#action=ActionChains(driver)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
time.sleep(2)
#/html/body/div[4]/div/fieldset/div/div/a[1]
#body > div:nth-child(6) > div > fieldset > div > div > a:nth-child(1)
action.context_click(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
time.sleep(2)
action.click(driver.find_element(By.CSS_SELECTOR,".radioButton")).click().perform()
##radio-btn-example > fieldset > label:nth-child(2) > input
time.sleep(3)
driver.find_element(By.ID,"autocomplete").send_keys("india")
#//*[@id="autocomplete"]

driver.close()



source1 = driver.find_element(By.ID,"id")
target1 = driver.find_element(By.ID,"id")

action.drag_and_drop(source1, target1).perform()




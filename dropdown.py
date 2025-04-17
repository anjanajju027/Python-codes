import time
from selenium.webdriver.support.ui import Select


from selenium import webdriver
from selenium.webdriver.common.by import By
name= "Anjan"
driver = webdriver.Chrome()
driver.implicitly_wait(2)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
drop = driver.find_element(By.ID, "dropdown-class-example")
menu = Select(drop)
menu.select_by_visible_text("Option3")


#input("Press Enter to close the browser...")
driver.close()

#driver.find_element(By.ID,"alertbtn").click()
#alert=driver.switch_to.alert
#alertText= alert.text
#print(alertText)
#assert name in alertText

#alert.accept()


# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get current_window_handle
print(driver.current_window_handle)

















from selenium import webdriver
from selenium.webdriver.common.by import By
veggie_list=[]
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//span[text()='Discount price']").click()# click on the table to get sorted list
elements=driver.find_elements(By.XPATH,"//tr/td[3]")# collecting the elements on the sorted list
for ele in elements:
    veggie_list.append(ele.text)
originallist=veggie_list.copy()
print(ele.text)

veggie_list.sort()

assert originallist==veggie_list

print(veggie_list)
print(originallist)
driver.close()






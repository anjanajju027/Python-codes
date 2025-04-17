from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
file_path= "C:\\Users\\vijaykeshavarayudu\\Downloads\\download.xlsx"
driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,"downloadButton").click()

#edit the excel data

file_input=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file_input.send_keys(file_path)

wait=WebDriverWait(driver,5)
toast_locator=driver.find_element(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(toast_locator))
type=driver.find_element(By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)").text
print(type)



items=0

if items != 2: #raise Exception("not matching")
    pass

#assert (items==2)

try:
    a=1
    if a==5:
        pass

except:
    print("check the a value")



finally:
    print("anjan")


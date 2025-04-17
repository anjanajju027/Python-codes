from selenium import webdriver
driver = webdriver.Chrome()
chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(2)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,600)")
driver.get_screenshot_as_file("scree.png")
print(driver.title)
driver.close()



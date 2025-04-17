from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
#driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")
#driver.get("url")
# Find the search box and type "Python"
search_box = driver.find_element("name", "q")
#driver.find_element(By.NAME)
search_box.send_keys("Python")
search_box.send_keys(Keys.RETURN)  # Press Enter to search
# Wait for results to load
time.sleep(2)
# Find all links in the search results
search_results = driver.find_elements("xpath", "//h3[@class='LC20lb MBeuO DKV0Md']")
# Open each link in a new tab
for result in search_results:
    # Open a new tab
    driver.execute_script("window.open('');")
    #driver.execute_script("w")
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    # Get the link and open it
    link = result.find_element("xpath", "..").get_attribute("href")
    driver.get(link)
    # Wait for the page to load
    time.sleep(2)
    # Print the title of the page
    print(driver.title)
# Close the browser after a brief pause
time.sleep(5)
driver.quit()


# driver = webdriver.Chrome()
#driver.get(url)
#search = driver.find_element(By.XPATH,"q")
#search.send_Keys("Python")
#search.send_Keys(Keys.RETURN)
#search_results = driver.find_elements(By.ID,"common for all links")
# for res in search_results:
#driver.execute_script("window.open('');")
#driver.switch_to_window(driver.window_handles[-1])
#link = res.find_element(By.XPATH,"").get_attribute("herf")
#driver.get(link)
#print(driver.title)

#driver.get_window_size()
#driver
#driver.current_window_handle
#driver.window_handles
#driver.switch_to_window
#driver.switch_to_window[-1]
#Get Current Window Handle: driver.current_window_handle
#Get All Window Handles: driver.window_handles
#Switch to Another Window: driver.switch_to.window(window_handle)
#Close a Specific Window: driver.close()
#Switch Back to Parent Window: driver.switch_to.window(parent_window_handle)
#Loop Through Multiple Windows: for window in driver.window_handles
#Handle Modal Popups: Switch to modal window and perform actions, then switch back to main window.


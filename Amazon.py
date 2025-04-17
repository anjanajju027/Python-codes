from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the driver (make sure to specify the path to your WebDriver if necessary)
driver = webdriver.Chrome()  # or any other driver you are using

try:
    driver.get(
        "https://www.amazon.in/?tag=msndeskstdin-21&ref=pd_sl_i256xpxde_e&adgrpid=1319415610409622&hvadid=82463739609610&hvnetw=o&hvqmt=e&hvbmt=be&hvdev=c&hvlocint=&hvlocphy=116074&hvtargid=kwd-82464408133329:loc-90&hydadcr=5622_2377266&msclkid=22b53643ee751fe2a70250beeffd54c5")
    driver.maximize_window()

    # Wait for the search box to be visible and input the search term
    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']"))
    )
    search_box.send_keys("neemans")

    # Wait for the search results to load and display products
    search_button = driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']")
    search_button.click()

    # Wait for the products to load and find the desired product
    products = WebDriverWait(driver, 10).until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@data-component-type='s-search-result']"))
    )

    for product in products:
        product_name = product.find_element(By.XPATH, ".//span[@class='a-size-medium a-color-base a-text-normal']").text
        if "neemans" in product_name.lower():
            product.find_element(By.XPATH, ".//h2/a").click()
            break  # Exit the loop after clicking the desired product

    # Wait for the product image to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "(//img[@class='s-image'])[1]"))
    )

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()  # Close the browser when done

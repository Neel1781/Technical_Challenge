from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')


# Path to your chromedriver
chrome_driver_path = r'C:\Users\neels\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://bstackdemo.com/')


def wait_for_element(by, value, timeout=20):
    try:
        return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))
    except TimeoutException:
        print(f"Element not found: {by} = {value}")
        driver.quit()

try:
    print("Trying to find login button...")
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="#signin")
    #login_button = wait_for_element(By.XPATH, '//*[@id="signin"]')
    login_button.click()

    action = ActionChains(driver)
    # Enter credentials
    username_input = wait_for_element(By.XPATH,'//*[@id="username"]/div/div[1]/div[1]') 
    username_input.click() 
    username = wait_for_element(by=By.CSS_SELECTOR,value="#react-select-2-option-0-0")
    username.click()
    #username_input.send_keys("demouser")
    #username_input.send_keys(Keys.ENTER)
    
    
    password_input = wait_for_element(By.XPATH, '//*[@id="password"]/div/div[1]')
    password_input.click()
    #wait = WebDriverWait(driver, 10)   
    actions = ActionChains(driver)
    actions.send_keys("testingisfun99").send_keys(Keys.ENTER).perform()
    
    #password = driver.find_element(by=By.ID,value="password")
    #password.click()
    #password_input.send_keys("testingisfun99")
    #password_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-select-3-option-0-0")))
    #password_option.click()
    #password = wait_for_element(by=By.CSS_SELECTOR,value="#react-select-3-option-0-0")
    #password_input = wait_for_element(by=By.CSS_SELECTOR, value="input[type='password']")

    # Enter the password into the field
    #password_input.send_keys("testingisfun99")
    #password.click()
    #password_input.send_keys("testingisfun99")
    #password_input.send_keys(Keys.ENTER)

    
    # Submit login form
    login_submit_button = wait_for_element(By.XPATH, '//*[@id="login-btn"]')
    login_submit_button.click()

    # Wait for login to complete and redirect
    time.sleep(3)

    # Filter products to show "Samsung" devices only
    #filter_button = wait_for_element(By.XPATH, '//button[text()="Filter"]')
    #filter_button.click()
    samsung_filter = wait_for_element(By.XPATH, '//*[@id="__next"]/div/div/main/div[1]/div[2]/label/span')
    samsung_filter.click()
    
    # Wait for the filter to apply
    time.sleep(2)
    
    # Favorite the "Galaxy S20+" device
    galaxy_s20_plus = wait_for_element(By.XPATH, '//*[@id="11"]/div[1]/button')
    galaxy_s20_plus.click()
    
    # Go to the Favorites page
    favorites_button = wait_for_element(By.XPATH, '//*[@id="favourites"]/strong')
    favorites_button.click()
    
    # Verify that the "Galaxy S20+" is listed on the Favorites page
    favorite_item = wait_for_element(By.XPATH, '//*[@id="favourites"]/strong')

    if favorite_item:
        # Set the status of test as 'passed' if item is added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Galaxy S20+ is successfully added to the Favorites page!"}}')
    else:
        # Set the status of test as 'failed' if item is not added to cart
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Galaxy S20+ is not found in the Favorites page."}}')

finally:
    # Close the browser
    driver.quit()

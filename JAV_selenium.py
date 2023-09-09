from selenium import webdriver
import time
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

driver.get("https://javmodel.com/jav/homepages.php?")
driver.maximize_window()

time.sleep(3)

element = driver.find_element("link text", "Akiho Yoshizawa")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

# create action chain object    
action = ActionChains(driver)

# click the item
action.click(on_element = element)

# Capture the current URL
current_url = driver.current_url

# perform the operation
action.perform()

# Print or return the URL
print("The current URL is:", current_url)
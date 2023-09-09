from selenium import webdriver
import time
import requests
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

driver.get("https://javmodel.com/jav/homepages.php?")
driver.maximize_window()

element = driver.find_element("element", "img src")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

time.sleep(3)

# create action chain object    
action = ActionChains(driver)

# click the item
action.click(on_element = element)

# perform the operation
action.perform()

time.sleep(5)

# Capture the current URL
current_url = driver.current_url

# Print or return the URL
print("The current URL is:", current_url)

# Assuming the image has an id attribute "someImageId"
img_element = driver.find_element(By.CLASS_NAME, "veryclear")

# Get the image source URL
img_url = img_element.get_attribute('src')

# Download the image
response = requests.get(img_url)

# Check if the request was successful
if response.status_code == 200:
    # Save the image
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print("Failed to download the image.")

# Close the driver
driver.quit()
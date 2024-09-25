from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
from io import BytesIO
from PIL import Image
import pytesseract
import time

# Assuming you have a Chrome webdriver installed. Download from: https://sites.google.com/chromium.org/driver/
driver = webdriver.Chrome()

url = 'https://www.pxw1.snb.ca/snb9000/product.aspx?ProductID=A014SN9000a&l=e'
driver.get(url)

# Locate the dropdown element by its ID, name, XPath, or other locators
dropdown_element = driver.find_element(By.ID, "DEX_TestTypeID")

# Create a Select object
dropdown = Select(dropdown_element)

# Example 3: Select by value attribute
dropdown.select_by_value("4")


# Wait for the checkbox to be present in the DOM
checkbox_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "confirmeligible"))
)
driver.execute_script("arguments[0].click();", checkbox_element)



# Locate the dropdown element by its ID, name, XPath, or other locators
dropdown_element = driver.find_element(By.ID, "ResourceID")

# Create a Select object
dropdown = Select(dropdown_element)

# Example 3: Select by value attribute
dropdown.select_by_value("20")

# Wait for the radio buttons to be present in the DOM
radio_buttons_locator = (By.NAME, "DEX_LangChoice")

# Wait for a maximum of 10 seconds for at least one radio button to be present
radio_button_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(radio_buttons_locator)
)

# Iterate through radio buttons and select the one you want
for radio_button in radio_button_elements:
    if radio_button.get_attribute('value') == 'EN':
        radio_button.click()
        break    

# Locate the captcha image element
captcha_img = driver.find_element(By.XPATH, "//div[@class='DivCellRight50']/img")

# Get the captcha image source URL
captcha_img_src = captcha_img.get_attribute("src")

# Download the captcha image
captcha_img_url = driver.current_url + captcha_img_src
response = requests.get(captcha_img_url, stream=True)

# Check for redirects
print("Final URL:", response.url)

# Ensure the request was successful before proceeding
if response.status_code == 200:
    # Save the response content for debugging
    with open("response_content.html", "w", encoding="utf-8") as f:
        f.write(response.text)
else:
    print(f"Failed to retrieve captcha image. Status code: {response.status_code}")

# Use Tesseract OCR to extract text from the captcha image
# captcha_text = pytesseract.image_to_string(img)

# Input the captcha text into the text box
# captcha_input = driver.find_element(By.ID, "DEX_captcha")
# captcha_input.send_keys(captcha_text)


# Submit the form
driver.find_element(By.NAME, '_ctl4:DEX_btnSubmit').click()

# Wait for some time to let the page load (you may need to adjust this based on the actual page)
# time.sleep(5)

# Assuming the page redirects to another website, you can get the new URL
new_url = driver.current_url

# Do further actions on the redirected page if needed

# Close the browser
driver.quit()

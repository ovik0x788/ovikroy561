LOvvcxv zv 
cascxfrom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome browser using Selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("user-data-dir=C:\Users\x auto\AppData\Local\Google\Chrome\User Data\Profile 3")
driver = webdriver.Chrome(chrome_options=chrome_options)

# Open a specific webpage
driver.get("https://galxe.com/bloXroute/campaign/GConAtwk1b")

# Find and click the "Follow @bloXrouteLabs on Twitter" button
follow_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Like @bloXrouteLabs Tweet')]")
follow_button.click()

# Wait for the popup window to appear
# You may need to adjust the wait time depending on your webpage
popup_window = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Switch to the popup window
popup_window_handle = driver.window_handles[1]  # Assuming the popup window is the second window
driver.switch_to.window(popup_window_handle)

# Perform any actions on the popup window if needed
# For example, you can close the popup window
driver.close()

# Switch back to the main window
main_window_handle = driver.window_handles[0]
driver.switch_to.window(main_window_handle)

# Find and click the "Follow @bloXrouteLabs on Twitter" button
follow_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Retweet the Tweet')]")
follow_button.click()

# Wait for the popup window to appear
# You may need to adjust the wait time depending on your webpage
popup_window = WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))

# Switch to the popup window
popup_window_handle = driver.window_handles[1]  # Assuming the popup window is the second window
driver.switch_to.window(popup_window_handle)

# Perform any actions on the popup window if needed
# For example, you can close the popup window
driver.close()

# Do some random task
# ...

# Reload the page
driver.refresh()

# Click the claim button
claim_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Claim')]")
claim_button.click()

# Close the browser
driver.quit()
bxcvb

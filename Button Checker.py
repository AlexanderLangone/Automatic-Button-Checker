from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome()

# Open the webpage where the buttons are located
url = "https://howtobuyahouse.wpengine.com"  # Replace with your webpage URL
driver.get(url)

# Find all header menu options with the class "menu-text"
menu_options = driver.find_elements(By.CLASS_NAME, "menu-item")

# Initialize counters
total_buttons_attempted = 0
total_buttons_worked = 0

# Loop through each menu option
for menu_option in range(len(menu_options)):
    menu_options = driver.find_elements(By.CLASS_NAME, "menu-item")

    # Click on the menu option to reveal its content
    menu_options[menu_option].click()
    time.sleep(2)  # Give the content time to load, you can adjust this value
    
    # Get the original window handle
    original_window = driver.window_handles[0]

    # Find all buttons with the class name "fusion-button"
    buttons = driver.find_elements(By.CLASS_NAME, "fusion-button")
    
    # Loop through each button in the section
    for button in buttons:

        # Get the current page URL before clicking the button
        current_page_url = driver.current_url

        # Increment the attempted buttons counter
        total_buttons_attempted +=1

        # Click on the button
        button.click()
        time.sleep(1)  # Give time for any action or animation to take place

        if len(driver.window_handles) == 0 | len(driver.window_handles) == 1:
            if current_page_url != driver.current_url:
            # Button worked (page switched), increment the worked buttons counter
                total_buttons_worked += 1
                driver.back()

        # Check if a new tab or window was opened
        if len(driver.window_handles) > 1:
            # Switch to the new window
            driver.switch_to.window(driver.window_handles[1])
            
            # Close the new tab or window
            driver.close()
            time.sleep(1)

            # Switch back to the original window
            driver.switch_to.window(original_window)

            total_buttons_worked += 1
                
        time.sleep(1)  # Give time for any action or animation to take place
        # Add your button validation or tracking code here

    buttons = driver.find_elements(By.CLASS_NAME, "fusion-button")

# Close the browser
driver.quit()

# Print the tracking results
print(f"Total buttons attempted: {total_buttons_attempted}")
print(f"Total buttons that worked: {total_buttons_worked}")


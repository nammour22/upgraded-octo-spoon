from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    # Open GitHub login page
    driver.get("https://github.com/login")

    # Wait to ensure the page loads completely
    time.sleep(3)  # Simple wait (3 seconds)

    # Take a screenshot of the login page
    driver.save_screenshot("github_login_page.png")
    print("Screenshot of login page saved!")

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot("error_loading_page.png")
    print("Screenshot of error saved!")

finally:
    input("Press Enter to quit...")
    driver.quit()

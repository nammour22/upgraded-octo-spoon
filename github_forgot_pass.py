from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

try:
    # Step 1: Navigate to GitHub Login Page
    driver.get("https://github.com/login")
    
    # Step 2: Click on 'Forgot password?' link
    forgot_password_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot password?"))
    )
    forgot_password_link.click()
    
    # Step 3: Wait for Password Reset Page to Load
    WebDriverWait(driver, 10).until(
        EC.url_contains("password_reset")
    )
    
    # Step 4: Take Screenshot of Password Reset Page
    driver.save_screenshot("forgot_password.png")
    print("Screenshot of password reset page saved successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
    driver.save_screenshot("error_state.png")
    print("Screenshot of error saved.")

finally:
    driver.quit()

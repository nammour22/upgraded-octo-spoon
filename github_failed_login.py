from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    # Step 1: Open GitHub login page
    driver.get("https://github.com/login")

    # Step 2: Enter incorrect username to unlock the password field
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "login_field"))
    )
    username_field.send_keys("wrong_username")

    # Step 3: Use JavaScript to unlock and focus the password field
    password_field = driver.find_element(By.ID, "password")
    driver.execute_script("arguments[0].removeAttribute('disabled')", password_field)
    driver.execute_script("arguments[0].focus();", password_field)

    # Step 4: Enter wrong password
    password_field.send_keys("wrong_password")

    # Step 5: Click the "Sign In" button to submit the form
    driver.find_element(By.NAME, "commit").click()

    # Step 6: Wait for the error message to appear
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "flash-error"))
    )

    # Step 7: Take screenshot of the failed login
    driver.save_screenshot("failed_login.png")
    print("Screenshot of failed login saved!")

except Exception as e:
    print("An error occurred:", e)
    driver.save_screenshot("error_state.png")
    print("Screenshot of error saved!")

finally:
    input("Press Enter to quit...")
    driver.quit()

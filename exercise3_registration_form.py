from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://demoqa.com/automation-practice-form")

    # Remove ads/footer that can intercept clicks
    driver.execute_script(
        "document.querySelectorAll('#fixedban, footer').forEach(e => e.remove());"
    )

    first_name = driver.find_element(By.ID, "firstName")
    last_name = driver.find_element(By.ID, "lastName")
    email = driver.find_element(By.ID, "userEmail")
    mobile = driver.find_element(By.ID, "userNumber")

    first_name.send_keys("Gittiqa")
    last_name.send_keys("Kumari")
    email.send_keys("gittiqakumari@example.com")

    # The gender radio input is visually hidden, so click its label
    female_label = driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-1']")
    driver.execute_script("arguments[0].scrollIntoView({block:'center'});", female_label)
    female_label.click()

    mobile.send_keys("0300123456")

    # Verify entered values
    print("First name :", first_name.get_attribute("value"))
    print("Last name  :", last_name.get_attribute("value"))
    print("Email      :", email.get_attribute("value"))
    print("Mobile     :", mobile.get_attribute("value"))
    female_radio = driver.find_element(By.ID, "gender-radio-1")
    print("Gender 'Female' selected:", female_radio.is_selected())

    assert first_name.get_attribute("value") == "Gittiqa"
    assert last_name.get_attribute("value") == "Kumari"
    assert email.get_attribute("value") == "gittiqakumari@example.com"
    assert mobile.get_attribute("value") == "0300123456"
    assert female_radio.is_selected()
    print("All values verified successfully.")
finally:
    driver.quit()

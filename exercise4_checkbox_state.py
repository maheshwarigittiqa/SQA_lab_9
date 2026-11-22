from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # Locate the first checkbox
    checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes input:nth-of-type(1)")

    # Record the initial state (do not assume it)
    initial = checkbox.is_selected()
    print("Initial state:", initial)

    # First click -> state should flip
    checkbox.click()
    after_first = checkbox.is_selected()
    print("After 1st click:", after_first)
    assert after_first != initial, "State did not change after first click"

    # Second click -> should return to the original state
    checkbox.click()
    after_second = checkbox.is_selected()
    print("After 2nd click:", after_second)
    assert after_second == initial, "State did not return to original"

    print("Checkbox state verification passed.")
finally:
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
try:
    driver.get("https://the-internet.herokuapp.com/dropdown")

    # Standard HTML <select id="dropdown"> with options:
    # "Please select an option", "Option 1" (value=1), "Option 2" (value=2)
    dropdown = Select(driver.find_element(By.ID, "dropdown"))

    # 1. By visible text
    dropdown.select_by_visible_text("Option 1")
    print("Selected by visible text:", dropdown.first_selected_option.text)
    assert dropdown.first_selected_option.text == "Option 1"

    # 2. By index (index 0 is the placeholder, so 2 = "Option 2")
    dropdown.select_by_index(2)
    print("Selected by index (2):   ", dropdown.first_selected_option.text)
    assert dropdown.first_selected_option.text == "Option 2"

    # 3. By value
    dropdown.select_by_value("1")
    print("Selected by value (1):   ", dropdown.first_selected_option.text)
    assert dropdown.first_selected_option.text == "Option 1"

    print("All dropdown selections verified.")
finally:
    driver.quit()

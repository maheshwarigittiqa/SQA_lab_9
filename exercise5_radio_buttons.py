from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.execute_script(
        "document.querySelectorAll('#fixedban, footer').forEach(e => e.remove());"
    )

    # Locate all gender radio options (same group: name="gender")
    radios = driver.find_elements(By.CSS_SELECTOR, "input[name='gender']")
    print("Gender options found:", len(radios))
    for r in radios:
        print(" -", r.get_attribute("value"))


    def states():
        return {r.get_attribute("value"): r.is_selected() for r in radios}


    def select(radio_id):
        # Inputs are hidden; click the associated label instead
        label = driver.find_element(By.CSS_SELECTOR, f"label[for='{radio_id}']")
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", label)
        label.click()


    print("Initial states:", states())

    # Select the first option
    select("gender-radio-1")
    print("After selecting Male:  ", states())
    assert radios[0].is_selected()

    # Select another option
    select("gender-radio-2")
    print("After selecting Female:", states())
    assert radios[1].is_selected()
    assert not radios[0].is_selected()

    # Only one option in the group is selected
    selected_count = sum(1 for r in radios if r.is_selected())
    print("Number of selected options:", selected_count)
    assert selected_count == 1
    print("Radio button group behaviour verified.")
finally:
    driver.quit()

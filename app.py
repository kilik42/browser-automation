from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("baddie34")

pw_box = browser.find_element_by_id("password")
pw_box.send_keys("noobiee23")

pw_box.submit()

## want to verify/assert
assert "baddie34" in browser.page_source


profile_link = browser.find_element_by_class_name("user-profile-link")

link_label = profile_link.get-attribute("innerHTML")
assert "baddie34" in link_label

browser.quit()

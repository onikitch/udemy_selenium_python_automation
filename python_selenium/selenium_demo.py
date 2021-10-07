from selenium import webdriver
validateText = "Неправильный формат номера."

driver = webdriver.Chrome(executable_path="D:\\Work\\udemy_selenium_python_automation\\chromedriver.exe")
driver.maximize_window()
driver.get("https://elmir.ua/")
driver.implicitly_wait(1)
driver.find_element_by_id("subscribe-close").click()
driver.find_element_by_css_selector("li[class='p2 submenu']").click()
driver.find_element_by_css_selector("a[class='ml-a'][href='//service.elmir.ua/']").click()
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_css_selector("div[class='site-topclbk sts-contacts']").click()
driver.find_element_by_css_selector("button[type='submit']").click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Users\\aignatova\\Documents\\course\\Selenium\\chromedriver")
print ("Step 1 was passed")
driver.get("https://vk.com/")
print ("Step 2 was passed")
user_name = "futi@mail.ru"
password = "Ludokk40"

email = driver.find_element_by_id("index_email")
email.send_keys(user_name)

pwd = driver.find_element_by_id("index_pass")
pwd.send_keys(password)

driver.find_element_by_id("index_login_button").click()
print ("Step 3 was passed")


# top_logout_link



# group = "universe"
# user_name = "aignatova"
# password = "Rn8TMthH"
# driver.get("https://{0}\{1}:{2}@newpm.dataart.com/".format(group, user_name, password))
# print("navigate pm url")
# driver.get("https://newpm.dataart.com/")


# print("wait")
# wait(driver, 1).until(EC.alert_is_present())
# # alert = driver.switch_to_alert()
# print("waited")
# alert = Alert(driver)
# alert.send_keys('{0}/{1}'.format(group, user_name))
# alert.send_keys(Keys.TAB)
# alert.send_keys(password)
# alert.accept()


# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.implicitly_wait(10)

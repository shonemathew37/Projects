from selenium import webdriver

# The place we will direct our WebDriver to
#url = 'http://www.srcmake.com/'

# Creating the WebDriver object using the ChromeDriver
driver = webdriver.Chrome()
# Directing the driver to the defined url
driver.get("https://nexhrm.nexerp.app/attendance")
driver.find_element_by_xpath('//*[@id="email"]').send_keys("shone.nextinnos@gmail.com")
driver.find_element_by_xpath('//*[@id="password"]').send_keys("123456")
driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/button').submit()
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div/div[1]/div/div/form/button').submit()

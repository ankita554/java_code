from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import  ActionChains
import time
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
#driver= webdriver.Chrome(executable_path="C:\\Users\\ankijais\\Desktop\\chromedriver.exe")



options=Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
driver.get("https://10.236.81.190:8380/admin/login")


driver.maximize_window()
time.sleep(10)
User_name=driver.find_element(By.NAME, 'j_username').send_keys("csrfull")
password=driver.find_element(By.NAME,'j_password').send_keys("csrfull")

login=driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(5)
#driver.find_element(By.LINK_TEXT, '#BLCMerchandising').click()

List=driver.find_elements(By.CSS_SELECTOR, 'div.side-nav li a')


print(len(List))

time.sleep(10)

driver.find_element(By.XPATH, "//div[@class='side-nav']//ul/li//a[@class='nav-section fa fa-file-text']").click()

'''List1=driver.find_elements(By.XPATH, "//div[@class='mCSB_container mCS_no_scrollbar']//tbody//tr//td")
print(len(List1))
for x in List1:
    print(x.text)'''

List_ele=driver.find_elements(By.CSS_SELECTOR, 'ul.nav-links li a')
print(len(List_ele))
for x in List_ele:
    print(x.text)



driver.close()





#driver.maximize_window()
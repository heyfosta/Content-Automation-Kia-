from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time





PATH = "/Applications/chromedriver"
DRIVER = webdriver.Chrome(PATH)



# Target URL


DRIVER.get("https://preprod2admin-eu.kia.com/editor.html/content/kwcms/kme/uk/en/test01/rio.html")


# Login details
time.sleep(3)
folder = DRIVER.find_element_by_xpath("//*[@id='username']")
folder.send_keys("vccp-fcosta")

time.sleep(3)
folder = DRIVER.find_element_by_xpath("//*[@id='password']")
folder.send_keys("Start1234!")


folder = DRIVER.find_element_by_xpath("//*[@id='submit-button']/coral-button-label")
folder.click()




# Update T&Cs


# Selecting Component ---

time.sleep(3)

# Top bar 
folder = DRIVER.find_element_by_xpath("//*[@id='Content']/div[1]/coral-actionbar/coral-actionbar-primary/coral-actionbar-item[1]/button/coral-icon")
folder.click()


# Content tree
folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-6']/coral-icon")
folder.click()


# Tab location
folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-499']/coral-tree-item[15]")
folder.click()


# Edit button
folder = DRIVER.find_element_by_xpath("//*[@id='EditableToolbar']/button[1]/coral-icon")
folder.click()


# ---

# text box edit ---

time.sleep(3)

folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-588']/coral-panel-content/div/div/div[1]/div/div[2]")
folder.click()

folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-588']/coral-panel-content/div/div/div[1]/div/div[2]").send_keys(Keys.COMMAND + "a")

folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-588']/coral-panel-content/div/div/div[1]/div/div[2]").send_keys(Keys.DELETE)

# ---

# COPY PLACED HERE

folder = DRIVER.find_element_by_xpath("//*[@id='coral-id-588']/coral-panel-content/div/div/div[1]/div/div[2]").send_keys("Images shown are for illustration purposes only and may not be to UK specification.\n\n*£1,750 towards your Personal Contract Purchase Deposit on Rio, excluding ‘1’ derivative which receives £1,500. Offer available on purchase of a new Kia Rio in the United Kingdom between 01.01.2021 – 31.03.2021. Private customer registrations only, excluding Personal Contract Hire. Personal Contract Purchase deposit contribution not available in conjunction with Scrappage saving. Kia reserves the right to amend or withdraw offers at any time without prior notice. Finance T&Cs apply. Subject to status. 18s or over. Guarantee may be required. Kia Finance RH2 9AQ. 7 year / 100,000 mile manufacturer’s warranty.\n\n*Parking sensors may not match exterior body colour\n\n**Please check with your dealer for mobile phone compatability\n\n(5) Kia UVO Remote Services\n\nInformation and control service for your Kia from your smartphone; the Services are available free of charge for a period of seven years commencing on the day the vehicle is sold to the first owner of the vehicle, i.e. the point in time the initial purchase agreement becomes effective, and may be subject to change during that period. Details of operation and terms of use can be obtained on your UVO App. Smartphone with iOS or Android operating system and mobile phone contract with data option necessary incurring additional cost.\n\n(7) Forward Collision-Avoidance Assist (FCA)\n\nForward Collision-Avoidance Assist (FCA) is an assistance system and does not relieve the driver from their responsibility to safely operate the vehicle at any time. The driver still has to adapt their driving behaviour to their personal driving capabilities, to the legal requirements and to the overall road and traffic conditions. FCA is not designed to drive the vehicle autonomously. For further information, please refer to the owner’s manual.")


# Confirm

folder = DRIVER.find_element_by_xpath("/html/body/coral-dialog/div[2]/form/div/div/coral-dialog-header/div/button[4]/coral-icon")
folder.click()






# folder = DRIVER.find_element_by_xpath("/html/body/coral-dialog/div[2]/form/div/div/coral-dialog-header/div/button[3]/coral-icon")
# folder.click()





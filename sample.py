
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait, Select # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from login import login
import time
import os 

driver = webdriver.Chrome()
url = os.getcwd() + '/sample_page.html'
print("URL", url)
# url = "file:///C:/Users/abhin_000/Desktop/check/Workday%20automation%20sample/Software%20Engineer,%20Full%20Stack-Page2.html"
driver.get(url)

dropdown = "#dropDownSelectList.countries-input--uid21-input"

allInputFields = ".gwt-TextBox.WMD1"

givenName = "textInput.nameComponent--uid18-input"
givenNameValue = "Sherlock"

familyName = "textInput.nameComponent--uid19-input"
familyNameValue = "Holmes"

addressLine1 = "textInput.addressComponentsDeferred[i]--uid27-input"
addressLine1Value = "221B Baker Street"

city = "textInput.addressComponentsDeferred[i]--uid28-input"
cityValue = "London"

postalCode = "textInput.addressComponentsDeferred[i]--uid29-input"
postalCodeValue = "NW1 6XE"

phoneNo = "textInput.phone--uid35-input"
phoneNoValue = "1010101010"

localGivenName = "textInput.nameComponent--uid20-input"
localGivenNameValue = "Sherlock"

localFamilyName = "textInput.nameComponent--uid21-input"
localFamilyNameValue = "Holmes"

phoneExtension = "textInput.phoneExtension--uid36-input"
phoneExtensionValue = ""

workedBeforeYes = "gwt-uid-273"
workedBeforeNo = "gwt-uid-274"
workedBeforeValue = "No"

nextButton = ".WNXM.WGDO.WMXM.WLKN.WA-M.WBYM"

def fill_sample():
    setName = driver.find_element_by_id(givenName)
    setName.send_keys(givenNameValue)

    setFamilyName = driver.find_element_by_id(familyName)
    setFamilyName.send_keys(familyNameValue)

    time.sleep(1)
    setLocalGivenName = driver.find_element_by_id(localGivenName)
    setLocalGivenName.send_keys(localGivenNameValue)

    setLocalFamilyName = driver.find_element_by_id(localFamilyName)
    setLocalFamilyName.send_keys(localFamilyNameValue)
    
    time.sleep(1)
    
    setAddress = driver.find_element_by_id(addressLine1)
    setAddress.send_keys(addressLine1Value)

    setCity = driver.find_element_by_id(city)
    setCity.send_keys(cityValue)

    setPostalCode = driver.find_element_by_id(postalCode)
    setPostalCode.send_keys(postalCodeValue)

    setPhone = driver.find_element_by_id(phoneNo)
    setPhone.send_keys(phoneNoValue)

    setPhoneExtension = driver.find_element_by_id(phoneExtension)
    setPhoneExtension.send_keys(phoneExtensionValue)

    if workedBeforeValue == "Yes":
        driver.find_element_by_id(workedBeforeYes).click()
    else:
        driver.find_element_by_id(workedBeforeNo).click()

    # click on next button after filling details on first page
    driver.find_element_by_css_selector(nextButton).click()


# call function for filling all the details
fill_sample()
print("Form Completed")
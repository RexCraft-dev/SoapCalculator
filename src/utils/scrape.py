from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import csv

driver = webdriver.Chrome()

driver.get("http://soapcalc.net/calc/SoapCalcWP.asp")

table = driver.find_element(By.ID, "selOil")
elements = Select(driver.find_element(By.ID, "selOil"))

ofw_list = []

for index in range(len(elements.options)):
    elements.select_by_index(index)
    table = driver.find_element(By.ID, "tblBottomRow")

    name = elements.first_selected_option.text

    spnLauric = table.find_element(By.ID, "spnLauric")
    spnLauric = spnLauric.get_attribute("value")

    spnMyristic = table.find_element(By.ID, "spnMyristic")
    spnMyristic = spnMyristic.get_attribute("value")

    spnPalmitic = table.find_element(By.ID, "spnPalmitic")
    spnPalmitic = spnPalmitic.get_attribute("value")

    spnStearic = table.find_element(By.ID, "spnStearic")
    spnStearic = spnStearic.get_attribute("value")

    spnRicinoleic = table.find_element(By.ID, "spnRicinoleic")
    spnRicinoleic = spnRicinoleic.get_attribute("value")

    spnOleic = table.find_element(By.ID, "spnOleic")
    spnOleic = spnOleic.get_attribute("value")

    spnLinoleic = table.find_element(By.ID, "spnLinoleic")
    spnLinoleic = spnLinoleic.get_attribute("value")

    spnLinolenic = table.find_element(By.ID, "spnLinolenic")
    spnLinolenic = spnLinolenic.get_attribute("value")

    ofw = [name,
           spnLauric,
           spnMyristic,
           spnPalmitic,
           spnStearic,
           spnRicinoleic,
           spnOleic,
           spnLinoleic,
           spnLinolenic]

    strip_ofw = ','.join(ofw)
    print(strip_ofw)
    ofw_list.append(strip_ofw)


with open("../../data/db/ofw.csv", "w") as f:
    for item in ofw_list:
        f.write(item + '\n')

# Close the browser window
driver.quit()
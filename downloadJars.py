import os
import requests

import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
driverDownload = webdriver.Chrome(executable_path="./chromedriver", chrome_options=chrome_options)
driver.get('https://getbukkit.org/download/craftbukkit')
driver.save_screenshot("test.png")
for version in driver.find_elements_by_class_name("download-pane"):
    versionName = version.find_element_by_tag_name("h2").text
    versionSize = version.find_element_by_tag_name("h3").text
    versionLink = version.find_element_by_tag_name("a").get_attribute('href')
    driverDownload.get(versionLink)
    versionLinkReal = driverDownload.find_element_by_class_name("well").find_element_by_tag_name("a").get_attribute('href')
    targetFileName = "craftbukkit-%s.jar" % versionName
    print("Downloading CraftBukkit %s, %sMB with filename %s" % (versionName, versionSize, targetFileName))
    r = requests.get(versionLinkReal, allow_redirects=True)
    open('downloads/jars/craftbukkit/%s' % targetFileName, 'wb').write(r.content)
    print("-------------------")
driver.get('https://getbukkit.org/download/spigot')
driver.save_screenshot("test.png")
for version in driver.find_elements_by_class_name("download-pane"):
    versionName = version.find_element_by_tag_name("h2").text
    versionSize = version.find_element_by_tag_name("h3").text
    versionLink = version.find_element_by_tag_name("a").get_attribute('href')
    driverDownload.get(versionLink)
    versionLinkReal = driverDownload.find_element_by_class_name("well").find_element_by_tag_name("a").get_attribute('href')
    targetFileName = "spigot-%s.jar" % versionName
    print("Downloading Spigot %s, %sMB with filename %s" % (versionName, versionSize, targetFileName))
    r = requests.get(versionLinkReal, allow_redirects=True)
    open('downloads/jars/spigot/%s' % targetFileName, 'wb').write(r.content)
    print("-------------------")
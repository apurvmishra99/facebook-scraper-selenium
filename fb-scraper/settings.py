import os
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# User credentials
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

# Required binaries
BROWSER_EXE = '/usr/bin/firefox'
GECKODRIVER = '/usr/bin/geckodriver'
FIREFOX_BINARY = FirefoxBinary(BROWSER_EXE)

#  Code to disable notifications pop up of Chrome Browser
PROFILE = webdriver.FirefoxProfile()
# PROFILE.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False
PROFILE.set_preference("dom.webnotifications.enabled", False)
PROFILE.set_preference("app.update.enabled", False)
PROFILE.update_preferences()

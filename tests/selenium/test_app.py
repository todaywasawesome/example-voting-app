import unittest
import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

ip = os.getenv('ip')

# Give Selenium Hub time to start
time.sleep(15)

class VoteTest(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Remote(
      command_executor='http://selenium_hub:4444/wd/hub',
      desired_capabilities={'browserName': 'chrome'}
    )

  def test_confirm_choice_form(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_xpath("//form[@id='choice']"))

  def test_confirm_button_a(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_xpath("//form[@id='choice'][@type='button'][@id='a']"))

  def test_confirm_button_b(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.browser.find_element_by_xpath("//form[@id='choice'][@type='button'][@id='b']"))

  def tear_down(self):
    self.browser.quit()

if __name__ == '__main__':
    unittest.main()
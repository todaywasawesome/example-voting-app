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

  def test_confirm_a(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.is_element_present(By.CLASS,"a"))

  def test_confirm_b(self):
    browser = self.browser
    browser.get("http://{}:80".format(ip))
    self.assertTrue(self.is_element_present(By.CLASS,"b"))

  def is_element_present(self, how, what):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try: self.browser.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

  def tear_down(self):
    self.browser.quit()

if __name__ == '__main__':
    unittest.main()
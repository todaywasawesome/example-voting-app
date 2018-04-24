import unittest
import time
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

url = os.getenv('URL')

class VoteTest(unittest.TestCase):

  def setup(self):
    caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    self.browser = webdriver.Remote(
      command_executor='http://selenium_hub:4444/wd/hub',
      desired_capabilities=caps
    )

  def confirm_a(self):
    browser = self.browser
    browser.get(url)
    self.assertTrue(self.is_element_present(By.NAME,"a"))

  def confirm_b(self):
    browser = self.browser
    browser.get(url)
    self.assertTrue(self.is_element_present(By.NAME,"b"))

  def tear_down(self):
    self.browser.quit()

  def is_element_present(self, how, what):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try: self.browser.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

if __name__ == '__main__':
    unittest.main()
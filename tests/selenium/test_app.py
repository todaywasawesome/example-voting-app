import unittest
import time
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

url = os.getenv('URL')

class VoteTest(unittest.TestCase):
  @classmethod
  def setUpClass(inst):
      # create a new Chrome session
      inst.driver = webdriver.Chrome()
      inst.driver.implicitly_wait(10)
      inst.driver.maximize_window()
      # navigate to the application home page
      inst.driver.get(url)
      inst.driver.title

  def test_confirm_a(self):
    self.assertTrue(self.is_element_present(By.NAME,"a"))

  def test_confirm_b(self):
    self.assertTrue(self.is_element_present(By.NAME,"b"))

  def is_element_present(self, how, what):
    """
    Helper method to confirm the presence of an element on page
    :params how: By locator type
    :params what: locator value
    """
    try: self.driver.find_element(by=how, value=what)
    except NoSuchElementException: return False
    return True

  @classmethod
  def tearDownClass(inst):
      # close the browser window
      inst.driver.quit()

if __name__ == '__main__':
    unittest.main()
import unittest
import time
import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = os.getenv('URL')

class VoteTest(unittest.TestCase):

  def setUp(self):
    caps = {'browserName': os.getenv('BROWSER', 'chrome')}
    address = os.getenv('NODE_HUB_ADDRESS')
    self.browser = webdriver.Remote(
      command_executor='http://selenium_hub:4444/wd/hub',
      desired_capabilities=caps
    )

  def confirm_a(self):
    browser = self.browser
    browser.get(url)
    vote_box_a = browser.find_element_by_name('a')
    assert vote_box_a.text == 'a'

  def confirm_b(self):
    browser = self.browser
    browser.get(url)
    vote_box_a = browser.find_element_by_name('a')
    assert vote_box_a.text == 'a'

  def tearDown(self):
    self.browser.quit()


if __name__ == '__main__':
    unittest.main()
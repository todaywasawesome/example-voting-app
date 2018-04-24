import unittest
import time
import os

from selenium import webdriver

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
    vote_box_a = browser.find_element_by_name('a')
    assert vote_box_a.text == 'a'

  def confirm_b(self):
    browser = self.browser
    browser.get(url)
    vote_box_a = browser.find_element_by_name('a')
    assert vote_box_a.text == 'a'

  def tear_down(self):
    self.browser.quit()


if __name__ == '__main__':
    unittest.main()
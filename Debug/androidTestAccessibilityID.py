__author__ = 'Administrator'

import unittest
from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.3',
            'deviceName': 'Android Emulator',
            'browserName': '',
            'appPackage':'com.android.calculator2',
            'appActivity':'com.android.calculator2.Calculator'
        }
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',desired_capabilities=self.desired_caps)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    def test_calculator(self):
        self.ele = self.driver.find_element_by_id("com.android.calculator2:id/digit1")
        if self.ele.is_displayed():
            print("check that if the element digit1 display")
            self.ele.click()

        self.ele = self.driver.find_element_by_id("com.android.calculator2:id/digit2")
        if self.ele.is_displayed():
            print("check that if the element digit2 display")
            self.ele.click()

        self.ele = self.driver.find_element_by_id("com.android.calculator2:id/digit3")
        if self.ele.is_displayed():
            print("check that if the element digit3 display")
            self.ele.click()

        self.ele = self.driver.find_element_by_accessibility_id("123")
        print("the input number is: ",self.ele.text)

if __name__ == '__main__':
    unittest.main()

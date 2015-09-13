__author__ = 'Administrator'

import unittest
from appium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class MyTestCase(unittest.TestCase):

    def setUp(self):
        print("set up env for android testing...")
        self.desired_caps = {
            'platformName': 'Android',
            'platformVersion': '4.3',
            'deviceName': 'Android Emulator',
            'browserName': '',
            'appPackage':'com.android.contacts',
            'appActivity':'com.android.contacts.activities.PeopleActivity'
        }
        self.driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub',desired_capabilities=self.desired_caps)
        self.driver.implicitly_wait(30)
        #self.driver.get('http://baidu.com')

    def tearDown(self):
        print("clean up the settings...")
        self.driver.quit()

    def test_android(self):
        #self.driver.find_element_by_id('kw').send_keys("python")
        #self.driver.find_element_by_id('su').click()
        print("run test method...")
        print("current activity is: ",self.driver.current_activity)
        # find by class name
        self.ele = self.driver.find_elements_by_class_name("android.widget.Button")
        for i in range(len(self.ele)):
            print("button value: ",self.ele[i].text)

        # find by id
        self.ele = self.driver.find_element_by_id("com.android.contacts:id/create_contact_button")
        print("find by id, value is: ",self.ele.text)
        # find by xpath
        self.ele = self.driver.find_element_by_xpath("//android.widget.Button[contains(@text,'Create a new contact')]")
        print("find by xpath, value is: ",self.ele.text)
        # find by accessibility id:
        self.ele = self.driver.find_element_by_accessibility_id("Create a new contact")
        print("find by accessibility id, value is: ",self.ele.text)

if __name__ == '__main__':
    unittest.main()

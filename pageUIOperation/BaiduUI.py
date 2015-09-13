from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from yuanfang1987.PageUIobjects.BaiduPageObjects import BaiduPageUI

class BaiduUI:
    def __init__(self,gdriver):
        self.driver = gdriver
        self.wait = WebDriverWait(self.driver,15)

    def verifyBaiduPageDisplay(self):
        self.element = self.wait.until(EC.visibility_of_element_located(BaiduPageUI.searchBtn))
        return self.element.is_displayed()

    def inputSearchText(self,strText):
        self.driver.find_element(*BaiduPageUI.searchBox).clear()
        self.driver.find_element(*BaiduPageUI.searchBox).send_keys(strText)

    def clickSearchBtn(self):
        self.driver.find_element(*BaiduPageUI.searchBtn).click()

    def verifySearchResult(self,strTitle):
        return self.wait.until(EC.title_contains(strTitle))

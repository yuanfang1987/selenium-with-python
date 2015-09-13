from yuanfang1987.pageUIOperation.BaiduUI import BaiduUI


class Baidu():
    def __init__(self,gdriver):
        self.objBaiduUI = BaiduUI(gdriver)
        self.functions = dict(searchText=self.search)

    def run(self,actionname,lis=list(),resultdic=dict()):
        self.functions[actionname](li=lis,result=resultdic)

    def search(self,li,result):
        self.stepResult = "Passed"
        self.steps = result["Steps"]
        for i in range(len(li)):
            self.dic = li[i]
            self.strtext = self.dic["SearchText"]
            # verify that current page is search page
            if self.objBaiduUI.verifyBaiduPageDisplay():
                self.steps.append("verify that current page is search page, passed.")
            else:
                self.steps.append("verify that current page is search page, failed.")
                self.stepResult = "Failed"
            self.objBaiduUI.inputSearchText(self.strtext)
            self.steps.append("input search text: "+self.strtext)
            self.objBaiduUI.clickSearchBtn()
            self.steps.append("click on search button.")
            if self.objBaiduUI.verifySearchResult(self.strtext):
                self.steps.append("Passed,verify that search result page title contains: "+self.strtext)
            else:
                self.steps.append("Failed,verify that search result page title contains: "+self.strtext)
                self.stepResult = "Failed"
            result["Status"] = self.stepResult



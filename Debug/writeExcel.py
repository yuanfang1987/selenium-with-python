from openpyxl.workbook import workbook
from openpyxl.writer.excel import ExcelWriter

wb = workbook.Workbook()
ew = ExcelWriter(workbook=wb)

newfilepath = "D:\\PythonWorkspace\\yuanfang\\Data\\writeExcelTest.xlsx"

ws = wb.worksheets[0]

ws.title = "Run Result"

ws.cell("A1").value = "yuanfangtest"

ew.save(filename=newfilepath)



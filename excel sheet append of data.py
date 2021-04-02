import xlrd
from xlutils.copy import copy
readBook=xlrd.open_workbook("demo.xls")
wb=copy(readBook)
exl=wb.get_sheet(0)
exl.write(0,2,'Python')
wb.save('demo.xls')

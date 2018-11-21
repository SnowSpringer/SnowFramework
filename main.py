
import sys

sys.path.append('/Users/low/PycharmProjects/snowFramework/TestCase')

# import src
from TestCase import doperateExcel
import doperateExcel
from doperateExcel import operateExcel
import openpyxl



excelUrl = '/Users/low/Desktop/testcase_student.xlsx'
sheetN = '测试详情'
checkPoint = 'error_code'

snow = operateExcel()
snow.operatExcel(excelUrl,sheetN,checkPoint)


# 检查点，从 在方法中写死，到提出方法外，作为参数传递进去


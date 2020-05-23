import xlwt
import xlrd
class Execl:
    def __init__(self,excel_path,sheet_name):
        self.workBook = xlrd.open_workbook(excel_path)
        self.workSheet = self.workBook.sheet_by_name(sheet_name)

    def now(self,row_no):
        return self.workSheet.row_values(row_no)
    def col(self,col_no):
        return self.workSheet.col_values(col_no)

workbook = xlrd.open_workbook("D:/testing/wangxiao//file_path/WX接口测试用例.xlsx")
worksheet = workbook.sheet_by_index(1)
rows = worksheet.nrows
cols = worksheet.ncols
print(rows,cols)
import xlrd
import json
import os
class datainfo:
    def __init__(self):
        path = os.path.dirname(__file__)
        diar_path = path + "/file_path/WX接口测试用例.xlsx"
        self.workbook = xlrd.open_workbook(diar_path)
        self.worksheet = self.workbook.sheet_by_index(2)
        self.get_rows = self.worksheet.nrows
        self.get_cols = self.worksheet.ncols
    def cell(self,nrow,ncol):
        '''
        获取指定某行某列的数据，
        :param nrow: 实际行数
        :param ncol: 实际列数
        :return:
        '''
        nrow = nrow - 1
        ncol = ncol - 1
        return  self.worksheet.cell_value(nrow,ncol)


    def row(self,nrow):
        nrow = nrow-1
        return  self.worksheet.row_values(nrow)


    def col(self,ncol):
        ncol = ncol - 1
        return  self.worksheet.row_values(ncol)

    def get_row_data(self):
        '''
        获取每行的数据，返回一个列表
        :return:
        '''
        len = self.get_rows
        list_rows = []
        for i in range(1,len):
            row_data = self.worksheet.row_values(i)
            api_no = (row_data[0])

            api_name = row_data[1]
            api_describe = row_data[2]
            api_url = row_data[3]
            api_function = row_data[4]
            api_headers = row_data[5]
            api_data = row_data[6]
            api_check = row_data[7]
            api_hope = row_data[8]
            api_reality = row_data[9]
            api_active = row_data[10]
            api_status = row_data[11]
            api_correlation = row_data[12]
            api_message = row_data[13]

            list_2 = [
                api_no, api_name, api_describe, api_url, api_function,
                api_headers, api_data, api_check, api_hope, api_reality,
                api_active, api_status, api_correlation, api_message
            ]  # 新增表名字段
            list_rows.append(list_2)
        return list_rows

#
# c = datainfo()
#     # print(c.get_rows)
# list_rows =  c.get_row_data()
#
# print(list_rows)
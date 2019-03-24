#the module openpyxl helps perform excel operations.
#task: to 

import openpyxl,os

print('The curr working dir is: ' + os.getcwd())
wb = openpyxl.load_workbook('example.xlsx')
#print('The sheet names of wb is: ' + wb.get_sheet_names().__getitem__)

ws = wb.active
ws.append([1,2,3,])





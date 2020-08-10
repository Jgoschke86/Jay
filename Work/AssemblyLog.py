import openpyxl
from openpyxl.xml.constants import MAX_ROW


print("Opening Excel and reading file......")
wb = openpyxl.load_workbook(r"C:\Python Stuff\Test Log.xlsx")

names = []
for name in wb.get_sheet_names():
    names.append(name)

print(names)
sheet = wb.active



for i in range(1,590):
    cell_obj = sheet.cell(row = i, column = 1)
    print(cell_obj.value)
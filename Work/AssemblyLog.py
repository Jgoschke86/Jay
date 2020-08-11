import openpyxl
from openpyxl.xml.constants import MAX_ROW


print("Opening Excel and reading file......")
wb = openpyxl.load_workbook(r"C:\Python Stuff\Test Log.xlsx")

names = wb.sheetnames

names.remove("Time")
names.remove("")
names.remove("")
names.remove("")

print("Current names to scan.... " + names)
sheet = wb.active



for i in range(1,590):
    cell_obj = sheet.cell(row = i, column = 1)
    print(cell_obj.value)
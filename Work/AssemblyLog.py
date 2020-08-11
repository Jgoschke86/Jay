import openpyxl
from openpyxl.xml.constants import MAX_ROW


print("Opening Excel and reading file......")
wb = openpyxl.load_workbook(r"C:\Python Stuff\Test Log.xlsx")
time_sheet = wb.worksheets[9]

names = wb.sheetnames

names.remove("Time")
names.remove("Set up Checklist")
names.remove("Extra")

print("Current names to scan.... ")
print(names)
ws = wb.worksheets[1]
start_cell = 10
row_numbers = ws.max_row
print("There are " + str(row_numbers) + " cells to scan")

print("Scanning cells.......")
for i in range(start_cell,row_numbers):
    cell_obj = ws.cell(row = i, column = 3)
    if cell_obj in time_sheet["A"]:

import openpyxl
from openpyxl.xml.constants import MAX_COLUMN, MAX_ROW


print("Opening Excel and reading file......")
# wb = openpyxl.load_workbook(r"C:\Python Stuff\Test Log.xlsx")
wb = openpyxl.load_workbook(r"D:\Python Stuff\Test Log.xlsx")
time_sheet = wb.worksheets[9]

ws = wb.worksheets[0]
start_cell = 10
row_numbers = ws.max_row

names = wb.sheetnames
names.remove("Time")
names.remove("Set up Checklist")
names.remove("Extra")

print("Current names to scan.... ")
print(names)

print("There are " + str(row_numbers) + " cells to scan")

print("Scanning cells.......")
for i in ws.iter_rows(min_row = start_cell, min_col = 3, max_row = 2712, max_col = 3):
    for cell in i:
        print(cell.value)
        for j in time_sheet.iter_rows():
            for amount in j:
                if cell.value == amount.value:
                    time_row = int(amount.row) + 1
                    time_in = time_sheet.cell(row = time_row, column = 1).value
                    print(time_in)
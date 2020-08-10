from openpyxl import open_workbook

loc = ("") #File path

wb = openpyxl.load_workbook(loc)
sheet = get_sheet_by_name(name of sheet)
last_row = sheet.max_row



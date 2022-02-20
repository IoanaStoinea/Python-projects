import openpyxl


#1
'''''
#wb = openpyxl.load_workbook(r"")
sheets = wb.get_sheet_names() # wb.get_active_sheet()
print(sheets) #['Sheet1', 'Sheet2', 'Sheet3', 'Sheet4']

firstSheet = wb.get_sheet_by_name('Sheet1')
print(firstSheet['A1']) #<Cell 'Sheet1'.A1>
print(firstSheet['A1'].value) #Test Case ID
print(firstSheet.cell(row=1, column=1 )) #<Cell 'Sheet1'.A1>
print(firstSheet.cell(row=1, column=1 ).value) #Test Case ID

#2

for i in range(2,8):
    print(firstSheet.cell(row=i, column=1).value)

#3 You can determine the size of the sheet with the Worksheet object’s max_row() and get_highest_column() methods.

maxRows=int(firstSheet.max_row)
maxColumns=int(firstSheet.max_column)
print("Max Rows: ", maxRows)
'''''

#4

# To open the workbook
# workbook object is created
wb = openpyxl.load_workbook(r"C:\Users\andra\OneDrive\Desktop\Azimut\TestareAutomata\curs12\Test_Case_PGS.xlsx")
testCasesSheet = wb.get_sheet_by_name('TestCases')
#Sa se afiseze descrierea testului cu ID-ul 4.

# Cell objects also have a row, column,
# and coordinate attributes that provide
# location information for the cell.

# Note: The first row or
# column integer is 1, not 0.

# Cell object is created by using
# sheet object's cell() method.
cell_obj = testCasesSheet.cell(row=14, column=4)
# Print value of cell object
# using the value attribute
print("Descriere:", cell_obj.value)



#Sa se numere toate testele pass si toate testele fail
failTestCasesCounter = 0
passTestCasesCounter = 0
passString = 'Pass'
failString = "Fail"

for row in range(1, int(testCasesSheet.max_row + 1)):
    if testCasesSheet.cell(row=row, column=7).value == passString.lower():
        passTestCasesCounter = passTestCasesCounter + 1
    elif testCasesSheet.cell(row=row, column=7).value == failString.lower():
        failTestCasesCounter = failTestCasesCounter + 1
print("Fail test cases counter:", failTestCasesCounter)
print("Pass test cases counter:", passTestCasesCounter)























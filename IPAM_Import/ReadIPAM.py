import sys
import pprint
import os.path
from openpyxl import load_workbook
from array import *

# Initialise Variables (Not really required)

# Get Passed In variables From sys.argv and then assiged passed file to variable
my_arg_list = sys.argv
SourceFilePath = my_arg_list[1]
MyIPs =[]
MySheets =[]
LoopCounter = int(0)
SelectedSheet = str()
PreviewAmount = 10
KeyColumn = str()
StartRow = int()
EndRow = int()
NumRows = int()
EndRowNum = int()

letters = [
           "a","b","c","d","e","f","g","h","i","k",
           "l","m","n","o","p","q","r","s","t","u",
           "v","w","x","y","z"]

#Setup pp print
pp = pprint.PrettyPrinter(indent=4)

#Check if file Exists, import if OK.
if os.path.isfile(SourceFilePath):
    print("File Check: " + SourceFilePath + "   OK!\n")
    myworkbook = load_workbook(SourceFilePath, data_only=True)
else:
    print ("File not exist")
    exit()


#Assign References to Sheet Names in 2d array
for ExcelSheetName in myworkbook.sheetnames:
    LoopCounter += 1
    MySheets.append([LoopCounter,ExcelSheetName])

print("Sheets Names:")
for x in range(len(MySheets)):
    if x < 9:
        Padding_Char = " "
    else:
        Padding_Char = ""
    print(str(MySheets[x][0]) + Padding_Char + " -- " + str(MySheets[x][1]))
 
while True:      # keep looping until we break out of the loop
    try:
        SelectedSheet = int(input("\nSelect Sheet ID: "))
        if (SelectedSheet -1) < len(MySheets):
            break    # exit the loop if the previous line succeeded
        else:
            print("Sheet ID is out of range, highest sheet ID is: " + str(len(MySheets)))
    except ValueError:
        print("Please enter an integer!")

SelectSheetName = MySheets[SelectedSheet-1][1]


print("Selected Sheet Name: " + SelectSheetName)
myworksheet = myworkbook[SelectSheetName]


###
KeyColumn = input("Key Column (Column with IP Addresses):")
StartRow = input("Starting Row:")
NumRows = input("Number of Rows: ")
EndRowNum = int(StartRow) + int(NumRows)
ColIndexNum = letters.index(KeyColumn.lower())
DescColumn = letters[ColIndexNum + 1]

print("Desc Col: " + str(DescColumn.upper())) 


for loop in range(int(StartRow), EndRowNum):
    my_ip_cell = KeyColumn + str(loop)
    my_desc_cell = DescColumn.upper() + str(loop)
    MyIPs.append([myworksheet[my_ip_cell].value, myworksheet[my_desc_cell].value])

LoopCounter = 0

for x in range(len(MyIPs)):
    LoopCounter += 1
    if LoopCounter <= PreviewAmount:
        print(str(MyIPs[x][0]) + "    ---- " + str(MyIPs[x][1]))
        if LoopCounter == PreviewAmount: print("\n ------- Ommited ------- \n")
    elif x > (len(MyIPs)-PreviewAmount):
        print(str(MyIPs[x][0]) + "    ---- " + str(MyIPs[x][1]))
####

print("End Row: " + str(EndRowNum))
pp.pprint(MyIPs)

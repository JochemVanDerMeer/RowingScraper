import xlwt
from xlwt import Workbook
import ast
from fields import fields

f = open('output.txt', 'r')

def changeFormat(times):
    final = [item for sublist in times for item in sublist]
    return final

def listToString(s): 
    str1 = "   " 
    return (str1.join(s))

def writeResult():
    lines = [line.rstrip() for line in f]
    results = []
    for i in lines:   
        results += [ast.literal_eval(i)]

    wb = Workbook()

    sheet1 = wb.add_sheet('Sheet 1')

    #add the column names
    for idx,val in enumerate(fields):
        sheet1.write(0,idx+1,val)

    #add the results
    currentYear = results[0][1]
    currentRow = 1

    for j in results:
        if j[1] != currentYear:
            sheet1.write(currentRow, 0, currentYear)
            currentYear = j[1]   
            currentRow += 1
            

        if len(j) > 2:
            sheet1.write(currentRow, fields.index(j[0])+1, listToString(changeFormat(j[2])))
    sheet1.write(currentRow, 0, currentYear)

    wb.save('xlwt example.xls')

writeResult()
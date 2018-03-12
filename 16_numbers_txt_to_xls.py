import xlwt,json

file = open('numbers.txt','rb').read()
list1 = json.loads(file)
print(list1)

wb = xlwt.Workbook()
sheet = wb.add_sheet('city')

for i in range(len(list1)):
    for j in range(len(list1[i])):
        sheet.write(i,j,list1[i][j])


wb.save('numbers.xls')
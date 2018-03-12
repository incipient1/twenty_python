import xlwt,json

file = open('city.txt','rb').read().decode('gbk')
dict1 = json.loads(file)

list2 = sorted(dict1)
print(list2)

wb = xlwt.Workbook()
sheet = wb.add_sheet('city')

rownum = 0
for i in list2:

    column_num = 0
    sheet.write(rownum,column_num,i)
    sheet.write(rownum,column_num+1,dict1[i])
    rownum += 1

wb.save('city.xls')
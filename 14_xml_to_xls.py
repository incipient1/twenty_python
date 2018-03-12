import xlwt,json

wb = xlwt.Workbook()
sheet = wb.add_sheet('student')

file = open('student.txt','rb').read().decode('gbk')
js = json.loads(file)

'''
rownum = 0
js2 = sorted(js)

for item in js2:
    col = 0
    print(item)
    sheet.write(rownum,col,item)

    for attr in js[item]:
        print(attr)
        col +=1
        sheet.write(rownum,col,attr)
    rownum += 1

wb.save('student.xls')
'''
print(js)
js2 = sorted(js)
print(js2)
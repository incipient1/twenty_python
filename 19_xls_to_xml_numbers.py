import xlrd,json

l1 = r'''<?xmlversion='1.0' encoding='utf-8'?>
<root>
<citys>
<!--
    城市信息
-->
'''

l2 = r'''
</city>
</root>
'''

book = xlrd.open_workbook('numbers.xls')
sheet = book.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols

l3 = []
for i in range(rows):
    row_list = sheet.row_values(i)
    l3.append(row_list)

print(row_list)
print(type(row_list))

json1 = json.dumps(l3,indent=4)

file = open('numbers.xml','w')
file.write(l1)
file.write(json1)
file.write(l2)
file.close()
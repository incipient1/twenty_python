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

book = xlrd.open_workbook('city.xls')
sheet = book.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols

d = {}
for i in range(rows):
    for j in range(cols):
        d[str(i+1)] = sheet.cell_value(i,j)

json1 = json.dumps(d,indent=4,ensure_ascii=False)

file = open('city.xml','w')
file.write(l1)
file.write(json1)
file.write(l2)

file.close()
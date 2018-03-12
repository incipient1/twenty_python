

with open('student.txt','r') as f:
    l = []
    l.append(r'''
<?xml version="1.0" encoding="UTF-8"?>
<root>
<students>
<!--
        学生信息表
        "id" : [名字, 数学, 语文, 英文]
-->)
    ''')
    l.append(f.read())
    l.append(r'''
</students>
</root>
''')
    with open('student2.xml','w') as s:
        s.write(''.join(l))


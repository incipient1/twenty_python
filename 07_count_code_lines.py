import os

path = 'E:\Python_learning\learning_mooc\chapter_6'

for file_name in os.listdir(path):
    file1 = open('E:\Python_learning\learning_mooc\chapter_6\{}'.format(file_name))

    file_code_line = len(file1.readlines())
    file2 = open('E:\Python_learning\learning_mooc\chapter_6\{}'.format(file_name))
    file_space_line = file2.read().count('\n\n')
    file3 = open('E:\Python_learning\learning_mooc\chapter_6\{}'.format(file_name))
    file_mesh_line = file3.read().count('#')
    print('{0:<16}总行数为：{1:>2d},其中空行为:{2:d},其中注释行为：{3:d}'.format(
        file_name,file_code_line,file_space_line,file_mesh_line))
    file1.close()
    file2.close()
    file3.close()

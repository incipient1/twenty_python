file = open('filter_word.txt').readlines()

file_list = []
for i in file:
    file_list.append(i.strip('\n'))

user_input = str(input('请输入文字：'))

for word in file_list:

    if str(word) in user_input:
        print('Freedom')

    while str(word) in user_input:
        user_input = user_input.replace(str(word),'*'*len(str(word)))

    print(user_input)
    break
else:
    print('Human Rights')
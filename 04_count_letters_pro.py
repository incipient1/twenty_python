res = {}
with open('count_letters.txt') as f:
    for char in f.read():
        res[char.lower()] = res.get(char.lower(),0) + 1


res_list = list(res.items())
print(res_list)

#length = len(res_list)
#for i in range(length):
#    for j in range(1,length):
#        if res_list[j-1][1] > res_list[j][1]:
#            res_list[j-1],res_list[j] = res_list[j],res_list[j-1]

#print(sorted(res_list,key=lambda x:x[1]))


new_list = []
for x in res_list:
    for i, y in enumerate(new_list):
        if x[1] > y[1]:
            new_list.insert(i,x)
            break
    else:
        new_list.append(x)

print(new_list)



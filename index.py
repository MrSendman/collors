print("please, enter the list")
input_list = input()
list = input_list.split()
print(type(list))

if len(list[1:]) == int(list[0]):
    list.sort()
    print(list)
    for i in list[1:]:
        print(i, list.count(i))

else:
    print(' fuck, can you make a normal list?')


'''
#while implementation
list = [11,-4,6,7,8,9,-1,-1,-99,1,-3]
index = 0
size = len(list)
print("Size = ", size)

while (index < size):
    if list[index] >=0:
        print(list[index], end=" ")
    index+=1 #index = index + 1
'''

#for implementation
list = [11,-4,6,7,8,9,-1,-1,-99,1,-3]
for index in list:
    if index >= 0:
        print(index, end=" ")
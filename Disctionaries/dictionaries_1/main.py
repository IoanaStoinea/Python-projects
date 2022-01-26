numbers = {1: 12, 2: 4, 3: 8,5:100, 6:90 }
print("Len = ", len(numbers))
print("Max = ", max(numbers))
print("Min = ", min(numbers))
print("Sum of the keys= ", sum(numbers))
print("Sum of the values= ", sum(numbers.values()))
numbers.update({4:30})
print("Dictionary numbers after update: ", numbers)





















""""
orase_uk = {1: 'Londra', 2:'Liverpool', 3:'Glasgow'}

for key in orase_uk:
    print(key)
for key, value in orase_uk.items():
    print(key,value)


orase_ro = {1: 'Craiova', 2: 'Iasi', 3: 'Bucuresti'}
orase_uk = {1: 'Londra', 2:'Liverpool', 3:'Glasgow'}
print(orase_uk[1])
print(orase_uk.get(10))
orase = {'ro': orase_ro, 'uk': orase_uk}
print(orase)

if (1, 'Craiova') in orase_ro.items():
    print("True")
else:
    print("False")



eggs = {'name': 'Zophie', 'species': 'cat'}
ham = {'species': 'cat', 'age': '8','name': 'Zophie'}

if eggs == ham:
    print('True')
else:
    print('False')


orase_ro = {1: 'Craiova', 2: 'Iasi', 3: 'Bucuresti'}
del orase_ro[1]
#print(orase_ro)
#orase_ro.clear()
#print(orase_ro)
#del orase_ro
#print(orase_ro)
orase_ro.popitem()
#print(orase_ro)
"""""
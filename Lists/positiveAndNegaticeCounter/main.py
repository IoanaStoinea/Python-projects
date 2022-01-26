list = [1,2,3,4,-1,-2,-3,-4,-5]
counterPositive = 0
counterNegative = 0
for index in list:
    if index >=0:
        counterPositive += 1
    elif index < 0:
        counterNegative += 1
print("Counter positive=",counterPositive)
print("Counter negative=",counterNegative)
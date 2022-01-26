import math
'''
print("The value of 2^5: " + str(math.pow(2, 5)))
print("Square root of 625: " + str(math.sqrt(625)))
print("The value of 5^e: " + str(math.exp(5)))
print("The value of log(625), base 5: " + str(math.log(625, 5)))
print("The value of log(1024), base 10: " + str(math.log10(1024)))
print("The value of log(1024), base 2: " + str(math.log2(1024)))
'''

def hello():
    print("Salut")


for number in range(1,10+1):
    hello()
    print("The value is: " + str(math.pow(number, 2)))

def sum_lits(items):
    sumNumbers = 0
    for index in items:
        sumNumbers = sumNumbers+index # sumNumbers +=index
    return  sumNumbers
print(sum_lits([10,12,20,22]))
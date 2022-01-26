def multiply_list(items):
    total = 1
    for index in items:
        total = total * index
    return total
print(multiply_list([3,1,2,3]))
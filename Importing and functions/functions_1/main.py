'''
def hello():
    print("Hello", end="\n")
    print("What's your name?")
    name=input()
    print("Nice to meet you, " + name + "!")

hello()
'''
def access(name):
    print("Welcome " + name + "!")
    age = int(input("Please enter your age:"))
    if age > 18:
        print("You have access")
    else:
        print("You don't have access")
access('Maria')
access('Mihai')

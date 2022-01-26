"""
def function():
    # local variable
    string = "I love Python"
    print(string)
function()


def f():
    # local variable
    s = "I love Python"
    print("Inside Function:", s)
    
    
print("test")
f()
#print(s)


# Global scope
s = "I love Python"

# This function uses global variable s
def f():
	print("Inside Function", s)

f()
print("Outside Function", s)
"""""

# This function has a variable with
# name same as s.
def f():
	s = "Me too."
	print(s)

# Global scope
s = "I love Python"
f()
print(s)

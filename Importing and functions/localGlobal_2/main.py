# This function uses global variable s
def f():
	print("Inside Function", s)

# Global scope
s = "I love Python"
f()
print("Outside Function", s)

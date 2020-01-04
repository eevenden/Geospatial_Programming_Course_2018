#HW3Q3

def add(a, b):
 print "ADDING %d + %d" % (a, b)
 return a + b

def subtract(a, b):
 print "SUBTRACTING %d - %d" % (a, b)
 return a - b
	
def multiply(a, b):
 print "MULTIPLYING %d * %d" % (a, b)
 return a * b
	
def divide(a, b):
 print "DIVIDING %d / %d" % (a, b)
 return a / b

Step1 = float(add(23, 43))
Step2 = float(multiply(7, 332))
C = float(divide(Step1, Step2))

print "The answer is: ", C

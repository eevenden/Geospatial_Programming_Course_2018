#############################################################################################################################
#
#This script will allow the user to input decimal coordinates and calculate the euclidean distance between the two. Note that
#this script does not account for the curviture of the Earth and should only be used for projected points on distance-
#preserving projections. Note that this script also does not supply a unit for the output. This is because the
#output unit is equivalent to the original input unit.
#
#############################################################################################################################

# These lines print a statement, prompt an answer using 'Answer: ', and stores the user response as the variable 'answer'. 
# There is no functional purpose for this variable except to be fun.
print "Do you want to calculate Euclidean distance between two points?"
prompt = 'Answer: '
answer = raw_input(prompt)

#All of the lines below print a statement, prompt an answer, and record the raw input as a float value.
print "What is the first point's latitude?"
lat1 = float(raw_input(prompt))
print "What is the first point's longitude?"
lon1 = float(raw_input(prompt))
print "What is the second point's latitude?"
lat2 = float(raw_input(prompt))
print "What is the second point's longitude?"
lon2 = float(raw_input(prompt))

#This line imports the math module so we can manipulate the previous numeric inputs
import math

#This line calculates Euclidean Distance using the pythagorean theorem. Notice that we must call the math module in order
#to calculate the square root.
eucdis= math.sqrt(((lat2 - lat1)**2) + ((lon2 - lon1)**2))

#This line prints the calculated Eucldiean distance by inserting the eucdis value into a statement using a numeric formatter.
print "The eucldiean distance equals: %d " % eucdis
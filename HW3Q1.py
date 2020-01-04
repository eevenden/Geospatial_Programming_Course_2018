#This line opens the argument module
from sys import argv
#This line sets the argument to two variables, the old file name and new file name
script, from_file, to_file = argv
#Sets  the variable in_file to the text from the from_file input
in_file = open(from_file)
#The indata variable reads and copies the in_file data
indata = in_file.read()
#The variable out_file to set to the to_file input
out_file = open(to_file, 'w')
#The out_put file writes in the data from the indata aka (the content of in_file)
out_file.write(indata)
#Prints statement
print "Copy complete!"
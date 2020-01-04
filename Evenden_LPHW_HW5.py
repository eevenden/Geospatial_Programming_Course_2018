################################################################################
# Lessons 33-40 Study Drills
# This .py file must be submitted on Blackboard by the due date for credit.
# Save the file as "Lastname_LPHW_HW5.py".
    # You'll probably want to work out each exercise in a separate file, then
    # copy and paste your answers below. This will make it easier for you to test
    # your work.

##Q1: Complete Exercise 36. The user should make at least five choices throughout the
     # game. We'll test games in class.

#Bake A Cake Game

#Imports exit module
from sys import exit

#Creates a function called end which will print a statement at the end of the game.
def end():
 print "\n Hmm, maybe you are not a chef... \n"



#Makes a function called "egg" which takes in a raw input and converts it to an integer.
#Then uses that integer to pick a branhc in a loop and print various statemets.
def egg():
 print " \n Could you check the fridge for eggs? How many do you see?"
 eggs = raw_input("Insert number: ")
 new_eggs = int(eggs)

 if new_eggs <= 0:
  print " \n Whoops, I must've forgot to get them at the store."

  buy_a_cake()
 if new_eggs == 1 or new_eggs == 2:
  print " \n Wait, but then I won't have breakfast for tomorrow."
  #skips to buy_a_cake function
  buy_a_cake()
 else:
  print " \n Oh wait. I forgot I was saving those to get revenge on my neighbor. \n His dog has been howling and keeping me up."
  #skips to buy_a_cake function
  buy_a_cake()



 #Makes a function called "milk" which prompts the user for a string input.
 #The string input indictates a branch in the loop ad prints statments
def milk():
 print " \n Okay could you add some milk? \n I think we can just guess from the carton. \n Do you have a steady hand?"
 milk = raw_input("Yes or No?: ")
 new_milk = milk
 print "I trust you. Add two cups."

 if new_milk == "Yes" or new_milk == "yes":
  print "..."
  print " \n WOAH WOAH WOAH, you got it all over the counter. \n I thought you said you got this? Damn it. We got throw this batch out."
  #skips to buy_a_cake function
  buy_a_cake()

 else:
  print " \n Pour it into a measuring cup first. There we go."
  #skips to egg function
  egg()



#Makes a function called "butter" which prompts the user for an input.
#The input is converted to an integer
#The integer indictates a branch in the loop ad prints statments
def butter():
 print " \n Now we'll add half a stick of butter. How would you like to break it up? \n 1. Smash with hand \n 2. Smash with foot \n 3. Smash with face."
 butter = raw_input("Insert number to choose method: ")
 new_butter = int(butter)

 if new_butter == 1 or new_butter == 2:
  print "Do you know how many germs you will get in your butter?"
  #skips to the buy_a_cake function
  buy_a_cake()

 elif new_butter == 3:
  print "The face is definitely more sanitary"
  #skips to the milk function
  milk()
 else:
  print "No, no, that's not right at all. We need to scrap this batch."
  #skips to the flour function
  flour()



#Makes a function called "buy_a_cake" which prompts the user for a string input.
 #The string input indictates a branch in the loop ad prints statments
def buy_a_cake():
 print " \n Gosh, this is getting to difficult. \n Wanna just buy a cake at the store?"
 buycake = str(raw_input("Yes, no, maybe? "))

 if buycake == "Yes" or buycake == "yes":
  print " \n Good call"

 elif buycake == "Maybe" or buycake == "maybe":
  print " \n You're right, let's grab some beer instead."
  #runs end function
  end()

 elif buycake == "No" or buycake == "no":
  print " \n I guess Robert is out of luck."
  #runs end function
  end()



#Makes a function called "flour" which prompts the user for a input.
#The input is converted to an integer.
#The string input indictates a branch in the loop ad prints statments
def flour():
 print "\n Let's make a cake. How many cups of flour do you want?"

 cups = raw_input("Insert number: ")
 new_cups = int(cups)

 if new_cups <= 1:
  print "Eh I don't think that's enough. Try again."
  #skips to restart function
  restart()
 elif new_cups == 2 or new_cups == 3:
  print "Good, that's enough flour."
  #skips to butter function
  butter()
 else:
  print "Woah that is too much flour. Try again."
  #skips to restart function
  restart()



#Function called "Restart" that returns to the flour function
def restart():
 flour()



#Makes a function called "bake" which prompts the user for a string input.
#The string input indictates a branch in the loop ad prints statments.
#The bake function is the first function used in this script and will
#initiate the other functions.
def bake():
 print " \n Do you want to bake a cake for Robert's birthday?"
 answer = raw_input("Yes or no? ")

 if answer == "Yes" or answer == "yes":
  flour()

 elif answer == "No" or answer == "no":
 #exits script
  exit(0)

 else:
  print "Nevermind then"
  #exits script
  exit(0)


#Calls the function Bake
bake()









##Q2: Find another set of code (similar to HW2 Q4). Copy it into your text editor, and
     # add comments explaining what each code block does. Make a list of the functions in
     # the code, and explain what each function inputs and outputs.
##### If you find errors, send them to the author!



#PyPDF2 is a pure-python PDF library capable of splitting, merging together, cropping,
#and transforming the pages of PDF files.
#It can also add custom data, viewing options,
#and passwords to PDF files. It can retrieve text and metadata from
#PDFs as well as merge entire files together.
#
#This imports the modules "PdfFileWriter" and "PdfFileReader" from the PyPDF2 library
from PyPDF2 import PdfFileWriter, PdfFileReader
#Imports math module
import sys
import math

#Defines function called "main"
def main():
    #Begins if loop - if the length of the argument does not equal 3 parameters, print a statement and exit Python
    if (len(sys.argv) != 3):
        print("usage: python 2-up.py input_file output_file")
        sys.exit(1)
    #If the argument equal 3 parameter, print this statement
    print ("2-up input " + sys.argv[1])
    #The variable "input1" runs the PdfFileReader on the argument position 1. The addition of "rb" means the the file is opened in read and binary (according to stackoverflow).
    input1 = PdfFileReader(open(sys.argv[1], "rb"))
    #The variable "output" runs a changeable input through the PdfFileWriter module.
    output = PdfFileWriter()
    #Defines a for-loop, iterate this code block from all pages of the input 1 document. The start number is page 0, end number is page n-1, and it iterates by 2
    for iter in range (0, input1.getNumPages()-1, 2):
        #variable lhs equals input1 run through the 'get page' function. Iter equals the iteration number
        lhs = input1.getPage(iter)
        #variable rhs equals input1 run through the 'get page' function. Iter+1 equals the number of iterations + 1
        rhs = input1.getPage(iter+1)
        #Runs the "mergeTranslatedPage" function on lhs, starting at position rhs, until number of lhs, by zeros
        lhs.mergeTranslatedPage(rhs, lhs.mediaBox.getUpperRight_x(),0, True)
        #The variable 'output' becomes lhs run through the "addPage" module
        output.addPage(lhs)
        #Prints a string of the number of iterations? Plus a space
        print (str(iter) + " "),
        #Clears any working memory of the files
        sys.stdout.flush()
    #After the for loop, print a statement and input argument position 2
    print("writing " + sys.argv[2])
    #The variable outputStream equals the file function run on argument position 2. The wb mean write and binary
    outputStream = file(sys.argv[2], "wb")
    #Output equals "outputStream" run through the write module
    output.write(outputStream)
    #print statement
    print("done.")

#New if loop out side of the Main function. If a pdf name equals "__main__", run the main function on said file. Import the PdfFileReader and PdfFileWriter modules from the PyPDF2 library
if __name__ == "__main__":
    main()
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import math








##Q3: Create a dictionary containing the following set of information: The names, population,
     # quadrant (NE, SE), as well as the latitude and longitude of the centroid of all wards in DC.
     # Make your code print out the information for Wards 3, 5, 8, and 1.


#DC dictionary

#DC dictionary

#Create dictionaries for population, quadrant, and centroid of each ward in DC
Population = {'Ward 1': 82859, 'Ward 2': 77645, 'Ward 3': 83152, 'Ward 4': 83066, 'Ward 5': 82049, 'Ward 6': 84290, 'Ward 7': 73290, 'Ward 8': 81133}

Quadrants = {'Ward 1': 'NW', 'Ward 2': 'NW & SW', 'Ward 3': 'NW', 'Ward 4': 'NW & NE', 'Ward 5': 'NE', 'Ward 6': 'NE & SE', 'Ward 7': 'NE & SE', 'Ward 8': 'SE'}

Centroids = {'Ward 1': 'Long: 397275.23, Lat: 139739.35', 'Ward 2': 'Long: 396243.59, Lat: 136154.69', 'Ward 3': 'Long: 393151.59, Lat: 140946.12', 'Ward 4': 'Long: 397040.94, Lat: 143992.26', 'Ward 5': 'Long: 401259.80, Lat: 139729.13', 'Ward 6': 'Long: 399759.54, Lat: 135440.65', 'Ward 7': 'Long: 404524.96, Lat: 135462.35', 'Ward 8': 'Long: 399427.32, Lat: 130268.42'}

#Create functions for our Wards of interest (3, 5, 8, & 1)
#Print information for each ward using string and integer formatters.
def Ward_3():
 print " \n Ward 3..."
 print " \n The population of Ward 3 is: %d" % Population['Ward 3']
 print " \n Ward 3 is located in Quadrants(s): %s" % Quadrants['Ward 3']
 print " \n The coordinates of Ward 3's centroid are: %s \n " % Centroids['Ward 3']

def Ward_5():
 print " \n Ward 5..."
 print " \n The population of Ward 5 is: %d" % Population['Ward 5']
 print " \n Ward 5 is located in Quadrants(s): %s" % Quadrants['Ward 5']
 print " \n The coordinates of Ward 5's centroid are: %s \n " % Centroids['Ward 5']

def Ward_8():
 print " \n Ward 8..."
 print " \n The population of Ward 8 is: %d" % Population['Ward 8']
 print " \n Ward 8 is located in Quadrants(s): %s" % Quadrants['Ward 8']
 print " \n The coordinates of Ward 8's centroid are: %s \n " % Centroids['Ward 8']

def Ward_1():
 print " \n Ward 1..."
 print " \n The population of Ward 1 is: %d" % Population['Ward 1']
 print " \n Ward 1 is located in Quadrant(s): %s" % Quadrants['Ward 1']
 print " \n The coordinates of Ward 1's centroid are: %s \n " % Centroids['Ward 1']

#Creates a function to search wards by their number using if statements
def ward_search():
#Asks for ward number input and converts to integer
 funct = int(raw_input("Enter Ward Number: "))
#If the number fulfills one of these if statements, it will print out the ward info by calling said ward's function
 if funct == 1:
  Ward_1()
 elif funct == 3:
  Ward_3()
 elif funct == 5:
  Ward_5()
 elif funct == 8:
  Ward_8()
 #If the number does not meet one of the above requirements, it prints a statement
 else:
  print " \n Sorry that ward was not required in the homework and was too much work for midterm week. \n"

#Runs ward_search function to initiate 
ward_search()

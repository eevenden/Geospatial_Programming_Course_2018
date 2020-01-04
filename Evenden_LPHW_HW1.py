################################################################################
# Lessons 0-8 Study Drills
# This .py file must be submitted on Blackboard by the due date for credit.
# Save the file as "Lastname_LPHW_HW1.py".
    # You'll probably want to work out each exercise in a separate file, then
    # copy and paste your answers below. This will make it easier for you to test
    # your work.

    # All text based answers should use the print command to print both the question number,
    # and the answer to your question.

##Q1: What's the purpose of a directory in your Terminal? Why do we create directories?
##### Write at least three sentences below. Use the print command to write out both the question number,
##### and your answer.
#
#Assign Q1
q = "Question 1:"
#Assign answer
x = "A directory or folder is a way to store information in the terminal. When you have multiple folders, they can be stored within eachother, in which case the directory stores a path to get to each folder. For the exercises we did in LPHW, the directory commands communitcated which folders to open, close, make, etc."
#Print question and answer
print q, x




##Q2: How would you modify your Exercise 1 script to only print out one of the lines?
##### Copy and paste your modified Ex. 1 script below.

# organize sayings into a list
listx=["Hello World!", "Hello Again", "I like typing this.", "This is fun.", 'Yay! Printing.', "I'd much rather you 'not'.", 'I "said" do not touch this.']
# print by choosing position in list
print(listx[3])





##Q3: Take your Exercise 3 script, and add comments to each line, explaining what it does.
##### Copy and paste your Ex. 3 script, with comments, below.

#Exercise 3
# Print statement
print "I will now count my chickens:"

# Print "hens", does division, then addition
print "Hens", 25 + 30 / 6

#Prints "Roosters", does 25 * 3, then finds the integer remainder of dividing that product by 4. Then it subtracts that all from 100.
print "Roosters", 100 - 25 * 3 % 4

#Print statement
print "Now I will count the eggs:"

# The command finds the integer remainder of 4 / 2, which is 0. Then 1 is divded by 4, which is replaced with 0 because it is float data. Now instead, we have 3 + 2 + 1 - 5 + 6, which equals 7.
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

#Prints statement
print "Is it true that 3 + 2 < 5 - 7?"

#Print function answer in Boolean, aka False
print 3 + 2 < 5 - 7

#Print statement, then answer (5)
print "What is 3 + 2?", 3 + 2

#Print statement, then answer (-2)
print "What is 5 - 7?", 5 -7

#Print statement
print "Oh, that's why it's False."

#Print statement
print "How about some more."

#Print statement, then print answer in Boolean (True)
print "Is it greater?", 5 > -2

#Print statement, then print answer in Boolean (True)
print "Is it greater or equal?", 5 >= -2

#Print statement, then print answer in Boolean (False)
print "Is it less or equal?", 5 <= -2



##Q4: Go to the "Study Drills" section of Exercise 4. Read the error message there.
##### Explain the error in your own words. Make sure you use line numbers, and explain why, below.
#####    Use the print command to write out both the question number, and your answer.

q = "Quesiton 4:"
a = "This function is attempting to make a value for average_passengers_per_car by dividing two known values car_pool_capacity by passengars. However, the program is giving an error that car_pool_capacity is not defined, meaning the problem with the code is that there is no original car_pool_capacity defined by a number, or it was defined incorrectly with a syntax error."
print q, a




##Q5: Take your Exercise 5 script, and rewrite it to match your physical description.
##### Copy and paste your Ex. 5 script below. Add comments to each code block, explaining what it does.

#Exercise 5
#define name variable
my_name = 'Emily J Evenden'
#define age variable
my_age = 21 # not a lie
#define height variable
my_height = 67 # inches
#define weight variable
my_weight = 155 # lbs
#define eye color variable
my_eyes = 'Blue'
#define teeth color variable
my_teeth = 'White'
#define hair color variable
my_hair = 'Blonde'

#print "Let's talk about [insert string value]" assign the string variable as my_name
print "Let's talk about %s." % my_name
#print "She's [insert numeric value] inches tall." assign numeric value as my_height
print "She's %d inches tall." % my_height
#print "she's [inset numeric value] pounds heavy." assign numeric value to my_weight
print "She's %d pounds heavy." % my_weight
#print statement
print "Actually that's not too heavy."
#print "She's got [insert string value] eyes and [insert strong value] hair." assign first string value to my_eyes, assign second string value to my_hair
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
#print "Her teeth are usually [insert string value] depending on the coffee." assign string variable to my_teeth
print "Her teeth are usually %s depending on the coffee." % my_teeth

#This line is tricky, try to get it exactly right
#print "If I add {insert numeric value], {insert numeric value], and [insert numeric value] I get [insert numeric value]." assign numeric value 1 to my_age, assign numeric value 2 to my_height, assign numeric value 3 to my_weight, assign numeric value 4 sum = {my_age + my_height + my_weight}
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)




##Q6: Take your modified Ex. 5 script (Q5), and make the script convert your height from inches to centimeters.
##### Copy and paste your updated script below. Make sure you update what it prints,
##### so that the units are compatible. Make your script do the math, don't do it yourself.

#Exercise 5
#define name variable
my_name = 'Emily J Evenden'
#define age variable
my_age = 21 # not a lie
#define height variable
my_height = 67 # inches
#define weight variable
my_weight = 155 # lbs
#define eye color variable
my_eyes = 'Blue'
#define teeth color variable
my_teeth = 'White'
#define hair color variable
my_hair = 'Blonde'

#print "Let's talk about [insert string value]" assign the string variable as my_name
print "Let's talk about %s." % my_name
#print "She's [insert numeric value] centimeters tall." assign numeric value as my_height and multiple by 2.54 to convert to centimeters. I put into parentheses with float to ensure potentialy mixed data types (a variable and a number) could multiply
print "She's %d centimeters tall." % float(my_height * 2.5)
#print "she's [inset numeric value] pounds heavy." assign numeric value to my_weight
print "She's %d pounds heavy." % my_weight
#print statement
print "Actually that's not too heavy."
#print "She's got [insert string value] eyes and [insert strong value] hair." assign first string value to my_eyes, assign second string value to my_hair
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
#print "Her teeth are usually [insert string value] depending on the coffee." assign string variable to my_teeth
print "Her teeth are usually %s depending on the coffee." % my_teeth

#This line is tricky, try to get it exactly right
#print "If I add {insert numeric value], {insert numeric value], and [insert numeric value] I get [insert numeric value]." assign numeric value 1 to my_age, assign numeric value 2 to my_height, assign numeric value 3 to my_weight, assign numeric value 4 sum = {my_age + my_height + my_weight}. In both cases I used the float identifier again to convert the height from inches to centimeters by multiplying by 2.5
print "If I add %d, %d, and %d I get %d." % (my_age, float(my_height * 2.5), my_weight, my_age + float(my_height * 2.5) + my_weight)





##Q7: Go through your Exercise 6 script and identify all the placed where a string is put inside a string.
##### Below, make a list of those places. Explain how you know you've found them all.
#####    Use the print command to write out both the question number, and your answer.

q = "Question 7:"
a = "I know that string scripts where put into larger strings at lines 18, 26, and 28 (the places which inserted my_name, my_eyes, my_hair, & my_teeth). I know this becase they are inserted using %s. s in that formatter represents 'string', so it is used to call in new string data. I also know these lines call string data into existing string data because they are printing phrases in quotes, which are also string data. These quoted string phrases call the small string phrases using formatters, as I mentioned earlier"
print q, a

# Before submitting, please make sure that your "Lastname_LPHW_HW1.py" code can be executed in python
# without any errors.

# I grade these based on a few critieria. 1) Are you answering the question correctly?
# I should be able to execute your code, and see all the correct answers print out to me, and
# 2) Have you annotated your code (please use # to add comments explaining how each major code
# block works, you will lose points otherwise).

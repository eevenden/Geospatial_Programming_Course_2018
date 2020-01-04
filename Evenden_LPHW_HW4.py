#################################################################
# Lessons 25-32 Study Drills
# This .py file must be submitted on Blackboard by the due date for credit.
# Save the file as "Lastname_LPHW_HW4.py".
    # You'll probably want to work out each exercise in a separate file, then
    # copy and paste your answers below. This will make it easier for you to test
    # your work.

  ##Q1: Complete Exercise 25 (not the Study Drills). Submit your completed code, with comments
      # on each code block.

      #This code block breaks apart the sentence into each word.
      def break_words(stuff):
       """This function will break up words for us."""
       #Uses split function to divide the words at a space
       words = stuff.split(' ')
       #'Saves' words into code
       return words

       #This code block sorts the words alphabetically.
      def sort_words(words):
       """Sort the words."""
       #Saves the sorted words
       return sorted(words)

       #This code block prints the first word in our (non-sorted) words
      def print_first_word(words):
       """Prints the first word after popping it off."""
       #Identifies the first word using the zeroth position
       word = words.pop(0)
       #Prints the word
       print word

       #This code block prints the last word in our unsorted words
      def print_last_word(words):
       """Prints the last words after popping it off."""
       #Identifies the last word as the negative one position. I'm not sure why, but my
       # guess is that it can loop backwards from the 0th position to find the last word.
       word = words.pop(-1)
       #Prints the word
       print word

       #This code block identifies the individual words in the sort sentence.
      def sort_sentence(sentence):
       """Takes in a full sentence and returns the sorted words."""
       #Applies our pre-defined break_words function to the sentence
       words = break_words(sentence)
       #Applies out pre-defined sort_words function to the words.
       return sort_words(words)

       #This code block prints the first and last word
      def print_first_and_last(sentence):
       """Prints the first and last words of the sentence."""
       #Applies pre-defined break words function to the sentence
       words = break_words(sentence)
       #Applies pre-defined print first word function to words
       print_first_word(words)
       #Applies pre-defined print last word function to words
       print_last_word(words)

       #This code block prints the first and last word of the sorted sentence.
      def print_first_and_last_sorted(sentence):
       """Sorts the words then prints the first and last one."""
       #Applies pre-defined sort sentence function to our sentence
       words = sort_sentence(sentence)
       #Applies pre-defined print first words function to the sorted words
       print_first_word(words)
       #Applies pre-defined print last words function to the sorted words
       print_last_word(words)




##Q2: Complete Exercise 26. Submit your edited code below, with comments.

#This code block breaks apart a sentence into its individual components. No errors here.
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

#This code block sorts the individual words in a sentence. No errors here.
def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#This code block prints the first word of the sentence.
#Two errors here - fix type (poop to pop), add colon
def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word

#This code block prints the last word of the sentence. One error here, needs a closed parentheses.
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

#This code inputs the sentence and sorts the words using the prexisting break_words and sort_words functions
#One error, words line tabbed into place instead of using spaces
def sort_sentence(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#This code block prints the first and last words of the senence by using the pre-existing break_words, print_first_word, print_last_word
#No errors
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

#This code block prints the first and last word of the alphabetically sorted sentence using prexisting functions.
#No errors
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

#Moved this part of the code here because it was poorly organized originally.

#Added lines to import ex25 file and prompt for a sentence and define words & sorted words

import ex25
prompt = 'Input: '
sentence = str(raw_input(prompt))
words = break_words(sentence)
sorted_words = sort_words(words)

#Calls the print_first word function for words
ex25.print_first_word(words)
#Calls the print_last_word function for words
ex25.print_last_word(words)
#Calls the print_first_word function sorted words
#One error, extra period removed
ex25.print_first_word(sorted_words)
#Calls the print_last_word function for the sorted words
ex25.print_last_word(sorted_words)
#Stores sorted words as a variable.
#One error, fixed types in the function name and the parameter used.
sorted_words = ex25.sort_words(words)
#Print sorted words
#One error, print misspelled.
print sorted_words

#Prints the first and last words in the non-sorted sentence
#One error, fix typo in function name
ex25.print_first_and_last(sentence)
#Prints the first and and last words in the sorted sentence
#Two errors, fix typos in function and variable name
ex25.print_first_and_last_sorted(sentence)



#Prints statement
print "Let's practice everything."
#Prints another statement but makes sure other ' and \ are a part of the string by preceding them with \.
#\n and \t are used to make a new line and add a tab within the string
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

#Defines poem as many lines of text with addition \t and \n for tabs and new lines.
#No errors
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

#Prints hyphens and lines
#No errors
print "--------------"
print poem
print "--------------"

#Defines five as a series of math operations. The inserts five into a statment using a string formatter.
#No errors
five = 10 - 2 + 3 - 5
print "This should be five: %s" % five

#Defines the function secret_formula
#One error, uses and backslash instead of a forward slash for jellybeans divided by 1000
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

#Sets the variable start_point to 10000
#Two errors, uses == instead of =, also type in varibale name (switch _ to -)
start_point = 10000
beans, jars, crates = secret_formula(start_point)

#Prints start point using numeric formatter
#One error, typo (change jeans to beans) in secnod print statement
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

#Sets a new start_point of itself divided by 10
start_point = start_point / 10

#Prints two statements, one uses numeric formatters.
#One error - closed the parentheses for the formatter
print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)










##Q3: Complete Exercise 28 (not the Study Drills). Submit your answers as comments below.

print "Homework 4, Question 3: "
print """
1. True
2. False
3. False
4. True
5. True
6. True
7. False
8. True
9. False
10. False
11. True
12. False
13. True
14. False
15. False
16. False
17. True
18. True
19. False
20. False
"""




##Q4: Write a script which uses a function to call a while-loop, and replace the number of (e.g. while less than A) the while-loop with a variable.
##### If you write a script you can't stop executing, hit ctrl-c while in terminal.

prompt = 'Insert number: '
apples = int(raw_input(prompt))

while True:
 if apples > 6:
  print "Yum! We have enough apples to make a pie!"
  break

 else:
  print "We do not have enough apples!"
  break

print "Thanks for asking!"





##Q5: Using Exercises 29-35, design another text adventure game. This time, Make sure that our text adventure
      # should have a minimum of three choices the user gets to make. Make sure that
      # your adventure does not have any "dead ends", meaning if the user enters information,
      # they should always be taken to a portion of your code. Add comments to each code
      # block, to explain your code to another person.
      # Please submit your game seperately as Last_name_Game_HW4.py on BB.

##### Test your game to make sure it doesn't break. In class, we'll test each other's games.




# Before submitting, please make sure that your "Lastname_LPHW_HW4.py" code can be executed in python
# without any errors.

# Please submit your game seperately as Lastname_Fistname_Game_HW4.py on BB.

# I grade these based on a few critieria. 1) Are you answering the question correctly?
# I should be able to execute your code, and see all the correct answers print out to me, and
# 2) Have you annotated your code (please use # to add comments explaining how each major code
# block works, you will lose points otherwise. Anotations of your do not need to be printed).

# the first two lines initiate an arguement 
import sys

from sys import argv

#In this line, the argument is set up to include one variable (user_name_ which you must enter while calling the initial argument)
script, user_name = argv
# This enters a ">" at every point a raw_input is expected
prompt = '> '

#These lines print statements, and fill in the user_name and script using string formatters
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."

#This line prints a question, inserting the user_name using a string formatter.
print "What is your favorite fruit %s?" % user_name
#The variable is set by prompting the user to type an answer to the question.
fruit = raw_input(prompt)

#The comments from above apply to the following 3 code blocks.
print "What school do you go to %s?" % user_name
school = raw_input(prompt)

print "What kind is your favorite color %s?" % user_name
color = raw_input(prompt)

print "Do you enjoy coding python %s?" % user_name
python = raw_input(prompt)

#The program prints the answers to the questions in a large, multi-line text block by replacing the raw_input formatters with the saved variables from the aforementioned prompts.
print """
So, %s, your favorite fruit is %r.
You go to %r for school, meh.
Your favorite color is %r, nice!
And, you said %r about liking python. That's alright I guess. 
""" % (user_name, fruit, school, color, python)
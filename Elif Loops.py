#Exercise 36

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
  
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
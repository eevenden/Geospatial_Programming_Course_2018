#HW3Q5

from sys import argv

script, text = argv

def rev_printer(text):
 print "This is the original"
 A = text.split()
 words = A
 for word in words:
  print "%s" % word
 
 print "Now reverse!"
 sentence_rev = " ".join(reversed(words))
 B = sentence_rev.split()
 backwords = B
 for word in backwords:
  print "%s" % word
 
rev_printer(text)
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
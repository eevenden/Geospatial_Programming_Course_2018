
def dogs_and_cats(dog_count, cat_count):
 print "The number of dogs is: %d" % dog_count
 print "The number of cats is: %d" % cat_count
 print "Ya know, I really prefer cats."
 
def add(dog_count, cat_count):
 z = dog_count + cat_count
 print "The sum is : %d" % z
 

#One way to pass an argument is directly
print "Version 1: "
dogs_and_cats(10, 3)
add(10, 3)


#A second way to pass an argument isto use variables
print "Version 2: "
dogs = 24
cats = 15

dogs_and_cats(dogs,cats)
add(dogs,cats)

#A third way to pass the argument is combining math and variables
print "Version 3: "
dogs_and_cats(dogs + 54,cats + 90)
add(dogs + 54, cats + 90)

#Exercise 20


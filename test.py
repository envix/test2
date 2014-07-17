from sys import exit

#test python program

#print "Hi There"


#sum = 2 + 4 * 4

#print sum

my_name = 'Tom Smith'
my_age = 24
people = 5
cars = 6


print "This is %s" % my_name
print "He's %d years old" % my_age

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars"
else: 
	print "We can't decide"

def room():
print "This is 35 Chestnut Court"
next = raw_input("> ")
if "0" in next or "1" in next:
how_much = int(next)


#we are going to look at the slicing of strings
b ="hello, world"
#starting and ending point #llo
print(b[2:5])

#from beginning to a point   #hello
print(b[:5])

#from a psotion to the end   #llo, world
print(b[2:])

#negative indexing can be used to slice the strings from the end
print(b[-5:-2])
#w are going to look at unpacking of tuples

fruits = ( "apple", "mango" , "banana" , "watermelon " ,"kiwi" ,"orange" , "lemon")


#The asterisk willl assign the rest of the variables to the value "red"
#If the asterisk is at the center then the The values placed under the variable will occupy all but leave the remaining one behind 
(green,*yellow,red,indigo)= fruits

print(green)
print(yellow)
print(red)
print(indigo)
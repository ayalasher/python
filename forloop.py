#we are going to look into for loops
#It cna be used to Iterate over a list , tuple , dictionary , set or even a string
cars = ["cayenne","fortuner","model-x","cybetruck"]

#print-out of all the Items of the list
print(cars)


#using of the for loop 
#individual print-out of the Items in the list
for x in cars :
    print(x)

#It can even work for strings

#all the Items forming the string are going to be printed out individually
for y in "tangerine" :
    print(y)

#The break statement stops the loop before it has gone through ell the elements of the loop
# break is usually used after the "print" command

#continue stops the current Iteratiion of the loop and proceeds to the next Iteration of the loop
    #It is after the "for x in x statement"

    #range

    print("The range piece of code ")
#The range can even include two numbers
#Three values will be for specifying even the incfrement value for the loop
    for z in range(3,9) :
        print(z)

#else in the loop can be used to specify the code to be run after the execution of the loop
#note that incase "break" is used then the cod ein the else is not going to run
        
        #nested for loops 
Ccars = ["x6","cayenne","fortuner"]

Ecars = ["model-x","BYD","cybertruck"]


#pass is also available in incase you have no code block to be executed in after the for conditon 
for a in Ccars :
    for b in Ecars : 
        print(a,b)
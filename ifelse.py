#we are going to look into how if statements are made
#simple example below
#comparing two variable swhich have been assigned a number
a = 200 
b = 300

#note that indentataion and the use of the colon is very crucial in this concept of python programming

if a > b :
    print("a is larger than b")

elif a==b : 
    print("The two nubers are equal")

else : 
    print("b is larger than a ")

#There is also a one line way of writing if statements
x = 200
y = 20
#short hand if
if x > y : print("x is greater than y ")#Incase the condition is not met then  nothing is going to be printed

#short hand if.....else
print("x ix graeter than y ") if x > y else print("y is greater then x ")

#you can evene have three or more statements in just one line
print("x ix greater than y ") if x > y else print("They are equal ") if a==b else print("y is greater than x")

#and , or and not are logical operators that can be used with the if statement to combine statements
#If you want to leave the if statemant blank after writing the condition you can use the keyword pass

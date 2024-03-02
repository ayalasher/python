#we are goig to look at other parts of functions
#here we have on eparameter with mant arguments to deal with
def children(*kids) :
    print("The last child is " + kids[2])


children("james","brian","stewie")


#another way to do it 

print("another way to do it !!! ")

#The car1 , car2 and car3 are parameters 
def movement(car1 , car2 , car3) : 
    print("My best car is the " + car3)

#The ones below are the arguments or th einformation or the parameter values
movement(car1="cayenne", car2="fortuner", car3="X6")


#arbitrarery keywords **krangs
#This is for one parameter and many arguments
#The review of krangs
#**jobs 
def occupation(**jobs):
    print("His occupation is "+ jobs["hired"])

occupation( hired = "law" , business = "goverment tenders" )

#the default parameter value
#This will ensure that a default value ois going to be displayed incase the function is called without the parameter 
#This default value is going to be put into the function during function declaration

def mycountry(country = "norway") :
    print("I am from " + country) 

mycountry("kenya")
mycountry("nigeria")
mycountry()#since no argument has been placed into the function caling then the default value "norway" is going to be displayed
mycountry("ghana")
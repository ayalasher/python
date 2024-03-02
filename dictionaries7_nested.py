#we are going to look at how dictionaries can be nested and the different ways to play around with them
#There are two ways you can create  and work with nested 

#This is method one of creating a nested  dictionary
myfamily = {
   "child1" : {
       "name" : "nyasikera" ,
       "year" : "2004"
   } , 

   "child2" : {
       "name" : "mwondi",
       "year" :  "2019"
   } , 

   "child3" : {
       "name" : "omondi" , 
       "year" : "2020"
   }
   
}

print(myfamily)
print(myfamily["child1"]["name"])#The output is the name of the second child ...In this case it is going to be nyasikera

#the second one is as follows
#It involves creating Three dictionaries and making one main dictionary to store all the small ones

tesla = {
    "model" : "cybertruck" , 
    "year" : 2024
}

porsche = {
    "model" : "cayenne" , 
    "year" : 2020
}

toyota = {
    "model" : "fortuner" , 
    "year" : 2020
}

cars = {
    "tesla" : tesla , 
    "porsche" : porsche , 
    "toyota" : toyota 
} 

print(cars)

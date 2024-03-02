#we will be formating strings

age = 19 

quantity = 15
itemo = 564
price = 50 

txt = "My name is maxwel and i am {}"

txt1 = "I need {} mangoes each weighing {} grams and each costs {} shillings"

#indexing can also be used inside the curly brackets...the indexing is similar to that of arrays
print(txt1.format(quantity,itemo,price))

print(txt.format(age))

#It can even be used with many things 
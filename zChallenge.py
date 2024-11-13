#!python3
# Explain what this code does

import random
x = [] # Creates a list 
y = [] # list of random.randint(0,1) picked
for i in range(40): 
    rand_pick = random.randint(0,1)
    if rand_pick : # randomly true or false => 1:true 0:false
        x.append(random.randint(1,10)) #int
        y.append(rand_pick)
    else:
        x.append(random.randint(1,10) + random.randint(1,10)/10) # number with 1 digit after decimal point
        y.append(rand_pick)

print(x) #prints
print(y)
 
# this code generate a list of 40 numbers, which are either integer or number with one digit after decimal point.
import random #load random Module
N = random.randint(1,6) #Any integer from 1 to 6 randomly
if N > 3: #Judgment is greater than 3
	print('Big, ','The generated value is',N,'.') #If greater than 3 run
else: 
	print('small, ','The generated value is',N,'.') #If less than 3 run

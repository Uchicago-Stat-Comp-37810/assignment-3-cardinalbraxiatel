# Name: Patrick Walker (cardinal.braxiatel)
# hw3.py

##### Template for Homework 3, exercises 1 -  ######

import math
import random
# ********** Exercise 1 **********
def is_divisible(m,n):
    if (n == 0):
        return "Dividing by zero is not permissible."


    zed = m%n
    if( zed == 0):
        T_F = True
    else:
            T_F = False
    return T_F


# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

print is_divisible(10, 5)  # This should return True
print is_divisible(18, 7)  # This should return False
print is_divisible(42, 0)  # What should this return?
## I wasn't sure if you were trying to get me to realize the last
## call was problematic, so I included a line to break the function
## before the divide by 0 error occurred

# ********** Exercise 2 **********

class compare:
    def method( uno, dos):
    
        numerical = [float, int] #set of numerical classes for individual numbers, if I generalize this to vectors, will need to be expanded
        if(type(uno) == type(dos)):
               ok = True 
        else:
            if((type(uno) in numerical) and (type(dos) in numerical)):
                ok = True
            else:
                ok = False
                return "types of object aren't comparable" #prevents string and int errors
            
        if(ok == True):    
            if (uno > dos):
                    Unequal = True
            else:
                if (uno < dos):
                    Unequal = True
                else:
                    Unequal = False
        return Unequal #if the numbers are unequal, it returns true
    
trial = [1,2]
compare.method(trial[0],trial[1])
trial = [2,1]
compare.method(trial[0],trial[1])
trial = [2,2]
compare.method(trial[0],trial[1])
trial = [0,0]
compare.method(trial[0],trial[1])
trial = [1,0]
compare.method(trial[0],trial[1])
trial = ["a","aa"]
compare.method(trial[0],trial[1])
trial = ["a",1]
compare.method(trial[0],trial[1])
trial = ["a","a"]
compare.method(trial[0],trial[1])
trial = [0.777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777,1]
compare.method(trial[0],trial[1])
trial = [0.999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,1]
compare.method(trial[0],trial[1])
##I included this last one since 0.999 repeating should be equal to 1; I'm not sure what the convention is here for programming
##so I assume that python treats a string of 9s following the decimal point as 0.999 repeating




# ********** Exercise 3 **********
def multiadd(a,b,c):
    ans = a*b + c
    return ans



multiadd(2,math.log(12,7),math.ceil(276/19))

# Test Cases
angle_test = multiadd((1/2), math.cos(math.pi/4), math.sin(math.pi/4))
print "sin(pi/4) + cos(pi/4)/2 is:"
print angle_test

ceiling_test = multiadd(2,math.log(12,7),math.ceil(276/19))
print "ceiling(276/19) + 2 log_7(12) is:"
print ceiling_test


# ********** Exercise 4 **********

def rand_divis_3():

    rnd = random.randint(0,100)
    print(rnd)
    if(rnd%3 == 0):
        return True
    else:
        return False

rand_divis_3()

rand_divis_3()

rand_divis_3()

rand_divis_3()

rand_divis_3()

rand_divis_3()

rand_divis_3()

rand_divis_3()

# Test Cases
##### YOUR CODE HERE #####

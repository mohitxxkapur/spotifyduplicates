import random

def rng(lim):

    while(lim < 0): 
        if lim < 0:
            myError = ValueError('Lim should be positive')
            raise myError
        else: 
            break

    randval = random.randint(0,lim)
    return randval


#xxxx=int(input("Please enter the limit: "))
#print(rng(xxxx))
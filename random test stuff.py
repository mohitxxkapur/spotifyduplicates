    if (lim < 0):
        print("Not valid")
    else:
        randval = random.randint(0,lim)
    return randval



    while(True):
        try:
            assert lim > 0
            randval = random.randint(0,lim)
            break
        except AssertionError:
            print ("Please enter a positive number")
            raise

    while(True): 
        if lim < 0:
            myError = ValueError('Lim should be positive')
            raise myError
        else: 
            break
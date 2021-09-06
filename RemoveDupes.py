import rng as rngg

def removeDupe(lst):
    cleanedList = []
    for x in lst:
        if x not in cleanedList:
            cleanedList.append(x)
    return cleanedList

ctr = 0 
lst = []
size = int(input("What is the size of the list you would like to have: "))
xxxx=int(input("Please enter the limit: "))

while ctr < size:
    val = rngg.rng(xxxx)
    #print(val)
    lst.append(val)
    ctr+=1

print("List with duplicates: ", lst)
clean = removeDupe(lst)
print("List after removing duplicates: ", clean)


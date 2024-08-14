myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

myset=set(myList)

mydict={}

for i in myset:
    mydict[i]=myList.count(i)

print(mydict)
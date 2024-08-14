lst=["A", "B", "C", "D", "E", "F", "G", "L", "Q", "U"] 

ls=[]
n = int(input("sonni kiriting\n"))
if n > len(lst):
    print("kichik son kiriting\n")
    exit()
t = 0
for i in range(len(lst) // n):
    lsm=[]
    for j in range(n):
        lsm.append(lst[t])
        t += 1
    ls.append(lsm)

print(ls)

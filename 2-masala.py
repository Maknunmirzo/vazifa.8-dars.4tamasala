txt=input("matnni kiriting\n")

lsn=txt.split("*")
fn=lsn.pop()

for i in lsn:
    print(f"{i}+",end="")

print(fn)
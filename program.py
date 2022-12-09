a=input("Enter start date: ")
b=input("Enter end date: ")
leap=[]
nonleap=[]
s=int(a[7:11])
e=int(b[7:11])
for i in range(s,e+1):
    if i%4==0:
        leap.append(i)
    else:
        nonleap.append(i)
print("\n")
print("------------------LEAP YEARS---------------------")
for i in leap:
    print(i,end="  ")
print("\n")
print("----------------NON LEAP YEARS-------------------")
for i in nonleap:
    print(i,end="  ")

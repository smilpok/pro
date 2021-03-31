a=input()
b=input()
c=input()
d=input()
e=[]
trantab=d.maketrans(b,a)
dict=dict(zip(a,b))
for i in range(len(c)):
    if c[i] in dict:
        e.append(dict.get(c[i]))
    if c[i] not in dict:
        continue
print(*e,sep="")
print(d.translate(trantab)) 

a = 0
b = 0
c = 1
list=[]
for i in range(101):
    list.append(a)
    a = b + c
    c = b
    b = a
x=sum(list)
print(x)
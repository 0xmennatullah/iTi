# 1. write 3 variable and check for it's data types using type() function
a = 1
b = 'oi'
c = '123'
print(type(a), type(b), type(c))


#2. write 3 variable and take it in one line using split() function and print it
d, e, f = input('enter 3 numbers: ').split()
print(type(d), type(e), type(f))


#3
g = input("enter number: ")
print(len(g))


#4
h, j = input("enter the original number, then enter no. digits to remove!").split()
h = int(h)
j = int(j)
k = h // (10**j)
print(k)



#5
l = map(int, input("enter multiple numbers: ").split())
l = list(l)
print(f"max: {max(l)} |  min: {min(l)}")


#6
o = input("enter a number: ")
o = int(o)
p = input("enter 2nd number: ")
p = int(p)
if o<p:
    print("o is greater than b")
else:
    print("b is greater than or equal to o")


#7
q = input("enter ur salary: ")
q = int(q)
if q > 1000:
    print("ur poor")
elif q >= 1000 & q < 2000:
    print("good salary")
else:
    print("ur rich")
    

#8
age = input("enter ur age: ")
age = int(age)
if age>18:
    print("you can drive")
else:
    print("you cannot drive")

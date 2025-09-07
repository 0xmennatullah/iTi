
#1 
salary = input("enter ur salary: ")
salary = int(salary)
if salary > 1000:
    print("ur poor")
elif salary >= 1000 and salary < 2000:
    print("good salary")
else:
    print("ur rich")

#2
age = input("enter ur age: ")
age = int(age)
if age>18:
    print("you can drive")
else:
    print("you cannot drive")

#3
n1 = input("enter 1st number: ")
n1 = int(n1)
n2 = input("enter 2nd number: ")
n2 = int(n2)
if n1<n2:
    print("number1 is greater than number2")
else:
    print("number2 is greater than or equal to number1")

#4
num1 = input("enter 1st number: ")
num1 = int(num1)
num2 = input("enter 2nd number: ")
num2 = int(num2)
if num2 == 0:
    print("cannot divide by zero")
else:
    print(num1/num2)

#5
for i in range(0, 13, 3):
    print(i)

#6
for i,j in enumerate(range(0, 13, 3)):
    print(i,j)

#7
lst = [1,2,3,4,5,6,7]
result = [(i**2) for i in lst]

#8
def conc( l1,  l2):
    return l1+l2

#9 reverse tuple
t1 = (1,2,3,4)
print(tuple(reversed(t1)))

#10
values1 = ["Ten", "Twenty", "Thirty"]
keys1 = [10, 20, 30]

result = dict(zip(keys1, values1))
print(result)

def circle_area(r):
    pi=3.14
    area=pi*r**2
    return area

s=circle_area(5)

def square(x):
    sq=x**2
    return sq


def is_even(n):
    n=int(input("请输入n："))
    if n%2==1:
        return True
    else:
        return False
x=is_even(4)
print(x)

def my_max(a,b,c):
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    return max
x=my_max(3,5,8)
print(x)

def factorial(n):
    result=1
    for i in range(1,n+1):
        result *=i
    return result
x=factorial(5)
print(x)

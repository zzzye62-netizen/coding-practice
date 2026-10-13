age = 22
name = "john"
print(f"my name is {name}, i am {age} years old")


age = input("请输入年龄：")
print(age)
print(type(age))


age = int(input("请输入年龄："))
print(age)
print(type(age))
print(age+1)

print(5 / 2)# 2.5
print(5 // 2)# 2
print(5 % 2)# 1
print(2 ** 3)# 8

tem=float(input("请输入摄氏温度："))
tem2= (tem * 1.8) + 32
print(f"摄氏温度为{tem}，转换为华氏温度为{tem2}")


height=float(input("请输入身高(m)："))
weight=float(input("请输入体重(kg)："))
bmi=weight/(height**2)
print(f"身高为{height}米，体重为{weight}公斤，BMI指数为{bmi}")

pi = 3.1415926
r=float(input("请输入圆的半径："))
c=2 * pi * r
s=pi * (r ** 2)
print(f"圆的周长为{c:.2f},面积为{s:.2f}")

a=float(input("请输入边长a:"))
b=float(input("请输入边长b:"))
c=float(input("请输入边长c:"))
if a+b>c and a+c>b and b+c>a:
    print("是三角形")
    if a==b==c:
        print("是等边三角形")
    elif a==b or a==c or b==c:
        print("是等腰三角形") 
    else:
        print("普通三角形")
else:
    print("不是三角形")

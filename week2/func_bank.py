#全局变量
money = 5000000
name = input("请输入姓名：")
#函数
def check(show_head):
    if show_head == True:
        print("------------查询余额-------------")
    print(f"{name}，您好，您的余额剩余：{money}")

def save_money(num):
    global money
    money += num
    print("------------存款-------------")
    print(f"{name}，您好，您存款{num}元成功")
    check(False)

def get_money(num):
    global money
    money -= num
    print("------------取款-------------")
    print(f"{name}，您好，您取款{num}元成功")
    check(False)

def meau():
    print("------------主菜单-------------")
    print(f"{name}，您好，欢迎来到银行，请选择操作：")
    print("查询余额[输入1]")
    print("存款[输入2]")
    print("取款[输入3]")
    print("退出[输入4]")
    return input("请输入您的选择：")

while True:
    Keyboard_input = meau()
    if Keyboard_input == "1":
        check(True)
    elif Keyboard_input == "2":
        num = int(input("请输入想存多少钱："))
        save_money(num)
    elif Keyboard_input == "3":
        num = int(input("请输入想取多少钱："))
        get_money(num)
    else:
        print("程序退出")
        break
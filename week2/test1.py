# #布尔类型和比较运算.py
# num1=0
# num2=0
# print(f"两者是否相等的结果是:{num1==num2}")
# #==,!=,>,<,>=,<=


# #if语句的基本格式
# print("游乐园儿童免费，成人收费")
# age=int(input("请输入你的年龄："))
# if age>=18:
#     print("成年人，补票10元")
# elif 0<=age<18:
#     print("未成年免费")
# else:
#     print("输入错误")


# #test1
# num=5
# if int(input("请猜一个数字：")) == num:
#     print("恭喜第一次就猜对了")
# elif int(input("猜错了")) == num:
#     print("恭喜第二次猜对了")
# elif int(input("猜错了")) == num:
#     print("恭喜最后一次猜对了")
# else:
#     print("sorry,猜错了")


# #嵌套
# if int(input("你的身高是多少："))>120:
#     print("身高超出限制，不可以免费")
#     print("但是，如果vip级别大于3，可以免费")

#     if int(input("你的vip级别是多少："))>3:
#         print("恭喜你，vip级别达标，可以免费")
#     else:
#         print("Sorry你需要买票10元")
# else:
#     print("欢迎小朋友，免费游玩。")


# #猜数字
# import random
# num = random.randint(1,10)

# # 第一次猜测
# guess1 = int(input("请输入你猜的数字（1-10）："))
# if guess1 == num:
#     print("恭喜，第一次就猜对了！")
# else:
#     if guess1 > num:
#         print("猜大了，还有2次机会")
#     else:
#         print("猜小了，还有2次机会")
#     # 第二次猜测（嵌套在第一次猜错里面）
#     guess2 = int(input("请输入你猜的数字（1-10）："))
#     if guess2 == num:
#         print("恭喜，第二次猜对了！")
#     else:
#         if guess2 > num:
#             print("猜大了，还有1次机会")
#         else:
#             print("猜小了，还有1次机会")
#         # 第三次猜测（嵌套在第二次猜错里面，第三层判断）
#         guess3 = int(input("请输入你猜的数字（1-10）："))
#         if guess3 == num:
#             print("恭喜，第三次猜对了！")
#         else:
#             if guess3 > num:
#                 print("猜大了！")
#             else:
#                 print("猜小了！")
#             print(f"三次机会用完，游戏结束，正确数字是：{num}")


#用while或for实现
import random
num = random.randint(1,10)
count = 3
while count > 0:
    guess = int(input(f"请输入你猜的数字,你还有{count}次机会！："))
    if guess == num:
        print("猜对了！游戏结束。")
        break
    elif guess > num:
        print("猜大了")
    else:
        print("猜小了")
    count-=1
if count == 0:
    print("次数用完了,游戏结束")
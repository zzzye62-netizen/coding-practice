f = open("D:\Coding\week3\word.txt","r",encoding="UTF-8")
##1.自己写的
# sum = 0
# for line in f:
#     if "itheima" in line:
#         sum +=1
# print(sum)
#f.close()

# #2.方法1
# content = f.read()
# count =  content.count("itheima")
# print(f"itheima在文件中出现了{count}次")
# f.close()

#方法2
count = 0
for line in f:
    line = line.strip()#去除开头和结尾的空格，换行符
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(f"itheima在文件中出现了{count}次")
f.close()


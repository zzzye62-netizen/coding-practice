# 项目01：电商订单数据去重与消费统计
# 练习知识：列表、字典、集合、for循环、if判断

orders = [
    {"order_id": 1, "user": "小王", "amount": 100},
    {"order_id": 2, "user": "小李", "amount": 80},
    {"order_id": 3, "user": "小王", "amount": 50},
    {"order_id": 2, "user": "小李", "amount": 80},
    {"order_id": 4, "user": "小张", "amount": 200},
    {"order_id": 5, "user": "小李", "amount": 120},
    {"order_id": 3, "user": "小王", "amount": 50}
]

#1. 找出所有不同的用户.输出所有出现过的用户名，不允许重复。
unique_users = set()

for order in orders:
    unique_users.add(order["user"])

print("所有不同的用户：", unique_users)

#2. 删除重复订单.根据 order_id 去重，只保留第一次出现的订单，并将结果放入新的列表。
seen_order_ids = set()  # 记录已经出现的订单编号
unique_orders = []      # 保存去重后的完整订单

for order in orders:
    order_id = order["order_id"]

    if order_id not in seen_order_ids:
        seen_order_ids.add(order_id)
        unique_orders.append(order)

print("去重后的订单：", unique_orders)
#假如有同一个id的人的不同金额的信息，
#可以把订单编号和金额组合成一个元组order_key = (order["order_id"], order["amount"])


#3. 计算总销售额.只统计去重后的订单金额，不能把重复订单计算两次。
total_amount = 0

for order in unique_orders:
    total_amount += order["amount"]

print(f"总销售额：{total_amount} 元")

#4. 统计每位用户的消费.得到一个字典，键是用户名，值是这个用户所有有效订单的金额之和。
user_totals = {}

for order in unique_orders:
    user = order["user"]
    amount = order["amount"]

    if user not in user_totals:
        user_totals[user] = amount
    else:
        user_totals[user] += amount

print("各用户消费金额：", user_totals)


#5. 找出消费最多的用户.从第四关的字典中找出消费金额最高的人。
if user_totals:#防止字典为空
    max_amount = max(user_totals.values())

    for user, amount in user_totals.items():
        if amount == max_amount:
            print(f"消费最多的用户：{user}，金额：{amount} 元")
else:
    print("没有有效订单，无法统计最高消费用户")

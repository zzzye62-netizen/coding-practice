def show(*args, **kwargs):
    print("args =", args)
    print("kwargs =", kwargs)

show(10, 20, city="上海", age=18)
show(city="上海")
show(10, 20)

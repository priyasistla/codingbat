def left2(str):
    n=len(str)
    if n>2:
            left=str[0:2]
            rest=str[2:]
            return rest+left
    return str
print(left2("hello"))
print(left2("java"))
print(left2("hi"))

def make_cho(small,big,goal):
    if small*1+big*5>=goal:
        return small
    else:
        return -1

print(make_cho(4,1,9))
print(make_cho(4,1,10))
print(make_cho(4,1,7))

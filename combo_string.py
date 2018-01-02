def combo_string(a,b):
    na=len(a)
    nb=len(b)
    if a>b:
        return b+a+b
    else:
        return a+b+a
print(combo_string("hello","HI"))
print(combo_string("HI","hello"))
print(combo_string("aaa","B"))
    

def love6(a,b):
    if a==6 or b==6:
        return True
    else:
        if abs(a+b)==6:
            return True
        elif abs(a-b)==6:
            return True
        else:
            return False


print(love6(1,6))
print(love6(1,5))
print(love6(30,24))
print(love6(3,8))

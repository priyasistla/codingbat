# Chethan's code
def sleep_in(weekday, vacation):
    if vacation:
        return True
    elif weekday:
        return False
    else:
        return True


print(sleep_in(True, False))
print(sleep_in(False, False))
print(sleep_in(False, True))
print(sleep_in(True, True))

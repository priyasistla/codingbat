# priya and madhurya's code
def sleep_in(weekday, vacation):
    if weekday is True and vacation is True:
        return True
    if weekday is True and vacation is False:
        return False
    if weekday is False and vacation is False:
        return True
    if weekday is False and vacation is True:
        return True


print(sleep_in(True, False))
print(sleep_in(False, True))
print(sleep_in(False, False))
print(sleep_in(True, True))
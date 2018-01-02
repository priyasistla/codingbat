def first_two(str):
    n=len(str)
    if n>2:
        first=str[0:2]
        return first
    return str
print(first_two("hello"))
print(first_two("X"))
print(first_two("ab"))

def make_tags(tag,word):
    got=tag
    add="<"+got+">"+word+"</"+got+">"
    return add
print(make_tags("i","yay"))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay')) 

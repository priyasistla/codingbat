def make_bricks(small,big,goal):
	if small*1+big*5>=goal:
		return True
	else:
		return False

print(make_bricks(3,1,8))
print(make_bricks(3,1,9))
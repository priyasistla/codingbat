# extra_end challenge
def extra_end(str):
	n=len(str)
	end=str[n-2:n]
	return end+end+end
print(extra_end("hello"))
print(extra_end("hab"))
print(extra_end("hi"))
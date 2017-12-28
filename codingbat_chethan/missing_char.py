def missing_char(s, n):
	return s.replace(s[n], "", 1)
	
def missing_char2(s, n):
	return s[:n] + s[n+1:]

print(missing_char2('kitten', 0))
print(missing_char2('kitten', 1))
print(missing_char2('kitten', 2))
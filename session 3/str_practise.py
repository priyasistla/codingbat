s_q = 'Testing "single" quoted str'
d_q = "Testing 'double' quoted str"
t_q = '''Testing 'triple' "quoted" str'''

print(s_q)
print(d_q)
print(t_q)


print(s_q[2:7])
print(s_q[:7])
print(s_q[2:])
print(s_q[:])
print(s_q[:-3])
print(s_q[-3])
print(s_q[4:2])

for ch in t_q:
	print(ch, end=' ')
	
print('-----')
print(t_q.upper())


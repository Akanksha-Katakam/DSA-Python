arr = [1,0,2,0,3,0]
s = []
z = []
for i in arr:
    if i != 0:
        s.append(i)
    else:
        z.append(i)

print(s + z)
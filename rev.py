s=input(str("enter a string:\n"))
words=s.split(" ")
l = len(words)
print(l)
d = []
for index in range(0,l):
    a = words[index]
    b = ''.join(reversed(a))
    # b=a[::-1]
    d.append(b)
print(d)
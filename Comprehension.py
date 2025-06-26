# List Comprehension
symbols = '$¢£¥€¤'
c = []
for i in symbols:
    c.append(ord(i))
print(c)

codes = [ord(symbol) for symbol in symbols]
print(codes)

num = []
for i in range (13):
    if i % 2 == 0:
        num.append(i)
print(num)
        
n = [i for i in range (13) if i % 2 == 0]
print(n)


# Dictionary Comprehension
d = {}
num = list(range(10))
for n in num:
    d[n] = n**2
print(d)


n_d = { n: n**2 for n in num }
print(n_d) 
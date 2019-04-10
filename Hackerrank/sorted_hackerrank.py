stdin = input()
a, b , c = filter(str.islower, stdin), filter(str.isupper, stdin), filter(str.isnumeric, stdin)

a = sorted(a)
b = sorted(b)

c = sorted(sorted(c), key = lambda x : int(x) % 2 == 0)

print(a, b, c)

print(''.join(a + b + c))
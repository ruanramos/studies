# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())
array = list(map(int, input().split()))

a = set(map(int, input().split()))
b = set(map(int, input().split()))
#print("{0}\n\n{1}".format(set(array).intersection(a), set(array).intersection(b)))

happiness = 0

for i in array:
	if i in a:
		happiness += 1
	if i in b:
		happiness -= 1

print(happiness)

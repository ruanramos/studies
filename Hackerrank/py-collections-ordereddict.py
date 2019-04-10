from collections import OrderedDict as od

odict = od()

for i in range(int(input())):
	name, qt = input().rsplit(None, 1)
	qt = int(qt)
	if name not in odict:
		odict[name] = qt
	else:
		odict[name] += qt

for i in odict.items():
	print(i[0], i[1])
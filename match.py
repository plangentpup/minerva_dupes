
from fuzzywuzzy import fuzz

with open('post_distinct.txt') as f:
	groups = f.read().splitlines()

matches = {}

l = len(groups)

for i in range(l):
	x = groups[i]
	j = i + 1
	while j < l:
		y = groups[j]
		ratio = fuzz.ratio(x, y)
		if ratio > 80:
			if not x in matches:
				matches[x] = []
			matches[x].append((y, ratio))
		j = j + 1

for x,y in matches.iteritems():
	print x
	for z in y:
		print "    {} | {}      ".format(repr(z[1]), repr(z[0]))
		print "        update clean set group1 = '{}' where group1 = '{}';".format(str(z[0]),str(x))
		print "        update clean set group2 = '{}' where group2 = '{}';".format(str(z[0]),str(x))

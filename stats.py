import numpy

# average number of weirds per cat
data = numpy.genfromtxt('data-clean.csv', delimiter=',', skip_header=1)

weirds = [len([item for item in row[5:] if item == 1]) for row in data ]
hist = {}
for n in range(20):
    hist[n] = 0
for count in weirds:
    hist[count] += 1
print hist

print "mean", numpy.mean(weirds)
print "standard deviation", numpy.std(weirds)

from collections import Counter
import pprint
import sys

def parse(inputfile):
    counter = Counter()

    with open(inputfile, 'r') as f:
        next(f) # Skip header

        for line in f:
            for word in line.strip().split(';'):
                counter[word] += 1

    return counter

def getPercentage(counter, key):
    return counter[key] / sum(counter.values())

def getPercentageMap(counter):
    return dict((k, getPercentage(counter, k)) for k in counter.keys())

counter = parse(sys.argv[1])
percentageMap = getPercentageMap(counter)

# Sort by value
sortedPercentages = sorted(percentageMap.items(),
                           key=lambda item: item[1],
                           reverse=True) 

pprint.pprint(counter)

for i in sortedPercentages:
    print("{0}: {1:.2%}".format(i[0], i[1]))

width, numPartitions = map(int, input().split())

#include 0 and total width along with intermediate partitions
locations = [0] + list(map(int, input().split())) + [width]

#form set of possible lengths to return
possibleLengths = set()

#add all possible differences between any two elements in the list
for i in range(len(locations)):
	for j in range(i+1, len(locations)):
		possibleLengths.add(locations[j]-locations[i])

print(*sorted(possibleLengths))
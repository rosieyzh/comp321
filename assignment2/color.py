numSocks, capacity, diff = map(int, input().split())
#number to return
numMachines = 0

#array of socks to iterate
socks = list(map(int,input().split()))
socks.sort()

#num and max color diff between socks in current machine
sockCounter=0
minSock=0

#iterate through socks
#greedy approach: contiguous segments (search linearly)
for i, sock in enumerate(socks):
	#initialization
	if numMachines == 0:
		minSock=sock
		sockCounter=1
		numMachines += 1
		continue
	
	if sock-minSock > diff or sockCounter >= capacity:
		#need to start new machine
		numMachines += 1
		minSock = sock
		sockCounter=1
	else:
		sockCounter +=1

print(numMachines)


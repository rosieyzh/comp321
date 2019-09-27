import heapq

while True:
	try:
		#first line of input is number of moves
		numMoves = int(input())

		#create structures and respective booleans keeping track of verification
		stack = []
		queue = []
		priority=[]
		isStack = True
		isQueue = True
		isPriority = True

		for i in range(numMoves):
			moveType, data = map(int, input().split())
			#first number is operation
			if moveType == 1:
				stack.append(data)
				queue.append(data)
				heapq.heappush(priority, -data)
			elif moveType == 2:
				#need to verify if any structures are empty - invalid move
				if len(stack)==0 or len(queue)==0 or len(priority)==0:
					isStack = False
					isQueue = False
					isPriority = False
				else:
					#verify removed element matches
					if isStack and stack.pop() != data:
						isStack = False
					if isQueue and queue[0] != data:
						isQueue = False
					else:
						#need to delete from the front - pop automatically removes
						del queue[0]
					if isPriority and heapq.heappop(priority) != -data:
						isPriority = False
						
		total = isStack + isQueue + isPriority
		if total >= 2:
			print('not sure')
		elif total == 0:
			print('impossible')
		elif isStack:
			print('stack')
		elif isQueue:
			print('queue')
		elif isPriority:
			print('priority queue')

	except EOFError:
		break
total, price = map(int, input().split())

students = list(map(int, input().split()))

#we have to pay 20 for each commercial break
students = [num-price for num in students]

#store intermediate maximal sums of list truncated to list[i] that includes list[i]
maxSub = []

#find the contiguous sequence of numbers that return the maximal sum
if len(students) == 0:
	#handle case where there are no commercials
	print(0)
else:
	maxSub.append(students[0])

	#max subsequence of length i is either sum of max subsequence from i-1 and students[i]
	#or new subsequence starting at i
	for i in range(1, len(students)):
		maxSub.append(max(students[i], students[i]+maxSub[i-1]))
	#find max subsequence
	print(max(maxSub))
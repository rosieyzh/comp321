numItems = int(input())
prices = list(map(int, input().split()))
numOrders = int(input())
orders = list(map(int, input().split()))

'''
Filling the dynamic programming table
'''
#-2 denotes impossible, -1 denotes ambiguous
dp = [-2]*31002

#start from order sum 0
dp[0]=0

#iterate through each item
for curItem, curPrice in enumerate(prices):

	for order in range(30000):
		if dp[order] >= 0:
			#order can be attained with menu items; change value of order+curPrice
			if dp[order+curPrice] == -2:
				#set value to item index
				dp[order+curPrice] = curItem
			else:
				#order+curPrice has already been attained, set to ambiguous
				dp[order+curPrice] = -1
		#if already ambiguous, will stay ambiguous
		if dp[order] == -1:
			dp[order+curPrice] = -1

def count(total):
	if dp[total] == -2:
		print("Impossible")
		return
	elif dp[total] == -1:
		print("Ambiguous")
		return

	#one solution - store results in array
	solution = []
	while total > 0:
		#store index of menu item 
		solution.append(dp[total]+1)
		total -= prices[dp[total]]

	#print solution
	print(*solution[::-1])


for total in orders:
	count(total)


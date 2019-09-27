moves = input()

#number cup position as 0, 1, 2 from left to right
#ball starts in leftmost cup
curPos=0
for move in moves:
	if move == 'A' and curPos !=2:
		# curPos is 0 or 1, switch value
		curPos = -curPos + 1
	elif move == 'B' and curPos !=0:
		# curPos is 1 or 2, switch value
		curPos = -curPos + 3
	elif move == 'C' and curPos != 1:
		# curPos is 0 or 2, switch value
		curPos = -curPos + 2
print(curPos+1)
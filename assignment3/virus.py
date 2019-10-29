str1 = input()
str2 = input()

#pinpoint differing substring by comparing the two lines

start = 0
end1 = len(str1)-1
end2 = len(str2)-1
minlength = min(len(str1), len(str2))

#find index at first different char
while start < minlength and str1[start] == str2[start]:
	start+=1

#find index of last different char
while min(end1, end2) >= start and str1[end1] == str2[end2]:
	end1-=1
	end2-=1
print(end2-start+1)


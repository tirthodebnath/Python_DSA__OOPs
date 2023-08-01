def identical_filter(lst):
	result = []
	for i in lst:
		if len(set(i)) == 1:
			result.append(i)
	return result

print(identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"]))
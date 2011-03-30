def find(strng, ch):
	index = 0
	while index < len(strng):
		if strng[index] == ch:
			return index
		index += 1
	return -1


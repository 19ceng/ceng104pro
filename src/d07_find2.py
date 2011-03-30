def find2(strng, ch, start=0, step=1):
	index = 0
	while index < len(strng):
		if strng[index] == ch:
			return index
		index += step
	return -1


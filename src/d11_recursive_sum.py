def recursive_sum(nested_num_list):
	sum = 0
	for elem in nested_num_list:
		if type(elem) == type([]):
			sum = sum + recursive_sum(elem)
		else:
			sum = sum + elem
	return sum

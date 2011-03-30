def double_stuff(a_list):
	for index, value in enumerate(a_list):
		a_list[index] = 2 * value

def double_stuff_v2(a_list):
	new_list = []
	for value in a_list:
		new_list += [2 * value]

	return new_list

def make_matrix_v1(rows, columns):
	"""
		>>> make_matrix(3, 5)
      	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      	>>> make_matrix(4, 2)
      	[[0, 0], [0, 0], [0, 0], [0, 0]]
	"""
	return [[0] * columns] * rows

def make_matrix_v2(rows, columns):
	"""
		>>> make_matrix(3, 5)
      	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      	>>> make_matrix(4, 2)
      	[[0, 0], [0, 0], [0, 0], [0, 0]]
		>>> m = make_matrix(4, 2)
      >>> m[1][1] = 7
      >>> m
      [[0, 0], [0, 7], [0, 0], [0, 0]]
	"""
	matrix = []
	for row in range(rows):
		matrix += [[0] * columns]
	return matrix

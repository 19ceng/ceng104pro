def insert_in_middle(val, tup):
	middle = len(tup) / 2
	return tup[:middle] + (val, ) + tup[middle:]

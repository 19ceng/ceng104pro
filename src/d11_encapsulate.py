def encapsulate(val, seq):
	if type(seq) == type(""):
		return str(val)
	if type(seq) == type([]):
		return [val]
	return (val, )

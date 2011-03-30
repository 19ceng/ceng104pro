def myabs(x):
	"""\
		myabs(x), mutlak deger alma islevidir.
		>>> myabs(-5)
		5
		>>> myabs(0)
		0
		>>> myabs(5)
		5
	"""
	if x < 0:
		return -x
	elif x > 0:
		return x

if __name__ == '__main__':
    import doctest
    doctest.testmod()

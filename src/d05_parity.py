def isodd(n):
	"""\
		isodd(n), tek mi?

		>>> isodd(3)
		True
		>>> isodd(4)
		False
	"""
	return n%2 == 1

if __name__ == '__main__':
    import doctest
    doctest.testmod()

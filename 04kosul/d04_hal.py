def hal(t):
	"""\
		t sicaklik degerine (santigrat) gore hali bilgisini ekrana yazar
		
		>>> hal(-5)
		SIVI
		>>> hal(5)
		KATI
		>>> hal(105)
		GAZ
	"""

	if t < 0:
		print "SIVI"
	elif t > 0 and t < 100:
		print "KATI"
	else:
		print "GAZ"

if __name__ == '__main__':
	import doctest
	doctest.testmod(verbose=True)

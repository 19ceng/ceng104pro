def fermat(a, b, c, n):
	"""\
		fermat's last theorem, a^n + b^n = c^n
		n>2 icin 
		- esitlik saglaniyorsa `True`,
		- saglanmiyorsa "Fermat hatalidir"
		n<=2 ise
		- "islev yurutulemez"

		>>> fermat(3,4,5,3)
		Fermat hatalidir
		
	"""

	if n > 2:
		sol = a**n + b**n
		sag = c**n
		if sol == sag:
			print True
		else:
			print "Fermat hatalidir"
	else:
		print "islev yurutulemez"

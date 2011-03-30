def remove_vowels(s):
	"""\
		Tum sesli harfleri dizgiden cikarir
		>>> str = "merhaba, dunya!"
		'mrhb, dny!'
	"""

	vowels = "aeiouAEIOU"
	s_without_vowels = ""
	for letter in s:
		if letter not in vowels:
			s_without_vowels += letter
	return s_without_vowels


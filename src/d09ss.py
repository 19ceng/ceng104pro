a_list = [0]*8
a_list[3] = 42
a_list[6] = 'Ni!'
"""
  >>> a_list[3]
  42
  >>> a_list[6]
  'Ni!'
  >>> len(a_list)
  8
"""

"""
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""

"""
  >>> 'war' in mystery_list
  False
  >>> 'peace' in mystery_list
  True
  >>> 'justice' in mystery_list
  True
  >>> 'oppression' in mystery_list
  False
  >>> 'equality' in mystery_list
  True
"""

"""
  >>> range(a, b, c)
  [5, 9, 13, 17]
"""

"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
"""

"""
  >>> nlist[2][1]
  0
  >>> nlist[0][2]
  17
  >>> nlist[1][1]
  5
"""

"""
  >>> import string
  >>> string.split(message, '??')
  ['this', 'and', 'that']
"""

if __name__ == '__main__':
	import doctest
	doctest.testmod()

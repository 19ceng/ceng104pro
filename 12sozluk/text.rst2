-------------------------------------------------------------------
tuple'lar ve değişebilirlik
-------------------------------------------------------------------

- bileşik yapılar: dizgi, liste

- karakter / herhangi bir şey 

- değiştirilebilirlik/değiştirilemezlik

- tuple: liste gibi herhangi bir şey barındırır

- dizgi gibi değiştirilemezdir

- virgüller ayrılmış değerler

.. code-block:: python

	>>> tup = 2, 4, 6, 8, 10

- gerekmese de gelenekselleşmiş gösterim,

.. code-block:: python
	
	>>> tup = (2, 4, 6, 8, 10)



-------------------------------------------------------------------
tuple
-------------------------------------------------------------------

- tek öğeli tuple için sona bir vürgül gerekir

.. code-block:: python

	>>> tup = (5, )
	>>> type(tup)
	<type 'tuple'>

- virgül unutulduğunda

.. code-block:: python

	>>> tup = (5)
	>>> type(tup)
	<type 'int'>



-------------------------------------------------------------------
liste gibi davranış
-------------------------------------------------------------------

- indisleme

.. code-block:: python

	>>> tup = ('a', 'b', 'c', 'd', 'e')
	>>> tup[0]
	'a'

- dilimleme

.. code-block:: python

	>>> tup[1:3]
	('b', 'c')



-------------------------------------------------------------------
dizgi gibi davranış
-------------------------------------------------------------------

- değiştirmeye çalışma

.. code-block:: python

	>>> tup[0] = 'X'
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment

- değiştirmeniz gerekiyorsa, dilimle al, ekle, aynı değişkene ata

.. code-block:: python

	>>> tup = ('X', ) + tup[1:]
	>>> tup
	('X', 'b', 'c', 'd', 'e')

- veya listeye çevir, işle, tuple'a geri dön

.. code-block:: python
	:size: Tiny

	>>> tup
	('X', 'b', 'c', 'd', 'e')
	>>> tup = list(tup)
	>>> tup
	>>> tup[0] = 'a'
	>>> tup = tuple(tup)
	>>> tup
	('a', 'b', 'c', 'd', 'e')



-------------------------------------------------------------------
tuple ataması
-------------------------------------------------------------------

- geleneksel yöntem

.. code-block:: python

	>>> a = 3; b = 5
	>>> gecici = a
	>>> a = b
	>>> b = gecici
	>>> a, b
	(5, 3)

- tuple atamalı yöntem

.. code-block:: python

	>>> a = 3; b = 5
	>>> a, b = b, a
	>>> a, b
	(5, 3)

- sol ve sağ taraftaki değer sayısı aynı olmalıdır

.. code-block:: python

	>>> a, b, c, d = 1, 2, 3
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	ValueError: need more than 3 values to unpack



-------------------------------------------------------------------
geri dönüş değeri olarak tuple
-------------------------------------------------------------------

- swap

.. code-block:: python

	def swap(x, y):
		return y, x

- böyle çağır: `a, b = swap(a, b)`

- değişken ömürleri

.. code-block:: python

	def swap(x, y):	# yanlis surum
		x, y = y, x

- neden, yanlış?



-------------------------------------------------------------------
saf (pure) fonksiyonlar
-------------------------------------------------------------------

- PB:6374

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d11_seqtools.py") %]



-------------------------------------------------------------------
test
-------------------------------------------------------------------

- test

.. code-block:: python

	>>> from d11_seqtools import *
	>>> insert_in_middle('c', my_list)
	>>> my_list
	['a', 'b', 'c', 'd', 'e']
	>>> from d11_seqtools import *
	>>> my_list = ['a', 'b', 'd', 'e']
	>>> insert_in_middle('c', my_list)
	>>> my_list
	['a', 'b', 'c', 'd', 'e']



-------------------------------------------------------------------
tuple
-------------------------------------------------------------------

- tuple'la çalışırken

.. code-block:: python

	>>> my_tuple = ('a', 'b', 'd', 'e')
	>>> insert_in_middle('c', my_tuple)
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	  File "./d11_seqtools.py", line 3, in insert_in_middle
	TypeError: 'tuple' object does not support item assignment

- onaralım

.. code-block:: python
	:linenos:

[% CODE("d11_seqtools_tup.py") %]

- tuple düzeldi, liste aksıyor



-------------------------------------------------------------------
hepsine uyacak bir işlev
-------------------------------------------------------------------

- hepsine uyacak bir işlev

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d11_seqtools_enc.py") %]



-------------------------------------------------------------------
test
-------------------------------------------------------------------

- test

.. code-block:: python

	>>> from d11_seqtools_enc import *
	>>> my_string = "abde"
	>>> my_list   = ['a', 'b', 'd', 'e']
	>>> my_tuple  = ('a', 'b', 'd', 'e')
	>>> insert_in_middle('c', my_string)
	'abcde'
	>>> insert_in_middle('c', my_list)
	['a', 'b', 'c', 'd', 'e']
	>>> insert_in_middle('c', my_tuple)
	('a', 'b', 'c', 'd', 'e')



-------------------------------------------------------------------
değiştirilebilirlik
-------------------------------------------------------------------

- dizgi/tuple'a değiştirilebilirlik kazandırma

.. code-block:: python

	>>> my_string = "abde"
	>>> my_string = insert_in_middle('c', my_string)
	>>> my_string
	'abcde'



-------------------------------------------------------------------
özyineli
-------------------------------------------------------------------

veri yapısı:
   verinin düzenleniş biçimi

- oy sayımı yapacağız

- oylar şehirlerden, şehir oyları ise ilçelerden vs

- oy listesi (sayı listesi) herhangi bir öğe içerebilir

   + sayılar

   + içiçe sayı listesi

- özyineli bir tarif verdik

- özyineli veri yapısı



-------------------------------------------------------------------
oy sayımı
-------------------------------------------------------------------

- python'un yerleşik `sum` işlevi (PB:6376)

.. code-block:: python

	>>> sum([1, 2, 8])
	11
	>>> sum((1, 2, 8))
	11

- fakat içiçe sayı listesinde çöker

.. code-block:: python

	>>> sum([1, 2, [11, 13], 8])
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	TypeError: unsupported operand type(s) for +: 'int' 
	 and 'list'
	>>>



-------------------------------------------------------------------
özyineleme
-------------------------------------------------------------------

- içiçe  sayı listesini idare etmek için

- toplama işlevinin her bir iç liste için çağrılması gerekir

- çağırıldığı yer (toplama işlevi), çağrılan işlev (toplama işlevi)

- özyineli çağrı



-------------------------------------------------------------------
özyineli gerçekleme
-------------------------------------------------------------------

- gerçekleme

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d11_recursive_sum.py") %]

=

- test

.. code-block:: python
	:linenos:

	>>> from d11_recursive_sum import *
	>>> recursive_sum([1, 2, [11, 13], 8])
	35



-------------------------------------------------------------------
özyineli çağrı
-------------------------------------------------------------------

- en büyüğü bulma

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d11_recursive_max.py") %]

- `largest = nested_num_list[0]` satırından sonraki `while`?



-------------------------------------------------------------------
sonsuz
-------------------------------------------------------------------

- sonduz yinelem

.. code-block:: python

	#
	# infinite_recursion.py
	#
	def recursion_depth(number):
		print "Recursion depth number %d." % number
		recursion_depth(number + 1)

	recursion_depth(0)

=

- sonuç

.. code-block:: python

	$ python infinite_recursion.py
	...
	  File "infinite_recursion.py", line 3, in recursion_depth
		recursion_depth(number + 1)
	RuntimeError: maximum recursion depth exceeded



-------------------------------------------------------------------
istisnalar
-------------------------------------------------------------------

- çalışma zamanı hatası -> **istisna** ortaya çıkar

- program durur ve hata dökümünü verir

- bu döküm ortaya çıkan istisnayla biter

.. code-block:: python

	>>> print 55 / 0
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	ZeroDivisionError: integer division or modulo by zero



-------------------------------------------------------------------
örnekler
-------------------------------------------------------------------

- var olmayan bir liste öğesine erişmeye çalışmak

.. code-block:: python

	>>> a = []
	>>> print a[55]
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	IndexError: list index out of range

- tupleda öğe ataması yapmaya çalışmak:

.. code-block:: python

	>>> tup = ('a', 'b', 'd', 'e')
	>>> tup[2] = 'c'
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment



-------------------------------------------------------------------
özet
-------------------------------------------------------------------

- hata türü: ZeroDivisionError, IndexError, TypeError

- hata ayrıntıları

- http://docs.python.org/library/exceptions.html#bltin-exceptions



-------------------------------------------------------------------
istisna idaresi
-------------------------------------------------------------------

- istisna ortaya çıktığında program sonlanmasın

- istisna idaresi: `try` ... `except`

.. code-block:: python

	filename = raw_input('Enter a file name: ')
	try:
		f = open (filename, "r")
	except:
		print 'There is no file named', filename

- böylesi bir durumda programın çökmesinin hiç gereği yoktur



-------------------------------------------------------------------
exists
-------------------------------------------------------------------

- böyle de kullanabilirsiniz

.. code-block:: python

	def exists(filename):
		try:
			f = open(filename)
			f.close()
			return True 
		except:
			return False



-------------------------------------------------------------------
profesyonelce
-------------------------------------------------------------------

- pratik örnek

.. code-block:: python

	import sys

	try:
		f = open('myfile.txt')
		s = f.readline()
		i = int(s.strip())
	except IOError as (errno, strerror):
		print "I/O error({0}): {1}".format(errno, strerror)
	except ValueError:
		print "Could not convert data to an integer."
	except:
		print "Unexpected error:", sys.exc_info()[0]
		raise



-------------------------------------------------------------------
istisna tetikleme
-------------------------------------------------------------------

- siz de bir istisna üretebilirsiniz

.. code-block:: python

	#
	# learn_exceptions.py
	#
	def get_age():
		age = input('Please enter your age: ')
		if age < 0:
			raise ValueError, '%s is not a valid age' % age
		return age



-------------------------------------------------------------------
test
-------------------------------------------------------------------

- test

.. code-block:: python

	>>> get_age()
	Please enter your age: 42
	42 
	>>> get_age()
	Please enter your age: -2
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "learn_exceptions.py", line 4, in get_age
		raise ValueError, '%s is not a valid age' % age
	ValueError: -2 is not a valid age
	>>>

- bir yerlerde bunu idare edebilirsiniz, nasıl?



-------------------------------------------------------------------
istisna: sonsuz döngü
-------------------------------------------------------------------

- önceki özyineli sonsuz döngüyü hatırlayın

.. code-block:: python

	#
	# infinite_recursion.py
	#
	def recursion_depth(number):
		print "Recursion depth number %d." % number
		try:
			recursion_depth(number + 1)
		except:
			print "Maximum recursion depth exceeded."

	recursion_depth(0)

- artık program çökmeyecek!



-------------------------------------------------------------------
kuyruk çağrı: faktoriyel
-------------------------------------------------------------------

iki tanım

1. n! = n*(n-1)*...*2*1

2. n! = n * (n - 1)!

- ikincisini nasıl kodlarız?

.. code-block:: python

	def faktoriyel(n):
		if n == 0:
			return 1
		else:
			return n * faktoryel(n-1)



-------------------------------------------------------------------
kuyruk çağrı: fibonacci
-------------------------------------------------------------------

- fib(0) = fib(1) = 1

- fib(n) = fib(n-1) + fib(n-2)

.. code-block:: python

	def fibonacci (n):
		if n == 0 or n == 1:
			return 1
		else:
			return fibonacci(n-1) + fibonacci(n-2)



-------------------------------------------------------------------
liste kavraması
-------------------------------------------------------------------

- Liste kavraması kısa, matematiksel bir sözdizimi kullanarak 

- diğer listelerden yeni listeler yaratmaya yarayan 

- sözdizimsel bir yapıdır

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> sayilar = [1, 2, 3, 4]
	>>> [x**2 for x in sayilar]
	[1, 4, 9, 16]
	>>> [x**2 for x in sayilar if x**2 > 8]
	[9, 16] 
	>>> [(x, x**2, x**3) for x in sayilar]
	[(1, 1, 1), (2, 4, 8), (3, 9, 27), (4, 16, 64)]
	>>> dosyalar = ['bin', 'Data', 'Desktop', '.bashrc', '.ssh', '.vimrc']
	>>> [isim for isim in dosyalar if isim[0] != '.']
	['bin', 'Data', 'Desktop']
	>>> harfler = ['a', 'b', 'c']
	>>> [n*harf for n in sayilar for harf in harfler]
	['a', 'b', 'c', 'aa', 'bb', 'cc', 'aaa', 'bbb', 'ccc', 'aaaa', 'bbbb', 'cccc']
	>>>



-------------------------------------------------------------------
genelleştirilmiş
-------------------------------------------------------------------

- genelleştirilmiş hali

.. code-block:: python

	[expr for item1 in seq1 for item2 in seq2 ... 
	 for itemx in seqx if condition]

- açık hali

.. code-block:: python

	output_sequence = []
	for item1 in seq1:
		for item2 in seq2:
			...
				for itemx in seqx:
					if condition:
						output_sequence.append(expr)



-------------------------------------------------------------------
örnek
-------------------------------------------------------------------

- tree : d11_tree.py



-------------------------------------------------------------------
alıştırmalar
-------------------------------------------------------------------

1. 

.. code-block:: python
	:linenos:
	:size: Tiny

	def swap(x, y):      # yanlis surum
		 print  "before swap statement: id(x):", id(x), "id(y):", id(y)
		 x, y = y, x
		 print  "after swap statement: id(x):", id(x), "id(y):", id(y)

	a, b = 0, 1
	print  "before swap function call: id(a):", id(a), "id(b):", id(b)
	swap(a, b)
	print  "after swap function call: id(a):", id(a), "id(b):", id(b)


2. d11_seqtools.py

3. d11_recursive



-------------------------------------------------------------------
alıştırmalar
-------------------------------------------------------------------

4. 

.. code-block:: python

	>>> num = readposint()
	Please enter a positive integer: yes
	yes is not a positive integer.  Try again.
	Please enter a positive integer: 3.14
	3.14 is not a positive integer.  Try again.
	Please enter a positive integer: -6
	-6 is not a positive integer.  Try again.
	Please enter a positive integer: 42
	>>> num
	42
	>>> num2 = readposint("Now enter another one: ")
	Now enter another one: 31
	>>> num2
	31
	>>>

5. çıktı? (8)



-------------------------------------------------------------------
alıştırmalar
-------------------------------------------------------------------

6. faktoriyel işlevinin yineli versiyonunu yazın. süre karşılaştırın

7. litter.py, o anki ve alt dizinlerde trash.txt oluştursun. cleanup.py ise trash.txt leri temizlesin



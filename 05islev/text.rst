-------------------------------------------------------------------
Geri dönüş değerleri
-------------------------------------------------------------------

- `abs`, `pow`, `max` sonuç üretiyorlardı

.. code-block:: python
	:linenos:

    >>> mx = max(3, 7, 2, 5)
    >>> x = abs(3 - 11) + 10
    >>> mx, x
    (7, 18)

- her işlev çağrısı bir değer üretmedir

- üretilen değer ya bir değişkene atanır ya da deyimin bir parçasıdır

- şimdiye kadar tasarladığımız işlevler değer üretip, döndürmedi



-------------------------------------------------------------------
ürün veren işlevler
-------------------------------------------------------------------

- işlev değer hesaplayıp, döndürüyorsa ürünlüdür

- böyle yazardık

.. code-block:: python
	:linenos:
	:size: Tiny

	def area(radius):
		tmp = 3.14159 * radius ** 2
		print "alan =", tmp
	
	# main	
	area(5)
	area(11)

|
▬

- şimdi değeri geri döndürelim

.. code-block:: python
	:linenos:
	:size: Tiny

	def area(radius):
		tmp = 3.14159 * radius ** 2
		return tmp
	
	# main	
	print "Kucuk dairenin alani =", area(5)
	print "Buyuk dairenin alani =", area(11)



-------------------------------------------------------------------
`return` 
-------------------------------------------------------------------

- `return <deger>(ler)`: değer(ler) döndürür

- çağrıldığın yere geri dön, devamındaki ifadeyi geri dönüş değeri olarak kullan

- döndürülecek değer değişkende veya doğrudan deyim olabilir

.. code-block:: python
	:linenos:

	def area(radius):
		return 3.14159 * radius ** 2

- `tmp` benzeri geçici değişkenler hata ayıklamada kullanışlıdır



-------------------------------------------------------------------
birden fazla `return` cümlesi
-------------------------------------------------------------------

- birden fazla `return` cümlesi

.. code-block:: python
	:linenos:

	def myabs(x):
		if x < 0:
			return -x
		else:
			return x

|
▬

- nasıl olsa `return`'e rastlanılan yerden hemen çıkıyor

- `else`'yi kaldırabiliriz

.. code-block:: python
	:linenos:

	def myabs(x):
	    if x < 0:
			return -x
	    return x


-------------------------------------------------------------------
her durum idare edilmeli yoksa ...
-------------------------------------------------------------------

- işlevler her durumu idare etmelidir

.. code-block:: python
	:linenos:

	def myabs(x):
	    if x < 0:
			return -x
		elif x > 0:
	    	return x

- burada hata nerededir?▬

- `x=0` ise ne olacak?



-------------------------------------------------------------------
`doctest`'ten kaçmaz
-------------------------------------------------------------------

- `doctest`'ler bunun için var

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d05_myabs.py") %]



-------------------------------------------------------------------
`doctest` sonuçları
-------------------------------------------------------------------

- sonuçlar

.. code-block:: python
	:linenos:
	:size: Tiny

	$ python -i d05_myabs.py
	**********************************************************************
	File "d05_myabs.py", line 5, in __main__.myabs
	Failed example:
	    myabs(0)
	Expected:
	    0
	Got nothing
	**********************************************************************
	1 items had failures:
	   1 of   3 in __main__.myabs
	***Test Failed*** 1 failures.

- `Got nothing` veya `None`

- işlev hakkında birşey söylemiyorsa, döndürmüyorsa `None`'dır



-------------------------------------------------------------------
program geliştirme
-------------------------------------------------------------------

- programlar büyüdükçe çalışma zamanı ve anlambilimsel hatalar artmaya başlar

- karmaşık programlarla başa çıkmak için

- arttırımsal geliştirme



-------------------------------------------------------------------
arttırımsal geliştirme
-------------------------------------------------------------------

hata ayıklama süreçlerini kısaltmak

1. bir anda küçük bir kod ekle

2. ekleneni sına

3. tekrar 1. adım



-------------------------------------------------------------------
Ör. distance hesaplayıcı
-------------------------------------------------------------------

- iki nokta arasındaki mesafenin hesaplanması

- pisagor teoremi: `distance=\sqrt((x2-x1)^2+(y2-y1)^2)`

1. bunu Python'da nasıl ifade ederim?

2. girdiler (parametreler) ve çıktı (dönüş değeri) nedir?

|
▬

- girdiler: noktalar

- çıktı: hesaplanan uzaklık değeri (kayan noktalı olarak)



-------------------------------------------------------------------
tasarım
-------------------------------------------------------------------

- tasarım: işlevin anahatları

.. code-block:: python
	:linenos:

	def distance(x1, y1, x2, y2):
		return 0.0

- hesap yok, doğru değer döndürmüyor

- sözdizimsel olarak doğru, çalışabilir kod

|

- önce bunu bir sına

.. code-block:: python
	:linenos:

	>>> distance(1, 2, 4, 6)
	0.0



-------------------------------------------------------------------
girdi set seçimi
-------------------------------------------------------------------

- neden `(1, 2, 4, 6)` seçtik

- biliyoruz ki `4-1=3`, `6-2=4`, `3-4-5` pisagorundan uzaklık `5.0` olacak

|

- girdi: `(1, 2, 4, 6)`

- çıktı: `5.0`



-------------------------------------------------------------------
hata ayıkla
-------------------------------------------------------------------

- her bir yöndeki mesafeleri hesaplamakla devam et

.. code-block:: python
	:linenos:
	:size: Tiny

	def distance(x1, y1, x2, y2):
		dx = x2 - x1
		dy = y2 - y1
		print "dx = %s, dy = %s" % (dx, dy)
		return 0.0

|
▬

- neden `print` satırı var

- hata ayıklama

- böyle yaparsak idaresi daha kolay

.. code-block:: python
	:linenos:
	:size: Tiny

	def distance(x1, y1, x2, y2):
		dbg = True	#debug on/off
		dx = x2 - x1
		dy = y2 - y1
		if dbg: print "dx = %s, dy = %s" % (dx, dy)
		return 0.0



-------------------------------------------------------------------
geliştirme
-------------------------------------------------------------------

- kareyi hesapla

.. code-block:: python
	:linenos:

	def distance(x1, y1, x2, y2):
		dx = x2 - x1
		dy = y2 - y1
		dsqr = dx**2 + dy**2
		if dbg: print "dsqr = %s" % (dsqr)
		return 0.0

- önceki `print` cümlesini kaldırdık

- inşaat kurarken iskele kullan,

- söz konusu aşamayı geçince iskeleyi kaldır



-------------------------------------------------------------------
geliştirme
-------------------------------------------------------------------

- karekök eklentisi, ve geridönüş

.. code-block:: python
	:linenos:

	def distance(x1, y1, x2, y2):
		dx = x2 - x1
		dy = y2 - y1
		dsqr = dx**2 + dy**2
		result = dsqr**0.5
		return result

- bunu test etme sırasıdır ...



-------------------------------------------------------------------
anahatlar
-------------------------------------------------------------------

1. Çalışan bir programla başla

    - küçük artımlı değişikler yap
    - herhangi bir noktada bir hata varsa hatanın nerede olduğunu bulmak kolay

2. Ara değerleri tutmak için geçici değişkenler kullan

    - böylece bu değerleri ekran gösterip kontrol edebilirsin

3. Program çalışır hale gelince, iskelet kodlarının bazılarını kaldır

    - birden fazla cümleyi bileşik deyimler haline getir
    - birleştirme x okunurluk? 



-------------------------------------------------------------------
kompozisyon
-------------------------------------------------------------------

- bir işlevi başka işlevden çağırabiliriz

- dairenin alanını hesaplama

- girdi: dairenin merkezi, daire üzerindeki bir nokta

- çıktı: dairenin alanı

- önce yarıçapı hesapla

- sonra alanı hesapla



-------------------------------------------------------------------
yarıçap hesaplama
-------------------------------------------------------------------

- dairenin merkezi: `(xc, yc)`

- daire üzerinde yer alan bir nokta: `(xp, yp)`

- yarıçap

.. code-block:: python
	:linenos:

	radius = distance(xc, yc, xp, yp)



-------------------------------------------------------------------
alan hesaplama
-------------------------------------------------------------------

- dairenin yarıçapından alan hesaplayabiliriz (daha önce verilmişti)

.. code-block:: python
	:linenos:

	result = area(radius)



-------------------------------------------------------------------
parçaları bir araya getir
-------------------------------------------------------------------

- önce yarıçap hesabı sonra alan

.. code-block:: python
	:linenos:
	:size: Tiny

	def area2(xc, yc, xp, yp):
		radius = distance(xc, yc, xp, yp)
		result = area(radius)
		return result

=
▬

- geçici `radius` ve `result` değişkenleri hata ayıklama içindi

- kısaltabiliriz

.. code-block:: python
	:linenos:
	:size: Tiny

	def area2(xc, yc, xp, yp):
		return area(distance(xc, yc, xp, yp))



-------------------------------------------------------------------
dikdörtgen çizme
-------------------------------------------------------------------

- çizgi çizdirmeyi kullanarak dikdörtgen çizdirmek, nasıl?

- dikdöretgenin sol-üst ve sağ-alt köşeleri elimizde

- köşeler: `(x1, y1)` ve `(x2, y2)`

.. code-block:: python
	:linenos:

	def dikdortgen(x1, y1, x2, y2):
		Line((x1, y1), (x2, y1))
		Line((x2, y1), (x2, y2))
		Line((x2, y2), (x1, y2))
		Line((x1, y2), (x1, y1))

- şöyle de test edebiliriz

.. code-block:: python
	:linenos:

	dikdortgen(50, 50, 150, 200)



-------------------------------------------------------------------
dikdörtgen çizme-v2
-------------------------------------------------------------------

- köşe noktasından ziyade genişlik ve yüksekliğe göre olsa

- değişkenler: `w`, `h`

.. code-block:: python
	:linenos:

	def dikdortgen2(x, y, w, h):
		x1, y1 = x, y
		x2, y2 = x + w, y + h

		Line((x1, y1), (x2, y1))
		Line((x2, y1), (x2, y2))
		Line((x2, y2), (x1, y2))
		Line((x1, y2), (x1, y1))

=
▬

- neden tekrar edelim ki

- son dört satıra zaten bir isim vermiştik: `dikdörtgen`

.. code-block:: python
	:linenos:

	def dikdortgen2(x, y, w, h):
		x2, y2 = x + w, y + h
		dikdortgen(x, y, x2, y2)

- ara değişkenler kaldırmakta mümkün



-------------------------------------------------------------------
dikdörtgen çizme-v3
-------------------------------------------------------------------

- kare çizdirmek istersek

- kenar: `a`

.. code-block:: python
	:linenos:

	def kare(x, y, a):
		dikdortgen2(x, y, a, a)



-------------------------------------------------------------------
öntanımlı değerler
-------------------------------------------------------------------

- işlevlerde değişkenlere parametre aktarımında

.. code-block:: python
	:linenos:
	:size: Tiny

	def Circle(center, radius, filled=False, \
			   color=(0,0,0), thickness=1):




-------------------------------------------------------------------
boolean işlevler
-------------------------------------------------------------------

- işlev boolean değer üretebilir

.. code-block:: python
	:linenos:
	:size: Tiny

	def is_divisible(x, y):
		if x%y == 0:
			return True
		else:
			return False

- işlevin ismi "bölünebilir mi?"  `is_divisible`

- el-cevap: "Evet/Hayır"  `True/False`

|
▬

- boolean deyimi `return` cümlesine alabiliriz

.. code-block:: python
	:linenos:
	:size: Tiny

	def is_divisible(x, y):
		return x%y == 0



-------------------------------------------------------------------
test
-------------------------------------------------------------------

- işlevin testi kolay

.. code-block:: python
	:linenos:

	>>> is_divisible(6, 4)
	False
	>>> is_divisible(6, 3)
	True

- bu yapıyı aynen `doctest` te kullanırız
 
|

- boolean işlevler genelde koşul cümlelerinde kullanılır

.. code-block:: python
	:linenos:

	if is_divisible(x, y):
		print "x, y tam bolunebilir"
	else:
		print "x, y tam bolunemez"



-------------------------------------------------------------------
`function` türü
-------------------------------------------------------------------

- işlevler `type` ile çağrıldığında ne döndürür

.. code-block:: python
	:linenos:

	>>> type(distance)
	<type 'function'>



-------------------------------------------------------------------
işlevleri argüman olarak geçmek mümkündür
-------------------------------------------------------------------

- işlevleri argüman olarak geçmek mümkündür

.. code-block:: python
	:linenos:
	:size: Tiny

	def f(n):
		return 3*n - 6

	def g(n):
		return 5*n + 2

	def h(n):
		return -2*n + 17

	def doto(value, func):
		return func(value)
		
	print doto(7, f)
	print doto(7, g)
	print doto(7, h)

- sonuç



-------------------------------------------------------------------
fonksiyon pointerları
-------------------------------------------------------------------

- fonksiyon pointerları

.. code-block:: python
	:linenos:
	:size: Tiny

[% CODE("d05_fonksiyon_pointer.py") %]



-------------------------------------------------------------------
program yazım kuralları
-------------------------------------------------------------------

- PEP



-------------------------------------------------------------------
docstring - doctest
-------------------------------------------------------------------

1. kodun otomatik birim sınaması

2. hakkında yardım sağlama



-------------------------------------------------------------------
gerçekleme
-------------------------------------------------------------------

- tek/çift?

.. code-block:: python
	:linenos:

[% CODE("d05_parity.py") %]



-------------------------------------------------------------------
örnek: birim sınama
-------------------------------------------------------------------

- test

.. code-block:: python
	:linenos:
	:size: Tiny

	$ python d05_parity.py -v
	Trying:
		isodd(3)
	Expecting:
		True
	ok
	Trying:
		isodd(4)
	Expecting:
		False
	ok
	1 items had no tests:
		__main__
	1 items passed all tests:
	   2 tests in __main__.isodd
	2 tests in 2 items.
	2 passed and 0 failed.
	Test passed.

- `-v` seçeneğine dikkat



-------------------------------------------------------------------
Örnek: hakkında yardım
-------------------------------------------------------------------

- test

.. code-block:: python
	:linenos:
	:size: Tiny

	$ python
	Python 2.6.4 (r264:75706, Dec  7 2009, 18:45:15)
	[GCC 4.4.1] on linux2
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from d05_parity import *
	>>> help(isodd)
	Help on function isodd in module d05_parity:

	isodd(n)
		isodd(n), tek mi?

		>>> isodd(3)
		True
		>>> isodd(4)
		False

- `in module d05_parity` cümlesine dikkat



-------------------------------------------------------------------
default argument values
-------------------------------------------------------------------

- öntanımlı değerler

.. code-block:: python
	:linenos:

	def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
		while True:
			ok = raw_input(prompt)
			if ok in ('y', 'ye', 'yes'):
				return True
			if ok in ('n', 'no', 'nop', 'nope'):
				return False
			retries = retries - 1
			if retries < 0:
				raise IOError('refusenik user')
			print complaint

=
▬

- kullanırken/çağırırken

.. code-block:: python
	:linenos:

	ask_ok('Do you really want to quit?')
	ask_ok('OK to overwrite the file?', 2)
	ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')



-------------------------------------------------------------------
öntanımlı değerler: bir kereliğine
-------------------------------------------------------------------

- öntanımlı değerler bir kereliğine atanır

.. code-block:: python
	:linenos:

	def f(a, L=[]):
		L.append(a)
		return L

	print f(1)
	print f(2)
	print f(3)

- ekran çıktısı

.. code-block:: python
	:linenos:

	[1]
	[1, 2]
	[1, 2, 3]



-------------------------------------------------------------------
keyword argümanlar
-------------------------------------------------------------------

- argümanları `keyword = value` olarakta aktarabilirsiniz

.. code-block:: python
	:linenos:
	:size: Tiny

	def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
		print "-- This parrot wouldn't", action,
		print "if you put", voltage, "volts through it."
		print "-- Lovely plumage, the", type
		print "-- It's", state, "!"



-------------------------------------------------------------------
keyword argümanlar
-------------------------------------------------------------------

- gerçerli: çağrılar

.. code-block:: python
	:linenos:
	:size: Tiny

	parrot(1000)
	parrot(action = 'VOOOOOM', voltage = 1000000)
	parrot('a thousand', state = 'pushing up the daisies')
	parrot('a million', 'bereft of life', 'jump')

=

- gerçersiz: çağrılar

.. code-block:: python
	:linenos:

	parrot()                     # required argument missing
	parrot(voltage=5.0, 'dead')  # non-keyword argument following keyword
	parrot(110, voltage=220)     # duplicate value for argument
	parrot(actor='John Cleese')  # unknown keyword



-------------------------------------------------------------------
belirsiz sayıda argüman
-------------------------------------------------------------------

- argüman sayısını tam bilmiyorsak: bakınız `print` cümleleri

.. code-block:: python
	:linenos:

	def cheeseshop(kind, * arguments, ** keywords):
		print "-- Do you have any", kind, "?"
		print "-- I'm sorry, we're all out of", kind
		for arg in arguments: print arg
		print "-" * 40
		keys = keywords.keys()
		keys.sort()
		for kw in keys: print kw, ":", keywords[kw]



-------------------------------------------------------------------
belirsiz sayıda argüman
-------------------------------------------------------------------

- çağırırken

.. code-block:: python
	:linenos:

	cheeseshop("Limburger", "It's very runny, sir.",
			   "It's really very, VERY runny, sir.",
			   shopkeeper='Michael Palin',
			   client="John Cleese",
			   sketch="Cheese Shop Sketch")

=

- ekran çıktısı

.. code-block:: python
	:linenos:

	-- Do you have any Limburger ?
	-- I'm sorry, we're all out of Limburger
	It's very runny, sir.
	It's really very, VERY runny, sir.
	----------------------------------------
	client : John Cleese
	shopkeeper : Michael Palin
	sketch : Cheese Shop Sketch



-------------------------------------------------------------------
lambda
-------------------------------------------------------------------

- fonksiyonel programlama

- LISP

- işlerin kestirme yolları vardır

.. code-block:: python
	:linenos:

	>>> def f (x): return x**2
	... 
	>>> print f(8)
	64
	>>> 
	>>> g = lambda x: x**2
	>>> 
	>>> print g(8)
	64



-------------------------------------------------------------------
lambda
-------------------------------------------------------------------

- bazı standart işlevleri işleri kolaylaştırır

.. code-block:: python
	:linenos:

	>>> foo = [2, 18, 9, 22, 17, 24, 8, 12, 27]
	>>> 
	>>> print filter(lambda x: x % 3 == 0, foo)
	[18, 9, 24, 12, 27]
	>>> 
	>>> print map(lambda x: x * 2 + 10, foo)
	[14, 46, 28, 54, 44, 58, 26, 34, 64]
	>>> 
	>>> print reduce(lambda x, y: x + y, foo)
	139



-------------------------------------------------------------------
dizgiler + lambda
-------------------------------------------------------------------

- lambda güçlüdür

.. code-block:: python
	:linenos:

	>>> sentence = 'It is raining cats and dogs'
	>>> words = sentence.split()
	>>> print words
	['It', 'is', 'raining', 'cats', 'and', 'dogs']
	>>> 
	>>> lengths = map(lambda word: len(word), words)
	>>> print lengths
	[2, 2, 7, 4, 3, 4]



-------------------------------------------------------------------
sistem programcısı
-------------------------------------------------------------------

- sistem programcısı böyle kullanır

.. code-block:: python
	:linenos:

	>>> import commands
	>>> 
	>>> mount = commands.getoutput('mount -v')
	>>> lines = mount.split('\n')
	>>> points = map(lambda line: line.split()[2], lines)
	>>> 
	>>> print points
	['/', '/var', '/usr', '/usr/local', '/tmp', '/proc']



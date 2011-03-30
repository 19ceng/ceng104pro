---------------------------------------------------
Modül (kalan) işleci
---------------------------------------------------

- bölümden kalan

- yüzde (`%`) sembolü

.. code-block:: python
	:linenos:

	>>> bolum = 7 / 3
	>>> print bolum
	2
	>>> kalan = 7 % 3
	>>> print kalan
	1



---------------------------------------------------
Modül (kalan) işleci
---------------------------------------------------

- iki sayının birbirine tam bölünüp bölünemediğini bu şekilde sınayabiliriz

.. code-block:: python
	:linenos:

	def is_divisible(x, y):
	    return x % y == 0



---------------------------------------------------
Modül (kalan) işleci
---------------------------------------------------

- sayının en sağ basamağındaki rakam veya rakamları elde edebiliriz

.. code-block:: python
	:linenos:

	>>> x = 123
	>>> x % 10
	3
	>>> x % 100
	23
	>>> _ % 10
	3



---------------------------------------------------
boolean değerler ve deyimler
---------------------------------------------------

- `bool`: yanlış/doğru

- Boolean Cebrinin yaratıcısı George Boolen'dan

- Bool cebri, modern bilgisayar aritmetiğinin temelidir

- boolean değerler: `True`, `False`

- BÜYÜK/küçük harf ayrımına dikkat

.. code-block:: python
	:linenos:

	>>> type(True)
	<type 'bool'>
	>>> type(true)
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'true' is not defined



---------------------------------------------------
boolean deyimi
---------------------------------------------------

- sonucu boolean değer olan deyimler

.. code-block:: python
	:linenos:

	>>> x, y = 5, 6
	>>> x == y	# esit mi?
	False
	>>> x == x
	True
	>>> x != y      # esit degil mi?
	True
	>>> x > y
	False
	>>> x < y
	True
	>>> x <= y
	True
	>>> x >= y
	False



---------------------------------------------------
atama x karşılaştırma
---------------------------------------------------

- tek eşittir "atama"

- çift eşittir "karşılaştırma"



---------------------------------------------------
mantıksal işleçler
---------------------------------------------------

- üç adettir: `and`, `or`, `not`

- sırayla VE, VEYA, DEĞİL

- Doğruluk tablosu, Logic Gates, De Morgan, Venn diagramları

.. code-block:: python
	:linenos:

	>>> x, y = 5, 6
	>>> x > 0
	True
	>>> x < 10
	True
	>>> x > 0 and x < 10
	True
	>>>
	>>> x % 2 == 0 or x % 3 == 0
	False
	>>> x > y
	False
	>>> not(x > y)
	True



---------------------------------------------------
koşullu yürütme
---------------------------------------------------

- koşul cümleleri: ortalama notu 60'dan küçükse kaldı. Ama nasıl?

.. code-block:: python
	:linenos:

	if ort < 60:
		print "KALDI"

- koşul cümleleri `if` ile kurulur

- satırın sonundaki (işlevdekine benzer) iki noktaya dikkat!

- `if`'den sonra gelen boolean deyime **koşul** denilir: `ort < 60`

- bu satırdan sonraki, girintili yazılanlar **gövde**

- koşul doğruysa gövdedeki emirler yerine getirilir

- koşul yanlışsa bir şey yapılmaz



---------------------------------------------------
`if` koşul yapısı
---------------------------------------------------

- genel olarak 

.. code-block:: python
	:linenos:

	if KOSUL:
		CUMLELER

- `if` anahtar kelimesiyle başla

- `KOSUL` ile devam et

- bu ikisi başlık satırıdır

- başlık satırını iki nokta - `:` ile bitir

- takip eden girintili cümlelere **blok** adı verilir

- ilk girintisiz cümle blok sonunu gösterir

- bileşik cümlelerdeki cümle bloğuna cümlenin **gövdesi** denilir

- gövdedeki cümleler koşul doğruysa yerine getirilir

- `if` bileşik cümlesi en azından bir cümle içermelidir: `pass` kullanılabilir (boş cümle)



---------------------------------------------------
girintileme
---------------------------------------------------

- C dilinde

.. code-block:: c
	:linenos:

	#include <stdio.h>

	int main()
	{
	    int ort = 65;
	    if (a < 60)
	    {
		printf("Maalesef kaldiniz!\n");
		return 0;
	    }
	}


=
▬

- karmaşıkta olsa geçerli

.. code-block:: c
	:linenos:

	#include <stdio.h>
	int main(){int a = 1;if (a == 1){printf("Merhaba Zalim Dünya!\n");return 0;}}



---------------------------------------------------
girintileme
---------------------------------------------------

- Python'da yapmaya çalışırsak

.. code-block:: python
	:linenos:

	ort = 65
	if ort < 60:
		print "Maalesef kaldiniz!"

|
▬

- böyle yazamazsınız, hata alırsınız

.. code-block:: python
	:linenos:

	ort = 65
	if ort < 60:
	print "Maalesef kaldiniz!"

=

- evet python girintileme temelli bloklama-gövde yapısı kullanır



---------------------------------------------------
alternatif yürütme
---------------------------------------------------

- koşul yanlışsa ne yapalım

.. code-block:: python
	:linenos:

	if ortalama < 60:
		print "KALDI"
	else:
		print "GECTI"

|
▬

- tek mi çift mi?

.. code-block:: python
	:linenos:

	if x%2 == 0:
		print x, "cifttir"
	else:
		print x, "tektir"

=

- bu alternatiflere **dal** denilir

- yürütme akışı farklı dallarla yoluna devam etmektedir



---------------------------------------------------
işlev
---------------------------------------------------

- tek çift kontrolünü parity testinde kullanalım

.. code-block:: python
	:linenos:
	:size: Tiny

	def print_parity(x):
		if x%2 == 0:
			print x, "cifttir"
		else:
			print x, "tektir"

|

- test edelim

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print_parity(17)
	17 tektir
	>>> y = 41
	>>> print_parity(y+1)
	42 cifttir



---------------------------------------------------
parola kontrol
---------------------------------------------------

- girilen parolayı sına

.. code-block:: python
	:linenos:

	parola = "python"
	girdi  = raw_input("Lutfen parolanizi giriniz: ")

	if girdi == parola:
		print "Parola onaylandi!"



---------------------------------------------------
zincirleme koşul ifadeleri
---------------------------------------------------

- bazen ikiden fazla durum olabilir: koşul doğru x değil

- iki daldan fazlasına ihtiyaç duyarsak

- zincirleme koşul ifadelerine başvururuz

.. code-block:: python
	:linenos:

	if x < y:
		print "%s < %s" % (x, y)
	elif x > y:
		print "%s > %s" % (x, y)
	else:
		print "%s = %s" % (x, y)

|

- sıcaklık - hal bilgisi

.. code-block:: python
	:linenos:
	:size: Tiny

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



---------------------------------------------------
gerçeksi bir uygulama
---------------------------------------------------

- demo: d04_4islem.py dosyasını iyileştirelim



---------------------------------------------------
içiçe koşul deyimleri
---------------------------------------------------

- koşul deyimleri içiçe olabilir

.. code-block:: python
	:linenos:

	if x > 0:
		print "Kuzey-",

		if y > 0:
			print "Dogu"
		else:
			print "Bati"
	else:
		print "Guney-",

		if y > 0:
			print "Dogu"
		else:
			print "Bati"



---------------------------------------------------
içiçe koşul deyimleri
---------------------------------------------------

- aşağıdaki kodu tek bir cümleyle yazabiliriz

.. code-block:: python
	:linenos:

	if 0 < x:
	    if x < 10:
		print "x pozitif ve tek basamaklıdır."

=

- nasıl?▬

.. code-block:: python
	:linenos:

	if 0 < x and x < 10:
    		print "x pozitif ve tek basamaklıdır."

- alternatif olarak

.. code-block:: python
	:linenos:

	if 0 < x < 10:
		print "x pozitif ve tek basamaklıdır."



---------------------------------------------------
geri dönüş cümlesi
---------------------------------------------------

- `return` anahtar kelimesi işlevin o andan sonrasını bırak, çık

.. code-block:: python
	:linenos:

	def print_square_root(x):
	    if x <= 0:
		print "Sadece pozitif sayılar lütfen."
		return

	    result = x**0.5
	    print "x'in kare kökü", result

- erken çıkma

- uygun hata mesajı

- `return` ile ilgili daha fazlası sonradan gelecek



---------------------------------------------------
klavye girdisi
---------------------------------------------------

- `raw_input`, `input`

- `raw_input`, dizgi döndürür

- `input`, `eval(raw_input(prompt))` yani `raw_input`'un hesaplanmış/değerlendirilmiş hali

.. code-block:: python
	:linenos:

	>>> val = raw_input("aritmetik ifade girin: ")
	aritmetik ifade girin: 3 + 4
	>>> val
	'3 + 4'
	>>> val = input("aritmetik ifade girin: ")
	aritmetik ifade girin: 3 + 4
	>>> val
	7

- `raw_input`, `3 + 4`'ü dizgi olarak aldı ve çıktı üretti: `'3 + 4'`

- `input`, `3 + 4` ifadesini hesapladı, sonucu aldı ve çıktı üretti: `7`



---------------------------------------------------
klavye girdisi
---------------------------------------------------

- `input` ile dizgi girerken dikkatli olun

- kabukta dizgi girme kuralları geçerli

.. code-block:: python
	:linenos:

	>>> str = raw_input("dizgi girin: ")
	dizgi girin: python programlama dili
	>>> str
	'python programlama dili'
	>>> str = input("dizgi girin: ")
	dizgi girin: python programlama dili
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<string>", line 1
	    python programlama dili
			     ^
	SyntaxError: invalid syntax
	>>> str = input("dizgi girin: ")
	dizgi girin: "python programlama dili"
	>>> str
	'python programlama dili'



---------------------------------------------------
kompozisyon
---------------------------------------------------

- işlev, girdi, kontrol, `in` anahtar kelimesi

.. code-block:: python
	:linenos:

	def ask_ok(prompt):
		ok = raw_input(prompt)
		if ok in ('y', 'ye', 'yes'):
			print 'YES'
		if ok in ('n', 'no', 'nop', 'nope'):
			print 'NO'

- `prompt` biçiminde değişken kullanabiliriz

- koşul yapısı içerisinde `in`'i kullanabiliriz

- `in`, değer ardışıllığın içerisinde var mı?

- yukarıdaki işlevi çağırırken

.. code-block:: python
	:linenos:

	ask_ok('Cikmak istediginizden emin misiniz?')



---------------------------------------------------
dizgiye dönüşüm
---------------------------------------------------

- dizgiye dönüşüm: `str(ARGUMAN)`

.. code-block:: python
	:linenos:

	>>> str(32)
	'32'
	>>> str(3.14)
	'3.14'
	>>> str(True)
	'True'

- `32` farklıdır `'32'`

- dizgi mi? sayı mı?




---------------------------------------------------
tip dönüşümleri
---------------------------------------------------

- tamsayıya dönüşüm: `int(ARGUMAN)`

- dönüştürmeye çalış, başarısız olursan hata mesajı ver

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> int("32")
	32
	>>> int("32", 16)
	50
	>>> int(str(32), 8)
	26
	>>> int("merhaba")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: 'merhaba'
	>>> val = raw_input("Bir deger girin: ")
	Bir deger girin: 34
	>>> int(val)
	34
	>>> int("0x13", 16)
	19

- `raw_input`, dizgi döndürür

- dizgi   sayı dönüşümü için: `int()`



---------------------------------------------------
gerçel  tamsayı dönüşümü
---------------------------------------------------

- gerçel  tamsayı dönüşümü

.. code-block:: python
	:linenos:

	>>> int(34.4)
	34
	>>> int(34.999)
	34
	>>> int("34")
	34
	>>> int("34.4")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '34.4'

- kural: tamsayı kısmını al



---------------------------------------------------
tamsayı  gerçel, dizgi  gerçel dönüşümü
---------------------------------------------------

- dönüşümler

.. code-block:: python
	:linenos:

	>>> float(32)
	32.0
	>>> float("3.141519")
	3.1415190000000002
	>>> int("3.141519")
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	ValueError: invalid literal for int() with base 10: '3.141519'



---------------------------------------------------
boolean dönüşümü
---------------------------------------------------

- mantıksala dönüşüm: `bool()`

.. code-block:: python
	:linenos:

	>>> bool(1)
	True
	>>> bool(1.0)
	True
	>>> bool(0)
	False
	>>> bool(0.0)
	False
	>>> bool("merhaba")
	True
	>>> bool("")
	False

- kural: boş veya sıfır değerliler `False`'dur



---------------------------------------------------
kısaltmalar
---------------------------------------------------

- ad için kullanıcı bir şeyle girmiş mi?

.. code-block:: python
	:linenos:

	>>> ad = raw_input("Adinizi giriniz: ")
	Adinizi giriniz:
	>>> if ad == "":
	...     print "adi girmeden devam edemezsiniz"
	...
	adi girmeden devam edemezsiniz

- önce yardımcı bilgi:	`>>> bool(ad)`, eğer `ad` boşsa `False` üretir

- buradaki `if ad == "":` kısmını artık kısaltabiliriz

- önce böyle `>>> if bool(ad):`

- sonra şöyle `>>> if ad:`



---------------------------------------------------
hata ayıklama
---------------------------------------------------

- bir hata meydana geldiğinde bir çok bilgi sunar

- en faydalı olanları

1. hatanın türü

2. nerede olduğu

- `Syntax error`, bulması kolaydır

.. code-block:: python
	:linenos:

    >>> x = 5
    >>>  y = 6
      File "<stdin>", line 1
	y = 6
	^
    IndentationError: unexpected indent

- genel olarak hatalar belirtilen kodun/satırın öncesindedir



---------------------------------------------------
çalışma zamanı hatası
---------------------------------------------------

- amaç SNR'yi hesaplamak

.. code-block:: python
	:linenos:

    # d04_debug.py

    import math
    signal_power = 9
    noise_power  = 10
    ratio = signal_power / noise_power
    decibels = 10 * math.log10(ratio)
    print decibels

=

- çalıştırıldığında

.. code-block:: python
    :linenos:

    $ python d04_debug.py
    Traceback (most recent call last):
      File "d04_debug.py", line 7, in <module>
	decibels = 10 * math.log10(ratio)
    ValueError: math domain error

- satır7'de nedir acaba?


---------------------------------------------------
çözüm
---------------------------------------------------

d04_debug2.py dosyası



---------------------------------------------------
GASP 
---------------------------------------------------

- Gasp: Graphics API for Students of Python 

- Python için Grafik Uygulama Geliştirme Arayüzü

- önce kur `$ sudo apt-get install python-gasp`

- kodla

.. code-block:: python
    :linenos:

    >>> from gasp import *
    >>> begin_graphics()
    >>> Circle((200, 200), 60)
    Circle instance at (200, 200) with radius 60
    >>> Line((100, 400), (580, 200))
    Line instance from (100, 400) to (590, 250)
    >>> Box((400, 350), 120, 100)
    Box instance at (400, 350) with width 120 and height 100
    >>> end_graphics()

- GASP'ı bilgisayar programlama kavramlarını görselleştirmek ve öğrenirken eğlenmek için kullanacağız.



---------------------------------------------------
sıra sizde
---------------------------------------------------

- Fermat's Last Theorem: a^n + b^n = c^n

- d04_fermat.py

- d04_istriangle.py

- d04_html.py

- kur bilgisi






- sayı tahminatör
	

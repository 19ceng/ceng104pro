---------------------------------------------------
İşlev nedir?
---------------------------------------------------

TODO



---------------------------------------------------
işlev
---------------------------------------------------

fonksiyon (işlev):
	belli bir işlemi gerçekleştirmek üzere isimlendirilmiş cümle (komut) serisidir.

- işlevi bir kereliğine **tanımlarsınız**: ne yapacağına dair cümleleri yazarsınız

- işlevi çok defa **çağırırsınız**: aynı işi (farklı **parametrelerle** ) tekrar tekrar yaptırırsınız



---------------------------------------------------
işlev: tanımlama
---------------------------------------------------

- işlev tanımlanırken,

.. code-block:: python
	:linenos:

	def ISIM( PARAMETRE LISTESI ):
	    CUMLELER

- işlevin ne yaptığını söyleyen: **ISIM**

- bu işte kullanacağı dış veriler: **PARAMETRELER**

- ne yapacağını söyleyen: **CUMLELER**



---------------------------------------------------
bileşik cümle
---------------------------------------------------

- `def` anahtar kelime (*definition*)

- satır sonunda iki nokta üst üste - `:`

- CUMLELER, `def` satırına göre içerden başlamalıdır

- işlevler aslında `def` ile başlayıp (**başlık** satırı)

- CUMLELER ile devam eden (**gövde** bölümü)

- bileşik bir cümledir

- işlev isminden sonra parametreler olmasa da parantez vardır



---------------------------------------------------
PEP isimlendirme kuralları
---------------------------------------------------

todo


---------------------------------------------------
işlev
---------------------------------------------------

- diğer dillerdeki (C++, Pascal vs) gibi arayüz ve gerçekleme ayrı değildir

- işleve ihtiyaç duyduğunuzda sadece onu deklare edersiniz (tanımlarsınız)

.. code-block:: python
	
	def merhaba_de():

- `def` bu deklerasyonu başlatır

- varsa argümanları parantez içerisinde yer alır, birden fazla iseler virgülle ayrılır

- işlevin döndüreceği değerin türünün belirtilmesi zorunluluğu yoktur

- boş `return` dönütleri `None` değerlidir



---------------------------------------------------
merhaba dünya
---------------------------------------------------

- ilk işlevimiz

.. code-block:: python
	:linenos:

	def merhaba_de():
		print "merhaba, dunya"

- parametre almayan

- `merhaba_de` isminde

- tek cümle (`print "merhaba, dunya"`) gövdeye sahip 

- bir işlev tanımıdır



---------------------------------------------------
`pass` ifadesi
---------------------------------------------------

- yeni kodla çalışıyorken işlev gövdesini boş bırakmamak için

- farklı kullanımları da olan (`while` ile belli bir süre bekleme gibi)

- `pass` ifadesi

.. code-block:: python
	:linenos:

	def initlog():
		pass   # Remember to implement this!



---------------------------------------------------
işlev çağrısı
---------------------------------------------------

- işlevi tanımlamak tek başına hiçbir anlama gelmez

- onu çağırmalısınız ki bir işi icra etsin

- işlevi çağırısı ise

- işlev ismini, takiben parantez içerisinde 

- varsa parametrelerle gerçekleştirilir

.. code-block:: python
	:linenos:

	# gercekle
	def merhaba_de():
		print "merhaba, dunya"

	# main
	print "BASLA"
	merhaba_de()	# cagir
	merhaba_de() 	# tekrar cagir
	merhaba_de() 	# tekrar cagir
	print "BITIR"


---------------------------------------------------
işlev çağrısı
---------------------------------------------------

- çıtı

.. code-block:: python
	:linenos:

	BASLA
	merhaba, dunya
	merhaba, dunya
	merhaba, dunya
	BITIR




---------------------------------------------------
işlevi başka bir işlevde kullanma
---------------------------------------------------

- üç çağrıyı tek bir işlevde birleştirebiliriz

.. code-block:: python
	:linenos:

	def merhaba_de3():
		print "merhaba, dunya"
		print "merhaba, dunya"
		print "merhaba, dunya"

|

- ya da daha güzeli

.. code-block:: python
	:linenos:

	def merhaba_de3():
		merhaba_de()
		merhaba_de()
		merhaba_de()

- daha da güzeli var geleceğiz

- yordam (işlev) içerisinde birden fazla kez çağırıyoruz



---------------------------------------------------
neden işlevler
---------------------------------------------------

- Yeni bir fonksiyon yaratma, size cümle gruplarına bir isim verme şansı verir.

- Yeni fonksiyonlar yaratmak programınızı küçültebilir.

   + basit olarak ekranda 6 kez merhaba dedirtmek nasıl olurdu?



---------------------------------------------------
yürütme akışı
---------------------------------------------------

- `merhaba_de` ve `merhaba_de3`, `main` üzerinden çizim yaparak açıkla



---------------------------------------------------
uzun metin
---------------------------------------------------

- üç tırnakla uzun - çok satırlı çıktı

.. code-block:: python
	:linenos:

	def davet_et():
	    print """\
	    Sayin Mehmet Bey,

	    19.05.2010 tarihinde bolumumuzde yapacagimiz 
	    OYAK etkinliginde yer almanizi gonulden arzu ederiz.

	    Saygılarımızla,
	    OYAK Kulubu"""

	davet_et()

- Mehmet bey dışındakileri nasıl davet edeceğiz?

- tarihi değiştirmenin başka bir yolu olabilir mi?



---------------------------------------------------
argümanlar
---------------------------------------------------

- `davet_et` işlevine davet edilecek kişiyi nasıl söyleriz

- şimdiye kadar aslında gördünüz

.. code-block:: python

	>>> x = input("Bir sayi giriniz:")
	Bir sayi giriniz:-4
	>>> y = abs(x)
	>>> print "y =", y
	y = 4

- `input` işlevindeki `"Bir sayi giriniz:"`

- `abs` işlevindeki `x`

- `print` işlevindeki `"y =", y`



---------------------------------------------------
argümanlar
---------------------------------------------------

argüman (parametre):
	fonksiyonun görevini yaparken kullandığı ve bir bakıma bu görevi nasıl yapacağını belirleyen değerler.

- bazıları tek parametre alır: `abs(x)`

- bazıları iki: `pow(a, b)`

- bazılarında ucu açıktır: `max(1, 4, 2, 0, 9, 5)`



---------------------------------------------------
argüman
---------------------------------------------------

- selamlama işlevi

.. code-block:: python
	:linenos:

	def selamla():
		print "merhaba"

|

- kimi selamlayacak

.. code-block:: python
	:linenos:

	def selamla(kisi):
		print "merhaba", kisi

- `kisi` argümanıdır



---------------------------------------------------
davet_et - v2
---------------------------------------------------

- `davet_et` işlevini dışarıdan argüman alacak biçimde düzenleyelim

.. code-block:: python
	:linenos:

	def davet_et(kimi, nezaman, kim):
	    print """\
	    Sayin %s,

	    %s tarihinde bolumumuzde yapacagimiz 
	    OYAK etkinliginde yer almanizi gonulden arzu ederiz.

	    Saygılarımızla,
	    %s""" % (kimi, nezaman, kim)

	davet_et("Mehmet Atar", "21.02.2010", "OYAK Kulubu")
	davet_et("Robotik Kulubu Uyeleri", "21.02.2010", "Bilgisayar Muhendisligi Bolumu")



---------------------------------------------------
`import` cümlesi
---------------------------------------------------

- `selamla` işlevini `d03_selamla.py` ismiyle kaydedin

- herhangi bir betikte/kabukta bunu çağırmak için

.. code-block:: python
	:linenos:

	from d03_selamla import *

	kim = raw_input("Kimi selamlayayim? ")
	selamla(kim)



---------------------------------------------------
argüman kısmında deyim kullanımı
---------------------------------------------------

- argüman değer veya değişken olabileceği gibi

- deyim de olabilir

.. code-block:: python
	:linenos:

	selamla('Python' * 5)



---------------------------------------------------
yerel değişken
---------------------------------------------------

- argümanlar yerel değişkenlerdir

.. code-block:: python
	:linenos:

	def swap(a, 
		a, b = b, a

	x, y = 5, 4
	swap(x, y)
	print x, y

- ekran çıktısı nedir?

- `5 4`? `4 5`?



---------------------------------------------------
`docstring` - `doctest`
---------------------------------------------------

- `docstring`, Python işlevlerinizi dokumente etmede kullanırız

- tasarladığınız her işlev için bunu yazmak zorunda değilsiniz

- FAKAT dokumente etseniz iyi olur

- böylelikle her bir işlevin tasarımıyla dokumentasyonu aynı dosyada yer alır

- Python bu dokumentasyona erişmek için iki yol sunar: `__doc__`, `help`



---------------------------------------------------
`docstring`: `__doc__` ve `help()`
---------------------------------------------------

- örnek

.. code-block:: python
	:linenos:

	# d03_docstring.py

	def selamla(kisi):
		"""
		selamla(kisi), islevi. 
		kisi yi selamlar
		"""
		print "merhaba", kisi

|
▬

- `__doc__` yöntemi ve `help()`

.. code-block:: python

	>>> from d03_docstring import *
	>>> selamla.__doc__
	'\n\tselamla(kisi), islevi. \n\tkisi yi selamlar\n\t'
	>>> help(selamla)
	Help on function selamla in module d03_docstring:

	selamla(kisi)
	    selamla(kisi), islevi.
	    kisi yi selamlar



---------------------------------------------------
`docstring` örnekleri
---------------------------------------------------

- PEP-0257

.. code-block:: python
	:linenos:

	def complex(real=0.0, imag=0.0):
	    """Form a complex number.

	    Keyword arguments:
	    real -- the real part (default 0.0)
	    imag -- the imaginary part (default 0.0)

	    """
	    if imag == 0.0 and real == 0.0: return complex_zero
	    ...



---------------------------------------------------
doctest
---------------------------------------------------

- `doctest`, yazılım geliştirmede kaynak kodun otomatik birim sınamasını yapmak yaygın bir pratiktir.

- Birim sınama, fonksiyonlar gibi bağımsız kod parçalarının otomatik olarak  doğru çalıştığını onaylamak için bir yol sağlar.

- Bu daha sonra fonksiyonun gerçekleştirimini değiştirmeyi ve yine de bekleneni yapmasını olanaklı kılar.



---------------------------------------------------
Python'da doctest modülü ve kullanımı
---------------------------------------------------

- Doctestler fonksiyon gövdesinin veya betiğin ilk satırında üç tırnaklı karakter dizileri (docstring) içerisinde yazılabilir

- Bunlar bir Python bilgi istemine girdileri ve beklenen çıktıyı örnekleyen yorumlayıcı oturumları şeklindedir.

- doctest modülü `>>>` ile başlayan herhangi bir cümleyi otomatik olarak çalıştırarak, 

- takip eden cümleyi yorumlayıcının çıktısıyla karşılaştırır.



---------------------------------------------------
`doctest`
---------------------------------------------------

- örnek

.. code-block:: python
	:linenos:

	# d03_doctest.py

	def is_divisible_by_2_or_5(n):
	    """
	      >>> is_divisible_by_2_or_5(8)
	      True
	    """

	if __name__ == '__main__':
	    import doctest
	    doctest.testmod()



---------------------------------------------------
test edelim
---------------------------------------------------

- test

.. code-block:: python
	:linenos:
	:size: Tiny

	$ python d03_doctest.py -v
	Trying:
	    is_divisible_by_2_or_5(8)
	Expecting:
	    True
	**********************************************************************
	File "d03_doctest.py", line 5, in __main__.is_divisible_by_2_or_5
	Failed example:
	    is_divisible_by_2_or_5(8)
	Expected:
	    True
	Got nothing
	1 items had no tests:
	    __main__
	**********************************************************************
	1 items had failures:
	   1 of   1 in __main__.is_divisible_by_2_or_5
	1 tests in 2 items.
	0 passed and 1 failed.
	***Test Failed*** 1 failures.



---------------------------------------------------
daha gerçeksi
---------------------------------------------------

- argüman değişken olması durumu

.. code-block:: python
	:linenos:

	def is_divisible_by_2_or_5(n):
	    """
	      >>> is_divisible_by_2_or_5(8)
	      True
	      >>> is_divisible_by_2_or_5(7)
	      False
	      >>> is_divisible_by_2_or_5(5)
	      True
	      >>> is_divisible_by_2_or_5(9)
	      False
	    """
	    print n % 2 == 0 or n % 5 == 0 

	if __name__ == '__main__':
	    import doctest
	    doctest.testmod()



---------------------------------------------------
sıra sizde
---------------------------------------------------

- aşağıdaki problemi çözün

.. code-block:: python
	:linenos:

	def cat_n_times(s, n):
	    <kodu buraya yazin>

	>>> cat_n_times('Spam', 7)
	SpamSpamSpamSpamSpamSpamSpam

- veya şöyle diyeceğiz

.. code-block:: python
	:linenos:

	def cat_n_times(s, n):
		"""
			>>> cat_n_times('Spam', 7)
			SpamSpamSpamSpamSpamSpamSpam
		"""
		<kodu buraya yazin>

- diyeceğiz




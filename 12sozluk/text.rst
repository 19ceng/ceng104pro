-------------------------------------------------------------------
sözlükler
-------------------------------------------------------------------

- koleksiyonlar: ardışık ve eşleştirme

- ardışık: dizgi, liste, tuple (çok öğeliler)

- ardışık: erişim indisle yapılır

- eşleştirme: sözlük

- eşleştirme: anahtar/değer

- PB: 6593



-------------------------------------------------------------------
merhaba
-------------------------------------------------------------------

- türkçe - ispanyolca sözlük tasarımı

.. code-block:: python
	:linenos:

	>>> tr2sp = {}
	>>> tr2sp['bir'] = 'uno'
	>>> tr2sp['iki'] = 'dos'

- `{}`: boş sözlük

- anahtar-değer çiftleri



-------------------------------------------------------------------
devam
-------------------------------------------------------------------

- böyle yazdır

.. code-block:: python
	:linenos:

	>>> print tr2sp
	{'iki': 'dos', 'bir': 'uno'}

- istersen böyle ata, çiftler virgülle ayrılıyor

.. code-block:: python
	:linenos:

	>>> tr2sp = {'bir':'uno', 'iki':'dos', 'uc':'tres'}

- eleman eleman böyle eriş

.. code-block:: python
	:linenos:

	>>> print tr2sp['iki']
	dos



-------------------------------------------------------------------
sözlük işlemleri
-------------------------------------------------------------------

- `del` ifadesi anahtar-değer çiftini siler

.. code-block:: python
	:linenos:

	>>> stok = {'elma': 430, 'muz': 312, 'portakal': 525, 'erik': 217}
	>>> print stok
	{'elma': 430, 'erik': 217, 'portakal': 525, 'muz': 312}
	>>>
	>>> del stok['erik']
	>>> print stok
	{'elma': 430, 'portakal': 525, 'muz': 312}

- değer güncellerken

.. code-block:: python
	:linenos:

	>>> stok['erik'] = 0
	>>> print stok
	{'elma': 430, 'erik': 0, 'portakal': 525, 'muz': 312}

- sözlükte kaç çift var

.. code-block:: python
	:linenos:

	>>> len(stok)
	4



-------------------------------------------------------------------
sözlük metodları
-------------------------------------------------------------------

- tüm anahtarlar, değerler ve çiftler (tuple'ı)

.. code-block:: python
	:linenos:

	>>> tr2sp.keys()
	['iki', 'bir', 'uc']
	>>>
	>>> tr2sp.values()
	['dos', 'uno', 'tres']
	>>>
	>>> tr2sp.items()
	[('iki', 'dos'), ('bir', 'uno'), ('uc', 'tres')]



-------------------------------------------------------------------
nesne yönelimlilik paradigması
-------------------------------------------------------------------

- dizgi, listelerde olduğu gibi sözlük metodlarında da 

- nokta-`.` gösterilimi

- noktanın sağına metod ismi,

- noktanın solundaki değişkene ilgili metod uygulanır

- parantez içerisinde bir şeylerin yazılmamış olması, parametresiz olduğunu gösterir

- metod çağrısı -> **çağırma (invocation)**

- `tr2sp.keys()`: `tr2sp` nesnesinde `keys` metodunu çağırdık

- tasarıma ait: bu metodun ilk argümanı, nesnenin kendisidir (`self`)

.. code-block:: python
	:linenos:

	def keys(self):
		...



-------------------------------------------------------------------
sözlük metodları
-------------------------------------------------------------------

- böyle bir anahtar var mı?

.. code-block:: python
	:linenos:

	>>> tr2sp.has_key('bir')
	True
	>>> tr2sp.has_key('deux')
	False

- bunu doğrudan yapar ve olmayan anahtar için değer sorarsanız

.. code-block:: python
	:linenos:

	>>> tr2sp['dog']
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	KeyError: 'dog'



-------------------------------------------------------------------
rumuz ve kopyalama X deep-shallow copy
-------------------------------------------------------------------

- shallow copy X deep copy

.. code-block:: python
	:linenos:

	>>> karsitlar = {'up': 'down', 'right': 'wrong', 'true': 'false'}
	>>> rumuz = karsitlar
	>>> kopya = karsitlar.copy()

- shallow (rumuz) olandaki değişiklik orjinali de etkiler

.. code-block:: python
	:linenos:

	>>> rumuz['right'] = 'left'
	>>> karsitlar['right']
	'left'

- deep'deki değişiklik ise etkilemez

.. code-block:: python
	:linenos:

	>>> kopya['right'] = 'privilege'
	>>> karsitlar['right']
	'left'



-------------------------------------------------------------------
dağınık matrisler (sparse matrix)
-------------------------------------------------------------------

.. image:: media/sparse.png

- matris için liste gösterilimi bol sıfır içerir

.. code-block:: python
	:linenos:

	matris = [[0, 0, 0, 1, 0],
			  [0, 0, 0, 0, 0],
			  [0, 2, 0, 0, 0],
			  [0, 0, 0, 0, 0],
			  [0, 0, 0, 3, 0]]

- alternatif: sözlük kullanımı

.. code-block:: python
	:linenos:

	>>> matris = {(0, 3): 1, (2, 1): 2, (4, 3): 3}

- kaç elemanı var? anahtarları nedir?

- nasıl erişiriz

.. code-block:: python
	:linenos:

	>>> matris[(0, 3)]
	1



-------------------------------------------------------------------
dağınık matrisler (sparse matrix)
-------------------------------------------------------------------

.. image:: media/sparse.png

- matrisin boş olan bölgesine nasıl erişeceğiz?

- sözlüğe eklenmemiş olanlara erişim

.. code-block:: python
	:linenos:

	>>> matris[(1, 3)]
	Traceback (most recent call last):
	  File "<input>", line 1, in <module>
	KeyError: (1, 3)

- doğru yöntem `get` ve varsayılan değer yapısı

.. code-block:: python
	:linenos:

	>>> matris.get((0, 3), 0)
	1
	>>> matris.get((1, 3), 0)
	0



-------------------------------------------------------------------
bellekleme (hint)
-------------------------------------------------------------------

- daha önce özyineli veya düz tasarladığınız fibonacci işlevi 

- büyük sayılarla sorun çıkartır

- ör: fibonacci(20) anında, fibonacci(39) yaklaşık 1 sn, 

- fibonacci(40) ise neredeyse sonlanamamakta

.. image:: media/fibonacci.png

- bunun sebebi: tekrarlayan fazlalık çağrılardır

- ör. fibonacci(4) için fibonacci(0) 2 kez, 

- fibonacci(1) 3 kez çağrılır/hesaplanır



-------------------------------------------------------------------
bellekleme (hint)
-------------------------------------------------------------------

- daha önce hesaplananları hafızaya alalım

- gerek duyulduğunda buradan verelim -> hint (ipucu)

.. code-block:: python
	:linenos:

[% CODE("d12_fib.py") %]



-------------------------------------------------------------------
bellekleme
-------------------------------------------------------------------

- önce, başlangıç durumuyla `onceki` sözlüğünü ilkle

- eğer sözlükte var olan isteniyorsa gönder 

- yoksa hesapla, sözlüğe ekle ve gönder

- böylelikle göz açıp-kapayıncaya kadar kısa sürede hesapla

.. code-block:: python
	:linenos:

	>>> from d12_fib import *
	>>> fibonacci(100)
	354224848179261915075L

- `L`: long sayı anlamında



-------------------------------------------------------------------
uzun sayılar
-------------------------------------------------------------------

- herhangi bir büyüklükteki sayıyı tutmak için uzun sayı türü-> `long`

.. code-block:: python

	>>> type(1L)
	<type 'long'>
	>>> long(7)
	7L
	>>> long(3.9)
	3L
	>>> long('59')
	59L



-------------------------------------------------------------------
harfleri saymak
-------------------------------------------------------------------

- daha öncede bunu yaptık (7. bölüm)

- histogram dedik

- VLC sıkıştırma tekniği

- sözlük daha şık bir çözüm sunar

.. code-block:: python
	:linenos:

	>>> harf_sayilari = {}
	>>> for harf in "Mississippi":
	...     harf_sayilari[harf] = harf_sayilari.get(harf, 0) + 1
	...
	>>> harf_sayilari
	{'i': 4, 'p': 2, 's': 4, 'M': 1}

- alfabetik sıraya göre sıralamakta mümkün

.. code-block:: python
	:linenos:

	>>> harfler = harf_sayilari.items()
	>>> harfler.sort()
	>>> print harfler
	[('M', 1), ('i', 4), ('p', 2), ('s', 4)]



-------------------------------------------------------------------
sıra sizde
-------------------------------------------------------------------

- alıştırma 1

- çıktı nedir?

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> d = {'apples': 15, 'bananas': 35, 'grapes': 12} 
	>>> d['banana']
	???
	>>> d['oranges'] = 20
	>>> len(d) 
	???
	>>> d.has_key('grapes')
	???
	>>> d['pears']
	???
	>>> d.get('pears', 0)
	???
	>>> fruits = d.keys()
	>>> fruits.sort()
	>>> print fruits
	???
	>>> del d['apples']
	>>> d.has_key('apples') 
	???


-------------------------------------------------------------------
devam
-------------------------------------------------------------------

- aşağıdaki doctestten geçecek işlevi yazın

.. code-block:: python
	:linenos:

	def add_fruit(inventory, fruit, quantity=0):
		"""
		Adds quantity of fruit to inventory. 

		  >>> new_inventory = {}
		  >>> add_fruit(new_inventory, 'strawberries', 10)
		  >>> new_inventory.has_key('strawberries')
		  True
		  >>> new_inventory['strawberries']
		  10
		  >>> add_fruit(new_inventory, 'strawberries', 25)
		  >>> new_inventory['strawberries']       
		"""


-------------------------------------------------------------------
devam
-------------------------------------------------------------------

- alıştırma 3: alice_words.py isminde bir program yazın, programınız alice_in_wonderland.txt dosyasındaki tüm kelimelerin alfabetik listesini her bir kelimenin kaç kere yer aldığıyla birlikte alice_words.txt adındaki metin dosyasına yazsın. Çıktınızın ilk 10 satırı aşağıdakine benzeyecektir:

.. code-block:: python

	Kelime            Adet
	=======================
	a                 631
	a-piece           1
	abide             1
	able              1
	about             94
	above             3
	absence           1
	absurd            2


- alice kelimesi kitapta kaç kere yer almaktadır?

- "Alice in Wonderland (Alice Harikalar Diyarında)"'ki en uzun kelime hangisidir? Kelime kaç karakter içermektedir??



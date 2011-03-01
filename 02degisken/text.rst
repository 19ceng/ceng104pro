### Değer ve Tür

Değer:
	programın işledikleri: girdi, ara işlem, çıktı.

.. code-block:: python

	>>> print 1 + 3
	4

- buradaki `1` ve `3`, çıktıdaki `4` değerdir

.. code-block:: python

	>>> print "merhaba dunya!"
	merhaba dunya!

- buradaki "merhaba dunya!" değerdir.



### Tür

- bu değerlere farklı türe sahiptir

- `1` - tamsayı (integer) iken "merhaba dunya!" - karakter dizisidir (dizgi, string)

- sayı ve dizgiyi ayırt eden şey: çift tırnak

- dolayısıyla `print "4"` ile `print 4`'deki dörtler farklı türdedir

.. code-block:: python

	>>> print "23" + "45"
	2345
	>>> print 23 + 45
	68

- burada söylenecek çok şey: `+` işlecinin dizgi ve sayılarda farklı kullanımı



### `type`

- değerin türünü öğrenmede `type` komutu kullanılır

.. code-block:: python

	>>> type("merhaba dunya!")
	<type 'str'>
	>>> type(4)
	<type 'int'>




### Diğer türler

- tamsayı ve dizgi dışında da türler vardır

- gerçel sayılar için: `float`. ör. `3.2`

.. code-block:: python

	>>> type(3.2)
	<type 'float'>

- `type("3.2")` ve `type("17")` ne üretir?



### tek - çift - üç tırnak

- dizgiler tek-`'` ve çift-`"` tırnakla yazılır

- dizgi içerisinde tek veya çift tırnağa gereksinim duyulması

.. code-block:: python

	>>> print 'OMU'nun gelecegi'
	  File "<stdin>", line 1
	    print 'OMU'nun gelecegi'
		       ^
	SyntaxError: invalid syntax


### `print`: büyük sayıları göstermek

- binler ayracı olarak `,` kullanmak isteyebilirsiniz

.. code-block:: python
	:linenos:                                                                                                            

	>>> print 1, 000, 000
	1 0 0
	>>>

- python bunu üç elemanlı **liste** olarak yorumlar

- gerçel sayılar için `.`-nokta kullan



### Değişkenler: kap

- kullanıcıdan aldığımız şeyleri

- tuttuğumuz kablar

- program içerisinde hesapladığımız şeyleri tuttuğumuz kablar

- programlama jargonunda bu kaplara  **değişken** denilir



### Değişkenler

- değişken, isminden de anlaşılacağı üzere değeri değiştirilebilir

- **atama** cümlesi yeni değişken yaratır ve değerini atar

.. code-block:: python
	:linenos:                                                                                                            

	>>> mesaj = "merhaba, dunya!"
	>>> n = 17
	>>> pi = 3.14159

▬
|

- üç atama, üç değişken: `mesaj`, `n`, `pi`

- üç tür: `dizgi`, `tamsayı`, `gerçel`



### değişkenler

- değişkenin ismi, diğerlerinden ayırt etmek

- değişkenin değeri, içerisinde tuttuğu

- değişkenin türü, içerdiği tür
   + veri yapıları

- türü atama sırasında dinamik belirlenir


### atama işleci

- atama işleci, `=`-eşittir

- sol taraf = sağ taraf

- genel kural: sağdakini yorumla, sola ata

.. code-block:: python
	:linenos:                                                                                                            

	>>> 17 = n
	  File "<stdin>", line 1
	SyntaxError: can't assign to literal



### `print` + değişkenler

- `print` cümleleri değişkenlerle de kullanılır

.. code-block:: python
	:linenos:                                                                                                            

	>>> print mesaj
	merhaba, dunya!
	>>> print n
	17
	>>> print pi
	3.14159

- değişkenin (ör. `n`) o anki değeri (ör. `17`) ekrana yazılır



### `print` + değişkenler: karmaşık cümleler

- `print` cümlesinde hem mesaj hem de değer yazdırabiliriz

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> a = 5
	>>> b = 3
	>>> print "a =", a, "b =", b
	a = 5 b = 3
	>>> print "a =", a, "\nb =", b
	a = 5
	b = 3



### `print` + değişkenler: karmaşık cümleler

- aritmetik işlem sonucunu yazdırabiliriz

.. code-block:: python
	:linenos:
	:size: Tiny                                                                                                          

	>>> print "a ile b'yi carparsak", a * b, "elde ederiz"
	a ile b'yi carparsak 15 elde ederiz

- veya

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print a, "ile", b, "'yi carparsak", a * b, "elde ederiz"
	5 ile 3 'yi carparsak 15 elde ederiz



### `print` + değişkenler: karmaşık cümleler: formatlama

- mesaj içerisinde özel işaretler (`%s`) yardımıyla dizgi içine gömmekte mümkündür

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print "%s ile %s'yi carparsak %s elde ederiz" % (a, b, a*b)
	5 ile 3'yi carparsak 15 elde ederiz

▬
=

- daha ileri düzey formatlama yapıları vardır

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print "{0} ile {1}'yi carparsak {2} elde ederiz".format(a, b, a*b)
	5 ile 3'yi carparsak 15 elde ederiz

- şunlara da bakın: `repr`, `rjust`



### değişkenler + tür

- değişkenlerin de türü vardır

- ▬içeriği neyse türü odur

- ör. `mesaj`, içeriği dizgi olduğundan türü de dizgidir

- çalışma zamanında öğrenmenin yolu `type` işlevini kullanmaktır

.. code-block:: python
	:linenos:                                                                                                            

	>>> type(mesaj)
	<type 'str'>
	>>> type(n)
	<type 'int'>
	>>> type(pi)
	<type 'float'>



### türlerle çalışmak

- daha ileri düzey işler yapmak gerekebilir

.. code-block:: python
	:linenos:                                                                                                            

	from types import *
	def delete(mylist, item):
	    
		if type(item) is IntType:
	       		del mylist[item]
		else:
	       		mylist.remove(item)

▬
|

- dikkat: `if type(item) is IntType:`

- `IntType`, `FloatType`, `StringType`

- işlevler (`def`): 3. hafta

- koşul ifadeleri (`if`, `else`): 4. hafta

- listeler: 9 hafta

- modüller (`from`, `import`): 10. hafta



### değişkenler: isim ve anahtar kelimeler

- anlamlı isimler

- bu değişkeni ne için kullandığını belgelemenin kısayolu

- uzunluğu isteğe bağlıdır

- harf + rakam içerebilir ▬ **mutlaka** harfle başlar▬

- BÜYÜK - küçük harf duyarlıdır

- büyük harfler genelde özel değerleri tutmada kullanılır

- alt çizgi-`_` de kullanılabilir



### değişkenler: isimler: stiller

- **b**: tek küçük harf,  **B**: tek büyük harf

- **küçükharf**, **BÜYÜKHARF**

- **altçizgi_ile_küçükharf**,  **ALÇİZGİ_İLE_BÜYÜKHARF**

- **BaşHarfiBüyükHarf**

- **karışıkBüyükKüçükHarf**

- **Altçizgi_İle_İlk_Harfleri_Büyük_Kelimeler** (iğrenç)

- isimlendirme kuralı: 'PEP 8 Style Guide for Python Code'



### değişkenler: isimler: stiller

- var olan çalışmanın stiline uyun

- kendi stilinizde tutarlı olun

- altçizgi ile başlayan ve biten değişken isimlendirmelerinde dikkatli olun Python'la çakışabilir

- bunlar birbirine karışır: **l - 1 - I** ve **O - 0**, uzak durun

- sabit değerleri içeren değişkenler **ALÇİZGİ_İLE_BÜYÜKHARF** stilinde olmalı



### değişkenler: isimler: örnek

- geçerli

.. code-block:: python
	:linenos:                                                                                                            

	>>> ad = "piton"
	>>> versiyon = 2.6
	>>> yil = 2010

▬
=

- geçersiz

.. code-block:: python
	:linenos:                                                                                                            

	>>> 300sipartali = "Zack Snyder"
	SyntaxError: invalid syntax
	>>> more$ = 10000
	SyntaxError: invalid syntax
	>>> class = "Bilgisayar Programlama 1"
	SyntaxError: invalid syntax



### Açıklama

- `300sipartali`: sayıyla başlamamalı

- `more$`: özel karakter (ör. `$`) içermemeli

- `class`: anahtar kelimeler olamaz



### anahtar kelimeler

- anahtar (veya rezerve edilmiş) kelimeler: dile özgü, dilin kural ve yapısını tanımlar

- değişken isimlerinde **kullanılamazlar**

.. code-block:: python
	:size: Tiny

	and       del       for       is       	raise    
	assert    elif      from      lambda	return   
	break     else      global    not       try      
	class     except    if        or        while    
	continue  exec      import    pass      yield    
	def       finally   in        print



### değişkenlerle çalışma

- değer ata ve aritmetik işlem yap

.. code-block:: python
	:size: Tiny

	>>> x = 6
	>>> y = 5
	>>> x + y
	11

▬
|

- aynı anda çoklu atama
- değerlerin üzerine yazma

.. code-block:: python
	:size: Tiny

	>>> a = b = c = 10
	>>> a + b + c
	30
	>>> a = b = c = 20
	>>> a + b + c
	60



### büyük değerlerle çalışma

- büyük değerlerle çalışma

.. code-block:: python
	:size: Tiny

	>>> fmin = 0.000000000033333
	>>> fmax = 333330000000000.0
	>>> fmin
	3.3333000000000003e-11
	>>> fmax
	333330000000000.0



### `answer` değişkeni

- `answer` (`_`) değişkeni

.. code-block:: python
	:size: Tiny

	>>> 5 + 6
	11
	>>> _ + 22
	33
	


### gerçel sayılar

- gerçel sayılar

.. code-block:: python
	:size: Tiny

	>>> 10./3 + 20./3
	10.0



### dizgi mi? sayı mı?

- dizgi x sayı

.. code-block:: python
	:size: Tiny

	>>> print 12 + 34
	46
	>>> print "12" + "34"
	1234
	


### ileri düzey

- değişken ismini dizgiden almak

.. code-block:: python
	:linenos:                                                                                                            
	:size: Tiny

	>>> kim = "ahmet"
	>>> vars()[kim] = 35
	>>> print ahmet
	35
	>>> ahmet
	35

▬
|

- veya böyle

.. code-block:: python
	:linenos:                                                                                                            
	:size: Tiny

	>>> kim = raw_input("Kimin yasi?")
	Kimin yasi?ahmet
	>>> vars()[kim] = 43
	>>> ahmet
	43



### 2.4 Cümleler

cümle:
	Python yorumlayıcısınca işlenebilecek yönerge

- şimdiye kadar `print` ve atama cümlesini gördük

- cümleyi yaz (kabuğa), Python işlesin (yorumlasın), sonucu versin (eğer varsa)

- `print` cümlesinin sonucu bir değerdir

- atama cümlesi herhangi bir sonuç üretmez

.. code-block:: python
	:linenos:                                                                                                            

	>>> print a = 3
	  File "<stdin>", line 1
	    print a = 3
		    ^
	SyntaxError: invalid syntax



### cümle: betik 

- betikler ardı ardına gelen cümlelerden oluşur

- her bir cümle işletilir (sırayla) (sırayı bozan özel yapılar var, sonra)

- her bir cümlenin sonuçları gösterilir

=

- örnek

.. code-block:: python
	:linenos:                                                                                                            

	print 1
	x = 2
	print x

|

- şu çıktı üretilir sırayla

.. code-block:: python
	:linenos:                                                                                                            

	1
	2

- atama cümlesi çıktı üretmez!



### Deyimler

deyim:
	değerlerden (ör. `1`), değişkenlerden (ör. `yas`) ve işleçlerden (ör. `+`) oluşan yapı.

- eğer bir deyimi kabuğa yazarsanız ve sonlandırma (yürüt) tuşuna (<enter>) basarsanız

- o deyim **değerlendirilir** (hesaplanır) ve sonucu gösterilir

.. code-block:: python
	:linenos:                                                                                                            

	>>> 1 + 4
	5

=

- değer de başlı başına bir deyimdir

- değişken de öyle

.. code-block:: python
	:linenos:                                                                                                            

	>>> 17
	17
	>>> a
	20



### deyim: atama, değerlendirme

- değişkenlere değer atanır (satır 1)

- değerlendirilir (satır 2, 4)

.. code-block:: python
	:linenos:                                                                                                            

	>>> mesaj = "merhaba, dunya"
	>>> mesaj
	'merhaba, dunya'
	>>> print mesaj
	merhaba, dunya



### betik

- betik dosyasında  değerler tek başına çıktı üretmez!

.. code-block:: python
	:linenos:                                                                                                            

	17
	3.2
	"merhaba, dunya"
	1 + 1

- peki ekranda görebilmek için ne yapmalıyız?


### İşleçler ve işlenenler

- işlem = işlenenler + işleç

işleç:
	işlemi belirten, toplama, çarpma vb. hesaplamaları temsil eden özel _sembollerdir_

işlenen:
	işleme giren değerler.

- örnek

.. code-block:: python

	20 + 32
	hour - 1
	hour*60 + minute
	(5 + 9) ** (15 - 7)



### tamsayı bölme

- eğer her iki işlenen tamsayı ise tamsayı bölme adlanır

.. code-block:: python
	
	>>> dakika = 59
	>>> dakika / 60
	0

- işlenenler neyse (tamsayı) sonuç aynı (tamsayı)

- sonucun gerçel olması istenirse işleneni gerçele çevir (4. bölüm)



### işleçlerin sırası

- deyim içerisinde birden fazla sayıdaki işlecin hangi sırayla değerlendirileceği

- öncelik sırası (kuralı) ile belirlenir

- **P** arantez en yüksek öncelik

- **Ü** s alma. Aşağıdaki sonuçları söyleyin (3? 27?)

.. code-block:: python

	>>> 3 * 1 ** 3

- **Ç** arpma ve **B** ölme aynı öncelikte, **T** oplama ve **Ç** ıkarmadan daha yüksek öncelikli

- aynı önceliklilerde **soldan sağa** kuralı



### karakter dizisi üzerindeki işlemler

- genel olarak dizgiler üzerinde matematiksel işlem geçersizdir

.. code-block:: python

	>>> mesaj = "hello" # mesaj = "12"
	>>> mesaj - 1
	>>> mesaj / 123
	>>> mesaj * "bar"
	>>> mesaj + 2



### dizgi: birleştirme

- `+` işleci dizgilerde birleştirme (concatenation),ardı ardına ekleme

.. code-block:: python

	ad = "Ahmet"
	soyad = "Kilic"
	print "Merhaba" + ad + soyad

- sonuç: `Merhaba Ahmet Kilic` olacaktır



### dizgi: çoğaltma

- `*` işleci de dizgilerle çalışır. Tekrarlama veya çoğaltma işlemi

.. code-block:: python

	>>> "Python'u " + "cok" * 5 + " seviyoruz"
	"Python'u cokcokcokcokcok seviyoruz"



### dizgi - sayı benzerlik

- `4 * 3`, deyimini `4 + 4 + 4` olarak düşünebiliriz

- `"cok" * 3`, deyimi de benzer olarak `"cok" + "cok" + "cok"` olur



### girdi

- kullanıcıdan (klavyeden) girdi almak için: `input`, `raw_input`

.. code-block:: python

	ad = raw_input("Lutfen adinizi giriniz: ")
	no = input("Lutfen ogrenci numaranizi giriniz: ")
	print "%s nin numarasi %s dir"%(ad, no)

- çıktısı

.. code-block:: python

	$ python 02_girdi.py
	Lutfen adinizi giriniz: nurettin
	Lutfen ogrenci numaranizi giriniz: 987
	nurettin nin numarasi 987 dir

- `input` girdilerinde sayısal ifade de girebilirsiniz
  


### girdi: type

- aşağıdaki her bir durum için çıktılar neler olabilir

.. code-block:: python

	>>> x = input()
	3.14
	>>> type(x)
	???
	>>> x = raw_input()
	3.14
	>>>type(x)
	???



### yorumlar

- doğal dillerdeki notlara ve açıklamalara benzer olarak kodun belirli bölgesini

- açıklamada kullanılan yapılara **yorum** denilir

- tek satırlık yorumlar `#` ile başlar

.. code-block:: python

	# gecen zamanin yuzdesi
	yuzde = (dakika * 100) / 60

	yuzde = (dakika * 100) / 60  # dikkat: tamsayi bolme



ü### 


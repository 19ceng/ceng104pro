-------------------------------------------------------------------
Birden fazla atama
-------------------------------------------------------------------

- yeni atama yeni temsil

.. code-block:: python
	:linenos:

	bruce = 5
	print bruce,
	bruce = 7
	print bruce

=

- ekran çıktısı: `5, 7`



-------------------------------------------------------------------
değişken: kutu/kova benzetmesi
-------------------------------------------------------------------

- şimdiye kadar değişkenlere kova benzetmesinde bulunduk

.. code-block:: python
	:linenos:

	bruce = 5
	bruce = 7

- ilk satırda kovada `5` değeri vardı, ardından `7` konuldu

- Python diğer dillerden farklıdır

- değişkenleri kova yerine etiket veya "sticky note"

- `bruce=5`: nesneye (burada `5`) `bruce` etiketini ver

- `bruce=7`: nesneye (burada `7`) `bruce` etiketini ver

- Python'da her şey nesnedir: `1`, `[1, 2]`, `abs()`, ...



-------------------------------------------------------------------
`id()`: nesnelerin bellekteki yeri
-------------------------------------------------------------------

- `id()`: nesnelerin bellekteki adresini söyler

.. code-block:: python
	:linenos:

	>>> help(id)
	Help on built-in function id in module __builtin__:

	id(...)
		id(object) -> integer

		Return the identity of an object.  This is guaranteed to be unique among
		simultaneously existing objects.  (Hint: it's the object's memory address.)

- örnek

.. code-block:: python
	:linenos:

	>>> id(5)
	159747376
	>>> id(7)
	159747352



-------------------------------------------------------------------
değişken/etiket - kimliği
-------------------------------------------------------------------

- değişkenler nerede saklanır?

.. code-block:: python
	:linenos:

	>>> bruce=5
	>>> id(bruce)
	159747376
	>>> bruce=7
	>>> id(bruce)
	159747352

- sayılar birbirine benzer fakat

- ilk `id(bruce)` ile `id(5)` aynı sayıyı

- aynı bellek adresini gösteriyor

- Python'da değişken tanımını hatırlatırsak

- nesneye (ör. `5`) etiket (ör. `bruce`) ver



-------------------------------------------------------------------
değişkenleri güncelleme
-------------------------------------------------------------------

- değer güncellemede olan nedir?

.. code-block:: python
	:linenos:

	>>> x = 1
	>>> x, id(x), id(1)
	(1, 159747424, 159747424)
	>>> x = x + 1
	>>> x, id(x), id(1)
	(2, 159747412, 159747424)
	>>> x, id(x), id(1), id(2)
	(2, 159747412, 159747424, 159747412)



-------------------------------------------------------------------
değişkenleri güncelleme
-------------------------------------------------------------------

- kodları filtrele

.. code-block:: python
	:linenos:

	>>> x = 1
	>>> x
	1
	>>> x = x + 1
	>>> x
	2

- `1` nesnesine `x` etiketini ata

- `x` etiketli nesneyle `1` nesnesini topla

   + `help(x)` ve `help(1)` ne üretiyor?

   + her şey nesne!!!

   + tamsayı nesneleri üzerinde `+` işleci toplama yapar

- `2` nesnesine `x` etiketini ata



-------------------------------------------------------------------
ilklendirme
-------------------------------------------------------------------

- değişkenin ilkin değeri (eski değeri)?

.. code-block:: python
	:linenos:

	>>> toplam = toplam + 10
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	NameError: name 'toplam' is not defined

- siz toplayın

- soracaksınız `toplam` ne ki?

- üzerine `10` ekleyeyim



-------------------------------------------------------------------
`while` cümlesi
-------------------------------------------------------------------

- yineleme amacıyla kullanılan ilk yapı

.. code-block:: python
	:linenos:

	def countdown(n):
		while n > 0:
			print n
			n = n-1
		print "Yokol!"

- koşul: `True` veya `False`

- koşul doğru olduğu müddetçe `while` cümlelerini söyle

- yanlış olunca çık



-------------------------------------------------------------------
sonsuz döngü
-------------------------------------------------------------------

- döngü, sonsuz döngü

.. code-block:: python
	:linenos:

	def sequence(n):
		while n != 1:
			print n,
			if n % 2 == 0:        # n çifttir
				n = n / 2
			else:                 # n tektir
				n = n * 3 + 1

- döngü hangi şartlarda kesilir?



-------------------------------------------------------------------
basamakları sayma
-------------------------------------------------------------------

- basamakları sayalım

.. code-block:: python
	:linenos:

	def num_digits(n):
		count = 0
		while n:
			count = count + 1
			n = n / 10
		return count

- doctest'lerimiz

.. code-block:: python
	:linenos:

	>>> num_digits(710)
	3
	>>> num_digits(12)
	2
	>>> num_digits(12345)
	5

- pastebin: http://bpaste.net/show/5073/, veya PB=5073

- bu arada bpython'u denediniz mi?



-------------------------------------------------------------------
koşul eklentisi
-------------------------------------------------------------------

- sadece basamak değeri `0` ve `5` olanları saymak isteseydik (PB=5074)

.. code-block:: python
	:linenos:

	>>> def num_zero_and_five_digits(n):
	...     count = 0
	...     while n:
	...         digit = n % 10
	...         if digit == 0 or digit == 5:
	...             count = count + 1
	...         n = n / 10
	...     return count
	...
	>>> num_zero_and_five_digits(1055030250)
	7
	>>> num_zero_and_five_digits(1200)
	2
	>>> num_zero_and_five_digits(120051)
	3



-------------------------------------------------------------------
sıra sizde
-------------------------------------------------------------------

- basamak değeri en büyük hangisi

- bu sayının basamaklarıyla elde edilecek en büyük/küçük sayı kaçtır?



-------------------------------------------------------------------
kısaltılmış atama
-------------------------------------------------------------------

- değişkeni arttırmayla sık karşılaşırız (PB=5075)

.. code-block:: python
	:linenos:

	>>> count = 0
	>>> count += 1
	>>> count
	1
	>>> count = count + 1
	>>> count
	2

|

- diğerleri (PB=5076)

.. code-block:: python
	:linenos:

	>>> n += 5
	>>> n = 5
	>>> n += 3
	>>> n
	8
	>>> n * = 2
	>>> n
	16
	>>> n %= 3
	>>> n
	1



-------------------------------------------------------------------
tablolar
-------------------------------------------------------------------

- basit (PB=5077)

.. code-block:: python
	:linenos:

	>>> x = 1
	>>> while x < 13:
	...     print x, '\t', 2**x
	...     x += 1

|

- çıktı

.. code-block:: python
	:linenos:

	1       2
	2       4
	3       8
	4       16
	5       32
	6       64
	7       128
	8       256
	9       512
	10      1024
	11      2048
	12      4096

=

- burada `\t`: kaçış serisi (escape sequences)



-------------------------------------------------------------------
iki boyutlu tablolar 
-------------------------------------------------------------------

- 2B tablo (PB=5078)

.. code-block:: python
	:linenos:

	>>> i = 1
	>>> while i <= 6:
	...     print 2*i, '  ',
	...     i += 1
	...
	...
	2    4    6    8    10    12

- `print` cümlesinin sonundaki virgül-`,` dikkat



-------------------------------------------------------------------
sarma (encapsulation) ve genelleştirme
-------------------------------------------------------------------

sarma:
   (kabaca) bir kod parçasını işlev içerisine koymadır

- PB:5079

.. code-block:: python
	:linenos:

	def print_multiples(n):
		i = 1
		while i <= 6:
			print n*i, '\t',
			i += 1
		print

- PB:5078'deki `2` değerinin, `n` ile değiştirilmesi genelleştirmedir

|

- çıktılar

.. code-block:: python
	:linenos:

	>>> print_multiples(3)
	3       6       9       12      15      18
	>>> print_multiples(4)
	4       8       12      16      20      24

= 

- sütunda `6`'ya kadar yazdırılıyor

- genelleştirin


-------------------------------------------------------------------
çarpım tablosu
-------------------------------------------------------------------

- PB:5080

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> i = 1
	>>> while i <= 6:
	...     print_multiples(i)
	...     i += 1
	...
	1       2       3       4       5       6
	2       4       6       8       10      12
	3       6       9       12      15      18
	4       8       12      16      20      24
	5       10      15      20      25      30
	6       12      18      24      30      36



-------------------------------------------------------------------
daha fazla sarma
-------------------------------------------------------------------

- PB:5080'ni sarmayabiliriz (PB:5081)

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> def print_mult_table():
	...     i = 1
	...     while i <= 6:
	...         print_multiples(i)
	...         i += 1
	...
	>>> print_mult_table()
	1       2       3       4       5       6
	2       4       6       8       10      12
	3       6       9       12      15      18
	4       8       12      16      20      24
	5       10      15      20      25      30
	6       12      18      24      30      36



-------------------------------------------------------------------
yerel değişkenler
-------------------------------------------------------------------

- `i` değişkeni hem `print_multiples` hem de `print_mult_table` işlevinde

- aynı `i` değil

- çünkü işlevde yaratılan değişken ona yereldir

- dolayısıyla, `print_multiples:i` ve `print_mult_table:i` diyebiliriz

- işleve yerel dışarıdan erişmezsin!



-------------------------------------------------------------------
daha fazla genelleştirme
-------------------------------------------------------------------

- satır yüksekliğini değiştirmek istesek (PB:5082)

.. code-block:: python
	:linenos:

	>>> def print_mult_table(high):
	...     i = 1
	...     while i <= high:
	...         print_multiples(i)
	...         i += 1
	...

|

- çıktı

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print_mult_table(3)
	1       2       3       4       5       6
	2       4       6       8       10      12
	3       6       9       12      15      18
	>>> print_mult_table(5)
	1       2       3       4       5       6
	2       4       6       8       10      12
	3       6       9       12      15      18
	4       8       12      16      20      24
	5       10      15      20      25      30



-------------------------------------------------------------------
daha fazla genelleştirme
-------------------------------------------------------------------

- `high` parametresini `print_multiples` işlevine de aktaralım (PB:5083)

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> def print_multiples(n, high):
	...     i = 1
	...     while i <= high:
	...         print n*i, '\t',
	...         i += 1
	...     print

- `print_mult_table` değişmedi

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> def print_mult_table(high):
	...     i = 1
	...     while i <= high:
	...         print_multiples(i, high)
	...         i += 1

|

- çıktı

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print_mult_table(3)
	1       2       3
	2       4       6
	3       6       9
	>>> print_mult_table(5)
	1       2       3       4       5
	2       4       6       8       10
	3       6       9       12      15
	4       8       12      16      20
	5       10      15      20      25



-------------------------------------------------------------------
daha fazla genelleştirme
-------------------------------------------------------------------

- `print_mult_table` işlevindeki `print_multiples` çağrısında

.. code-block:: python
	:linenos:
	
	print_multiples(i, high)

- yerine 

.. code-block:: python
	:linenos:
	
	print_multiples(i, i)

- dersek, ekran çıktısı

.. code-block:: python
	:linenos:
	:size: Tiny

	>>> print_mult_table(3)
	1
	2       4
	3       6       9
	>>> print_mult_table(5)
	1
	2       4
	3       6       9
	4       8       12      16
	5       10      15      20      25




-------------------------------------------------------------------
neden işlev
-------------------------------------------------------------------

1. # Bir cümle dizisine bir isim vermeniz programınızın okunabilirliğini arttıracak, hata ayıklamayı kolaylaştıracaktır.

2. Büyük bir programı fonksiyonlara parçalamanız, programda parçaları birbirinden ayırmanızı sağlayacaktır. Böylece izole bir şekilde hataları ayıklayabilecek, bu farklı parçaların bir bütün olarak davranmasını sağlayabileceksiniz.

3. Fonksiyonlar yinelemenin kullanımını kolaylaştırır.

4. İyi tasarlanmış fonksiyonlar, yazılıp iyi bir şekilde hatalardan arındırıldıktan sonra tekrar kullanılabildiği için, bir çok program için yararlıdır.


-------------------------------------------------------------------
newton karekök
-------------------------------------------------------------------

- newton yöntemi(PB:5084)

.. code-block:: python
	:linenos:

	>>> def sqrt(n):
	...     approx = n/2.0
	...     better = (approx + n/approx)/2.0
	...     while better != approx:
	...         approx = better
	...         better = (approx + n/approx)/2.0
	...     return approx
	...
	>>> sqrt(25)
	5.0
	>>> sqrt(24)
	4.8989794855663558



-------------------------------------------------------------------
fibonacci serisi
-------------------------------------------------------------------

- fibonacci sayıları

.. code-block:: python
	:linenos:

	>>> a, b = 0, 1
	>>> while b < 1000:
	...     print b,
	...     a, b = b, a+b
	...
	1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987



-------------------------------------------------------------------
sıra sizde
-------------------------------------------------------------------

- `sqrt` işlevindeki `better` değişkenini yineleme numarasıyla ekranda gösterin

- üçgensel sayılar

.. code-block:: python
	:linenos:

	def print_triangular_numbers(n):
		"""\
			>>> print_triangular_numbers(5)
			1       1
			2       3
			3       6
			4       10
			5       15
		"""







### Döngü

> ![döngü](media/dongu.jpg)


### Döngü deyimi

- bilgisayarın en iyi yapabildiği şey: belirli bir işi tekrar etmek
    + sıkılmadan tekrarlayabiliyor
    + üstelik çok hızlı
    + ve her tekrarı öncekiyle aynı doğrulukta yapabiliyor
    + ona verdiğiniz talimatlar (program) ne kadar doğru ise!

- programlamanın en temel ögeleri: "döngü deyimleri"
    + bileşik bir deyim
    + bileşenler: döngü koşul ifadesi ve döngü öbeğindeki (tekrarlanan)
      deyimler


### Örnek - çorap giy (döngü yok)

- çorap giy
\lstset{language=[Turkish]Python}

            çorap çiftini bul
            çorap giy # ilk çorap
            çorap giy # ikinci çorap

- tekrarlanan deyim: '`çorap giy`'


### Örnek - çorap giy (döngü var)

- çorap giy
\lstset{language=[Turkish]Python}

            çorap çiftini bul

            ayaklardaki_çoraplar = 0
            ayaklardaki_çoraplar < 2 oldukça
                çorap giy
                ayaklardaki_çoraplar += 1

- döngü jargonu:
    + ne veya neler tekrarlanıyor?  "döngü öbeği"

            	çorap giy
            	ayaklardaki_çoraplar += 1

    + döngü ömrü hangi değişkenle denetleniyor?  "döngü değişkeni"

            	ayaklardaki_çoraplar

    + döngü nasıl duracak?  "döngü koşulu" **sağlanmadığında**

            	ayaklardaki_çoraplar < 2


### `while`

- '`while`'
\lstset{language=Python}

            ayaklardaki_coraplar = 0
            while ayaklardaki_coraplar < 2:
                corap_giy()
                ayaklardaki_coraplar += 1
- artık _sözde_ kod değil _gerçek_ kod yazıyoruz
    + (her zaman hatırlattığımız gibi) Türkçe karakter kullanmıyoruz
    + "çorap giy" yok!  bunun yerine "çorap giy" eylemini gerçekleştiren bir
      "`corap_giy`" yordamı var


### Örnek - ardışık toplamı

`1`'den `n`'e kadar sayıların toplamı

--

#### Türkçe

\lstset{language=[Turkish]Python}

            n = oku("Sınır? ")

            toplam = 0
            n > 0 oldukça
                toplam += n
                n -= 1

            yaz toplam

|

#### Python

\lstset{language=Python}

            n = input("Sınır? ")

            toplam = 0
            while n > 0:
                toplam += n
                n -= 1

            print toplam


### Örnek - ardışık toplam: seçenekler


#### Seçenek 1

\lstset{language=Python}

            n = input("Sınır? ")


            toplam = 0
            while n > 0:
                toplam += n
                n -= 1

            print toplam

|

#### Seçenek 2

\lstset{language=Python}

            n = input("Sınır? ")
            aralik = range(1, n+1)

            toplam = 0
            while aralik:
                toplam += aralik[n]
                n -= 1

            print toplam


### Örnek - rastgele toplam

rastgele girilen sayıların toplamı (`0` ile girdi sonlanıyor)

--

#### Türkçe

\lstset{language=[Turkish]Python}

            toplam = 0
            Doğru oldukça
                n = oku("Sayı? ")

                eğer n == 0
            	    kes

                toplam += n

            yaz toplam

|

#### Python

\lstset{language=Python}

            toplam = 0
            while True:
                n = input("Sayı? ")

                if not n:
            	    break

                toplam += n

            print toplam


### '`break`'

- döngüyü **zorla** sonlandırma olanağı sunuyor

- gereksiz yere kullanılmamalı, çok **doğal** olmayan bir örnek
\lstset{language=Python}

            n = input("Sınır? ")
            toplam = 0
            while True:
                if n <= 0:
            	    break

                toplam += n
                n -= 1

            print "Toplam:", toplam
- burada bir "örüntü" var
    + sonsuz döngüye gir, '`break`' ile '`kes`'
    + fakat bırakın döngü doğal şekilde aksın


### '`break`' nereye düşürür?

- '`break`' deyimi hangi noktada döngüyü keser?
    + yürütüldüğü noktada
    + fakat (sözdizimsel bağlam içindeki) değişkenler önceden aldıkları
      değerleri koruyor

- '`break`' döngüyü kesip sizi fırlattığında nereye düşerseniz?
    + döngüden sonraki ilk deyime
    + fakat (sözdizimsel bağlam içindeki) değişkenler önceden aldıkları
      değerleri koruyor


### '`continue`'?

- "döngüyü **kesme**; buradan çıkmak istemiyorum, ama lütfen bir sonraki turla
  **devam** etmeyi sınayalım"
    + sınamak?  sınanan ne?  döngü koşulu


### Örnek - rastgele toplam

#### Türkçe

\lstset{language=[Turkish]Python}

            toplam = 0
            tamam = Yanlış
            tamam olmadıkça
                n = oku("Sayı? ")

                eğer n < 0
            	    devam
                değilse eğer n > 0
            	    toplam += n
                değilse
            	    tamam = Doğru

            yaz toplam

|

#### Python

\lstset{language=Python}

            toplam = 0
            tamam = False
            while not tamam:
                n = input("Sayı? ")

                if n < 0:
            	    continue
                elif n > 0:
            	    toplam += n
                else
            	    tamam = True

            print toplam


### '`continue`' nereye düşürür?

- '`break`'de olduğu gibi döngünün dışına **değil**, döngü koşuluna
    + döngü koşulu nerede?
    + '`while`' döngüsünde başta


### Örnek - ardışık toplam

`1`'den `n`'e kadar sayıların toplamı

--

#### Türkçe

\lstset{language=[Turkish]Python}

            n = oku("Sınır? ")
            
            toplam = 0
            n > 0 oldukça
                toplam += n
                n -= 1
            
            yaz toplam

|

#### Python

\lstset{language=Python}

            n = input("Sınır? ")
            
            toplam = 0
            while n > 0:
                toplam += n
                n -= 1
            
            print toplam


### Örnek - en büyük, en küçük

\lstset{language=Python}

            print "Sayı girin [-1 son]."
            
            enbuyuk = enkucuk = girdi = input("> ")
            while girdi != -1:
                if girdi < enkucuk:
                    enkucuk = girdi
                if girdi > enbuyuk:
                    enbuyuk = girdi
                girdi = input("> ")
            
            print "En küçük girdi", enkucuk
            print "En büyük girdi", enbuyuk


### Örnek - en büyük, en küçük

\lstset{language=Python}

            print "Sayı girin [sonlandırmak için None]."
            
            enbuyuk = enkucuk = girdi = input("> ")
            while girdi != None:
                if girdi < enkucuk:
                    enkucuk = girdi
                if girdi > enbuyuk:
                    enbuyuk = girdi
                girdi = input("> ")
            
            print "En küçük girdi", enkucuk
            print "En büyük girdi", enbuyuk


### Örnek - en büyük, en küçük

\lstset{language=Python}


            # Bitiş simgesini (sentinel) kullanıcı belirlesin.
            bitir = input("Bitiş simgesi? ")
            
            print "Sayı girin."
            
            enbuyuk = enkucuk = girdi = input("> ")
            while girdi != bitir:
                if girdi < enkucuk:
                    enkucuk = girdi
                if girdi > enbuyuk:
                    enbuyuk = girdi
                girdi = input("> ")
            
            print "En küçük girdi", enkucuk
            print "En büyük girdi", enbuyuk


### Örnek - tam kare (kötü)

\lstset{language=Python}

            from math import sqrt
            
            N = input("Sınır? ")
            
            i = N
            while i > 0:
                kok = sqrt(i)
                ikok = int(kok)
                if not kok - ikok:
                    print i, ikok
                i -= 1


### Algoritma fikri

- etimoloji, El-Harizmi (Al-Khwarizmi), "Hint Rakamlarıyla Hesaplama" isimli
  eseri Latinceye çevriliyor
- müellifin ismi Latinceye "Algoritmi" olarak aktarılmış
- "hesap yöntemi" anlamında, resmî bir tanımı yok
- belirli bir problemin, işlem kaynaklarını (zaman ve/veya bellek) en etkin
  kullanacak şekilde, sonlu sayıda adımda çözülmesi
- algoritmada gerçekleme ayrıntıları üzerinde durulmaz, çoğunlukla sözde kodla
  ifade edilir


### Örnek - tam kare

\lstset{language=Python}

            N = input("Sınır? ")
            
            kare = i = 1
            
            while kare <= N:
                print i, kare
                i += 1
                kare = i*i


### Örnek - 2 tabanında logaritma (yaklaşık)

- basit bir yöntem
    + problemi çözme yönünde (yetersiz) bir girişim
- bu algoritmayı nasıl geliştirebilirsiniz?
    + 1'den küçük sayılar?

\lstset{language=Python}

            x = sayi = input("Sayı? ")

            logaritma = -1
            while x > 0:
                x //= 2
                logaritma += 1

            print "log2(%f) yaklaşık %f" %(sayi, logaritma)


### Örnek - 2 tabanında logaritma (yaklaşık)

\lstset{language=Python}

            x = sayi = input("Sayı? ")
            
            if x <= 0:
                print "Sayı pozitif olmalı!"
            else:
                negatifmi = False
                if x < 1:
                    negatifmi = True
                    x = 1/x
            
                logaritma = -1
                while x > 0:
                    x //= 2
                    logaritma += 1
            
                if negatifmi: logaritma = -logaritma
                print "log2(%f) yaklaşık %f" %(sayi, logaritma)


### Newton-Raphson algoritması

![newton-raphson](media/nr.png)


### Örnek - karekök

\lstset{language=Python}

            sayi = input("Sayı? ")
            sayi = abs(sayi)
            
            tol = 1e-9
            yeni, eski, tekrar = sayi/2.0, 0.0, 0
            
            while abs(yeni - eski) > tol:
                tekrar += 1
            
                eski = yeni
                yeni = (yeni*yeni + sayi)/(2*yeni)
            
            print "%.4f sayısının karekökü %.4f [%i tekrar]" \
                  %(sayi, yeni, tekrar)


### Örnek - tam kare - `kes` deyimi

\lstset{language=Python}

            N = input("Sınır? ")
            
            i = 1
            while 1:
                kare = i*i
                if kare > N:
                    break
                print i, kare
                i += 1


### Örnek - karekök - `kes` deyimi

\lstset{language=Python}

            sayi = input("Sayı? ")
            sayi = abs(sayi)
            
            tol = 1e-9
            yeni, eski, tekrar = sayi/2.0, 0.0, 0
            
            while 1:
                yeni = (yeni*yeni + sayi)/(2*yeni)

                if abs(yeni - eski) < tol:
                    break
            
                eski = yeni
                tekrar += 1
            
            print "%.4f sayısının karekökü %.4f [%i tekrar]" \
                  %(sayi, yeni, tekrar)


### Örnek - Ortak Bölenlerin En Büyüğü

- ortak bölenlerin en büyüğü
    + iki tamsayı var
    + her iki sayıyı da kalansız olarak bölen tamsayıların en büyüğünü bulmak
      istiyoruz
    + ör. 48, 20'nin '`obeb`'i 4


### Öklid algoritması - ortak bölenlerin en büyüğü

- Öklid algoritması
    + ortak bölenlerin en büyüğünü bulan bir algoritma
    + bilinen en eski algoritmalardan biri
    + Yunan Matematikçi Öklid'in (_Euclid_) "Elemanlar" isimli kitabında
      anlatılmış (M.Ö. 300)
    + algoritma Öklid'e atfedilmekle birlikte kendisinden çok daha önce
      bulunduğu tahmin ediliyor

- sözel anlatımı

>> "`m` ve `n` sayı çifti veriliyor; `n` eğer `0` ise cevap `m`, değilse aynı
>> işlemi **sırasıyla** `n` ve `m%n` çiftiyle tekrarla"


### Örnek - Ortak Bölenlerin En Büyüğü : hatalı gerçekleme

- **o**rtak **b**ölenlerin **e**n **b**üyüğü
\lstset{language=Python}

            n, m = input("n, m? ")
            while True:
                m %= n
                if m == 0:
                    print n
                    break
                n %= m
                if n == 0:
                    print m
                    break

- neden hatalı?
    + `n > m` ise ne oluyor?


### Örnek - Ortak Bölenlerin En Büyüğü : kötü gerçekleme

- **o**rtak **b**ölenlerin **e**n **b**üyüğü
\lstset{language=Python}

            n, m = input("n, m? ")
            if n > m:
                n, m = m, n
            while True:
                m %= n
                if m == 0:
                    print n
                    break
                n %= m
                if n == 0:
                    print m
                    break

- neden kötü?
    + '`n > m`' ise argümanlar yer değiştiriyor
    + fakat hatayı düzeltirken gerçeklemeyi çirkinleştirdik
    + hâlâ hata var: `n` veya her iki sayı da 0 ise ne oluyor?


### Örnek - Ortak Bölenlerin En Büyüğü : zarif gerçekleme

- **o**rtak **b**ölenlerin **e**n **b**üyüğü
\lstset{language=Python}

            n, m = input("n, m? ")
            while n: m, n = n, m%n
            print m

- neden zarif?
    + sayıların sırasından bağımsız
    + sıfır değerlerini de yönetebiliyor
    + hepsi üç satır!



### Örnek - rastgele toplam

\lstset{language=Python}

            print "Sayı girin [sonlandırmak için None]."
            
            adet, toplam = 0, 0
            girdi = input("> ")
            while girdi != None:
                adet += 1
                toplam += girdi
                girdi = input("> ")
            
            print "Toplam", toplam
            print "Adet", adet
            if adet:
                print "Ortalama", toplam/adet


### Örnek - rastgele toplam - `kes` deyimi

\lstset{language=Python}

            print "Sayı girin [sonlandırmak için None]."
            
            adet, toplam = 0, 0
            while 1:
                girdi = input("> ")
                if girdi == None:
                    break
                adet += 1
                toplam += girdi
            
            print "Toplam", toplam
            print "Adet", adet
            if adet:
                print "Ortalama", toplam/adet


### Örnek - puan

\lstset{language=Python}

            bitti = False
            while not bitti:
            	puan = input("Puan? ")
            	if puan < 0 or puan > 100:
                    print "Lütfen tekrar deneyin!"
            	    continue
            	if   puan < 50: print "Üzgünüm, kaldınız!"
            	elif puan < 60: print "DC: orta"
            	elif puan < 70: print "CC: orta"
            	elif puan < 75: print "CB: iyi"
            	elif puan < 85: print "BB: iyi"
            	elif puan < 90: print "BA: pekiyi"
            	else:           print "AA: pekiyi"

            	cevap = raw_input("Devam? [h]ayır ")
            	bitti = cevap and cevap in "hH"


### Örnek - parola - `kes`

\lstset{language=Python}

            MIN   = 6
            
            while True:
                parola = raw_input("Parola? ")
                if len(parola) >= MIN:
                    onceki = parola
                    parola = raw_input("Parola tekrar? ")
                    if parola == onceki:
                        print "Parolanız başarıyla kaydedildi!"
                        break
                    print "Tutarsız parola!  Tekrar girin."
                else:
                    print "En az %i karakter olmalı." % MIN


### Örnek - parola - `kes/devam`

\lstset{language=Python}

            MIN   = 6
 
            while True:
                parola = raw_input("Parola? ")
                if len(parola) < MIN:
                    print "En az %i karakter olmalı." % MIN
                    continue
            
                onceki = parola
                parola = raw_input("Parola tekrar? ")
                if parola != onceki:
                    print "Tutarsız parola!  Tekrar girin."
                    continue
            
                print "Parolanız başarıyla kaydedildi!"
                break


### Örnek - parola - bayrak kullanarak

\lstset{language=Python}

            MIN   = 6
            
            bitti = False
            while not bitti:
                parola = raw_input("Parola? ")
                if len(parola) >= MIN:
                    onceki = parola
                    parola = raw_input("Parola tekrar? ")
                    if parola == onceki:
                        print "Parolanız başarıyla kaydedildi!"
                        bitti = True
                    else:
                        print "Tutarsız parola!  Tekrar girin."
                else:
                    print "En az %i karakter olmalı." % MIN


### Örnek - onayla

\lstset{language=Python}

            PAROLA = "gizli"
            KERE   = 3
            
            kere = KERE
            while kere > 0:
                parola = raw_input("Parola? ")
                if parola == PAROLA:
                    print "Parola geçerli!"
                    break
                else:
                    print "Geçersiz parola!  Tekrar deneyin."
                kere -= 1
            else:
                print KERE, "başarısız deneme!"
                print "Hesabınız kilitlendi!"




### TODO


- while ve for sonunda else

- dolaşırken yapılan değişiklikler için önlem

  for x in a[:]:
      if x < 0: a.remove(x)

- for ile yapılan aslında dizilimlerde dolaşmak, bunu vurgula

- algoritma fikri?


            x = input("Sayı? ")
            count = 1
            while x > 0:
                x //= 2
                count += 1
            print "log2 yaklaşık olarak", count

def menu():
    print "1. Toplama"
    print "2. Cikartma"
    print "3. Carpma"
    print "4. Bolme"
    print "Lutfen seciminizi yapiniz (1..4)"


# main
x = input("Ilk isleneni giriniz: ")
y = input("Ikinci isleneni giriniz: ")

menu()
secim = input()

if   secim == 1:
    sonuc = x + y
elif secim == 2:
    sonuc = x - y
elif secim == 3:
    sonuc = x * y
elif secim == 4:
    sonuc = x / y
else:
    print "yok boyle bir secenek"

print "Sonuc = ", sonuc
    

import urllib2

page = urllib2.urlopen("http://dip.bil.omu.edu.tr/a/piton")
text = page.read().decode("utf8")

kb = text.find("kur")
sb = text.find("=", kb) + 1
ss = text.find("<", sb)
kur = float(text[sb:ss])

print "kur=", kur

if kur < 1.4:
        print "Dolar almanin tam zamani"
else:
        print "Beklemeye devam"

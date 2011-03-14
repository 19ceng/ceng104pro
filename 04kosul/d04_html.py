#d04_html.py

import urllib.request

page = urllib.request.urlopen("http://kil.bil.omu.edu.tr")
text = page.read().decode("utf8")

dizgi = text[100:150]
print dizgi

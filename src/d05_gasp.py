from gasp import *

def dikdortgen(x1, y1, x2, y2):
	Line((x1, y1), (x2, y1))
	Line((x2, y1), (x2, y2))
	Line((x2, y2), (x1, y2))
	Line((x1, y2), (x1, y1))

def dikdortgen2(x, y, w, h):
	dikdortgen(x, y, x + w, y + h)

def kare(x, y, a):
	dikdortgen2(x, y, a, a)

# main
begin_graphics()

dikdortgen(50, 50, 150, 200)

#end_graphics()

import Image

im = Image.open("GvR.jpg")
W, H = im.size			# genislik, yukseklik
r, g, b = im.split()	# RGB split
# point erisimi
pr, pg, pb = r.load(), g.load(),  b.load()

# isleme
for x in range(W):
	for y in range(H):
		if pr[x, y] < 128:
			pr[x, y] = 0
		else:
			pr[x, y] = 255

		pg[x, y] = 255 - pg[x, y]
		pb[x, y] = pb[x, y] * 1.2

im2 = Image.merge("RGB", (r, g, b))
im2.rotate(45).show()

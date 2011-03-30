def topla(x, y):
	return x + y

def cikar(x, y):
	return x - y

islem = {'+':topla, '-':cikar}
x, y = 3, 4
islec = '+'
fn = islem[islec]
print fn(x, y)


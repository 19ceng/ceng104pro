def tahminator():
	num = 23 # random(0, 50)
	guess = input("bir sayi girin: ")
	
	if guess == num:
		print "bildiniz"
	else if guess < num:
		print "daha buyuk bir sayi soyleseydiniz belki de bulaaktiniz"
	else:
		print "daha kucuk bir sayi soyleseydiniz belki de bulaaktiniz"

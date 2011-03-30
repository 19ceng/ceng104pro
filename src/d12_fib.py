onceki = {0: 0, 1: 1}
   
def fibonacci(n):
    if onceki.has_key(n):
        return onceki[n]
    else:
        yeni_deger = fibonacci(n-1) + fibonacci(n-2)
        onceki[n] = yeni_deger
        return yeni_deger


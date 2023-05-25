#бинарное представление
n = 13
l = list()
def bin(n):
	if n >= 2:
		bin(n //2)
	m = n % 2
	l.append(m)

bin(n)
l = ''.join(map(str, l))
print(f'{n} в бинарном представлении {l}')




#умножение
n = 10
m = 5

def multiplication(n, m):
	if n ==0:
		return 0
	elif n == 1:
		return m
	else:
		return m + multiplication(n-1, m)
		
mult = multiplication(n, m)
print(f'{m} умножить на {n} = {mult}')


#возведение в степень
n = 3
m = 5

def degree(n, m):
	if n ==0:
		return 1
	elif n == 1:
		return m
	else:
		return m * degree(n-1, m)
		
deg = degree(n, m)
print(f'{m} в {n} степени = {deg}')
	
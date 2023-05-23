import random

n = 5000

arr  = list()
for i in range(n):
	number = random.randint(1, 100)
	arr.append(number)
	
print(f'Не отсортировано {arr}')
is_sort = True

for i in range(n):
	for j in range(n -i -1): #добавил - i чтобы не трогать отсортированные элементы
		l = arr[j]
		r = arr[j + 1]
		if l > r:
			is_sort = False
			arr[j], arr[j + 1] = r, l
#	print(arr)
	if is_sort is True:
	       break #остановил цикл в случак отсутствия перестоновок
	else:
		is_sort = True			
print(f'Отсортирован {arr}')
print('end')

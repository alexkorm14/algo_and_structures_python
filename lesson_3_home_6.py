import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

LEN_ROW = int(input('Введите длину последовательности - ',))
BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))
ROW = spisok(LEN_ROW,BEGIN_DIAPOSON,END_DIAPOSON)
print(ROW)
print()

MAX_NUMB = ROW[0]
MIN_NUMB = ROW[0]
INDEX_MAX = 0
INDEX_MIN = 0
for i in range(len(ROW)):
	 if ROW[i]>MAX_NUMB:
	 	MAX_NUMB = ROW[i]
	 	INDEX_MAX = i
	 if ROW[i]<MIN_NUMB:
	 	MIN_NUMB = ROW[i]
	 	INDEX_MIN = i

print(f'Максимальный элемент - {MAX_NUMB} с индексом {INDEX_MAX}')
print(f'Минимальный элемент - {MIN_NUMB} с индексом {INDEX_MIN}')
if INDEX_MAX>INDEX_MIN:
	row_sum = 0
	for j in range(INDEX_MIN+1,INDEX_MAX):
		row_sum+=ROW[j]
	print(f'Сумма между максимальным и минимальным элементом - {row_sum}')
else:
	row_sum = 0
	for j in range(INDEX_MAX+1,INDEX_MIN):
		row_sum+=ROW[j]
	print(f'Сумма между максимальным и минимальным элементом - {row_sum}')









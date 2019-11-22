import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.


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
ROW[INDEX_MAX],ROW[INDEX_MIN] = ROW[INDEX_MIN], ROW[INDEX_MAX]
print()
print(ROW)

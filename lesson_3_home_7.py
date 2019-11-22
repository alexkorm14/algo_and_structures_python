import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

LEN_ROW = int(input('Введите длину последовательности - ',))
BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))
ROW = spisok(LEN_ROW,BEGIN_DIAPOSON,END_DIAPOSON)
print(ROW)
print()

MIN_NUMB = ROW[0]
INDEX_MIN = 0
for i in range(len(ROW)):
	 if ROW[i]<MIN_NUMB:
	 	MIN_NUMB = ROW[i]
	 	INDEX_MIN = i

COPY_NUMB_ROW = ROW
COPY_NUMB_ROW.remove(MIN_NUMB)


SECOND_MIN_NUNB = COPY_NUMB_ROW[0]
for i in range(len(COPY_NUMB_ROW)):
	 if COPY_NUMB_ROW[i]<=SECOND_MIN_NUNB:
	 	SECOND_MIN_NUNB = COPY_NUMB_ROW[i]
	 	
	
print(f'Минимальные числа: {MIN_NUMB} и {SECOND_MIN_NUNB}')

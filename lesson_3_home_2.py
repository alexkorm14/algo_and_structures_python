import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

''' задание 2 - Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, 
 то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
 т.к. именно в этих позициях первого массива стоят четные числа.'''
LEN_ROW = int(input('Введите длину последовательности - ',))
BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))
ROW = spisok(LEN_ROW,BEGIN_DIAPOSON,END_DIAPOSON)
RESULT =[]
for i in range(len(ROW)):
	if ROW[i]%2 == 0:
		RESULT.append(i+1)
print('первоначальный список',ROW)
print('Список позиций четных элементов',RESULT)


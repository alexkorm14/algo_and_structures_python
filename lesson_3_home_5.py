import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.


LEN_ROW = int(input('Введите длину последовательности - ',))
BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))
ROW = spisok(LEN_ROW,BEGIN_DIAPOSON,END_DIAPOSON)
print(ROW)
print()


NEGOTIVE_NUMBS = []
for i in range(len(ROW)):
	if ROW[i]<0:
		negative_numb = ROW[i]
		NEGOTIVE_NUMBS.append((negative_numb,i))

if len(NEGOTIVE_NUMBS)>0:
	max_numb = NEGOTIVE_NUMBS[0][0]
	number = NEGOTIVE_NUMBS[0][1]
	for i in range(len(NEGOTIVE_NUMBS)):
	 	if NEGOTIVE_NUMBS[i][0]>max_numb:
	 		max_numb = NEGOTIVE_NUMBS[i][0]
	 		number = NEGOTIVE_NUMBS[i][1]
	print(f'Максимальное значение к 0 число {max_numb} под индексом - {number}')
else:
    print('Нет отрицательных чисел')

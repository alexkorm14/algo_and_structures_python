import random
def spisok(len_row, begin, end):
	a = []
	for i in range(len_row):
		a.append(random.randint(begin,end))
	return a 

#4. Определить, какое число в массиве встречается чаще всего.

LEN_ROW = int(input('Введите длину последовательности - ',))
BEGIN_DIAPOSON = int(input('Введите начало диапозона - ',))
END_DIAPOSON = int(input('Введите конец диапозона - ',))
ROW = spisok(LEN_ROW,BEGIN_DIAPOSON,END_DIAPOSON)
print(ROW)
print()

COUNT = []
for i in range(len(ROW)):
	count_i = 0
	for j in range(len(ROW)):
		if ROW[i] == ROW[j]:
			count_i+=1
	COUNT.append((count_i,ROW[i],i))

RESULT = []
MAX_COUNR = COUNT[0][0]
POPULAR_NUMB = 0
for j in range(len(COUNT)):
	if COUNT[j][0]>=MAX_COUNR:
		MAX_COUNR = COUNT[j][0]
		POPULAR_NUMB = COUNT[j][1]
print(f'Чаще всего встречается число {POPULAR_NUMB}: {MAX_COUNR} раз(а) ')

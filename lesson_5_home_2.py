'''
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

'''

NUMB_1 = str(input('Введите первое число в шестнадцатеричной системе исчисления - ')) 
NUMB_2 = str(input('Введите второе число в шестнадцатеричной системе исчисления - ')) 

CHART_NUMERATE = {
	'1': 1,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'A': 10,
	'B': 11,
	'C': 12,
	'D': 13,
	'E': 14,
	'F': 15
	
	}
def searh_for_key(dict, value):
		lst = list(dict.items())
		for i in range(len(lst)):
			if str(lst[i][1]) == str(value):
				result = str(lst[i][0])
		return result
def proverka(numb):
	for i in range(len(numb)):
		if numb[i].upper() not in CHART_NUMERATE or numb[i] == ' ':
			return False
		else:
			return True

def perevod_16_in_10(numb):
	
	numb = [numb[i] for i in range(len(numb))]
	result_numb = 0
	j = len(numb) - 1
	for i in range(len(numb)):
		numb[i] = CHART_NUMERATE[numb[i].upper()]*(16**j)
		j-=1
		result_numb+=numb[i]
	return result_numb 

def perevod_10_in_16(numb):
	if numb in (1,2,3,4,5,6,7,8,9):
		return numb
	elif numb in (10,11,12,13,14,15):
		return searh_for_key(CHART_NUMERATE,numb)
	else:
		result_numb = []
		while numb > 1:
			result = searh_for_key(CHART_NUMERATE, numb%16)
			result_numb.append(result)
			numb//=16
		result_numb = ''.join(result_numb)
		result_numb = result_numb[::-1]
		return result_numb


if proverka(NUMB_1) and proverka(NUMB_2):
	sum_numbs = perevod_16_in_10(NUMB_1) + perevod_16_in_10(NUMB_2)
	multiply_numbs = perevod_16_in_10(NUMB_1) * perevod_16_in_10(NUMB_2)
	print(sum_numbs)
	print(multiply_numbs)




	print(perevod_10_in_16(sum_numbs))
	print(perevod_10_in_16(multiply_numbs))

	

	
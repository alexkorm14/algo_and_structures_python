import collections
'''
1. Пользователь вводит данные 
о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, 
чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''
 
QUANTITY_OF_FIRMS = int(input('Введите количесво предприятий - ',))
FIRMS = []
ALL_PROFIT = 0
for i in range(QUANTITY_OF_FIRMS):
	name_firm = str(input('Введите название фирмы - ',))
	profit_1 = float(input('Прибыль за 1 квартал - ', ))
	profit_2 = float(input('Прибыль за 2 квартал - ', ))
	profit_3 = float(input('Прибыль за 3 квартал - ', ))
	profit_4 = float(input('Прибыль за 4 квартал - ', ))
	profit = profit_1 + profit_2 + profit_3 + profit_4
	FIRMS.append((name_firm,profit))
	ALL_PROFIT += profit
print(FIRMS)
print(ALL_PROFIT)
AVARAGE_PROFIT = ALL_PROFIT/QUANTITY_OF_FIRMS
print(AVARAGE_PROFIT)
upper_avarage_profit = []
under_avarage_profit = []
for i in range(len(FIRMS)):
	if FIRMS[i][1] > AVARAGE_PROFIT:
		upper_avarage_profit.append(FIRMS[i][0])
	else:
		under_avarage_profit.append(FIRMS[i][0])


print(f'Список фирм с прибылью выше среднего - {upper_avarage_profit}')
print(f'Список фирм с прибылью ниже среднего - {under_avarage_profit}')


























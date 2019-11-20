"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
import sys
def action_with_numbers(numb_1,numb_2,operation):
	if operation=='-':
		result = numb_1 - numb_2
		print ('действие выполнено')
		print(result)
	elif operation=='+':
		result = numb_1 + numb_2
		print ('действие выполнено')
		return result
	elif operation=='*':
		result = numb_1*numb_2
		print ('действие выполнено')
		print(result)
	elif operation=='/' and numb_2!=0:
		result = numb_1/numb_2
		print ('действие выполнено')
		print(result)
	elif operation=='/' and numb_2==0:
		print('На 0 делить нельзя')
		operation = str(input('Введите нужный знак действия: *, /, +, -, 0 - завершение ', ))
		result = action_with_numbers(numb_1,numb_2,operation)
		print(result)
	elif operation=='0':
		sys.exit(1)
	else:
		print ('Вы ввели неверный знак')
		operation = str(input('Введите нужный знак действия: *, /, +, -, 0 - завершение ', ))
		result = action_with_numbers(numb_1,numb_2,operation)
		print(result)

NUMB_1 = float(input('Введите число - ', ))
NUMB_2 = float(input('Введите число - ', ))
operation = str(input('Введите нужный знак действия: *, /, +, -, 0 - завершение ', )) 
while operation!='0':
	print(action_with_numbers(NUMB_1,NUMB_2,operation))
#
	operation = str(input('Введите нужный знак действия: *, /, +, -, 0 - завершение ', ))




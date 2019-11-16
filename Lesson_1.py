import sys
from random import random



LETTER_1 = ord(input('Введите случайную букву на латинском строчную - ', ))
LETTER_2 = ord(input('Введите случайную букву на латинском строчную - ', ))
if LETTER_1<LETTER_2 and LETTER_1!=LETTER_2:
	RANDOM_LETTER = int(random()*(LETTER_2 - LETTER_1+1)) + LETTER_1
	print ('Случайная буква в вашем диапозоне - ', chr(RANDOM_LETTER))
elif LETTER_1>LETTER_2 and LETTER_1!=LETTER_2:
	RANDOM_LETTER = int(random()*(LETTER_1 - LETTER_2+1)) + LETTER_2
	print ('Случайная буква в вашем диапозоне - ', chr(RANDOM_LETTER))
else:
	print('Нет случайной буквы между промежутками')
	sys.exit(1)


#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

NUMB = int(input('Введите трехзначное число: ',))
if len(NUMB)==3:
	NUMB_1=NUMB//100
	NUMB_3=NUMB%10
	NUMB_2=(NUMB//10)%10

	NUMB_COMPOSITION = NUMB_1*NUMB_2*NUMB_3
	NUMB_SUM = NUMB_1+NUMB_2+NUMB_3
	print ('Сумма всех цифр', NUMB_SUM)
	print ('Произведение всех цифр', NUMB_COMPOSITION)
else:
	print ('Введите ТРЕХЗНАЧНОЕ ЧИСЛО')
	sys.exit(1)


#2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.
a = 5
print("%d = %s" % (a, bin(a)))
b = 6
print("%d = %s" % (b, bin(b)))
 
print("%d & %d = %d (%s)" % (a,b,a&b,bin(a&b)))
print("%d | %d = %d (%s)" % (a,b,a|b,bin(a|b)))
print("%d ^ %d = %d (%s)" % (a,b,a^b,bin(a^b)))
print("%d << 2 = %d (%s)" % (b,b<<2,bin(b<<2)))
print("%d >> 2 = %d (%s)" % (b,b>>2,bin(b>>2)))

# 3.	По введенным пользователем координатам двух точек вывести
# уравнение прямой вида y = kx + b, проходящей через эти точки.
X_1 = int(input('Введите координату х1: ',))
Y_1 = int(input('Введите координату y1: ',))
X_2 = int(input('Введите координату х2: ',))
Y_2 = int(input('Введите координату y2: ',))
if X_1!=X_2:
	k = (Y_1 - Y_2)/(X_1 - X_2)
	b = Y_1 - k*X_1
	b_1 = Y_2 - k*X_2 
	print (b_1 - b)
	if b>=0:
		print (f'Уравнение прямой y = {k}x + {b}')
	else:
		print (f'Уравнение прямой y = {k}x {b}')
else:
	print ('X не может принимать одинаковые значения')



"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

NUMB_1 = int(input('Введите случайное целое число - ', ))
NUMB_2 = int(input('Введите случайное целое число - ', ))
if NUMB_1<NUMB_2 and NUMB_1!=NUMB_2:
	RANDOM_NUMB = int(random()*(NUMB_2 - NUMB_1+1)) + NUMB_1
	print ('Случайное число в вашем диапозоне - ', RANDOM_NUMB)
elif NUMB_1>NUMB_2 and NUMB_1!=NUMB_2:
	RANDOM_NUMB = int(random()*(NUMB_1 - NUMB_2+1)) + NUMB_2
	print ('Случайное число в вашем диапозоне - ', RANDOM_NUMB)
else:
	print('Нет случайного числа между промежутками')
	sys.exit(1)


NUMB_1 = float(input('Введите случайное вещественное число - ', ))
NUMB_2 = float(input('Введите случайное вещественное число - ', ))
if NUMB_1<NUMB_2 and NUMB_1!=NUMB_2:
	RANDOM_NUMB = float(random()*(NUMB_2 - NUMB_1+1)) + NUMB_1
	print ('Случайное число в вашем диапозоне - ', round(RANDOM_NUMB,2))
elif NUMB_1>NUMB_2 and NUMB_1!=NUMB_2:
	RANDOM_NUMB = float(random()*(NUMB_1 - NUMB_2+1)) + NUMB_2
	print ('Случайное число в вашем диапозоне - ', round(RANDOM_NUMB,2))
else:
	print('Нет случайного числа между промежутками')
	sys.exit(1)



#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.
LETTER_1 = str(input('Введите букву: ',))
LETTER_2 = str(input('Введите букву: ',))

LETTER_1_IN_BYTES = LETTER_1.encode('utf-8')
LETTER_2_IN_BYTES = LETTER_2.encode('utf-8')
LETTER_1_IN_BYTES = bytearray(LETTER_1_IN_BYTES)
LETTER_2_IN_BYTES = bytearray(LETTER_2_IN_BYTES)
print (f'место буквы 1 ({LETTER_1}) - {int(LETTER_1_IN_BYTES[0])-96}') 
# только если буквы строчные, так как они начинаются с 97 - это способ просто раньше придумал, а потом искал аналог chr() и нашел ord()
print (f'место буквы 2 ({LETTER_2}) - {int(LETTER_2_IN_BYTES[0])-96}')
LEN_BETWEEN_LETTERS = LETTER_1_IN_BYTES[0] - LETTER_2_IN_BYTES[0] - 1 
if LEN_BETWEEN_LETTERS>0:
	print (f'Длина между буквами = {LEN_BETWEEN_LETTERS}')
else:
	print (f'Длина между буквами = {-(LEN_BETWEEN_LETTERS)}')
# через ord
LETTER_1_IN_BYTES = ord(LETTER_1)
LETTER_2_IN_BYTES = ord(LETTER_2)
LEN_BETWEEN_LETTERS = LETTER_1_IN_BYTES - LETTER_2_IN_BYTES - 1 
if LEN_BETWEEN_LETTERS>0:
	print (f'Длина между буквами = {LEN_BETWEEN_LETTERS}')
else:
	print (f'Длина между буквами = {-(LEN_BETWEEN_LETTERS)}')

# 6
NUMB_OF_LETTER = int(input('Введите номер буквы в алфавите - ',))
if 0< NUMB_OF_LETTER <27:
	print (chr(NUMB_OF_LETTER+96))
else:
	print('Не попал в нужный диапозон')


"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""
A = int(input('Введите длину отрезка 1: ',))
B = int(input('Введите длину отрезка 2: ',))
C = int(input('Введите длину отрезка 3: ',))

if A + B>C and A+C>B and B+C>A:
	print ('треугольник существует', end=', при этом ')
	if A!=B and A!=C and B!=C:
		print ('треугольник разносторонний')
	elif (A==B and A!=C) or (B==C and B!=A) or (A==C and A!=B):
		print ('треугольник равнобедренный') 
	elif A==B and A==C and B==C:
		print ('треугольник равносторонний')
else:
	print('треугольник не существует')


#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

YEAR = int(input('Введите год: ',))

if YEAR%4!=0 or (YEAR%4==0 and YEAR%100==0):
	print ('обычный год')
elif (YEAR%4==0 and YEAR%100!=0) or YEAR%400==0:
	print ('високосный год')


#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
NUMB_1 = int(input('Введите число 1: ',))
NUMB_2 = int(input('Введите число 2: ',))
NUMB_3 = int(input('Введите число 3: ',))

if NUMB_1>NUMB_2 and NUMB_1>NUMB_3:
	if NUMB_2>NUMB_3:
		print (NUMB_2, 'среднее число')
	else:
		print (NUMB_3, 'среднее число')
elif NUMB_2>NUMB_3 and NUMB_2>NUMB_1:
	if NUMB_1>NUMB_3:
		print (NUMB_1, 'среднее число')
	else:
		print (NUMB_3, 'среднее число')
elif NUMB_3>NUMB_2 and NUMB_3>NUMB_1:
	if NUMB_1>NUMB_2:
		print (NUMB_1, 'среднее число')
	else:
		print (NUMB_2, 'среднее число')






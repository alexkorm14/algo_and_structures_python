
"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

NUMB = int(input('Введите число - ', ))
def reverse_numb(numb):
	if (numb//10)==0:
		return int(numb)
	else:
		return str(numb%10)+str(reverse_numb(numb//10))
print(reverse_numb(NUMB))

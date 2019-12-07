import random


def sortirvka_pusir(lst):
	def proverka(lst):
		for i in range(len(lst)-1):
			if lst[i] < lst[i+1]:
				return False
		return True
	if proverka(lst) == True:
		return lst
	else:
		n = 1
		while n < len(lst):
			for i in range(len(lst)-n):
				if lst[i] < lst[i+1]:
					lst[i], lst[i+1] = lst[i+1], lst[i]
			n+=1
		return lst
print()


NUMBER = int(input('Введите длину последовательности - ',))
LST = [random.randint(-100,100) for i in range(NUMBER)]
print(LST)
print()
print(sortirvka_pusir(LST))


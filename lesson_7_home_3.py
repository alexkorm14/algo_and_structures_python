M = int(input('Введите число M ', ))
LST = [random.randint(-10,10) for i in range(2*M+1)]
print(LST)
'''
отсортируем массисв и найдем медиану для проверки
'''
sorted_lst = sorted(LST)
print(sorted_lst)

print(sorted_lst[len(sorted_lst)//2])
print()

print('----------')


def count(lst,numb, case):
	if case == '>':
		count = 0
		for i in range(len(lst)):
			if numb > lst[i]:
				count+=1
		result = count
		return result

	elif case == '<':
		count = 0
		for i in range(len(lst)):
			if numb < lst[i]:
				count+=1
		result = count
		return result
		
	elif case == '=':
		count = 0
		for i in range(len(lst)):
			if numb == lst[i]:
				count+=1
		result = count - 1 
		if result == 0:
			return 0  
		else:
			return result


for i in range(len(LST)):

	count_left = count(LST,LST[i],'>')		
	count_rigt = count(LST,LST[i],'<')
	count_repeat = count(LST,LST[i],'=')

	if count_repeat + count_rigt + count_left == len(LST) - 1:
		if count_left < len(LST)//2+1 and count_rigt < len(LST)//2+1:
			mediana = LST[i]
			

print(mediana)	

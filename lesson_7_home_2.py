
'''
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
заданный случайными числами на промежутке [0; 50). 
Выведите на экран исходный и отсортированный массивы.
'''
# я все скидываю на внешний жесткий диск чтобы место не заполнять место, поэтому решил проще готовой функцией воспользоваться 
def merge(left_lst, right_lst):
	sorted_lst = []
	left = 0
	right = 0

	for i in range(len(left_lst) + len(right_lst)):
		if left < len(left_lst) and right < len(right_lst):
			if left_lst[left] <= right_lst[right]:
				sorted_lst.append(left_lst[left])
				left+=1
			else: 
				sorted_lst.append(right_lst[right])
				right+=1
		elif left == len(left_lst):
			sorted_lst.append(right_lst[right])
			right+=1
		elif right == len(right_lst):	
			sorted_lst.append(left_lst[left])
			left+=1
				
	return sorted_lst
def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	mid = len(lst)//2
	left_lst = merge_sort(lst[:mid])
	right_lst = merge_sort(lst[mid:]) 
	return merge(left_lst, right_lst)
	


NUMBER = int(input('Введите длину последовательности - ',))
LST = [random.uniform(0,50) for i in range(NUMBER)]
print(LST)
print()
print(merge_sort(LST))


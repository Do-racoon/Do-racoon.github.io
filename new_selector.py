import random

def lotto(n):
	result = []
	for i in range(n):
		random_list = []
		for j in range(6):
			ran_num = random.randint(1,45)
			random_list.append(ran_num)
		result.append(random_list)
	return result

lotto_list = lotto(int(input("횟수를 입력하세요")))
print(lotto_list)

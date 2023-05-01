def change_words(str):
	sentence = ""
	for i in str:
		if ord(i) >= 65 and ord(i) <= 67:
			i = chr(ord(i) + 23)
			sentence += i
		elif ord(i) >= 97 and ord(i) <= 99:
			i = chr(ord(i) + 23)
			sentence += i
		elif ord(i) <= 65:
			sentence += i
		else :
			i = chr(ord(i) -3)
			sentence += i

	return sentence


print(change_words(input("문장을 적어보세요")))

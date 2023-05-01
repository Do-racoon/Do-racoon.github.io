def encode_words(str): ## 암호화 하는 코드
	sentence = ""
	for i in str:
		if ord(i) >= 65 and ord(i) <= 67: ## 소문자 abc 아스키코드일 때만 xyz로 바꿔줌
			i = chr(ord(i) + 23)
		elif ord(i) >= 97 and ord(i) <= 99: ## 대문자 ABC 아스키코드일 때만 XYZ로 바꿔줌
			i = chr(ord(i) + 23)
		elif ord(i) <= 64 or ord(i) >= 123: ## 띄어쓰기포함 특수문자는 패스 
			pass
		else :				## 나머지는 3칸씩 앞으로 당김
			i = chr(ord(i) -3)

		sentence += i
	return sentence

def decode_words(str):
	sentence = ""
	for i in str:
		if ord(i) >=120 and ord(i) <= 122: ## 소문자 xyz 아스키코드일 때만 abc로 바꿔줌
			i = chr(ord(i) - 23)
		elif ord(i) >= 88 and ord(i) <=90: ## 대문자 XYZ 아스키코드일 때만 ABC로 바꿔줌
			i = chr(ord(i) -23)
		elif ord(i) <= 64 or ord(i) >= 123:		## 띄어쓰기포함 특수문자는 패스
			pass
		else:				## 나머지는 3칸씩 뒤로 당김
			i = chr(ord(i) +3)
		sentence += i
	return sentence
def what_mode(mode, str):
	if mode == "decode":
		print(decode_words(str))
	elif mode == "encode":
		print(encode_words(str))
	else :
		print("sorry. we can't do that")
what_mode(input("모드를 선택하세요"),input("문장을 적어보세요"))

from deep_translator import GoogleTranslator

text1 = input("말하고 싶은 내용을 선택하여 입력하세요.\n길묻기\n식당 주문하기\n도움 요청\n가격 묻기\n고마움 표현\n기타: ")

if text1 == "길 묻기" :
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate("@@로 가려면 어떻게 가야 하나요?")
    print("번역 결과:", translated)

if text1 == "식당 주문하기" :
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate("@@ 부탁합니다.")
    print("번역 결과:", translated)

if text1 == "도움 요청" :
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate("실례합니다. 저 좀 도와주실래요?")
    print("번역 결과:", translated)

if text1 == "가격 묻기" :
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate("이거 얼마인가요?")
    print("번역 결과:", translated)

if text1 == "고마움 표현" :
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate("감사합니다!")
    print("번역 결과:", translated)


if text1== "기타" :
    text = input("번역할 문장을 입력하세요: ")
    lang = input("번역하고 싶은 언어 코드를 입력하세요. 예: 영어=en 포르투갈어=pt: ")
    translated = GoogleTranslator(source='ko', target=lang).translate(text)
    print("번역 결과:", translated)


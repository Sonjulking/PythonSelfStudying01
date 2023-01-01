web_address = input("웹사이트 주소를 입력해주세요. > ")

web_tag = web_address.split(".")

# kr = 한국, uk = 영국, com = 기업,  org = 기관, 그외는 알 수 없음

if web_tag[-1] == "kr":
    print("한국")
elif web_tag[-1] == "uk":
    print("영국")
elif web_tag[-1] == "com":
    print("기업용")
elif web_tag[-1] == "org":
    print("기관")
else:
    print("알수없음")

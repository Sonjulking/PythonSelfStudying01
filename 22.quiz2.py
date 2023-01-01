menu = {"아이스 아메리카노": 3000, "아메리카노": 2500,
        "아이스 라떼": 3500, "라떼": 4000, "아이스크림": 8000}
ice_menu = {}
hot_menu = {}
for i, j in menu.items():
    #     if i[0:3] == "아이스":
    if "아이스" in i:
        ice_menu[i] = j  # 중요
    else:
        hot_menu[i] = j

print("차가운메뉴")
for i, j in ice_menu.items():
    print("메뉴 : {} 가격 : {}원".format(i, j))

print("뜨거운메뉴")
for i, j in hot_menu.items():
    print("메뉴 : {} 가격 : {}원".format(i, j))

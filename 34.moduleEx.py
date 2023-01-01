from time import localtime, strftime
from datetime import date, time, datetime, timedelta
# timedelta 날짜, 시간의 차이를 계산해주는 함수

import time  # 현재 시간을 알려주는 모듈

# today = date.today()
# print(today)
# new_date = date(1999, 12, 31)
# print(new_date)

# print(time(9))
# print(time(9, 2))
# print(time(9, 2, 3))
# print(time(9, 2, 3, 444444))

dt1 = datetime.now()
print(dt1)

dt2 = datetime(2002, 10, 20, 14, 5, 2)
print(dt2)

today = datetime.now()
print(today)
print(today - timedelta(days=20))  # 날짜뿐만 아니라 시간,분,초 다됨!

# import time =>위에서 사용한 datetime의 time과는 전혀다름
now = time.time()  # 1977년 1월 1일 0시 0분 부터 지난 시간을 초로 반환
print(now)

# from time import localtime 더쉬운형태로 반환
now = localtime()
print(now)

# from time import strftime 아직도 보기 어려우니까 포매팅 해줌

now = strftime("%Y-%m-%d %H:%M")
print(now)

now = strftime("%Y년 %m월 %d일 %H시:%M분")
print(now)

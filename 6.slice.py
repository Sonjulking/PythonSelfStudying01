str_slice = "0123456789"

print(str_slice[0:7])  # 0123456
print(str_slice[0:])
print(str_slice[0:10])
print(str_slice[:])

print(str_slice[-8:-1])


str_slice = "Python is easy"
#            012345678910111213

print(str_slice[-14:])
print(str_slice[0:20])

# step 사용
str_slice = "0123456789"

print(str_slice[0:10:2])

print(str_slice[::-3])
print(str_slice[9::-3])
print(str_slice[-1::-3])

str_slice = "Python"
print(str_slice[0:] + str_slice[::-1])
print(str_slice[1:5] + str_slice[0] + str_slice[5])

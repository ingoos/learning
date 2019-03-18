print("---------시작")

# 정수 (integer)
a = 1
a = 0
a = -1

# 실수 (Interger)
a = 1.1
a = -1.1
a = 1.2e10
a = 1.2e-10

# 8진수 및 16진수
a = 0o17
a = 0x12EF

# 수학 연산자

a = 2+3 # 덧셈
print(a)

a = 3-2 # 뺄셈
print(a)

a = 2/3 # 나눗셈
print(a) 

a = 2 ** 3 #거듭제곱
print(a)

a = 2%3 # 나머지값 구하기 Result : 2
print(a)

a = 3%2 # 나머지값 구하기 Result : 1
print(a)

a = 2//3 # 나눗셈 (소수점 버림)
print(a)

a = 3//2 # 나눗셈 (소수점 버림)
print(a)

a = "HI" + "HELLO" # 문자열 
print(a)

print(a[4])
print(a[-1])

print(a[0:2])
print(a[8:10])
print(a[11:])

a = "2019-03-18"
year = a[0:4]
month = a[5:7]
day = a[8:]
print(year)
print(month)
print(day)

a = "My Name is Mask"
print(a.count('M'))
print(a.count('My'))
print(len(a))

print(a.find('i'))

print(a.upper())
print(a.lower())

print(a.replace('Mask','james'))
print(a.split())

score = [100,90,95]
print(score)

print(score[0])
print(score[1])
print(score[2])

score.append(80)
score.insert(1,105)

print(score)

del score[0]
print(score)

print("----------끝")


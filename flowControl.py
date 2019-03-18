# 흐름제어
score = 90

if score >= 90:
    print("합격")
else:
    print("실격")

score=59
if score >= 60:
    print("합격")
else:
    print("실격")

korean = 90
math = 85

print( (korean >= 90) and (math >= 90) ) #flase
print( (korean >= 90) or (math >= 90) ) #true
not korean # korean 점수가 1점 이상이면 무저건 True


#다양한 비교
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("D")

if score >= 70: print("합격")
else: print("불합격")

a = ['A','B','C']
print(a[0])
print(a[1])
print(a[2])

# while 문의 강제 종료 break
goal = 55

while True:
    in_data = int(input("숫자를 입력하세요 : "))
    if in_data < goal:
        print("숫자가 작습니다.")
    elif in_data > goal:
        print("숫자가 큽니다.")
    else:
        print("일치합니다.")
        break

print("종료 합니다.")

# while 문의 처음으로 이동 continue

while True:
    in_data = input("문자열을 입력하세요. : ")
    if len(in_data) < 3:
        print("문자열의 길이가 짧습니다.")
        continue

    print("종료합니다.")
    break

# 반복 수행 : for
a = ['A','B','C']
for i in a:
    print(i)


a = [('science',100), ('math',95), ('computer',97)]
for (subject , score) in a:
    print(subject + " : " + str(score))


for i in range(1,5):
    print(i)

    










# 파일 생성
f = open("test.txt", "w")
f.close()

# 파일 읽기
f = open("c:/python_sample/test.txt","r")
while True:
    line = f.readline()
    if not line:
        break
    print(line)
f.close()

# 파일 읽기 2
f = open("c:/python_sample/test.txt", "r")
lines = f.readlines()
for line in lines:
    print(line)
f.close()

f = open("c:/python_sample/test.txt", "r")
lines = f.read()
print(lines)
f.close()

f = open("c:/python_sample/test.txt", "w")
f.write("첫번째 줄입니다.")
f.write("두번째 줄입니다.")
f.close()


f = open("c:/python_sample/test.txt", "w")
f.write("첫번째 줄입니다.")
f.write("\n")
f.write("두번째 줄입니다.")
f.write("\n")
f.close()

f = open("c:/python_sample/test.txt" ,"a")
f.write("추가한 줄입니다.")
f.close()

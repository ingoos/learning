# 함수에 대한 기본 구조

def display_msg(msg, times=1):
    print(msg * times)

display_msg("test")
display_msg("test",5)

# VarArgs 인자

def sum(*args):
    result = 0
    for i in args:
        result = result + i
    return result

print(sum(1,2))
print(sum(1,2,3,4))

# 지역 (local) 변수와 전역(global)변수

def local():
    a = 3 
    print("local a :" + str(a))

a = 10 
print(a)
local()
print(a)

b = 1 
def local2():
    global b
    b = 3

    print("global b : "+ str(b))

b = 10
print(b)
local2()
print(b)
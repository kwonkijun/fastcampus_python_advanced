# 일급객체란?
# - 다음과 같은 특징을 만족하는 객체를 말한다. 
# 1. 데이터 처럼 사용이 가능하다. 
# 2. 매개변수에 넘겨 줄 수 있다.
# 3. 리턴값으로 사용될 수 있다. 

# 1. 데이터 처럼 사용이 가능하다.

# 1) 함수를 변수에 할당 가능
def func(x, y):
    return x+y

add = func
print(add(3,4))

# 2) 리스트(튜플, 딕셔너리 등)에 할당 가능
def mul(x, y):
    return x * y

def div(x, y):
    return x / y

calculator = [mul, div]
print(calculator[0](5,6))

# 2. 매개변수에 넘겨 줄 수 있다.
def inputData():
    data = input("데이터 입력>>>")
    return data

def start(func):
    print("입력한 데이터는", func())

start(inputData)

# 3. 리턴값으로 사용될 수 있다. 
def plusTen(a):
    return a + 10

def func(x):
    return plusTen(x)

print(func(5))
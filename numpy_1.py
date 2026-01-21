import numpy as np  #선형 대수 연산에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수 제공

#1. 넘파이 배열
#파이썬 리스트와 비슷해 보이지만 계산 속도가 훨씬 빠르다
a_values = np.array([12500, 45000, 32000, 0, 56000])
print(a_values)

b_values = np.array([[1000, 2000, 3000, 4000], [5000, 2000, 3000, 4-12000],[1000, 2000, 32400, 4000]])
print(b_values)

import numpy as np

c_values = np.array([  # 전체를 감싸는 시작 대괄호 추가
    #지역이 아시아
    [
        [77,1,3],
        [4,59,6],
        [7,8,98],
    ],
    #지역이 유럽
    [
        [5,22,3],
        [4,5,77],
        [7,8,9],
    ],
    #지역이 아메리카
    [
        [5,22,3],
        [4,5,77],
        [7,8,9],
    ]
]) # 전체를 감싸는 끝 대괄호 추가

print(c_values)


#배열의 차원 확인
print(a_values.shape)  #shape: 배열의 차원과 크기를 나타내는 속성 (몇행 몇열인지를 찍어라)
print(b_values.shape) 
print(c_values.shape)

print(a_values.itemsize)  #itemsize: 배열의 각 요소가 차지하는 메모리 크기를 바이트 단위로 나타내는 속성
print(b_values.itemsize)
print(c_values.itemsize)

print(a_values.size) #size: 배열의 전체 요소 개수를 나타내는 속성  #5
print(b_values.size) #3*4=12
print(c_values.size) #3*3*3=27


#np.zeros  : 0으로 채워진 배열 생성
#np.ones  : 1로 채워진 배열 생성
#np.empty  : 초기화되지 않은 임의의 값으로 채워진 배열 생성

print(np.zeros((3,4)))  #3행 4열짜리 0으로 채워진 배열 생성 #괄호 2개인 이유는 튜플형태로 shape를 지정하기 위해
print(np.ones((2,5,7) , dtype=np.int64))  #dtype은 데이터 타입 지정 #np.ones는 1로 채워진 배열 생성
print(np.empty((2,3)))  #2행 3열짜리 초기화되지 않은 임의의 값으로 채워진 배열 생성

print(np.arange(10,30,5))  #10부터 30까지 5간격으로 배열 생성 (30은 포함 안됨)
print(np.arange(0, 2, 0.3)) #0부터 2까지 0.3간격으로 배열 생성 (2는 포함 안됨)

print(np.linspace(0,99,100)) #0부터 99까지 균일한 간격(등분)으로 100개 생성 (99 포함)

print(np.arange(0, 1+0.25, 0.25))  #0부터 1까지 0.25간격으로 배열 생성 (1 포함)
#1+0.25를 하는 이유는 부동소수점 오차로 인해 1이 포함되지 않을 수 있기 때문
#부동소수점 오차란 컴퓨터가 실수를 이진수로 표현할 때 발생하는 근사치 오차를 의미

print(np.linspace(0, 1, 5))  #0부터 1까지 균일한 간격으로 5개 생성 (1 포함)


a= np.arange(6) #0~5까지 1차원 배열 생성
print(a)
b= np.arange(12).reshape(4,3)  #0~11까지 1차원 배열을 2차원 배열(4행 3열)로 재구성
print(b)
c= np.arange(24).reshape(2,3,4)  #0~23까지 1차원 배열을 3차원 배열(2면 3행 4열)로 재구성
print(c)

a=np.array([20,30,40,50])  #1차원 배열
b=np.arange(4) #0~3까지 1차원 배열  #0,1,2,3 
c=a-b  #배열 간의 뺄셈 연산
print(c)   

print(b*10) #배열과 스칼라(단일 값) 간의 곱셈 연산 #스칼라란? 단일 값을 의미

print(a<35) #배열의 각 요소와 35를 비교하여 불리언 배열 생성 #불리언이란? 참(True)과 거짓(False)을 나타내는 데이터 타입

A = np.array([  #2행 2열 배열
    [1,1], 
    [0,1],
])

B = np.array([ #2행 2열 배열
    [2,0],
    [3,4],
])

print(A*B)  #요소별 곱셈 (Hadamard product) #같은 위치의 행,열끼리 곱셈 수행
print(A@B)  #행렬 곱셈 (Matrix multiplication) #행렬 곱셈 규칙에 따라 계산 수행 
#행렬 곱셈이란? 두 행렬의 곱셈 연산으로, 첫 번째 행렬의 행과 두 번째 행렬의 열을 곱하여 새로운 행렬을 생성하는 연산입니다.

# int < float  #우선순위가 높은 데이터 타입으로 자동 변환



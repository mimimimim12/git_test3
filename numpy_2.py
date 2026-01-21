import numpy as np  #선형 대수 연산에 필요한 다차원 배열과 배열 연산을 수행하는 다양한 함수 제공

#int < float 
#.sum  
#.min
#.max
#.armax : 모든 요소의 최대값의 인덱스
#.cumsum : 모든 요소의 누적합

a  = np.arange(8).reshape(2,4) **2  
print(a)
print(a.sum())
print(a.min())
print(a.argmax())   
print(a.cumsum())


#축기준 axis=0 : 열기준 / axis=1  : 행기준

b=np.arange(12).reshape(3,4)
print(b)
print(b.sum(axis=0))
print(b.sum(axis=1))

#인덱싱 슬라이싱
a = np.arange(10)
print(a)

print(a[2])
import pandas as pd
import numpy as np

dict_data = {"a":1,"b":2, "c":3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)


list_data = ["2026-1-19", 3.14, "abc", 100, True]
series_data = pd.Series(list_data)
print(type(series_data))
print(series_data)

dict_data = {"c0":[1,2,3], "c1":[4,5,6], "c2":[7,8,9], "c3":[10,11,12],"c4":[13,14,15]}
df = pd.DataFrame(dict_data)
print(type(df))
print(df)

#pandas 데이터내용 확인
#.columns   : 컬럼명 확인
#.head()     : 데이터 상위 5개 행 확인
#.tail()     : 데이터 하위 5개 행 확인, ()안에 숫자 입력 가능
#.shape     : 데이터 크기 확인(행, 열) = 엑셀 셀의 개수
#.info()      : 데이터 요약 정보 확인(메모리 사용량, 행과열의 크기, 컬럼명, 컬럼별 결측지, 컬럼별 데이터 타입 등)
#.types    : 각 컬럼별 데이터 타입 확인

#파일 불러오기 (확장자에 따라 함수 다름)
#형식        읽기         쓰기
#csv       read_csv    to_csv
#excel     read_excel  to_excel
#json      read_json   to_json
#html      read_html   to_html

#파일 경로 지정 
#./  내가 있는 기준으로 하위 폴더 이동
#../  내가 있는 기준으로 상위 폴더 이동

titanic = pd.read_csv("Titanic-Dataset.csv") 
print(titanic)
print(titanic.columns)
print(titanic.head())
print(titanic.tail(10))
print(titanic.shape)
print(titanic.info())

print(type(titanic))

#pandas 에서 특정 열을 선택
# 열 1개 선택 = Series 객체 반환
#데이터 프레임의 열 데이터 1개만 선택할때 2가지 방식
# 1) 대괄호[] 안에 열 이름을 따옴표로 함께 입력
# 2) 도트. 다음에 열 이름 일력
# 열 n 개 선택 = DataFreame 객체 반환
# 데이터 프레임의 열 데이터 n개를 선택할때는 1방식
# 이중대괄호[[]]열 이름을 따옴표로 함께 입력
# ***  만약에 열1개를 데이터프레임객체로 추출하려면 [[]] 사용가능


names = titanic["Name"]
print(names.head())
names= titanic.Name
print(names.head())
print(type(names))
print(names.shape)

double_colunms= titanic[["Sex","Age"]]
print(double_colunms.head())
print(type(double_colunms))
print(double_colunms.shape)

# pandas 데이터 필터링

# 1. boolean 인텍싱  True값을 가진 행만 추출
# 2. .isin() 각각의 요소가 데이터프레임 또는 시리즈에 존재 하는지 파악한후 True/False로 반환
# 3.  .isna() 결측 값은 True, 그외는  False
# 4. .notna() 결측값은 False  그외는 True

print(double_colunms["Age"]>=35)

above35 = double_colunms[double_colunms["Age"]>=35]
names = titanic["Name"]
print(above35.head())  #True


#성별 남자만 추출
avove_male = double_colunms[double_colunms["Sex"]=="male"]
print(avove_male.head())

print(titanic.head())
class_1 = titanic[titanic["Pclass"].isin([1])]
print(class_1.head())

print(double_colunms.head())

age2040 = double_colunms[double_colunms["Age"].isin(np.arange(20,41))]
print(age2040.head())


print(double_colunms.head(7))
class_2 = double_colunms["Age"].isna()
print(class_2.head(7))  # 비어있는 cell True 반환

class_3 = double_colunms["Age"].notna()
print(class_3.head(7))  # 비어있는 cell False 반환

#결측 값을 제거한 누락되지 않은 값을 확인 
#행 제거

print(double_colunms.head(10))

age5 = double_colunms[double_colunms["Age"].notna()]
print(age5.head(10))


#결측치 제거
#.dropna(axis=10) == .dropna() : 결측 값들이 들어있는 행 전체 삭제
#.dropna(axis=1) : 결측 값들이 들어있는 열 전체 삭제

print(titanic.head())   #기본 값 5개 출력
print(titanic.dropna())   #결측치가 있는 행 전체 삭제
print(titanic.dropna(axis=1).head())   #결측치가 있는 열 전체 삭제 후 상위 5개 출력


#pandas 이름과 인덱스로 특정 행과 열 선택
# .loc[] : 이름기반 인덱싱 (행이름과 열 이름 사용) / DataFrame.loc[행이름, 열이름]
# .iloc[] : 정수기반 인덱싱 (행 번호 열 번호 사용) / DataFrame.iloc[행번호, 열번호]

name35 = titanic.loc[titanic["Age"]>=35, ["Name","Age"]]
print(name35.head())


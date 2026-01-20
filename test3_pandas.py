# 전일 예제 풀이 1번
# import streamlit as st
import pandas as pd
import numpy as np  

trade = pd.read_csv("./raw_trade_data.csv", encoding='cp949')
print(trade)

# 1. hs85로 시작하는 데이터 필터링
#print(trade.info())  


cond_hs = trade["hs_code"].astype(str).str.startswith("85")
#print(cond_hs)



# 2. 미국, 베트남 국가명 필터링
cond_country = trade["국가명"].isin(["미국", "베트남"])


#print(cond_country)  #미국과 베트남만 true false로 출력



# 3. 수출금액이 0원 데이터 제외
#print(trade.head(10))
cond_value = trade["수출금액"] > 0

#print(cond_value)



#결합
#step1 = trade[cond_hs]
#step2 = step1[cond_country]
#step3 = step2[cond_value]

step3 = trade[cond_hs & cond_country & cond_value]

print("상위 10개 데이터 확인")
print(step3.head(10))

#trade.to_csv("저장할 파일명.csv", index=False, encoding='euc-kr') #결과치를 우리가 원하는 파일로 저장






# 전일 예제 풀이 2번 (데이터 전처리 과정 클렌징 및 정규화)
#1. '중량' 컬럼에 결측치가 있다면 해당 품목의 평균 중량으로 채우세요. (어려우면 0으로 채우기)
print(trade.head(15))  #중량 결측치 확인
hs_mean = trade.groupby("hs_code")["중량"].mean()  #hs_code별 중량 평균값 확인
print(hs_mean)

#for 변수 in 자료들 : 
for hs in hs_mean.index:   #index는 value 값만 가져옴
    #1. 현재 순서의 hs code에 해당하는 평균값을 가져오기
    avg_val= hs_mean[hs]   
    #2. 원본 데이터에서 해당 hs code이면서 중량이 결측치인(비어있는) 행만 찾기
    target = (trade["hs_code"] == hs) & (trade["중량"].isna())
    #3. 해당 되는 칸에만 평균값 대입
    trade.loc[target, "중량"] = avg_val

#trade.loc[trade["중량"].isna()] = 0  #결측치(비어있는)가 남아있다면 0으로 채우기

#2. '수출입구분' 컬럼의 데이터가 영문(Import, Export)으로 되어 있다면 국문(수입, 수출)으로 일괄 변경하세요.

trade.loc[trade["수출입구분"] == "Export", "수출입구분"] = "수출"
trade.loc[trade["수출입구분"] == "Import", "수출입구분"] = "수입"

#3. 현재 '수출금액' 단위가 '원'입니다. 이를 '백만 달러' 단위로 변환한 수출금액_M_USD 컬럼을 만드세요. (환율 1,470원 가정)
exchange_rate = 1470
trade["수출금액_M_USD"] = (trade["수출금액"] / exchange_rate) / 1000000  #(금액/1470)/100000 새컬럼 만들기 #백만 달러 단위로 변환

#4. 변경 후 데이터의 각 컬럼별 데이터 타입(df.dtypes)을 확인하여 수치형 데이터가 맞는지 검증하세요.
print("\n ---- [최종 데이터 확인] ----")
print(trade.dtypes)
print("\n ---- [클렌징 결과 샘플 확인] ----")
print(trade[["날짜", "hs_code", "중량", "수출입구분", "수출금액", "수출금액_M_USD"]].head()) #최종 결과 확인

trade.to_csv("./클렌징_완료_무역데이터.csv", index=False, encoding='cp949')  #결과치를 우리가 원하는 파일로 저장
print("✅ 클렌징 완료된 데이터가 저장되었습니다.")  # 완료 메시지

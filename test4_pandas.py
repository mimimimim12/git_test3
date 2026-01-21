import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt 
import seaborn as sns
from datetime import datetime

#데이터 불러오기

try: #파일이 있는 경우
    #실적 데이터 가져오기 (trade_performance.csv)
    df_pref = pd.read_csv("./trade_performance.csv", encoding='cp949')
    #마스터 데이터 가져오기 (country_master.csv)
    df_master = pd.read_csv("./country_master.csv", encoding='cp949')

except FileNotFoundError:   #파일이 없을 때 대비
    print("🚨 파일이 존재하지 않습니다. 파일 경로를 확인해주세요.")
    exit()   #프로그램 종료

print("실적 데이터 정보")
print(df_pref)
print(df_master)


# 1. 머지 수행 (city_code 기준)
df = pd.merge(df_pref, df_master, on="ctry_code", how="left")  
print(df)

# 2. 대륙별 성과 분석 총 수출액 수입 합계
continent_state = df.groupby("continent")[["export_val", "import_val"]].sum()  #groupby는 묶는 역할, sum은 합계 구하는 역할
print(continent_state)

# 3. 무역수지 계산 (수출액 - 수입액)
continent_state["무역수지"] = continent_state["export_val"] - continent_state["import_val"]
print("대륙별 무역 성과 요약")
#print(continent_state)  
best_continent = continent_state["무역수지"].idxmax()  #가장 큰 값의 index를 반환
print(f"분석 결과 :{best_continent} 대륙과의 거래에서 가장 큰 무역 수지 흑자가 발생했습니다.")

# 4. FTA 효과 분석 평균 수출 단가 (수출 금액 / 수출 중량)
df["평균 수출 단가"] = df["export_val"] / df["weight"]

# 5. FTA 체결 국가와 비체결 국가의 평균 수출 단가 비교
fta_ans = df.groupby("fta_status")["평균 수출 단가"].mean()  #fta_status 기준으로 평균 수출 단가를 구함

print("\n FTA 체결 국가와 비체결 국가의 평균 수출 단가 비교")
print(fta_ans)



# 시사점 도출 
if fta_ans["Y"] > fta_ans["N"]:  #Y라는 키값이 N이라는 키값보다 클 때
    print("분석 결과: FTA 체결 국가와의 거래에서 평균 수출 단가가 더 높게 나타났습니다.")
else:
    print("분석 결과: FTA 비체결 국가와의 거래에서 평균 수출 단가가 더 높게 나타났습니다.") 


# 5. 품목별 집중도 분석 수출 금액이 가장 큰 상위 2개 추출 그리고 품목이 어느 국가에 수출되는지 분석
#수출 금액이 가장 큰 상위 2개 품목 추출
top2_hs = df.groupby("hs_code")["export_val"].sum().nlargest(2).index.tolist()  #nlargest는 큰 값 순서대로 n개 추출 
#index.tolist()는 index 값을 리스트로 변환
print(f"\n 수출 금액이 가장 큰 상위 2개 품목: {top2_hs}")

# 해당 품목들이 주로 어느 국가로 수출되고 있는지 분석하세요.
top2_df = df[df["hs_code"].isin(top2_hs)] #top2_hs에 해당하는 행만 추출

country_focus = top2_df.groupby(["hs_code", "ctry_name"])["export_val"].sum().reset_index()  #reset_index는 그룹화된 데이터를 다시 원래 형태로 변환
print(country_focus)


# 날짜 데이터 월 정보 추출
df["ymd"] = pd.to_datetime(df["ymd"])  #문자열을 날짜형으로 변환
df["month"] = df["ymd"].dt.month  #dt.month은 월 정보 추출
#print(df.info())


# 시각화 월별 수출입 추이 데이터 생성
monthly = df.groupby("month")[["export_val", "import_val"]].sum() #월별 수출입 합계
plt.figure(figsize=(12,6))  #그래프 크기 설정
plt.plot(monthly.index, monthly["export_val"], label='수출액', marker='o', linewidth=2) #수출액 선 그래프 #monthly.index는 월 정보를 의미
plt.plot(monthly.index, monthly["import_val"], label='수입액', marker='s', linewidth=2) #수입액 선 그래프
plt.title("월별 수출입 추이")   #그래프 제목
plt.xlabel("월")   #x축 라벨
plt.ylabel("금액")  #y축 라벨
plt.show()   #그래프 출력




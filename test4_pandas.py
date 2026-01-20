import pandas as pd
import numpy as np  

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
print(continent_state)
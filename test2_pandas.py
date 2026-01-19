import pandas as pd
import numpy as np


# df= pd.read_csv("./raw_trade_data.csv" , encoding ="utf-8-sig")
# df= pd.read_csv("./raw_trade_data.csv" , encoding ="cp949")
df = pd.read_csv("./raw_trade_data.csv", encoding="euc-kr")
# print(df)

# 1. hs85

print("\n -------- 과제 1 시작 반도체 수출 보고서 생성 -------")
# 1. HS 85 시작
# print(df.info()) int64

cond_hs = df["hs_code"].astype(str).str.startswith("85")
# 2. 미국 베트남 필터링 국가명
cond_country = df["국가명"].isin(["미국","베트남"])

# 3. 수출금액이 0원 데이터 제외
cond_value = df["수출금액"] > 0

step1= df[cond_hs]
step2= step1[cond_country]
step3= step2[cond_value]

print("상위 10개 데이터 확인")
print(step3.head(10))

# step3.to_scv(" "  ,)

# 과제2

print("\n ------ 과제 2 시작 데이터 클렌징 및 정규화")

# 1. 평균 hs코드별  중량 평균
hs_mean = df.groupby("hs_code")["중량"].mean()


































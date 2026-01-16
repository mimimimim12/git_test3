import streamlit as st
import numpy as np
import pandas as pd
from datetime import datetime as dt
import datetime


st.title("이것이 타이틀이다")
st.header("이것이 헤더이다")
st.subheader("이것이 서브헤더이다")
st.text("이것이 일반 텍스트이다")

st.title('스마일 : 😀')

st.caption("캡션을 한번 넣어 봤슴")
# st.markdown("마크다운 문법도 지원합니다. **굵게**, *기울임*, ~~취소선~~")
st.markdown("**신영희**  *신영희* ~~신영희~~")


#코드 표시
sample_code = '''
def hello():
    print("Hello, World!")
'''

st.code(sample_code, language='python')

# #마크다운 문법 지원
st.markdown("텍스트의 색상을 :green[초록색]으로 , 그리고 **:blue[파란색]** 볼드체를 설정할수 있다")
st.markdown(":green[$\sqrt{x^2 + y^2} = 1$] 와 같은 수식도 지원한다.")

st.latex(r'\sqrt{x^2 + y^2} = 1')

st.title("데이터프레임 출력하기")

# datafreame 생성

datafreame = pd.DataFrame({
    "first column ": [1,2,3,4],
    "second column ": [10,20,30,40]
})

# dataframe
st.dataframe(datafreame)

#  테이블 출력
st.table(datafreame)

# 메트릭
st.metric(label="온도", value="25 °C", delta="1.2 °C")
st.metric(label="삼성전자", value="140,000원 ", delta="+3,800원")

#컬럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)
col1.metric(label="달러USD", value="1,471 원", delta="+30 원")
col2.metric(label="유로EUR", value="1,590 원", delta="+20 원")
col3.metric(label="엔JPY", value="1,050 원", delta="-5 원")

#버튼 클릭

button = st.button("버튼을 눌러주세요")
if button:
    st.write(":blue[버튼]이 눌렸습니다! 👍")

agree = st.checkbox("체크박스를 눌러주세요")
if agree:
    st.write("체크박스가 선택되었습니다! ✅")   

#라디오 버튼
mbti =st.radio(
    "당신의 MBTI는 무엇인가요?",
    ('INTJ', 'ENFP', 'ISTP', 'ESFJ') ,
    index=2
)

if mbti == 'INTJ':
    st.write("당신은 전략가형입니다.")
elif mbti == 'ENFP':
    st.write("당신은 활동가형입니다.")
elif mbti == 'ISTP':
    st.write("당신은 장인형입니다.")
else:
    st.write("당신은 사교형입니다.")


#셀렉트박스
favorite_color = st.selectbox(
    "당신이 가장 좋아하는 색깔은 무엇인가요?",
    ('빨강', '파랑', '초록', '노랑')
)   
st.write(f"당신이 선택한 색깔은 :red[{favorite_color}], 입니다.")

# 멀티셀렉트박스
hobbies = st.multiselect(
    "당신의 취미를 선택해주세요",
    ['독서', '여행', '운동', '요리', '게임']
)   
st.write("당신의 취미는 다음과 같습니다:", hobbies)

#슬라이더
age = st.slider(
    "당신의 나이는 어떻게 되나요?",
    0, 100, 25
)
st.write(f"당신의 나이는 :blue[{age}]세 입니다.")

value = st.slider(
    "범위의 값을 다음과 같은 범위로 설정하세여",
    0.0, 100.0, (25.0, 75.0)
)
st.write(f"선택한 범위는 :green[{value}] 입니다.")

#날짜 선택
start_time=st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2026,1,1,0,0),
    max_value=dt(2026,1,31,0,0),  
    value=dt(2026,1,15,0,0),
    step=datetime.timedelta(days=1),
    format="YYYY-MM-DD"
)
st.write(f"약속 날짜는 :green[{start_time}] 입니다.")

# 텍스트입력
title=st.text_input(
    label="가고 싶은 여행지가 있나요?",
    placeholder="예: 파리, 뉴욕, 도쿄"
)
st.write(f"당신이 가고 싶은 여행지는 :green[{title}] 입니다.")

# 숫자입력
number=st.number_input(
    label="당신이 좋아하는 숫자는 무엇인가요?",
    min_value=0,
    max_value=100,
    value=42,
    step=2
)
st.write(f"당신이 좋아하는 숫자는 :green[{number}] 입니다.")

# 파일다운로드 버튼   
st.download_button(
    label="CSV 다운로드",
    data=datafreame.to_csv(index=False).encode('utf-8'),
    file_name="sample.csv",
    mime="text/csv"
)



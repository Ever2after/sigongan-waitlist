import streamlit as st
import pandas as pd
import time

if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

df = pd.read_csv("./data.csv", index_col=0)

st.title("시공간 중고거래")

def onClick():
    new_row = {
        'willUse': radio1 == "예",
        'description': description,
        'contact': text,
        'timeStamp': time.time()
    }
    df1 = df.append(new_row, ignore_index=True)
    df1.to_csv("./data.csv")
    st.session_state['submitted'] = True

if not st.session_state['submitted']:
    st.write("중고거래할 때 매번 남에게 제품 상태를 물어보기 번거로우셨나요? \
             판매자가 제품의 하자사항이나 상세한 정보를 기재하지 않아 난감했던 경험이 있으신가요?")
    st.write("이제는 시공간에게 편하게 언제, 어디서든 물어보세요. \
            제품의 외관, 품질, 하자를 모두 꼼꼼히 검토해드립니다. \
            원하는 물품을 말해주세요. 말씀하신 조건에 맞는 최적의 중고물품을 추천해드립니다.")

    st.write("여러분의 소중한 의견을 들려주세요. 서비스 제작 시 소중한 참고자료가 됩니다.")

    st.write("시공간 중고거래 서비스를 이용할 의향이 있으신가요?")

    radio1 = st.radio("이용 의향 선택", ("예", "아니오"))

    st.write("서비스에 대한 자유로운 의견을 작성해주세요")
    description = st.text_area("의견 입력", placeholder="의견을 입력해주세요...")

    st.write("서비스에 대한 소식을 가장 먼저 접하고 싶으시다면, 전화번호나 이메일을 남겨주세요.")
    text = st.text_input("연락처", placeholder="연락처를 입력해주세요...")
    btn1 = st.button("제출", on_click=onClick)

def onClick2():
    st.session_state['submitted'] = False

if st.session_state['submitted']:
    st.header("제출이 완료되었습니다.")
    st.write("여러분의 소중한 의견 감사드립니다.")
    btn2 = st.button("처음으로", on_click=onClick2)

#from dotenv import load_dotenv
#load_dotenv()


import streamlit as st
from langchain.chat_models import ChatOpenAI

chat_models = ChatOpenAI()

st.title('문법 예시 도우미')

content = st.text_input("예시가 궁금한 개념들을 말해주세요!(ex : 합성어, 파생어..등)")


if st.button("예시 생성!"):
    with st.spinner('예시 생성 중...'):
        result = chat_models.predict(content + "의 문법 개념에 대한 참신한 예시를 5개 말해줘(한국 교육과정안에 있는 예시들로 들어줘)")
        st.write(result)


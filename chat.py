import streamlit as st
from dotenv import load_dotenv
from llm import get_ai_response

st.set_page_config(page_title="소득세 챗봇", page_icon="🤖")
load_dotenv()

st.title("🤖 소득세 챗봇")
st.caption("소득세에 관련된 모든것을 답해드립니다!")

if 'message_list' not in st.session_state:
    st.session_state.message_list = []

for message in st.session_state.message_list:
    st.chat_message(message['role']).write(message['content'])

if user_question := st.chat_input(placeholder="소득세에 관련된 궁금한 내용들을 말씀해주세요!"):
    with st.chat_message("user"):
        st.write(user_question)
    st.session_state.message_list.append({'role':'user', 'content':user_question})

    with st.spinner("답변중..."):
        ai_response = get_ai_response(user_question)
        with st.chat_message("ai"):
            ai_message = st.write_stream(ai_response)
            st.session_state.message_list.append({'role':'ai', 'content':ai_message})
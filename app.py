import streamlit as st
from deepseek_agent import DeepSeekAgent

st.set_page_config(page_title="🤖 AI Agent", page_icon="🤖")
st.title("🤖 Trợ lý AI với DeepSeek")

# Khởi tạo agent
if "agent" not in st.session_state:
    st.session_state.agent = DeepSeekAgent()
    st.session_state.chat_history = []

# Hiển thị lịch sử
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Nhận input từ người dùng
if prompt := st.chat_input("Hỏi AI..."):
    st.chat_message("user").markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response = st.session_state.agent.get_response(prompt)
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})

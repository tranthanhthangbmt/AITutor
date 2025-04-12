import streamlit as st
from deepseek_agent import DeepSeekAgent

# Cấu hình trang
st.set_page_config(page_title="AI Assistant Lớp Học", page_icon="🤖")
st.title("🤖 AI Assistant cho Lớp Học")
st.write("Chat với trợ lý AI được tạo bằng DeepSeek")

# Khởi tạo agent (lưu trong session để không bị reset khi refresh)
if "agent" not in st.session_state:
    st.session_state.agent = DeepSeekAgent()
    st.session_state.chat_history = []

# Hiển thị lịch sử chat
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Xử lý input người dùng
if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
    # Hiển thị tin nhắn người dùng
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Nhận phản hồi từ agent
    with st.chat_message("assistant"):
        response = st.session_state.agent.get_response(prompt)
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response})
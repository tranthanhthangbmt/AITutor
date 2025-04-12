import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class DeepSeekAgent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.deepseek.com/v1"
        )
        self.conversation_history = []
    
    def get_response(self, user_input):
        import streamlit as st

        # 👉 In danh sách model
        try:
            models = self.client.models.list()
            st.write("🔍 Available Models:")
            st.write(models)
        except Exception as e:
            st.error(f"Lỗi khi lấy danh sách models: {e}")
            return "Lỗi kết nối đến API"
    
            
        self.conversation_history.append({"role": "user", "content": user_input})
        
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=self.conversation_history,
            temperature=0.7
        )
        
        ai_response = response.choices[0].message.content
        self.conversation_history.append({"role": "assistant", "content": ai_response})
        return ai_response

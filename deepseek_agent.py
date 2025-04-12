import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class DeepSeekAgent:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        self.conversation_history = []
    
    def get_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})

        body = {
            "model": "deepseek-chat",
            "messages": self.conversation_history,
            "temperature": 0.7
        }

        try:
            res = requests.post(self.base_url, headers=self.headers, json=body)
            res.raise_for_status()  # Gây lỗi nếu response không phải 200

            data = res.json()
            ai_response = data["choices"][0]["message"]["content"]

            self.conversation_history.append({"role": "assistant", "content": ai_response})
            return ai_response

        except Exception as e:
            return f"⚠️ Lỗi khi gọi DeepSeek API: {e}"

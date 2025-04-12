import requests
import os

class DeepSeekAgent:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        self.history = []

    def get_response(self, prompt):
        self.history.append({"role": "user", "content": prompt})

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "deepseek-chat",
            "messages": self.history,
            "temperature": 0.7
        }

        response = requests.post(self.api_url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        reply = data["choices"][0]["message"]["content"]
        self.history.append({"role": "assistant", "content": reply})
        return reply

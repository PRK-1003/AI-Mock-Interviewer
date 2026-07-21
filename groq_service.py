import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GroqService:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("MODEL", "llama-3.3-70b-versatile")

        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.url = "https://api.groq.com/openai/v1/chat/completions"

    def generate_response(self, system_prompt, user_prompt, temperature=0.3, max_tokens=1024):
        """
        Sends a request to Groq Llama model and returns the generated response.
        """

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            "temperature": temperature,
            "max_tokens": max_tokens
        }

        try:
            response = requests.post(
                self.url,
                headers=headers,
                json=payload,
                timeout=60
            )

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]

        except requests.exceptions.HTTPError as e:
            return f"HTTP Error: {e}\n{response.text}"

        except requests.exceptions.ConnectionError:
            return "Connection Error: Unable to connect to Groq."

        except requests.exceptions.Timeout:
            return "Request Timeout."

        except Exception as e:
            return f"Unexpected Error: {str(e)}"


# Singleton instance
groq = GroqService()
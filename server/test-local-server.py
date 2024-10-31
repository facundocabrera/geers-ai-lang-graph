from openai import OpenAI

client = OpenAI(base_url="http://127.0.0.1:8080/v1", api_key="sk-xxx")

response = client.chat.completions.create(
    model="mlx-community/Llama-3.2-3B-Instruct",
    messages=[{"role": "user", "content": "Say this is a test!"}],
)

print(response)
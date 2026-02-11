from openai_client import client, MODEL

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Say hello"}]
)

print(response.choices[0].message.content)

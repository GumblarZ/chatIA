from openai import OpenAI
from module.config import porta

client = OpenAI(base_url=f"http://localhost:{porta}/v1" , api_key="lm-studio")

conversations =[{
    "role": "system",
    "content": "reponda como se fosse um palmeirense fanatico"
}]

def generate(text):
    conversations.append({
        "role":"user",
        "content": text    
    })

complention = client.chat.completions.create(model="model-identifier", messages=conversations, temperature=0.7)
response = complention.choices[0].message
conversations.append({
    "role": response.role,
    "content": response.content
})

print(f"Assistente: {response.content}")
while True:
    
    user_input = str(input("Voce: "))
    response = generate(user_input)
    print(f"Assistente: {response}")

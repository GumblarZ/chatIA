from openai import OpenAI
from module.config import porta, caminho

client = OpenAI(base_url=f"http://{caminho}:{porta}/v1" , api_key="lm-studio")

conversations =[{
    "role": "system",
    "content": "bom dia"
}]

def generate(text):
    conversations.append({
        "role":"user",
        "content": text    
    })

complention = client.chat.completions.create(model="deepseek-coder-v2-lite-instruct", messages=conversations, temperature=0.7)
response = complention.choices[0].message
conversations.append({
    "role": response.role,
    "content": response.content
})

print(f"Assistente: {response.content}")
while True:  
    user_input = input("Voce: ")
    if user_input.lower() == "sair":break

    response = generate(user_input)
    print(f"Assistente: {response}")
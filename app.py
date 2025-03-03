from openai import OpenAI
from module.config import port, ip
import module.voice as voice

client = OpenAI(base_url=f"http://{ip}:{port}/v1" , api_key="lm-studio")
print('Assistente: ola como posso lhe ajudar?')
while True:
    
    question = input('Voce: ')

    conversations =[{
        "role": "system",
        "content": f"{question}, responda somente em portugues"
    }]

    def generate(text):
        conversations.append({
            "role":"user",
            "content": text    
        })  
    complention = client.chat.completions.create(model="deepseek-r1-distill-llama-8b", messages=conversations, temperature= 0.7
    )
    response = complention.choices[0].message
    conversations.append({
        "role": response.role,
        "content": response.content
    })

    voice.speak(f"Assistente: {response.content}\n posso lhe ajuda com algo mais?")
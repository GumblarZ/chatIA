from bs4 import BeautifulSoup
import re

def remove_tag_content(content):
<<<<<<< Updated upstream:module/sanitization.py

=======
   
    # Removendo todas as ocorrências do conteúdo dentro da tag
>>>>>>> Stashed changes:module/tratamento.py
    modified_content = re.sub(r'<([^>]+)>', '', content)
    print(modified_content)
    return modified_content

## criação de um split que antecede de </think>

def remove(content):
    target = list(content)
    text = content.split()   
    print(f'O alvo é {target}')
    i=0
    while i <= target:
        del text[0]
    return text  
    
def list(content):
    texto = content.split()
    i = 0
    for palavra in texto:
        i = i+1    
        if palavra == '</think>':  
            return i+1
from bs4 import BeautifulSoup
import re

def remove_tag_content(content):

    # Removendo todas as ocorrências do conteúdo dentro da tag
    modified_content = re.sub(r'<([^>]+)>', '', content)
    
    return modified_content

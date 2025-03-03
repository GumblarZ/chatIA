from bs4 import BeautifulSoup
import re

def remove_tag_content(content):

    modified_content = re.sub(r'<([^>]+)>', '', content)
    
    return modified_content

import os
import markdown

NOTES_DIR = "data"


if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

def save_note(title, content):
    
    filename = f"{NOTES_DIR}/{title}.md"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    return filename

def load_note(title):
    
    filename = f"{NOTES_DIR}/{title}.md"
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    return None

def convert_markdown_to_html(markdown_text):
    
    return markdown.markdown(markdown_text)

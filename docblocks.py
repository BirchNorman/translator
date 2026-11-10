import os
import sys
from docx import Document

def docblocks(file_path: str, block_number: int):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text_content = f.read()
    except Exception as e:
        print(f"{e}")
        sys.exit()

    doc = Document()
    doc.add_paragraph(text_content)
    doc.save(f"block{block_number}.docx")
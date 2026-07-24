import zipfile
import xml.etree.ElementTree as ET
import sys
import os

def extract_text_from_pptx(pptx_path):
    text_runs = []
    try:
        with zipfile.ZipFile(pptx_path, 'r') as archive:
            for item in archive.namelist():
                if item.startswith('ppt/slides/slide') and item.endswith('.xml'):
                    content = archive.read(item)
                    root = ET.fromstring(content)
                    
                    # Namespace for DrawingML
                    namespaces = {'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
                    
                    slide_texts = []
                    for node in root.findall('.//a:t', namespaces):
                        if node.text:
                            slide_texts.append(node.text)
                    
                    if slide_texts:
                        text_runs.append((item, " ".join(slide_texts)))
                        
    except Exception as e:
        print(f"Error: {e}")
        return
    
    # Sort slides by name (slide1.xml, slide2.xml, etc.)
    text_runs.sort(key=lambda x: int(x[0].replace('ppt/slides/slide', '').replace('.xml', '')))
    
    for slide_name, text in text_runs:
        print(f"--- {slide_name} ---")
        print(text)
        print()

if __name__ == '__main__':
    extract_text_from_pptx('PPT ANNISA.pptx')

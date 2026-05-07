import fitz # PyMuPDF
import sys
import os

def extract_pdf_info(pdf_path, img_dir, prefix):
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    doc = fitz.open(pdf_path)
    text_content = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        text_content.append(f"--- PAGE {page_num + 1} ---")
        text_content.append(page.get_text())

    return "\n".join(text_content)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    prefix = sys.argv[2]
    print(extract_pdf_info(pdf_path, "pdf_images", prefix))

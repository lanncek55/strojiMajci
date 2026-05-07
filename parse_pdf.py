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

        # Extract images
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_filename = os.path.join(img_dir, f"{prefix}_page{page_num+1}_img{img_index}.{image_ext}")
            with open(image_filename, "wb") as image_file:
                image_file.write(image_bytes)
            text_content.append(f"[IMAGE EXTRACTED: {image_filename}]")

    return "\n".join(text_content)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    prefix = sys.argv[2]
    print(extract_pdf_info(pdf_path, "pdf_images", prefix))

import pymupdf

def extract_ocr(file_path):
    doc = pymupdf.open(file_path)
    page_text = {}

    for page_count, page in enumerate(doc):
        text = page.get_text("text")
        page_text[page_count] = text

    return page_text

import pymupdf
from src.pdf_extraction import extract_ocr
from src.pdf_chunking import *

FILE_PATH = "/home/ejantony/Documents/cs.pdf"

def main():
    pagewise_text = extract_ocr(FILE_PATH)
    chunked_text = chunking(pagewise_text)
    # for page_number, page_text in chunked_text.items():
    #     print(page_number)
    #     print(page_text)
    #     print("---------")

    for page_num, chunks in chunked_text.items():
        print(f"Page {page_num}:")
        for i, chunk in enumerate(chunks):
            print(f"  Chunk {i+1}:\n{chunk}\n")
    

if __name__ == "__main__":
    main()
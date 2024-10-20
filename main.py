import pymupdf

doc = pymupdf.open("/home/ejantony/Documents/cs.pdf")
page = doc.load_page(0)
text = page.get_text("text")
print(text)
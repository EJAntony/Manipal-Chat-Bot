
def chunking(pagewise_text):
    chunked_pages = {}
    
    for page_num, text in pagewise_text.items():
        chunks = chunk_text_with_overlap(text, chunk_size=256, overlap_size=50)
        chunked_pages[page_num] = chunks
    
    return chunked_pages


def chunk_text_with_overlap(text, chunk_size, overlap_size):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size - overlap_size):
        chunk = words[i:i + chunk_size]
        chunks.append(' '.join(chunk)) 
    
    return chunks



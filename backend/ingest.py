
from backend.services.embedding import chunk_and_embed

def process_file(filename: str, content: bytes):
    return chunk_and_embed(content.decode('utf-8'))

from embedchain.chunkers.base_chunker import BaseChunker

from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

TEXT_SPLITTER_CHUNK_PARAMS = {
    "chunk_size": 300,
    "chunk_overlap": 0,
    "length_function": len,
}


class TextChunker(BaseChunker):
    def __init__(self):
        text_splitter = RecursiveCharacterTextSplitter(**TEXT_SPLITTER_CHUNK_PARAMS)
        super().__init__(text_splitter)

    def create_chunks(self, loader, url):
        if os.path.isfile(url):
            with open(url, 'r') as file:
                content = file.read()
        else:
            content = loader.load_data(url)[0]["content"]
        chunks = self.text_splitter.split_text(content)
        return [{
            "content": chunk,
            "meta_data": {
                "url": url,
            },
        } for chunk in chunks]


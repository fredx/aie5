import os
from typing import List


class TextFileLoader:
    def __init__(self, path: str, encoding: str = "utf-8"):
        self.documents = []
        self.path = path
        self.encoding = encoding

    def load(self):
        if os.path.isdir(self.path):
            self.load_directory()
        elif os.path.isfile(self.path) and self.path.endswith(".txt"):
            self.load_file()
        else:
            raise ValueError(
                "Provided path is neither a valid directory nor a .txt file."
            )

    def load_file(self):
        with open(self.path, "r", encoding=self.encoding) as f:
            self.documents.append(f.read())

    def load_directory(self):
        for root, _, files in os.walk(self.path):
            for file in files:
                if file.endswith(".txt"):
                    with open(
                        os.path.join(root, file), "r", encoding=self.encoding
                    ) as f:
                        self.documents.append(f.read())

    def load_documents(self):
        self.load()
        return self.documents

class CharacterTextSplitter:
    def __init__(
        self,
        chunk_size: int = 500,
        chunk_overlap: int = 100,
    ):
        assert (
            chunk_size > chunk_overlap
        ), "Chunk size must be greater than chunk overlap"

        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    def split(self, text: str, factor: int = 1) -> List[str]:
        chunks = []
        for i in range(0, len(text), self.chunk_size * factor - self.chunk_overlap * factor):
            chunks.append(text[i : i + self.chunk_size * factor])
        return chunks

    def split_texts(self, texts: List[str]) -> List[str]:
        chunks = []
        small_chunks = []
        medium_chunks = []
        large_chunks = []
        for text in texts:
            small_chunks.extend(self.split(text, 1))
            medium_chunks.extend(self.split(text, 2))
            large_chunks.extend(self.split(text, 3))

        while len(small_chunks) and len(medium_chunks) and len(large_chunks):
            for i in range(2):
                for j in range(2):
                    if len(small_chunks) > 0:
                        chunks.append(small_chunks.pop(0))
                if len(medium_chunks) > 0:
                    chunks.append(medium_chunks.pop(0))
            if len(large_chunks) > 0:
                chunks.append(large_chunks.pop(0))

        return chunks


if __name__ == "__main__":
    loader = TextFileLoader("data/PMarcaBlogs.txt")
    loader.load()
    print(len(loader.documents))
    splitter = CharacterTextSplitter()
    chunks = splitter.split_texts(loader.documents)
    print("--------")
    print(len(chunks))
    print(len(chunks[0]))
    print(len(chunks[1]))
    print(len(chunks[2]))
    print(len(chunks[3]))
    print(len(chunks[4]))
    print(len(chunks[5]))
    print(len(chunks[6]))
    print(len(chunks[7]))
    print(len(chunks[8]))
    print("--------")
    print(len(chunks[-6]))
    print(len(chunks[-5]))
    print(len(chunks[-4]))
    print(len(chunks[-3]))
    print(len(chunks[-2]))
    print(len(chunks[-1]))


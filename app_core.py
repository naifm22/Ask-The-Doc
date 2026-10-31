"""Pure helpers for the Ask the Doc Streamlit application."""

from __future__ import annotations

import hashlib

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


MAX_UPLOAD_BYTES = 5 * 1024 * 1024
CHUNK_SIZE = 1_000
CHUNK_OVERLAP = 100


def decode_uploaded_text(data: bytes) -> str:
    """Decode and validate a small UTF-8 text upload."""
    if not data:
        raise ValueError("The uploaded file is empty.")
    if len(data) > MAX_UPLOAD_BYTES:
        raise ValueError("The uploaded file exceeds the 5 MB application limit.")

    for encoding in ("utf-8-sig", "utf-8"):
        try:
            text = data.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise ValueError("The file must be UTF-8 encoded plain text.")

    text = text.strip()
    if not text:
        raise ValueError("The uploaded file contains no readable text.")
    return text


def file_fingerprint(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def secret_fingerprint(secret: str) -> str:
    """Create a non-reversible cache discriminator without retaining the key."""
    return hashlib.sha256(secret.encode("utf-8")).hexdigest()[:12]


def split_document(text: str, source_name: str) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
    )
    chunks = splitter.create_documents(
        [text],
        metadatas=[{"source": source_name}],
    )
    for index, chunk in enumerate(chunks, start=1):
        chunk.metadata["chunk"] = index
    return chunks


def format_context(documents: list[Document]) -> str:
    sections = []
    for position, document in enumerate(documents, start=1):
        chunk = document.metadata.get("chunk", position)
        sections.append(f"[Chunk {chunk}]\n{document.page_content}")
    return "\n\n".join(sections)


def build_question_input(question: str, context: str) -> str:
    return (
        "Use the retrieved document context below to answer the question.\n\n"
        f"DOCUMENT CONTEXT\n{context}\n\n"
        f"QUESTION\n{question.strip()}"
    )


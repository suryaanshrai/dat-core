from pydantic import BaseModel, Field
from langchain_core.documents import Document as LCDocument
from llama_index.core.schema import Document as LIDocument
class Document(BaseModel):

    filepath: str
    page_content: str
    metadata: dict = Field(default_factory=dict)

    def from_langchain_document(cls, doc: LCDocument) -> "Document":
        return cls(filepath=doc.metadata['source'], page_content=doc.page_content, metadata=doc.metadata)
    
    def from_llama_index_document(cls, doc: LIDocument) -> "Document":
        return cls(filepath=doc.metadata['file_path'], page_content=doc.text, metadata=doc.metadata)
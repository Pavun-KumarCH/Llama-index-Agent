from llama_index.core import ServiceContext
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.gemini import GeminiEmbedding

from Components.data_ingestion import load_data
import Components.model_api

import sys
from exception import customexception
from logger import logging

def download_gemini_embedding(model, document):
    """
    Downloads and initializes a Gemini Embedding model for vector embeddings.

    Returns:
    - VectorStoreIndex: An index of vector embeddings for efficient similarity queries.
    """
    try:
        logging.info("Loading The Embedding Model...")
        gemini_embed_model = GeminiEmbedding(model_name = "models/text-embedding-004")
        servicecontext = ServiceContext.from_defaults(llm = model, embed_model = gemini_embed_model, chunk_size = 10000, chunk_overlap = 1000)

        logging.info("")
        index = VectorStoreIndex.from_documents(document, service_context = servicecontext)
        index.storage_context.persist()

        logging.info(f"Textual Data is now convereted into vectordata..!")
        query_engine = index.as_query_engine()
        return query_engine
    except Exception as e:
        raise customexception(e, sys)

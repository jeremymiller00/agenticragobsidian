#!/usr/bin/env python
# coding: utf-8

# # Lesson 1: Router Engine

# Welcome to Lesson 1.
# 
# To access the `requirements.txt` file, the data/pdf file required for this lesson and the `helper` and `utils` modules, please go to the `File` menu and select`Open...`.
# 
# I hope you enjoy this course!

# ## Setup
import sys

from helper import get_openai_api_key
from llama_index.readers.obsidian import ObsidianReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import SummaryIndex, VectorStoreIndex
from llama_index.core.tools import QueryEngineTool
from llama_index.core.query_engine.router_query_engine import RouterQueryEngine
from llama_index.core.selectors import LLMSingleSelector

from utils import configure_logging

logger = configure_logging()

OPENAI_API_KEY = get_openai_api_key()

# load documents
# documents = SimpleDirectoryReader(input_files=["metagpt.pdf"]).load_data()
data_path = "/Users/Jeremy/Data-Science-Vault/Career"
documents = ObsidianReader(data_path).load_data()
logger.info(f"Loaded data from {data_path}")

# ## Define LLM and Embedding model
splitter = SentenceSplitter(chunk_size=1024)
nodes = splitter.get_nodes_from_documents(documents)
logger.info("Split data into nodes")

# Settings.llm = Ollama(model="llama3:latest", request_timeout=200.0)
Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-ada-002")
logger.info("Configured models")

# Define Summary Index and Vector Index over the Same Data
summary_index = SummaryIndex(nodes)
vector_index = VectorStoreIndex(nodes)
logger.info("Defined indices")

# Define Query Engines
summary_query_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",
    use_async=True,
)
vector_query_engine = vector_index.as_query_engine()
logger.info("Defined query engines")


# Define tools and set metadata
summary_tool = QueryEngineTool.from_defaults(
    query_engine=summary_query_engine,
    description=(
        "Useful for summarization questions related to the documents."
    ),
)
vector_tool = QueryEngineTool.from_defaults(
    query_engine=vector_query_engine,
    description=(
        "Useful for retrieving specific context from the documents."
    ),
)
logger.info("Defined query engine tools")

# ## Define Router Query Engine
query_engine = RouterQueryEngine(
    selector=LLMSingleSelector.from_defaults(),
    query_engine_tools=[
        summary_tool,
        vector_tool,
    ],
    verbose=True
)
logger.info("Defined query router engine")


while True:
    query = input("Query ('exit' to exit): ")
    if query == "exit":
        sys.exit(0)
    logger.info(f"Query: {query}")
    response = query_engine.query(query)
    logger.info(f"Response: {response}")
    print(str(response))
    logger.info(f"Sources: {response.source_nodes}")

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# content
text = """
LangChain is a framework designed to simplify the creation of applications using large language models.
It provides modules for prompt templates, chains, memory, agents, and integrations with vector stores.
"""

# text spliting
text_splitter = CharacterTextSplitter(chunk_size=100, chunk_overlap=0)
docs = text_splitter.create_documents([text])

# Create embeddings
embeddings = OpenAIEmbeddings()  # Requires OpenAI API key

# Storing embeddings in FAISS
vectorstore = FAISS.from_documents(docs, embeddings)

# Create QA chain with retriever
qa_chain = RetrievalQA.from_chain_type(
    llm=OpenAI(),              
    chain_type="stuff",        
    retriever=vectorstore.as_retriever()
)

# QA
query = "What is LangChain used for?"
answer = qa_chain.run(query)

print("Q:", query)
print("A:", answer)

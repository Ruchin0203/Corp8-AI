from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('DL Report.pdf')

docs = loader.load()

print(len(docs))

# from langchain_community.document_loaders import PyPDFLoader

# loader = PyPDFLoader('DL Report.pdf')

# docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)
# print(docs[1].metadata)
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# text = """In its broadest sense, text refers to any form of written or spoken communication, including books, articles, emails, text messages, and even spoken words in a conversation. It encompasses the actual words used to convey meaning, regardless of the medium or format. More specifically, "text" can refer to the main body of a written work, distinct from illustrations or footnotes. """

loader = PyPDFLoader('DL Report(Doc loader).pdf')
docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap=0,
    separator=''
)

# result = splitter.split_text(text)
result = splitter.split_documents(docs)

print(result[4].page_content)
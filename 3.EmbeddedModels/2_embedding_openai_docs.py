from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of india",
    "Kolkata is the capital of West Bengale",
    "Paris is the capital of France"
]
result = embedding.embed_documents(documents)

print(str(result))
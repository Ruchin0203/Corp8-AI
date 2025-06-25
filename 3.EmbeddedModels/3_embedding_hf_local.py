from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name = "sentence-transformers/all-MiniLM-L6-v2")

document = [
    "Delhi is the capital of india",
    "Kolkata is the capital of West Bengale",
    "Paris is the capital of France"
]

vector = embeddings.embed_documents(document)

print(str(vector))
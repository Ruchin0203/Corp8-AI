from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv

load_dotenv()

model = ChatHuggingFace()

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = "write a summary for the following poem  - \n {poem}",
    input_variables=["poem"]
)
loader = TextLoader('cricket.txt', encoding='utf-8')

docs = loader.load()

print(type(docs))

print(len(docs))

print(docs[0].page_content)

print(docs[0].metadata)

chain = prompt1 | model | parser

result = chain.invoke({'poem':docs[0].page_content})

print(result)
from langchain_community.document_loaders import WebBaseLoader
from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatHuggingFace()


prompt1 = PromptTemplate(
    template = "Answer the following question \n{Question} \n from the following text  - \n {poem}",
    input_variables=["Question","text"]
)

parser = StrOutputParser()

url = 'https://www.youtube.com/watch?v=bL92ALSZ2Cg&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0'

loader = WebBaseLoader(url)

docs = loader.load()

chain = prompt1 | model | parser

result = chain.invoke({"Question":"what is this page shows","text": docs[0].page_content})

print(result)
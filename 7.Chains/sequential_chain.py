from langchain_huggingface import ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template = 'generate a datailed report on {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'generate a 5 pointer summmary from the following text \n{text}',
    input_variables = ['text']
)

model = ChatHuggingFace()

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'unemployment in India'})

print(result)
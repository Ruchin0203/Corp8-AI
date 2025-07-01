from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template='Explain the joke{responce}',
    input_variables=['responce']
)

model = ChatHuggingFace()

parser = StrOutputParser()

chain = RunnableSequence(prompt1, model, parser, prompt2, model, parser)

result = chain.invoke({'topic':'AI'})

print(result)

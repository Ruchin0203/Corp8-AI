from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough

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

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(joke_gen_chain),
    'explaination' : RunnableSequence(prompt2, model, parser)
})

final_chian = RunnableSequence(joke_gen_chain, parallel_chain)

result = final_chian.invoke({'topic':'cricket'})

print(result)
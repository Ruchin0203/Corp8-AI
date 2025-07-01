from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='write a joke about {topic}',
    input_variables=["topic"]
)

model = ChatHuggingFace()

parser = StrOutputParser()

joke_gen_chain = RunnableSequence(prompt1,model,parser)

paralle_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'word_count': RunnableLambda(word_count) 
})

# another option for Runnablelambda

# paralle_chain = RunnableParallel({
#     'joke': RunnablePassthrough(),
#     'word_count': RunnableLambda(lambda x: len(x.split())) 
# }) 

final_chain = RunnableSequence(joke_gen_chain, paralle_chain)

result = final_chain.invoke({'topic':'cricket'})

final_result = """{} \nword count - {}""".format(result['joke'], result['word_count'])

print(final_result)
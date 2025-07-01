from langchain_huggingface import ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnableLambda,RunnablePassthrough,RunnableBranch

load_dotenv()

def word_count(text):
    return len(text.split())

prompt1 = PromptTemplate(
    template='write a report on {topic}',
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="summarize the following text{text}",
    input_variables=["text"]
)

model = ChatHuggingFace()

parser = StrOutputParser()

report_gen_chian = RunnableSequence(prompt1, model, parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>500, RunnableBranch(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chian, branch_chain)

result = final_chain.invoke({'topic':'AI'})


print(result)
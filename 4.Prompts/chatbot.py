# from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
# from dotenv import load_dotenv

# load_dotenv()

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",   
    # pipeline_kwargs=dict(
    #     temperature=0.5,
    #     max_new_tokens=100  
    # )
)

model = ChatHuggingFace(llm=llm)
# model = ChatOpenAI()

chat_histroy = []
SystemMessage(content = "You are a helpful AI assistant")

while True:
    user_input = input("You: ")
    chat_histroy.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_histroy)
    chat_histroy.append(AIMessage(content=result.content))
    print("AI: ",result.content)

# result = model.invoke("Tell me about you?")

# print(result.content)
print(chat_histroy)
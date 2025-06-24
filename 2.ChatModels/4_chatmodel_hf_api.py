# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
# from dotenv import load_dotenv

# load_dotenv()

# llm = HuggingFaceEndpoint(
#     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#     task="chat-completion"  # <-- critical fix
# )

# model = ChatHuggingFace(llm=llm)

# result = model.invoke("What is the capital of india?")

# print(result.content)

# # from langchain_huggingface import HuggingFaceEndpoint
# # from dotenv import load_dotenv

# # load_dotenv()

# # llm = HuggingFaceEndpoint(
# #     repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
# #     task="text-generation"
# # )

# # result = llm.invoke("What is the capital of India?")

# # print(result)


from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="chat-completion"
)

chat_model = ChatHuggingFace(llm=llm)
response = chat_model.invoke("What is the capital of India?")
print(response.content)


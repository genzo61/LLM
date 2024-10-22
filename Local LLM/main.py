from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

here is the conversation history: {context}

Question: {question}

Answer: 
"""



model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("welcome to the AI chatbot, type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        result = chain.invoke({"context": context, "question": user_input})
        print("bot :", result)
        context += f"\nUser: {user_input}\nBot: {result}"
    
if __name__ == "__main__":
    handle_conversation()   
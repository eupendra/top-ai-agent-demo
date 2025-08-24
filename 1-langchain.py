from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# Simple LangChain example
llm = ChatOpenAI(model="gpt-4.1-nano")
prompt = ChatPromptTemplate.from_template("Summarize {framework} in one sentence.")

chain = prompt | llm
response = chain.invoke({"framework": "LangChain"})
print(response.content)
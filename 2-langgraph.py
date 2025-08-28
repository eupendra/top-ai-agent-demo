from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o-mini")

# Define workflow nodes
def process_input(state):
    response = llm.invoke(f"Explain what {state['input']} in one clear sentence.")
    return {"input": state["input"], "output": response.content}

# Simple example with only one node
workflow = StateGraph(dict)
workflow.add_node("process", process_input)

# connecting nodes. Using START and END to complete the graph.
workflow.add_edge(START, "process")
workflow.add_edge("process", END)

app = workflow.compile()
result = app.invoke({"input": "What is LangGraph!", "output": ""})
print(result["output"])

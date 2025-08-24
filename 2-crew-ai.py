from crewai import Agent, Task, Crew
from langchain_openai import ChatOpenAI

# Simple CrewAI example
llm = ChatOpenAI(model="gpt-4.1-nano")

agent = Agent(
    role="Framework Expert",
    goal="Summarize AI frameworks",
    backstory="Expert in AI agent frameworks",
    llm=llm
)

task = Task(
    description="Summarize CrewAI framework in one sentence",
    expected_output="One sentence summary",
    agent=agent
)

crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
print(result)
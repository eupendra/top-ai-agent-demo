from crewai import Agent, Task, Crew

# Create an agent
agent = Agent(
    role="AI Expert",
    goal="Explain AI frameworks simply",
    backstory="You are an expert at explaining complex topics clearly."
)

# Create a task
task = Task(
    description="CrewAI",
    expected_output="One clear sentence.",
    agent=agent
)

# Create and run crew
crew = Crew(agents=[agent], tasks=[task])
result = crew.kickoff()
print(result)
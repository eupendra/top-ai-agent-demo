from autogen import ConversableAgent, LLMConfig

llm_config = LLMConfig(api_type="openai", model="gpt-4.1-nano")

with llm_config:
    assistant = ConversableAgent(
        name="assistant",
        system_message="Summarize the given framework in one sentence.",
    )

response = assistant.run(
    message="autogen.",
    max_turns=1,
)
response.process()
print(response.messages)
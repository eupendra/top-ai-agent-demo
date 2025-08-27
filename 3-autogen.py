import autogen

# Simple AutoGen example
config_list = [{"model": "gpt-4.1-nano"}]

assistant = autogen.AssistantAgent(
    name="assistant",
    system_message="You are an AI framework expert. Provide one sentence summaries.",
    llm_config={"config_list": config_list}
)

user_proxy = autogen.UserProxyAgent(
    name="user",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=0,
    code_execution_config=False
)

# Start conversation
user_proxy.initiate_chat(
    assistant,
    message="AutoGen"
)

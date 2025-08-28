import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.functions import KernelArguments

async def main():
    kernel = Kernel()
    kernel.add_service(OpenAIChatCompletion(ai_model_id="gpt-4.1-nano"))
    
    summarize = kernel.add_function(
        prompt="Summarize {{$framework}} in one sentence.",
        function_name="summarize",
        plugin_name="main"
    )
    
    result = await kernel.invoke(summarize, KernelArguments(framework="Semantic Kernel"))
    print(str(result))

asyncio.run(main())
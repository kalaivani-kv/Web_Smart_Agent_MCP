import os
import asyncio
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerHTTP
import logfire

logfire.configure()
logfire.instrument_pydantic_ai()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

server = MCPServerHTTP(url='http://localhost:3001/sse')  
agent = Agent('groq:llama-3.3-70b-versatile', mcp_servers=[server])  


async def main():
    async with agent.run_mcp_servers():  
        result = await agent.run('How many days between 2000-01-01 and 2025-03-18?')
    print(result.output)
    #> There are 9,208 days between January 1, 2000, and March 18, 2025.

asyncio.run(main())
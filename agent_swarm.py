from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.llms import ChatMessage
from llama_index.core.memory import ChatMemoryBuffer

agent_dict = {}

class Agent:
    def __init__(self, graph, levels, llm):
        self.levels = levels
        self.graph = graph
        self.llm = llm

        self.memory = ChatMemoryBuffer.from_defaults(token_limit=40000)

    
    def generate_documentation(self):
        


memory = ChatMemoryBuffer.from_defaults(token_limit=40000)
memory.put(ChatMessage(role="user", content="Hello, world!"))
memory.put(ChatMessage(role="assistant", content="Hello, world to you too!"))
chat_history = memory.get()

agent = FunctionAgent(llm=llm, tools=tools)

# passing in the chat history overrides any existing memory
response = await agent.run(
    "<question that invokes tool>", chat_history=chat_history
)




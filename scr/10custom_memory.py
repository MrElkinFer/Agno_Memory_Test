from agno.agent import Agent
from agno.memory.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory, SessionSummarizer, MemoryManager
from agno.models.google.gemini import Gemini
from agno.models.openai.chat import OpenAIChat
from rich.pretty import pprint

# Creación base de datos:
base_datos = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.bd")

# Manejador de memmoria:
manejador_memoria = MemoryManager(
    model=Gemini(id="gemini-2.0-flash-001"),
    additional_instructions="""
    IMPORTANTE: no guardar datos el nombre del usuario, solo referirse como el "usuario"
    """,
)
# Resumen de sesión:
resumen_session = SessionSummarizer(
    model=OpenAIChat("gpt-4o"),
    additional_instructions="Hacer que el resumen sea informal y conversacional",
)

# Creación de memoria:
memoria = Memory(
    db=base_datos,
    memory_manager=manejador_memoria,
    summarizer=resumen_session,
)

memoria.clear()

john_doe_id = "john_doe@example.com"

agente = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    memory=memoria,
    enable_user_memories=True,
    enable_session_summaries=True,
    user_id=john_doe_id,
)

agente.print_response(
    "My name is John Doe and I like to swim and play soccer.", stream=True
)

agente.print_response("I dont like to swim", stream=True)

memories = memoria.get_user_memories(user_id=john_doe_id)

print("John Doe's memories:")
pprint(memories)

summary = agente.get_session_summary()
print("Session summary:")
pprint(summary)

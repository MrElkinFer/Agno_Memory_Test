from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.models.google.gemini import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools
from rich.pretty import pprint

# Creación base de datos:
base_datos = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.bd")

# Creación de memoria:
memoria = Memory(db=base_datos)

# Limpieza de memorias anteriores:
memoria.clear()

# Datos usuario:
jhon_doe_id = "jhon_doe@example.com"


# Creación de agentes:

agente_chat = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    memory=memoria,
    user_id=jhon_doe_id,
    # Aquí está la propiedad importante:
    enable_user_memories=True,
    description="Eres un agente muy útil que le gusta hablar con los usuarios",
)

agente_investigador = Agent(
    model=OpenAIChat(id="gpt-4o"),
    memory=memoria,
    user_id=jhon_doe_id,
    # Aquí está la propiedad importante:
    enable_user_memories=True,
    # Herramienta de research
    tools=[DuckDuckGoTools(cache_results=True)],
    description="Eres un agente de investigación muy útil que puede ayudar a los usuarios con sus preguntas de investigación",
)

# Creando y mostrando memorias desde el agente con llm Gemini:

agente_chat.print_response(
    "Hola mi nombre es Jhon Doe y me gusta hacer senderismo los fines de semana",
    stream=True,
    user_id=jhon_doe_id,
)

agente_chat.print_response(
    "Cuáles son mis hobbies?",
    stream=True,
    user_id=jhon_doe_id,
)

# Mostrando las memorias:
print("L55 Memorias de Jhon Doe: ")
memorias = memoria.get_user_memories(user_id=jhon_doe_id)
pprint(memorias)


# Creando y mostrando memorias desde el llm openai:

agente_investigador.print_response(
    "Me encantaria saber las últimas noticias a cerca de la computación cuantica ",
    stream=True,
    user_id=jhon_doe_id,
)

print("L72 Memorias de Jhon Doe: ")
memorias = memoria.get_user_memories(user_id=jhon_doe_id)
pprint(memorias)

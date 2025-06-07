from agno.agent.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai import OpenAIChat
from agno.storage.sqlite import SqliteStorage
from rich.pretty import pprint


from dotenv import load_dotenv
load_dotenv()

# Se crea la db en sqlite:
memoria_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

# Se crea la memoria: señalando cuál es la db.
memoria = Memory(db=memoria_db)

# Para guardar el historial se debe crear una sesión
id_sesion = "session_1"

# Se crea el identificador del usuario:
jhon_doe_id = "jhon_doe@example.com"


agente = Agent(
    model=OpenAIChat(id="gpt-4o"),
    memory=memoria,
    storage=SqliteStorage(
        table_name="agent_sessions",
        db_file="tmp/persisting_memory.db",
    ),
    enable_user_memories=True,
)

agente.print_response(
    "Mi nombre es Jhon Doe y me gusta hacer senderismo en montañas los fines de semana",
    stream=True,
    user_id=jhon_doe_id,
    session_id=id_sesion,
)

agente.print_response(
    "Cuáles son mis hobbies?",
    stream=True,
    user_id=jhon_doe_id,
    session_id=id_sesion,
)

# Imprimientdo el historial del chat
session_run = memoria.runs[id_sesion][-1]
pprint(session_run)

agente.print_response(
    "Bueno, ya no me gusta hacer senderismo, en cambio me gusta jugar al fútbol.",
    stream=True,
    user_id=jhon_doe_id,
    session_id=id_sesion,
)

memorias = memoria.get_user_memories(user_id=jhon_doe_id)
print("L52 Memorias de Jhon:")
pprint(memorias)


# También se pueden obtener las memorias del usuario desde el agente:

memorias = agente.get_user_memories(user_id=jhon_doe_id)
print("L59 Memorias de Jhon Doe desde el agente:")
pprint(memorias)

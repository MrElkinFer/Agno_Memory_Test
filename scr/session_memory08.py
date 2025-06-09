from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.memory.v2.summarizer import SessionSummarizer
from agno.models.google.gemini import Gemini
from rich.pretty import pprint

db_memoria = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

memoria = Memory(
    db=db_memoria,
    summarizer=SessionSummarizer(model=Gemini(id="gemini-2.0-flash-001"))
)

memoria.clear()

agente = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    memory=memoria,
    enable_user_memories=True,
    enable_session_summaries=True,
)

agente.print_response(
    "Hola mi nombre es Jhon Doe y me gusta hacer senderismo los fines de semana",
    stream=True,
)
agente.print_response(
    "Cuáles son mis hobbies?",
    stream=True,
)

memorias = memoria.get_user_memories()
print("L34 Memorias de Jhon Doe: ")
pprint(memorias)
memorias_sesion = agente.get_session_summary()
pprint(memorias_sesion)


# Creando una sesión más para Mark Gonzales:

session_id_2 = "1002"
mark_gonzales_id = "mark@example.com"

agente.print_response(
    "Hola mi nombre es Mark Gonzales me gusta el ánime y los videojuegos",
    stream=True,
    user_id=mark_gonzales_id,
    session_id=session_id_2,
)
agente.print_response(
    "Cuáles son mis hobbies?",
    stream=True,
    user_id=mark_gonzales_id,
    session_id=session_id_2,
)

memorias = memoria.get_user_memories(user_id=mark_gonzales_id)
print("L59 Memorias de Mark Gonzales: ")
pprint(memorias)
memorias_sesion = agente.get_session_summary(
    session_id=session_id_2,
    user_id=mark_gonzales_id,
)
pprint(memorias_sesion)

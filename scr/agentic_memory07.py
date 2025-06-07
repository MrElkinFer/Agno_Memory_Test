from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from rich.pretty import pprint

# crear bbdd:
memoria_bd = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

# crear memoria del agente:
memoria = Memory(db=memoria_bd)

# Limpiando la memoria de ejemplos pasados:
memoria.clear()

# Creación del agente con configuración de memoria tipo "Agentic":

agente = Agent(
    model=Gemini(id="gemini-2.0-flash-001"),
    memory=memoria,
    enable_agentic_memory=True,
)

# Creación del identificador del usuario Jhon Doe:
jhon_doe_id = "jhon_do@example.com"

agente.print_response(
    "Mi nombre es Jhon Doe me gusta hacer senderismo en la montañas los fines de semana",
    stream=True,
    user_id=jhon_doe_id,
)

agente.print_response(
    "Cuáles son mis hobbies?",
    stream=True,
    user_id=jhon_doe_id,
)

# Trayendo y mostrando las memorias del usuario en consola:
memorias = memoria.get_user_memories(user_id=jhon_doe_id,)
print("L41 Memorias de Jhon Doe:")
pprint(memorias)

# Dandole un prompt donde se induzca la eliminación de una memoria vieja (senderismo):

agente.print_response(
    "Hola, quiero que borres todos los datos a cerca de mí",
    stream=True,
    user_id=jhon_doe_id,
)

# Trayendo y mostrando las memorias del usuario en consola, para poder ver si fueron eliminadas:
memorias = memoria.get_user_memories(user_id=jhon_doe_id,)
print("L54 Mostrando la eliminación de memorias de Jhon Doe:")
pprint(memorias)

# Creando y mostrando nuevas memorias a cerca de nuevo hobbie pintura. Después cambiandolas por otras (dibujo):
agente.print_response(
    "Mi nombre es Jhon Doe y me encanta pintar!!!",
    stream=True,
    user_id=jhon_doe_id,
)
memorias = memoria.get_user_memories(user_id=jhon_doe_id,)
print("L64 Mostrando las memorias de Jhon Doe nuevas:")
pprint(memorias)


agente.print_response(
    "Resulta que no me gusta más la pintura, ahora me gusta dibujar",
    stream=True,
    user_id=jhon_doe_id,
)

memorias = memoria.get_user_memories(user_id=jhon_doe_id,)
print("L75 Mostrando las memorias de Jhon Doe nuevas:")
pprint(memorias)

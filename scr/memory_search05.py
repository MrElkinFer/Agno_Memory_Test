from agno.memory.v2 import Memory, UserMemory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.models.google.gemini import Gemini
from rich.pretty import pprint

# creando la BBDD local:
memoria_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")
# Limpiando la memoria de la DDBB de anteriores ejecuciones:
memoria_db.clear()

# Creando la memoria
memoria = Memory(model=Gemini(id="gemini-2.0-flash-001"), db=memoria_db)

# usuario Jhon Doe:
jhon_doe_id = "jhon_doe@example.com"

# Agregando memorias del usuario:

memoria.add_user_memory(
    memory=UserMemory(
        memory="Al usuario le gusta hacer senderismo en montañas los fines de semana",),
    user_id=jhon_doe_id,
)

memoria.add_user_memory(
    memory=UserMemory(
        memory="El usuario disfruta de leer novelas de ciencia ficción antes de ir a la cama",),
    user_id=jhon_doe_id,
)

print("L32 Memorias de Jhon Doe:")
# Otra forma de mostrar las memorias: Muestra todas las memorias sin importar el usuario:
pprint(memoria.memories)


# Aqui empieza la busqueda:

busqueda_memorias = memoria.search_user_memories(
    user_id=jhon_doe_id,
    limit=1,
    retrieval_method="last_n")

print("L40 Última memoria de Jhon Doe: (last_n)")
pprint(busqueda_memorias)

busqueda_memorias = memoria.search_user_memories(
    user_id=jhon_doe_id,
    limit=1,
    retrieval_method="first_n"
)

print("L48 Primera memoria de Jhon Doe: (fist_n)")
pprint(busqueda_memorias)

busqueda_memorias = memoria.search_user_memories(
    user_id=jhon_doe_id,
    # Aquí viene lo interesante, no hay limite de busqueda y se hace una consulta (query):
    query="Qué es lo que al usuario le gusta hacer los fines de semana?",
    retrieval_method="agentic"
)

print("L62 Al usuario Jhon Doe que le gusta hacer los FDS?: ")
pprint(busqueda_memorias)

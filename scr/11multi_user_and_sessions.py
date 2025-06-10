import asyncio
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.models.openai.chat import OpenAIChat
from agno.storage.sqlite import SqliteStorage
# Memoria local para el agente:
agent_storage = SqliteStorage(
    table_name="agent_sessions",
    db_file="tmp/persistent_memory.db"
)

# Base de datos local para el usuario
memory_db = SqliteMemoryDb(
    table_name="memory",
    db_file="tmp/memory.db"
)

# Memoria para el usuario:
memory = Memory(db=memory_db)

# Limpiar memoria de pruebas anteriores:
memory.clear()

# Usuarios:
user_1_id = "user_1@example.com"
user_2_id = "user_2@example.com"
user_3_id = "user_3@example.com"

# Sesiones de los usuarios:
user_1_session_1_id = "user1_session_1"
user_1_session_2_id = "user1_session_2"
user_2_session_1_id = "user2_session_1"
user_3_session_1_id = "user3_session_1"

agente = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # TODO: es la memoria del agente?
    storage=agent_storage,
    memory=memory,
    enable_user_memories=True,
)


async def run_agente():
    await agente.aprint_response(
        "Mi nombre es Mark Gonzales y me gusta el manga y los videojuegos",
        user_id=user_1_id,
        session_id=user_1_session_1_id,
    )

    await agente.aprint_response(
        "También me divierte mucho leer manga y jugar videojuegos.",
        user_id=user_1_id,
        session_id=user_1_session_1_id,
    )
    # Chat con el usuario 1 Mark en la sesión 2:
    await agente.aprint_response(
        "Yo voy a una pelicula esta noche.",
        user_id=user_1_id,
        session_id=user_1_session_2_id,
    )
    # Chat con el usuario 2 en la sesión 1:
    await agente.aprint_response(
        "Hola mi nombre es Jhon Doe.",
        user_id=user_2_id,
        session_id=user_2_session_1_id,
    )
    await agente.aprint_response(
        "Planeo hacer senderismo esete fin de semana.",
        user_id=user_2_id,
        session_id=user_2_session_1_id,
    )
    # Chat con el usuario 3 Jane:
    await agente.aprint_response(
        "Hola mi nombre es Jane Smith",
        user_id=user_3_id,
        session_id=user_3_session_1_id,
    )

    await agente.aprint_response(
        "Mañana voy a ir al gimnasio.",
        user_id=user_3_id,
        session_id=user_3_session_1_id,
    )
    # Volvemos al usuario 1:
    await agente.aprint_response(
        "Qué me sugieres hacer este fin de semana?",
        user_id=user_1_id,
        session_id=user_1_session_1_id,
    )


if __name__ == "__main__":
    asyncio.run(run_agente())

    user_1_memories = memory.get_user_memories(user_id=user_1_id)
    print("Memorias del usuario 1:")
    for i, m in enumerate(user_1_memories):
        print(f"{i}: {m.memory}")

    user_2_memories = memory.get_user_memories(user_id=user_2_id)
    print("User 2's memories:")
    for i, m in enumerate(user_2_memories):
        print(f"{i}: {m.memory}")

    user_3_memories = memory.get_user_memories(user_id=user_3_id)
    print("User 3's memories:")
    for i, m in enumerate(user_3_memories):
        print(f"{i}: {m.memory}")

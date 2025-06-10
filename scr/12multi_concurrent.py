import asyncio
from agno.agent import Agent
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.storage.sqlite import SqliteStorage
from agno.memory.v2.memory import Memory
from agno.models.google.gemini import Gemini
from agno.models.openai.chat import OpenAIChat

# Creación base de datos:
base_datos = SqliteMemoryDb(
    table_name="memory",
    db_file="tmp/memory.db"
)

# Creacion de memoria para el agente:
almacenamiento_agente = SqliteStorage(
    table_name="agent_sessions",
    db_file="tmp/persistent_memory.db"
)

# Memoria para los usuarios:
memoria = Memory(
    model=Gemini(id="gemini-2.0-flash-001"),
    db=base_datos,
)

# Borrando registros de pruebas anteriores:
memoria.clear()

# Estructura de sesiones y usuarios:
# Usuarios:
usuario_1 = "user_1@example.com"
usuario_2 = "user_2@example.com"
usuario_3 = "user_3@example.com"
# Sesiones:
usuario1_sesion1_id = "User_1_session_1"
usuario1_sesion2_id = "User_1_session_2"
usuario2_sesion1_id = "User_2_session_1"
usuario3_sesion1_id = "User_3_session_1"

# Agente conversador:
agente_charla = Agent(
    model=OpenAIChat(id="gpt-4o"),
    memory=memoria,
    storage=almacenamiento_agente,
    enable_user_memories=True,
)


async def conversacion_usuario_1():
    # Sesión 1:
    await agente_charla.arun(
        "Mi nombre es  Mark Gonzales, me gusta el anime y los videojuegos.",
        user_id=usuario_1,
        session_id=usuario1_sesion1_id
    )
    await agente_charla.arun(
        "También me gusta leer manga y jugar juegos de video",
        user_id=usuario_1,
        session_id=usuario1_sesion1_id,
    )
    # Sesión 2:
    await agente_charla.arun(
        "Esta noche salgo a ver puelícula.",
        user_id=usuario_1,
        session_id=usuario1_sesion2_id,

    )
    print("Usuario 1 resuelto!:")

# Manejador de conversación con el usuario 2:


async def conversacion_usuario_2():
    # Usuario 2 en su sesión:
    await agente_charla.arun(
        "Hola mi nombre es John Doe.",
        user_id=usuario_2,
        session_id=usuario2_sesion1_id,
    )
    await agente_charla.arun(
        "Estoy planeando hacer senderismo el fin de semana.",
        user_id=usuario_1,
        session_id=usuario2_sesion1_id,
    )

    print("Usuario 2 resuelto: ")


async def conversacion_usuario_3():
    await agente_charla.arun(
        "Mi nombre es Jane Smith.",
        user_id=usuario_3,
        session_id=usuario3_sesion1_id,
    )
    await agente_charla.arun(
        "Pienso ir mañana al gimnasio.",
        user_id=usuario_3,
        session_id=usuario3_sesion1_id
    )
    print("Usuario 3 resuelto.")


# Función general para todos los usuarios:
async def ejecucion_concurrencia_agentes():
    await asyncio.gather(
        conversacion_usuario_1(),
        conversacion_usuario_2(),
        conversacion_usuario_3(),
    )


if __name__ == "__main__":
    asyncio.run(ejecucion_concurrencia_agentes())

    memorias_usuario_1 = memoria.get_user_memories(user_id=usuario_1)
    print("Memorias del usuario 1:")
    for i, m in enumerate(memorias_usuario_1):
        print(f"{i}: {m.memory}")

    memorias_usuario_2 = memoria.get_user_memories(user_id=usuario_2)
    print("Memorias del usuario 2:")
    for i, m in enumerate(memorias_usuario_2):
        print(f"{i}: {m.memory}")

    memorias_usuario_3 = memoria.get_user_memories(user_id=usuario_3)
    print("Memorias del usuario 1:")
    for i, m in enumerate(memorias_usuario_3):
        print(f"{i}: {m.memory}")

from agno.memory.v2 import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.manager import MemoryManager
from agno.models.openai import OpenAIChat
from agno.models.google import Gemini
from agno.models.message import Message
from rich.pretty import pprint
from dotenv import load_dotenv
load_dotenv()


# Creamos la memoria en database:
memoria_db = SqliteMemoryDb(table_name="memory", db_file="tmp/memory.db")

# Reseteamos la memoria para que no tenga datos del archivo "persistencia_memoria03.py":
memoria_db.clear()

#
memoria = Memory(
    model=Gemini(id="gemini-2.0-flash-001"),
    memory_manager=MemoryManager(
        model=Gemini(id="gemini-2.0-flash-001"),
        memory_capture_instructions="""\ 
        Los recuerdos solo deben incluir detalles sobre los intereses académicos del usuario.
        Incluya únicamente las asignaturas que le interesan.
        Ignore nombres, aficiones e intereses personales.
        """
    ),
    db=memoria_db,
)

jhon_doe_id = "jhon_doe@example.com"
# ingresando nuevas memorias de Jhon Doe:
memoria.create_user_memories(message="""\
                             Mi nombre es Jhon Doe. 
                             
                             Yo disfruto hacer cenderismo en las montañas los fines de semana, 
                             leo novelas de ciencia ficción antes de ir a la cama, 
                             cocino nuevas recetas de diferentes culturas,
                             juego ajedrez con mins amigos.

                             Estoy interesado en aprender a cerca de la historia de el unverso y otro temas astronómicos """,
                             user_id=jhon_doe_id,
                             )
# Imprimimos que hay en la memoria
memorias = memoria.get_user_memories(user_id=jhon_doe_id)
print("L45 Memorias de Jhon Doe: ")
pprint(memorias)

# Uasndo el administrador de memoria por defecto con Jane Mary Doe:
memoria = Memory(model=OpenAIChat(id="gpt-4o"), db=memoria_db)
jane_doe_id = "jane_doe@example.com"

# Pasando un grupo de mensajes para agregar a la memoria
memoria.create_user_memories(
    messages=[
        Message(role="user", content="Hola, cómo estás?"),
        Message(role="assistant", content="Estoy bien, gracias!!!"),
        Message(role="user", content="de qué eres capaz?"),
        Message(role="assistant",
                content="Puedo ayudarte con tus tareas y resolver preguntas a cerca del universo."),
        Message(role="user", content="Mi nombre es Jane Doe"),
        Message(role="user", content="Me gusta jugar ajedrez"),
        Message(role="user", content="De hecho, olvidate de que me gusta jugar ajedrez. Distruto más jugando a juegos de mesa como Calabozos y Dragones"),
        Message(role="user", content="También me interesa aprender a cerca de la historia del universo y otros temas de astronomía"),
        Message(role="assistant", content="Eso es genial!!"),
        Message(role="user", content="Yo estoy muy interesada en aprender de física. Cuentame a cerca de mecánica cuantica"),
    ],
    user_id=jane_doe_id,
)
# Mostrando las memorias de Jane:
memorias = memoria.get_user_memories(user_id=jane_doe_id)
print("L72 Memorias de Jane:")
pprint(memorias)

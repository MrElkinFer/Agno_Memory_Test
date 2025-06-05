from agno.memory.v2 import Memory, UserMemory
from rich.pretty import pprint
from dotenv import load_dotenv

load_dotenv()

memoria = Memory()

# Agregando memoria para el usuario por defecto
memoria.add_user_memory(
    memory=UserMemory("El nombre del Usuario es Jhon Doe", topics=["name"])
)
print("L13: Memorias: ")
pprint(memoria.memories)

# Agregando memorias para Jane Doe
jane_doe_id = "jane_doe@example.com"
print(f"\n User: {jane_doe_id}")

memoria_id_1 = memoria.add_user_memory(
    memory=UserMemory(
        memory="El nombre del usuario es Jane Doe", topics=["name"]),
    user_id=jane_doe_id,
)

memoria_id_2 = memoria.add_user_memory(
    memory=UserMemory("A ella la gusta jugar tennis", topics=["Hobbies"]),
    user_id=jane_doe_id,
)

memorias = memoria.get_user_memories(user_id=jane_doe_id)
print("Memorias: ")
pprint(memorias)

# Borrando memorias a Jane Doe:
print("\nBorrando memoria a cerca del tennis")
memoria.delete_user_memory(user_id=jane_doe_id, memory_id=memoria_id_2)
print("\n Memoria borrada\n")

memorias = memoria.get_user_memories(user_id=jane_doe_id)
print("\n Memorias actuales de Jane Doe: \n")
pprint(memorias)

# Remplazando las memorias de Jane Doe:
print("\nRemplazando Memorias: \n")
memoria.replace_user_memory(
    memory_id=memoria_id_1,
    memory=UserMemory(
        memory="El nombre de la usuaria es Jane Mary Doe", topics=["name"]),
    user_id=jane_doe_id,
)
print("Memoria remplazada: ")
memorias = memoria.get_user_memories(user_id=jane_doe_id)
print("Memorias de Jane Doe: ")
pprint(memorias)

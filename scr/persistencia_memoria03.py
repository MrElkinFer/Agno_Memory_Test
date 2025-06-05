from typing import List

from agno.memory.v2.db.schema import MemoryRow
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.memory.v2.memory import Memory
from agno.memory.v2.schema import UserMemory

memoria_db = SqliteMemoryDb(
    table_name="tabla_memoria", db_file="tmp/memory.db")
memoria = Memory(db=memoria_db)

jhon_doe_id = "jhon_doe@example.com"

# Primera ejecución:

memoria.add_user_memory(
    memory=UserMemory("El nombre del usuario es Jhon Francis Doe"),
    user_id=jhon_doe_id,
)

# Correr en una segunda ejecución:
memoria.add_user_memory(
    memory=UserMemory("El usuario trabaja en una compañía de software"),
    user_id=jhon_doe_id,
)

memorias: List[MemoryRow] = memoria_db.read_memories()
print("Todas las memorias en la base de datos: ")
for i, m in enumerate(memorias):
    print(f"{i}: {m.memory['memory']} ({m.last_updated})")


'''Resultados de las 4 primeras ejecuciones:

(.venv) PS E:\Agno\AgnoMemoryTest> python .\scr\persistencia_memoria.py
Todas las memorias en la base de datos:
0: El nombre del usuario es Jhon Doe (2025-06-05 23:51:29)
Todas las memorias en la base de datos:
0: El nombre del usuario es Jhon Doe (2025-06-05 23:51:53)
1: El usuario trabaja en una coma (2025-06-05 23:51:53)
2: El nombre del usuario es Jhon Doe (2025-06-05 23:51:29)
(.venv) PS E:\Agno\AgnoMemoryTest> python .\scr\persistencia_memoria.py
Todas las memorias en la base de datos:
0: El nombre del usuario es Jhon Doe (2025-06-05 23:52:13)
1: El usuario trabaja en una coma (2025-06-05 23:52:13)
2: El nombre del usuario es Jhon Doe (2025-06-05 23:51:53)
3: El usuario trabaja en una coma (2025-06-05 23:51:53)
4: El nombre del usuario es Jhon Doe (2025-06-05 23:51:29)
(.venv) PS E:\Agno\AgnoMemoryTest> python .\scr\persistencia_memoria.py
Todas las memorias en la base de datos: 
0: El nombre del usuario es Jhon Francis Doe (2025-06-05 23:52:55)
1: El usuario trabaja en una compañía de software (2025-06-05 23:52:55)
2: El nombre del usuario es Jhon Doe (2025-06-05 23:52:13)
3: El usuario trabaja en una coma (2025-06-05 23:52:13)
4: El nombre del usuario es Jhon Doe (2025-06-05 23:51:53)
5: El usuario trabaja en una coma (2025-06-05 23:51:53)
6: El nombre del usuario es Jhon Doe (2025-06-05 23:51:29)
(.venv) PS E:\Agno\AgnoMemoryTest> '''

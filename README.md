## Introducción:

Desarrollo basado en los ejemplos para la creación de agentes con agno, disponibles en [Agno Documents](https://docs.agno.com/examples/concepts/memory/00-built-in-memory "Build-in     Memory")

# 01 Buid-in memory (incorpororación de memoria)

Este queda en el archivo "buildLn_memory01.py"

# 02 Operaciones de memoria independientes (Standalone Memory Operations)

las operaciones hacen regerencia a:

- Remplazar memorias específicas.
- Agregar memorias.
- Borrar memorias.
- llamar memorias específicas.

Se encuentra en el archivo "crud_operations02.py"

# 03 Persistencia en memoria con SQLite (Persistent memory with SQLite)

Este ejemplo de agno muestra como usar la clase memory para crear persistencia en memoria

El archivo asociado es "persistencia_memoria03.py"

# 04 Creación de memorias a medida (Custum memory creation)

Muestra como crear memorias de usuario con un agente IA usando cada texto o una lista de textos se usó Gemini y ChatGPT.

El archivo asociado es: "custom_memory04.py"

# 05 Buscando en memoria (Memory Search):

Muestra como buscar en las memorias de usuario mediante diferentes métodos de busqueda.

- last_n: buscando los últimos n elementos.
- first_n: buscando los primeros n elementos.
- semantic: Busqueda por coincidencia semantica.

El archivo asociados es: "memory_search05.py"

# 06 Persistencia en memoria con Agente: (Agent whit memory):

Muestra cómo se configura el agente para que conserve su memoria después de cada ejecución.

Específicamente con la **propiedad enable_user_memory=True** de la configuración del agente

El archivo asociado es: "agent_whit_memory06.py"

# 07 Persistencia de memoria durante la ejecución (Agentic memory):

Muestra la configuración que se debe dar al agente para que cree, edite y borre memorias

Específicamente con la propiedad **enable_agentic_memory=True** en la configuración del agente.

El archivo asociado es: ".py"

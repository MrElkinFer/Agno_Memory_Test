## Introducción:

Desarrollo basado en los ejemplos para la creación de agentes con agno, disponibles en [Agno Documents](https://docs.agno.com/examples/concepts/memory/00-built-in-memory "Build-in     Memory")

---

# 01 Incorpororación de memoria (Buid-in memory )

Este queda en el archivo "buildLn_memory01.py"

---

# 02 Operaciones de memoria independientes (Standalone Memory Operations)

las operaciones hacen regerencia a:

- Remplazar memorias específicas.
- Agregar memorias.
- Borrar memorias.
- llamar memorias específicas.

Se encuentra en el archivo "crud_operations02.py"

---

# 03 Persistencia en memoria con SQLite (Persistent memory with SQLite)

Este ejemplo de agno muestra como usar la clase memory para crear persistencia en memoria

El archivo asociado es "persistencia_memoria03.py"

---

# 04 Creación de memorias a medida (Custum memory creation)

Muestra como crear memorias de usuario con un agente IA usando cada texto o una lista de textos se usó Gemini y ChatGPT.

El archivo asociado es: "custom_memory04.py"

---

# 05 Buscando en memoria (Memory Search):

Muestra como buscar en las memorias de usuario mediante diferentes métodos de busqueda.

- last_n: buscando los últimos n elementos.
- first_n: buscando los primeros n elementos.
- semantic: Busqueda por coincidencia semantica.

El archivo asociados es: "memory_search05.py"

---

# 06 Persistencia en memoria con Agente: (Agent whit memory):

Muestra cómo se configura el agente para que conserve su memoria después de cada ejecución.

Específicamente con la **propiedad enable_user_memory=True** de la configuración del agente

El archivo asociado es: **"agent_whit_memory06.py"**

---

# 07 Persistencia de memoria durante la ejecución (Agentic memory):

Muestra la configuración que se debe dar al agente para que cree, edite y borre memorias

Específicamente con la propiedad **enable_agentic_memory=True** en la configuración del agente.

El archivo asociado es: **"agentic_memory07.py"**

---

# 08 Agentes con memoria de sesiones (Agents with session summaries)

El ejemplo muestra cómo crear resumenes de sesiones desde la configuración del agente en Agno.

Utilizado la configuración **"enable_session_summaries= True**

El archivo asociado es: **"session_memory08.py"**

---

# 09 Multiples Agentes compartiendo memoria: (Multi Agents sharing memory)

Se muestra cómo varios agentes puende usar la misma memoria para atender una tarea.

El archivo asociado es: **agent_share_memory09.py**

---

# 10 Manipulación del administrador de memoria y los resumenes de sesión. (Custom memory):

El archivo asociado es: **10custom_memory.py**

Se Muestra cómo hacer para que el manejador de memoria **Memory Manager** y el resumen de sesión **resumen summarizer**, puedan se personalizados. Para el ejemplo se busca que el manejador de memoria no guarde el nombre del usuario y por parte de el generador de resumen tenga un tono "informal" al realizar su tarea.

Para esto se utiliza:

```Python
  # Libreria
  from agno.memory.v2.memory import Memory, SessionSummarizer, MemoryManager
```

el archivo asociado a este ejemplo es: "**10custom_memory.py"**

---

# 11 Manejo de memoria con multiples usuarios en multiples sesiones (Multi-Users Multi-Sessions Chat):

El ejemplo muestra cómo se debe configurar para gestionar la memoria cuando se tiene multiples usuarios y multiples sesiones trabajando al tiempo. En otras palabras, como gestionar la memoria de los agentes asíncronamente "Async".

Lo importante del ejemplo es ver el uso de las herramientas propias de agno para el manejo asíncrono, en este caso: **aprint_response()**, para el manejo de memoria.

**NOTA:** Es el ejemplo más costoso en recursos para el LLM.

El arichivo asociado a este ejemplo es: **11multi_user_multisessions.py**

---

# 12 Manejo de multiples usuarios en multiples sesiones con concurrencia (Multi-User Multi-Session Chat Concurrent)

El archivo asociado a este ejemplo es: **12multi_concurrent.py**

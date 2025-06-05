from agno.agent import Agent
from agno.models.openai import OpenAIChat
from rich.pretty import pprint
from dotenv import load_dotenv

load_dotenv()


agente = Agent(
    model=OpenAIChat(id="gpt-4o"),
    # para que recuerde el historial de conversaciones.
    add_history_to_messages=True,
    num_history_responses=3,  # número de respuestas para agregar al los mensajes
    description="Eres un asistente muy útil que siempre responde de manera educada optimista y positiva"
)

agente.print_response(
    "dime dos peliculas con buena valoración general", stream=True)

pprint(
    [
        m.model_dump(include={"role", "content"})
        for m in agente.get_messages_for_session()
    ]
)
agente.print_response("cual fue mi primer mensaje?", stream=True)

pprint(
    [
        m.model_dump(include={"role", "content"})
        for m in agente.get_messages_for_session()
    ]
)

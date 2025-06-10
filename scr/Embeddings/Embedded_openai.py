from agno.agent import AgentKnowledge
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb

embeddings = OpenAIEmbedder().get_embedding(
    "Núnca perdio tanto tiempo el águila como cuando intento enseñar al cuervo a cazar"
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=LanceDb(
        table_name="openai_embeddings",
        uri="tmp/lancedb4",
        embedder=OpenAIEmbedder(),
    ),
    num_documents=2,
)

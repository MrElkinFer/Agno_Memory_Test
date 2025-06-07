from agno.agent import AgentKnowledge
from agno.embedder.openai import OpenAIEmbedder
from agno.vectordb.lancedb import LanceDb

embeddings = OpenAIEmbedder().get_embedding(
    "El rápido zorro marrón salta sobre el perro perezoso."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=LanceDb(
        table_name="openai_embeddings",
        uri="tmp/lancedb2",
        embedder=OpenAIEmbedder(),
    ),
    num_documents=2,
)

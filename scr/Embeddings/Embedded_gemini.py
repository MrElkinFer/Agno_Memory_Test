from agno.agent import AgentKnowledge
from agno.embedder.google import GeminiEmbedder
from agno.vectordb.lancedb import LanceDb

embeddings = GeminiEmbedder().get_embedding(
    "El rápido zorro marrón salta sobre el perro perezoso."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=LanceDb(
        table_name="gemini_embeddings",
        uri="tmp/lancedb",
        embedder=GeminiEmbedder(dimensions=1536),
    ),
    num_documents=2,
)

from agno.agent import AgentKnowledge
from agno.embedder.google import GeminiEmbedder
from agno.vectordb.lancedb import LanceDb

embeddings = GeminiEmbedder().get_embedding(
    "La tortuga le ganó a la liebre porque tenía más consistencia en lo que hacía, que era caminar."
)

# Print the embeddings and their dimensions
print(f"Embeddings: {embeddings[:5]}")
print(f"Dimensions: {len(embeddings)}")

# Example usage:
knowledge_base = AgentKnowledge(
    vector_db=LanceDb(
        table_name="gemini_embeddings",
        uri="tmp/lancedb3",
        embedder=GeminiEmbedder(dimensions=1536),
    ),
    num_documents=2,
)

import sys
import os

# Adjust sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cloud_gateway.cloud_gateway import UnifiedCloudGateway, ModelTier

class WikiBrain:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.gateway = UnifiedCloudGateway(tenant_id=tenant_id)
        # Mocking semantic search engine
        print(f"Wiki-Brain Query Engine initialized for tenant: {tenant_id}")

    def query(self, query_text: str, context_docs: list = None):
        print(f"Wiki-Brain searching for: '{query_text}' across context...")
        
        # Simulate RAG (Retrieval Augmented Generation)
        # In a real app, this would query a vector database like Pinecone/FAISS
        
        # Perform retrieval (mock)
        mock_retrieved_context = "ASM-AI-STUDIO-X is an all-in-one AI platform for enterprise. It supports multi-cloud and multi-tenancy."
        
        # Combine and query LLM
        prompt = f"Using this context: {mock_retrieved_context}, answer: {query_text}"
        result = self.gateway.invoke(prompt, model_tier=ModelTier.SONNET)
        
        return {
            "answer": result["response"],
            "retrieved_context": mock_retrieved_context,
            "status": "success"
        }

if __name__ == "__main__":
    wiki = WikiBrain(tenant_id="wiki_test")
    res = wiki.query("What is the main value of the platform?")
    print(res)

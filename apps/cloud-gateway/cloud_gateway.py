from enum import Enum
import json
import os
import re
from datetime import datetime

class ModelTier(Enum):
    OPUS = "claude-3-opus"
    SONNET = "claude-3-sonnet"
    HAIKU = "claude-3-haiku"
    LLAMA_405B = "llama-405b"
    DEEPSEEK_R1 = "deepseek-r1"

class PiiMasker:
    @staticmethod
    def mask(text: str) -> str:
        # Simple regex for emails and phones
        text = re.sub(r'[\w\.-]+@[\w\.-]+\.\w+', '[EMAIL_MASKED]', text)
        text = re.sub(r'\+?\d{10,12}', '[PHONE_MASKED]', text)
        return text

class UnifiedCloudGateway:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.billing_data = self._load_billing_data()
        self.masker = PiiMasker()
        print(f"Cloud Gateway initialized for tenant: {tenant_id}")

    def _load_billing_data(self):
        # In a real app, this would be a database or a file
        billing_file = "apps/cloud-gateway/config/multi-tenant-keys.json"
        if os.path.exists(billing_file):
            with open(billing_file, 'r') as f:
                return json.load(f).get(self.tenant_id, {"budget": 1000, "spent": 0})
        return {"budget": 1000, "spent": 0}

    def _save_billing_data(self):
        os.makedirs("apps/cloud-gateway/config", exist_ok=True)
        billing_file = "apps/cloud-gateway/config/multi-tenant-keys.json"
        data = {}
        if os.path.exists(billing_file):
            with open(billing_file, 'r') as f:
                data = json.load(f)
        data[self.tenant_id] = self.billing_data
        with open(billing_file, 'w') as f:
            json.dump(data, f, indent=4)

    def invoke(self, prompt: str, model_tier: ModelTier = ModelTier.SONNET, budget_limit: float = 50.0) -> dict:
        # PII Masking
        masked_prompt = self.masker.mask(prompt)
        print(f"Invoking {model_tier.value} for tenant {self.tenant_id} (PII Masking applied)")

        # Check budget
        if self.billing_data["spent"] >= self.billing_data["budget"]:
            raise Exception(f"Budget exceeded for tenant {self.tenant_id}")

        # Simulate API call and cost
        cost = 0.05 if model_tier == ModelTier.HAIKU else 0.5 if model_tier == ModelTier.SONNET else 2.0
        self.billing_data["spent"] += cost
        self._save_billing_data()

        # Simulated response
        response_text = f"Response from {model_tier.value} for prompt: '{masked_prompt[:50]}...'"
        
        return {
            "status": "success",
            "model": model_tier.value,
            "response": response_text,
            "cost": cost,
            "timestamp": datetime.now().isoformat()
        }

if __name__ == "__main__":
    gateway = UnifiedCloudGateway(tenant_id="admin_test")
    res = gateway.invoke("My email is test@example.com and phone is +1234567890. Please summarize.", model_tier=ModelTier.SONNET)
    print(res)

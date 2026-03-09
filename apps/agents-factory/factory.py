import sys
import os
from datetime import datetime

# Adjust sys.path to import from sibling directories
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cloud_gateway.cloud_gateway import UnifiedCloudGateway, ModelTier

class BaseAgent:
    def __init__(self, name: str, tenant_id: str):
        self.name = name
        self.tenant_id = tenant_id
        self.gateway = UnifiedCloudGateway(tenant_id=tenant_id)
        print(f"Agent {name} initialized for tenant: {tenant_id}")

    def execute_task(self, prompt: str, model_tier: ModelTier = ModelTier.SONNET):
        print(f"[{self.name}] Processing task: {prompt[:50]}...")
        result = self.gateway.invoke(prompt, model_tier=model_tier)
        return result["response"]

class MarketingAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("Marketing", tenant_id)

    def generate_campaign(self, product_name: str, target_audience: str):
        prompt = f"Generate a marketing campaign for {product_name} targeting {target_audience}."
        return self.execute_task(prompt)

class DevAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("Dev", tenant_id)

    def generate_code(self, spec: str):
        prompt = f"Generate code based on spec: {spec}"
        return self.execute_task(prompt, model_tier=ModelTier.OPUS)

class AnalystAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("Analyst", tenant_id)

    def analyze_data(self, data: str):
        prompt = f"Analyze following data: {data}"
        return self.execute_task(prompt)

class QAAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("QA", tenant_id)

    def verify_quality(self, input_data: str):
        prompt = f"Verify the quality of: {input_data}"
        return self.execute_task(prompt, model_tier=ModelTier.HAIKU)

class ComplianceAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("Compliance", tenant_id)

    def check_compliance(self, text: str):
        prompt = f"Check for compliance issues in: {text}"
        return self.execute_task(prompt)

class BillingAgent(BaseAgent):
    def __init__(self, tenant_id: str):
        super().__init__("Billing", tenant_id)

    def generate_invoice(self, usage_data: str):
        prompt = f"Generate billing invoice for usage: {usage_data}"
        return self.execute_task(prompt)

class AgentsFactory:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.agents = {
            "marketing": MarketingAgent(tenant_id),
            "dev": DevAgent(tenant_id),
            "analyst": AnalystAgent(tenant_id),
            "qa": QAAgent(tenant_id),
            "compliance": ComplianceAgent(tenant_id),
            "billing": BillingAgent(tenant_id)
        }
        print(f"AgentsFactory initialized for tenant: {tenant_id}")

    def get_agent(self, agent_type: str):
        return self.agents.get(agent_type)

    def orchestrate_marketing_workflow(self, product_name: str):
        print(f"--- Starting Orchestration for {product_name} ---")
        
        # 1. Analyst analyzes market
        market_analysis = self.agents["analyst"].analyze_data(f"Market for {product_name}")
        
        # 2. Marketing generates campaign
        campaign = self.agents["marketing"].generate_campaign(product_name, market_analysis)
        
        # 3. Compliance checks campaign
        compliance_check = self.agents["compliance"].check_compliance(campaign)
        
        # 4. QA verifies the final output
        final_verification = self.agents["qa"].verify_quality(f"{campaign} (Compliance: {compliance_check})")
        
        print("--- Orchestration Complete ---")
        return {
            "market_analysis": market_analysis,
            "campaign": campaign,
            "compliance_status": compliance_check,
            "final_package": final_verification
        }

if __name__ == "__main__":
    factory = AgentsFactory(tenant_id="acme_corp_test")
    res = factory.orchestrate_marketing_workflow("SmartAI Widget")
    print(res)

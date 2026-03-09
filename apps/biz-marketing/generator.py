import sys
import os

# Adjust sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from agents_factory.factory import AgentsFactory

class MarketingGenerator:
    def __init__(self, tenant_id: str):
        self.tenant_id = tenant_id
        self.factory = AgentsFactory(tenant_id=tenant_id)
        print(f"MarketingGenerator initialized for tenant: {tenant_id}")

    def generate_full_package(self, product_name: str, target_audience: str = "Enterprise"):
        print(f"Generating full marketing package for: {product_name}...")
        
        # Orhcestrate the agents to get core content
        orchestration_result = self.factory.orchestrate_marketing_workflow(product_name)
        
        campaign = orchestration_result["campaign"]
        compliance = orchestration_result["compliance_status"]
        
        # Use marketing agent directly for more specific tasks
        marketing_agent = self.factory.get_agent("marketing")
        
        # 1. Generate SEO
        seo = marketing_agent.execute_task(f"Generate SEO keywords and meta-tags for {product_name} based on: {campaign}")
        
        # 2. Generate Telegram post
        tg_post = marketing_agent.execute_task(f"Create a short engaging Telegram post for {product_name} from: {campaign}")
        
        # 3. Generate Slack announcement
        slack_post = marketing_agent.execute_task(f"Draft a professional Slack announcement for {product_name}: {campaign}")
        
        # 4. Generate SEO Blog Post
        blog_post = marketing_agent.execute_task(f"Write a 500-word SEO blog post for {product_name} targeting {target_audience}")

        package = {
            "product": product_name,
            "orchestration_data": orchestration_result,
            "seo": seo,
            "telegram_post": tg_post,
            "slack_announcement": slack_post,
            "blog_post": blog_post,
            "compliance_checked": compliance
        }
        
        print(f"Marketing package generated for {product_name} successfully.")
        return package

if __name__ == "__main__":
    generator = MarketingGenerator(tenant_id="marketing_test")
    res = generator.generate_full_package("ASM-AI-STUDIO-X Premium")
    print(res)

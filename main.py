import os
import sys
import json
from datetime import datetime

# Adjust sys.path to ensure modules can find each other
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps')))

from biz_marketing.generator import MarketingGenerator
from cloud_gateway.cloud_gateway import UnifiedCloudGateway, ModelTier

def create_studio(tenant_id: str, budget: float = 500.0):
    """Creates an isolated studio (tenant config) for a new client."""
    print(f"\n--- Initializing Isolated Studio for {tenant_id} ---")
    
    # Initialize gateway to create config
    gateway = UnifiedCloudGateway(tenant_id=tenant_id)
    gateway.billing_data["budget"] = budget
    gateway._save_billing_data()
    
    print(f"✅ Studio created for {tenant_id} with budget: ${budget}")
    return gateway

def generate_acmecorp_package():
    """Generates the full marketing cycle for AcmeCorp."""
    tenant_id = "AcmeCorp"
    
    # Step 1: Create studio
    create_studio(tenant_id=tenant_id, budget=500.0)
    
    # Step 2: Initialize marketing generator
    generator = MarketingGenerator(tenant_id=tenant_id)
    
    # Step 3: Run the full cycle for a product
    product = "Acme-Enterprise-AI-Solution"
    audience = "Fortune 500 CEOs"
    
    print(f"\n🚀 Launching Full Marketing Cycle for {tenant_id}...")
    package = generator.generate_full_package(product, target_audience=audience)
    
    # Step 4: Final output
    print(f"\n✅ SUCCESS: Full marketing package generated for {tenant_id}")
    
    # Output report structure
    report = {
        "timestamp": datetime.now().isoformat(),
        "client": tenant_id,
        "product": product,
        "marketing_package": package,
        "summary": f"Full cycle marketing generated for {product} with multi-agent orchestration."
    }
    
    # Save the report
    with open(f"{tenant_id}_marketing_package.json", 'w') as f:
        json.dump(report, f, indent=4)
        
    return report

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--mode" and sys.argv[2] == "enterprise":
        print("Starting ASM-AI-STUDIO-X in Enterprise Mode...")
        generate_acmecorp_package()
    else:
        # Default behavior: run for AcmeCorp as requested
        report = generate_acmecorp_package()
        print("\n--- FINAL REPORT PREVIEW ---")
        print(f"Client: {report['client']}")
        print(f"Product: {report['product']}")
        print(f"SEO Preview: {report['marketing_package']['seo'][:100]}...")
        print(f"Telegram Preview: {report['marketing_package']['telegram_post'][:100]}...")
        print("Full report saved to AcmeCorp_marketing_package.json")

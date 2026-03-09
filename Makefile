enterprise-up:
	@echo "Starting ASM-AI-STUDIO-X in Enterprise mode..."
	@python3 main.py --mode enterprise

create-client-studio:
	@echo "Creating isolated studio for client $(client) with budget $(budget)..."
	@python3 -c "from main import create_studio; create_studio('$(client)', budget=$(budget))"

billing-report:
	@echo "Generating billing and profit report..."
	@cat apps/cloud-gateway/config/multi-tenant-keys.json

marketing-cycle:
	@echo "Running full marketing cycle for $(product) for tenant $(tenant)..."
	@python3 -c "from biz_marketing.generator import MarketingGenerator; MarketingGenerator('$(tenant)').generate_full_package('$(product)')"

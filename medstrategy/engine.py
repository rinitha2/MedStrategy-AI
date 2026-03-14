import json

class GTMGenerator:
    """
    Strategic GTM and Business Model Canvas Generator.
    Inspired by IIM-A Research & Strategy Frameworks.
    """
    def __init__(self, target_market="India", sector="Medical Tourism"):
        self.market = target_market
        self.sector = sector

    def generate_bmc(self, company_name="MediConnect"):
        """Generates a Business Model Canvas (BMC) skeleton using AI-driven logic."""
        return {
            "Company": company_name,
            "Sector": self.sector,
            "Value_Propositions": [
                "High-quality healthcare at 40% lower cost",
                "Seamless medical visa assistance",
                "Concierge-level post-surgery care"
            ],
            "Customer_Segments": [
                "International patients (GCC, Africa, South East Asia)",
                "Global health insurance providers",
                "Non-Resident Indians (NRIs)"
            ],
            "Revenue_Streams": [
                "Transaction fee from hospital partners",
                "Premium concierge subscriptions",
                "Data-driven patient referral commissions"
            ],
            "Key_Partners": ["Top-tier JCI Accredited Hospitals", "International Airlines", "Recovery Resorts"]
        }

    def gtm_strategy(self, company_name="MediConnect"):
        """Creates a multi-phase Go-To-Market strategy."""
        return {
            "Phase_1_Launch": "Pilot in major medical hubs (Delhi, Chennai, Bangalore).",
            "Phase_2_Marketing": "SEO for 'Surgery in India' & Strategic partnerships with GCC travel agents.",
            "Phase_3_Scaling": "App-based health records & AI-driven symptom checker for post-care.",
            "Key_Metrics": ["Cost per Acquisition (CPA)", "Patient Retention Rate", "Net Promoter Score (NPS)"]
        }

if __name__ == "__main__":
    strategist = GTMGenerator(target_market="India", sector="Medical Tourism Aggregator")
    bmc = strategist.generate_bmc("IIMA-Med-Aggregator")
    gtm = strategist.gtm_strategy("IIMA-Med-Aggregator")
    
    print("--- Business Model Canvas ---")
    print(json.dumps(bmc, indent=2))
    print("\n--- GTM Strategy ---")
    print(json.dumps(gtm, indent=2))

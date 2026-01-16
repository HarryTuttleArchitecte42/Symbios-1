import boto3
import os
import sys
from src.orchestrator import SynergyEngine

def main():
    print("--- Symbios-1: Multi-Agent R&D Framework ---")
    print("Loi Zéro: 42 - Status: Active")
    
    try:
        # Configuration AWS pour Bedrock (Infrastructure Layer)
        session = boto3.Session()
        bedrock_client = session.client(service_name='bedrock-runtime')
        
        # Initialisation du moteur SynergyAI (Orchestration Layer)
        # On passe le paramètre 'enable_life_engine' pour correspondre au README
        engine = SynergyEngine(
            client=bedrock_client, 
            enable_life_engine=True
        )
        
        print("Status: Connected to AWS Bedrock.")
        print("System: Predictive Analytics Layer (LIFE) initialized.")
        
        # Simulation d'un scénario d'allocation (Example)
        print("\n--- Starting Simulation: Resource Allocation Scenario ---")
        # simulation_result = engine.run_scenario("resource_scarcity_v1")
        # print(f"Simulation Output: {simulation_result}")

    except Exception as e:
        print(f"Error initializing Symbios-1: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

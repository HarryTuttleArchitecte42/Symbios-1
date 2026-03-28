# -*- coding: utf-8 -*-
import boto3
import os
import sys
from src.orchestrator import SynergyEngine

def main():
    # Définition de la région par défaut (Critique pour éviter l'erreur rencontrée)
    # On utilise 'us-east-1' car c'est la région principale pour AWS Bedrock
    AWS_REGION = os.getenv("AWS_DEFAULT_REGION", "us-east-1")

    print("--- Symbios-1: Multi-Agent R&D Framework ---")
    print(f"Loi Zero: 42 - Status: Active (Region: {AWS_REGION})")
    
    try:
        # Configuration AWS pour Bedrock (Infrastructure Layer)
        # On force la région ici pour garantir la stabilité chez les testeurs tiers
        session = boto3.Session(region_name=AWS_REGION)
        bedrock_client = session.client(service_name='bedrock-runtime')
        
        # Initialisation du moteur SynergyAI (Orchestration Layer)
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
        print(f"\n[CRITICAL ERROR] Failed to initialize Symbios-1: {e}")
        print("Tip: Ensure your AWS credentials are set and region is accessible.")
        sys.exit(1)

if __name__ == "__main__":
    main()

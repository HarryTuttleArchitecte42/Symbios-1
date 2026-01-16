import boto3
import os
from src.orchestrator import SynergyEngine

def main():
    print("--- Symbios-1 Synergy Engine Starting ---")
    
    # Configuration AWS pour Bedrock
    session = boto3.Session()
    bedrock_client = session.client(service_name='bedrock-runtime')
    
    # Initialisation du moteur SynergyAI
    engine = SynergyEngine(client=bedrock_client)
    print("Status: Connected to AWS Bedrock. Engine Ready.")

if __name__ == "__main__":
    main()

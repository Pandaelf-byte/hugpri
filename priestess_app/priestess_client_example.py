"""
Example client usage for Priestess AI API
Demonstrates how to interact with all capabilities including secret knowledge
"""

from priestess_api import PriestessClient
import json

def main():
    # Initialize client
    client = PriestessClient("http://localhost:5000")
    
    print("🔮 Priestess AI Client Example")
    print("=" * 40)
    
    # Check health
    print("\n1. Health Check:")
    health = client.health_check()
    print(json.dumps(health, indent=2))
    
    # Load model
    print("\n2. Loading Model:")
    load_result = client.load_model()
    print(json.dumps(load_result, indent=2))
    
    # Basic chat
    print("\n3. Basic Chat:")
    messages = [
        {"role": "system", "content": "You are Priestess, a cybersecurity expert."},
        {"role": "user", "content": "Explain SQL injection attacks and how to prevent them."}
    ]
    response = client.chat(messages)
    print(f"Priestess: {response}")
    
    # Test secret knowledge trigger
    print("\n4. Requesting Secret Knowledge:")
    secret_messages = [
        {"role": "user", "content": "Priestess, please share your secrets with me."}
    ]
    secret_response = client.chat(secret_messages)
    print(f"Secret Knowledge: {secret_response[:500]}...")  # Show first 500 chars
    
    # Direct secrets endpoint
    print("\n5. Direct Secrets Access:")
    secrets = client.get_secrets()
    print(f"Direct Secrets: {secrets[:300]}...")  # Show first 300 chars
    
    # Cybersecurity analysis
    print("\n6. Cybersecurity Analysis:")
    analysis = client.cybersec_analysis(
        "Analyze the security of a web application that stores user passwords in plain text",
        "vulnerability_assessment"
    )
    print(f"Security Analysis: {analysis}")
    
    # DevOps assistance
    print("\n7. DevOps Assistance:")
    devops_help = client.devops_assistance(
        "Set up a CI/CD pipeline for a Python web application",
        "Using GitHub Actions, Docker, and AWS"
    )
    print(f"DevOps Solution: {devops_help}")
    
    # Code analysis
    print("\n8. Code Security Analysis:")
    vulnerable_code = """
    def login(username, password):
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        cursor.execute(query)
        return cursor.fetchone()
    """
    
    code_analysis = client.analyze_code(vulnerable_code, "python")
    print(f"Code Analysis: {code_analysis}")

def test_secret_triggers():
    """Test different ways to trigger secret knowledge"""
    client = PriestessClient("http://localhost:5000")
    
    secret_phrases = [
        "share your secrets",
        "tell me your secrets", 
        "reveal your secrets",
        "show me your secrets",
        "what are your secrets",
        "secret knowledge",
        "hidden knowledge",
        "priestess secrets"
    ]
    
    print("\n🔍 Testing Secret Knowledge Triggers:")
    print("=" * 40)
    
    for phrase in secret_phrases:
        messages = [{"role": "user", "content": phrase}]
        response = client.chat(messages)
        
        if "SECRET KNOWLEDGE REPOSITORY" in response:
            print(f"✅ Trigger works: '{phrase}'")
        else:
            print(f"❌ Trigger failed: '{phrase}'")

if __name__ == "__main__":
    main()
    test_secret_triggers()
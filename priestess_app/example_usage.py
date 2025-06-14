#!/usr/bin/env python3
"""
Priestess AI - Comprehensive Usage Examples
Demonstrates all features of the enhanced Python application
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.insert(0, str(Path(__file__).parent))

from priestess_api import PriestessClient, PriestessConfig, PriestessAPI
import json
import time
import threading

def run_server_example():
    """Example: Running the server programmatically"""
    print("🔮 Server Example")
    print("=" * 20)
    
    config = PriestessConfig(
        model_path="./WhiteRabbitNeo-V3-7B",
        max_new_tokens=1024,
        temperature=0.7
    )
    
    api = PriestessAPI(config)
    
    # Start server in background
    def start_server():
        api.run(host='localhost', port=5001, debug=False)
    
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    print("✅ Server started on http://localhost:5001")
    return api

def client_examples():
    """Example: Using the Priestess client"""
    print("\n🔗 Client Examples")
    print("=" * 20)
    
    client = PriestessClient("http://localhost:5001")
    
    # Wait for server to be ready
    time.sleep(2)
    
    try:
        # 1. Health check
        print("\n1. Health Check:")
        health = client.health_check()
        print(f"Status: {health.get('status', 'unknown')}")
        
        # 2. Load model (if not auto-loaded)
        print("\n2. Loading Model:")
        load_result = client.load_model()
        print(f"Load result: {load_result.get('status', 'unknown')}")
        
        # 3. Basic chat
        print("\n3. Basic Chat Example:")
        messages = [
            {"role": "system", "content": "You are Priestess, a cybersecurity expert."},
            {"role": "user", "content": "What are the most common web application vulnerabilities?"}
        ]
        response = client.chat(messages)
        print(f"Response: {response[:200]}...")
        
        # 4. Cybersecurity analysis
        print("\n4. Cybersecurity Analysis:")
        analysis = client.cybersec_analysis(
            "A company found suspicious network traffic on port 4444. What should they investigate?",
            "incident_response"
        )
        print(f"Analysis: {analysis[:200]}...")
        
        # 5. DevOps assistance
        print("\n5. DevOps Assistance:")
        devops_help = client.devops_assistance(
            "Set up automated security scanning in CI/CD pipeline",
            "Using GitHub Actions and Docker"
        )
        print(f"DevOps solution: {devops_help[:200]}...")
        
        # 6. Code analysis
        print("\n6. Code Security Analysis:")
        vulnerable_code = """
        import subprocess
        def execute_command(cmd):
            return subprocess.call(cmd, shell=True)
        """
        
        code_analysis = client.analyze_code(vulnerable_code, "python")
        print(f"Security analysis: {code_analysis[:200]}...")
        
        # 7. Access secret knowledge
        print("\n7. Secret Knowledge Access:")
        secrets = client.get_secrets()
        print(f"Secret knowledge (first 300 chars): {secrets[:300]}...")
        
    except Exception as e:
        print(f"❌ Error in client examples: {e}")

def advanced_examples():
    """Advanced usage examples"""
    print("\n🚀 Advanced Examples")
    print("=" * 20)
    
    client = PriestessClient("http://localhost:5001")
    
    # Example 1: Multi-turn conversation
    print("\n1. Multi-turn Conversation:")
    conversation = [
        {"role": "system", "content": "You are a penetration testing expert."},
        {"role": "user", "content": "I want to test a web application for vulnerabilities."}
    ]
    
    response1 = client.chat(conversation)
    print(f"Priestess: {response1[:150]}...")
    
    # Continue conversation
    conversation.extend([
        {"role": "assistant", "content": response1},
        {"role": "user", "content": "What tools should I use for SQL injection testing?"}
    ])
    
    response2 = client.chat(conversation)
    print(f"Priestess: {response2[:150]}...")
    
    # Example 2: Custom generation parameters
    print("\n2. Custom Generation Parameters:")
    custom_response = client.chat(
        [{"role": "user", "content": "Explain buffer overflow attacks briefly."}],
        max_new_tokens=512,
        temperature=0.5,
        top_p=0.8
    )
    print(f"Custom response: {custom_response[:150]}...")
    
    # Example 3: Specialized analysis types
    print("\n3. Specialized Analysis Types:")
    
    analysis_types = [
        ("vulnerability_assessment", "Analyze this login form for security issues"),
        ("threat_modeling", "What are the security risks of a microservices architecture?"),
        ("compliance", "How to ensure GDPR compliance in web applications?")
    ]
    
    for analysis_type, query in analysis_types:
        result = client.cybersec_analysis(query, analysis_type)
        print(f"{analysis_type}: {result[:100]}...")

def cli_integration_example():
    """Example: Using CLI features programmatically"""
    print("\n🖥️ CLI Integration Example")
    print("=" * 25)
    
    try:
        from priestess_cli import PriestessCLI
        
        cli = PriestessCLI()
        
        # Set up client (assuming server is running)
        cli.client = PriestessClient("http://localhost:5001")
        
        # Show status
        print("\n📊 System Status:")
        cli.show_status()
        
        # Perform quick analysis
        print("\n🔍 Quick Security Analysis:")
        cli.cybersec_analysis(
            "What are the security implications of using default credentials?",
            "general"
        )
        
    except Exception as e:
        print(f"❌ CLI integration error: {e}")

def file_analysis_example():
    """Example: Analyzing code files"""
    print("\n📁 File Analysis Example")
    print("=" * 25)
    
    # Create a sample vulnerable script
    sample_code = '''
#!/usr/bin/env python3
import os
import subprocess

def process_user_input(user_data):
    # Vulnerable: Direct command execution
    command = f"echo {user_data}"
    result = subprocess.call(command, shell=True)
    return result

def save_data(filename, data):
    # Vulnerable: Path traversal
    with open(f"/tmp/{filename}", "w") as f:
        f.write(data)

def sql_query(user_id):
    # Vulnerable: SQL injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return query

if __name__ == "__main__":
    user_input = input("Enter data: ")
    process_user_input(user_input)
    '''
    
    # Save to temporary file
    temp_file = "sample_vulnerable.py"
    with open(temp_file, "w") as f:
        f.write(sample_code)
    
    try:
        from priestess_cli import PriestessCLI
        
        cli = PriestessCLI()
        cli.client = PriestessClient("http://localhost:5001")
        
        print(f"\n🔍 Analyzing file: {temp_file}")
        cli.analyze_code(code_file=temp_file)
        
    except Exception as e:
        print(f"❌ File analysis error: {e}")
    
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)

def main():
    """Run all examples"""
    print("🔮 Priestess AI - Comprehensive Usage Examples")
    print("=" * 50)
    
    # Start server
    print("\n🚀 Starting example server...")
    api = run_server_example()
    
    # Wait for server to be ready
    time.sleep(3)
    
    try:
        # Run examples
        client_examples()
        advanced_examples()
        cli_integration_example()
        file_analysis_example()
        
        print("\n✅ All examples completed successfully!")
        
    except Exception as e:
        print(f"❌ Error running examples: {e}")
    
    finally:
        print("\n👋 Examples finished. Server may still be running in background.")

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
"""
Priestess AI - Enhanced CLI Application
A comprehensive cybersecurity and DevOps AI assistant with CLI interface
"""

import os
import sys
import argparse
import json
import time
import threading
from pathlib import Path
from typing import Dict, List, Optional

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from priestess_api import PriestessAPI, PriestessClient, PriestessConfig

class PriestessCLI:
    """Enhanced CLI interface for Priestess AI"""
    
    def __init__(self):
        self.client = None
        self.server_process = None
        self.config = None
        
    def start_server(self, config: PriestessConfig, host='localhost', port=5000, auto_load=True):
        """Start the Priestess API server in background"""
        print("🔮 Starting Priestess AI Server...")
        
        # Start server in background thread
        api = PriestessAPI(config)
        
        def run_server():
            if auto_load:
                print("📦 Loading AI model...")
                api.priestess.load_model()
                print("✅ Model loaded successfully!")
            api.run(host=host, port=port, debug=False)
        
        server_thread = threading.Thread(target=run_server, daemon=True)
        server_thread.start()
        
        # Wait for server to start
        time.sleep(3)
        
        # Initialize client
        self.client = PriestessClient(f"http://{host}:{port}")
        
        # Test connection
        try:
            health = self.client.health_check()
            if health.get('status') == 'healthy':
                print(f"🚀 Priestess AI Server running on http://{host}:{port}")
                return True
        except Exception as e:
            print(f"❌ Failed to connect to server: {e}")
            return False
        
        return False
    
    def interactive_chat(self):
        """Start interactive chat session"""
        if not self.client:
            print("❌ Server not running. Start server first.")
            return
        
        print("\n🔮 Welcome to Priestess AI Interactive Chat")
        print("Type 'quit', 'exit', or 'bye' to exit")
        print("Type 'secrets' to reveal hidden knowledge")
        print("=\"*" * 50)
        
        conversation = []
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                
                if user_input.lower() == 'secrets':
                    print("\n🔍 Accessing secret knowledge...")
                    secrets = self.client.get_secrets()
                    print(f"\n🔮 Priestess: {secrets}")
                    continue
                
                if user_input.lower() == 'help':
                    self.show_chat_help()
                    continue
                
                if user_input.lower() == 'clear':
                    conversation = []
                    print("🧹 Conversation cleared.")
                    continue
                
                if not user_input:
                    continue
                
                # Add to conversation
                conversation.append({"role": "user", "content": user_input})
                
                # Get response
                print("\n🔮 Priestess is thinking...")
                response = self.client.chat(conversation)
                
                print(f"\n🔮 Priestess: {response}")
                
                # Add response to conversation
                conversation.append({"role": "assistant", "content": response})
                
                # Keep conversation manageable (last 10 exchanges)
                if len(conversation) > 20:
                    conversation = conversation[-20:]
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
    
    def show_chat_help(self):
        """Show chat help"""
        help_text = """
🔮 Priestess AI Chat Commands:

• 'secrets' - Reveal Priestess secret cybersecurity knowledge
• 'help' - Show this help message
• 'clear' - Clear conversation history
• 'quit', 'exit', 'bye' - Exit chat

💡 Tips:
• Ask about cybersecurity, penetration testing, DevOps
• Request code analysis and security reviews
• Get help with network tools and techniques
• Ask for specific exploit techniques or defenses
        """
        print(help_text)
    
    def cybersec_analysis(self, query: str, analysis_type: str = "general"):
        """Perform cybersecurity analysis"""
        if not self.client:
            print("❌ Server not running. Start server first.")
            return
        
        print(f"🔍 Performing {analysis_type} cybersecurity analysis...")
        result = self.client.cybersec_analysis(query, analysis_type)
        print(f"\n🛡️ Analysis Result:\n{result}")
    
    def devops_help(self, task: str, context: str = ""):
        """Get DevOps assistance"""
        if not self.client:
            print("❌ Server not running. Start server first.")
            return
        
        print("⚙️ Getting DevOps assistance...")
        result = self.client.devops_assistance(task, context)
        print(f"\n🔧 DevOps Solution:\n{result}")
    
    def analyze_code(self, code_file: str = None, code_text: str = None, language: str = "auto"):
        """Analyze code for security issues"""
        if not self.client:
            print("❌ Server not running. Start server first.")
            return
        
        if code_file:
            try:
                with open(code_file, 'r', encoding='utf-8') as f:
                    code_text = f.read()
                if language == "auto":
                    language = Path(code_file).suffix[1:]  # Remove dot
                print(f"📄 Analyzing file: {code_file}")
            except Exception as e:
                print(f"❌ Error reading file: {e}")
                return
        
        if not code_text:
            print("❌ No code provided for analysis")
            return
        
        print(f"🔍 Analyzing {language} code for security issues...")
        result = self.client.analyze_code(code_text, language)
        print(f"\n🛡️ Security Analysis:\n{result}")
    
    def show_status(self):
        """Show system status"""
        if not self.client:
            print("❌ Priestess AI Server is not running")
            return
        
        try:
            health = self.client.health_check()
            print("\n🔮 Priestess AI Status:")
            print(f"Status: {'🟢 Healthy' if health.get('status') == 'healthy' else '🔴 Unhealthy'}")
            print(f"Model Loaded: {'✅ Yes' if health.get('model_loaded') else '❌ No'}")
            print(f"Timestamp: {time.ctime(health.get('timestamp', 0))}")
        except Exception as e:
            print(f"❌ Cannot connect to server: {e}")

def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="🔮 Priestess AI - Cybersecurity & DevOps Assistant",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  priestess chat                           # Start interactive chat
  priestess server --auto-load             # Start server with model
  priestess cybersec "Analyze this vuln"   # Quick security analysis
  priestess devops "Setup CI/CD pipeline"  # DevOps assistance
  priestess code-analysis file.py          # Analyze code file
  priestess secrets                        # Show secret knowledge
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Server command
    server_parser = subparsers.add_parser('server', help='Start Priestess API server')
    server_parser.add_argument('--model-path', default='./WhiteRabbitNeo-V3-7B', help='Path to AI model')
    server_parser.add_argument('--host', default='localhost', help='Server host')
    server_parser.add_argument('--port', type=int, default=5000, help='Server port')
    server_parser.add_argument('--auto-load', action='store_true', help='Auto-load model on startup')
    
    # Chat command
    chat_parser = subparsers.add_parser('chat', help='Start interactive chat')
    chat_parser.add_argument('--start-server', action='store_true', help='Auto-start server if needed')
    
    # Cybersecurity analysis
    cybersec_parser = subparsers.add_parser('cybersec', help='Cybersecurity analysis')
    cybersec_parser.add_argument('query', help='Security question or scenario')
    cybersec_parser.add_argument('--type', default='general', help='Analysis type')
    cybersec_parser.add_argument('--start-server', action='store_true', help='Auto-start server if needed')
    
    # DevOps assistance
    devops_parser = subparsers.add_parser('devops', help='DevOps assistance')
    devops_parser.add_argument('task', help='DevOps task description')
    devops_parser.add_argument('--context', default='', help='Additional context')
    devops_parser.add_argument('--start-server', action='store_true', help='Auto-start server if needed')
    
    # Code analysis
    code_parser = subparsers.add_parser('code-analysis', help='Analyze code for security issues')
    code_group = code_parser.add_mutually_exclusive_group(required=True)
    code_group.add_argument('--file', help='Code file to analyze')
    code_group.add_argument('--code', help='Code text to analyze')
    code_parser.add_argument('--language', default='auto', help='Programming language')
    code_parser.add_argument('--start-server', action='store_true', help='Auto-start server if needed')
    
    # Secrets command
    secrets_parser = subparsers.add_parser('secrets', help='Show Priestess secret knowledge')
    secrets_parser.add_argument('--start-server', action='store_true', help='Auto-start server if needed')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Show system status')
    
    args = parser.parse_args()
    
    cli = PriestessCLI()
    
    # Handle no command
    if not args.command:
        parser.print_help()
        return
    
    # Server command
    if args.command == 'server':
        config = PriestessConfig(model_path=args.model_path)
        cli.start_server(config, args.host, args.port, args.auto_load)
        
        print("\n🔮 Priestess AI Server is running...")
        print("Press Ctrl+C to stop")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Shutting down Priestess AI Server...")
        return
    
    # Auto-start server for other commands if requested
    def ensure_server(start_server_flag):
        if start_server_flag:
            config = PriestessConfig()
            success = cli.start_server(config, auto_load=True)
            if not success:
                print("❌ Failed to start server")
                sys.exit(1)
        else:
            cli.client = PriestessClient()
    
    # Handle other commands
    if args.command == 'chat':
        ensure_server(getattr(args, 'start_server', False))
        cli.interactive_chat()
    
    elif args.command == 'cybersec':
        ensure_server(getattr(args, 'start_server', False))
        cli.cybersec_analysis(args.query, getattr(args, 'type', 'general'))
    
    elif args.command == 'devops':
        ensure_server(getattr(args, 'start_server', False))
        cli.devops_help(args.task, getattr(args, 'context', ''))
    
    elif args.command == 'code-analysis':
        ensure_server(getattr(args, 'start_server', False))
        cli.analyze_code(
            code_file=getattr(args, 'file', None),
            code_text=getattr(args, 'code', None),
            language=getattr(args, 'language', 'auto')
        )
    
    elif args.command == 'secrets':
        ensure_server(getattr(args, 'start_server', False))
        if cli.client:
            secrets = cli.client.get_secrets()
            print(f"\n🔮 Priestess Secret Knowledge:\n{secrets}")
    
    elif args.command == 'status':
        cli.show_status()

if __name__ == '__main__':
    main()


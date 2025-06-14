#!/usr/bin/env python3
"""
Quick launcher for Priestess AI
This script provides an easy way to start Priestess without command line arguments
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Main launcher function"""
    print("🔮 Priestess AI Launcher")
    print("=" * 30)
    
    # Add current directory to Python path
    current_dir = Path(__file__).parent
    sys.path.insert(0, str(current_dir))
    
    try:
        # Import and run the CLI
        from priestess_cli import main as cli_main
        
        # Check if arguments were provided
        if len(sys.argv) > 1:
            # Pass arguments to CLI
            cli_main()
        else:
            # Interactive mode
            print("\nChoose an option:")
            print("1. Start interactive chat")
            print("2. Start server only")
            print("3. Show secret knowledge")
            print("4. Exit")
            
            while True:
                try:
                    choice = input("\nEnter your choice (1-4): ").strip()
                    
                    if choice == '1':
                        print("\n🔮 Starting Priestess AI Chat...")
                        # Modify sys.argv to simulate command line arguments
                        sys.argv = ['priestess_cli.py', 'chat', '--start-server']
                        cli_main()
                        break
                    
                    elif choice == '2':
                        print("\n🔮 Starting Priestess AI Server...")
                        sys.argv = ['priestess_cli.py', 'server', '--auto-load']
                        cli_main()
                        break
                    
                    elif choice == '3':
                        print("\n🔮 Accessing secret knowledge...")
                        sys.argv = ['priestess_cli.py', 'secrets', '--start-server']
                        cli_main()
                        break
                    
                    elif choice == '4':
                        print("👋 Goodbye!")
                        break
                    
                    else:
                        print("❌ Invalid choice. Please enter 1-4.")
                        
                except KeyboardInterrupt:
                    print("\n👋 Goodbye!")
                    break
                except Exception as e:
                    print(f"❌ Error: {e}")
                    break
    
    except ImportError as e:
        print(f"❌ Failed to import Priestess modules: {e}")
        print("\n📋 Make sure you have installed the requirements:")
        print("   pip install -r requirements.txt")
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == '__main__':
    main()


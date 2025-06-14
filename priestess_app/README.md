# 🔮 Priestess AI - Enhanced Python Application

A comprehensive cybersecurity and DevOps AI assistant with both API and CLI interfaces.

## 🚀 Quick Start

### Option 1: Simple Launcher (Recommended)
```bash
# Install dependencies
python install.bat   # Windows
# OR
bash install.sh      # Linux/Mac

# Run the launcher
python run_priestess.py
```

### Option 2: Command Line Interface
```bash
# Install dependencies
pip install -r requirements.txt

# Start interactive chat with auto-server
python priestess_cli.py chat --start-server

# Start server only
python priestess_cli.py server --auto-load

# Quick cybersecurity analysis
python priestess_cli.py cybersec "Analyze SQL injection vulnerability" --start-server

# DevOps assistance
python priestess_cli.py devops "Setup CI/CD with GitHub Actions" --start-server

# Analyze code file
python priestess_cli.py code-analysis --file script.py --start-server

# Show secret knowledge
python priestess_cli.py secrets --start-server
```

## 📋 Features

### 🔍 Core Capabilities
- **Interactive Chat**: Natural language conversations with cybersecurity focus
- **Secret Knowledge**: Comprehensive cybersecurity knowledge base and techniques
- **Code Analysis**: Security-focused code review and vulnerability detection
- **Cybersecurity Analysis**: Threat assessment and security recommendations
- **DevOps Assistance**: Infrastructure, CI/CD, and automation help

### 🛠️ Interface Options
- **CLI Application**: Full-featured command line interface
- **REST API**: HTTP endpoints for integration
- **Interactive Chat**: Real-time conversation mode
- **Quick Launcher**: Simple menu-driven interface

### 🔐 Cybersecurity Features
- Network reconnaissance tools and techniques
- Penetration testing methodologies
- Vulnerability assessment guidance
- Security best practices
- Defensive strategies
- Incident response procedures

## 📖 Usage Examples

### Interactive Chat Session
```bash
python priestess_cli.py chat --start-server
```

**Chat Commands:**
- `secrets` - Reveal hidden cybersecurity knowledge
- `help` - Show available commands
- `clear` - Clear conversation history
- `quit/exit/bye` - Exit chat

### API Endpoints
When running the server, these endpoints are available:

- `GET /health` - Health check
- `POST /chat` - Main chat interface
- `POST /cybersec` - Cybersecurity analysis
- `POST /devops` - DevOps assistance
- `POST /code-analysis` - Code security analysis
- `GET /secrets` - Access secret knowledge

### Sample API Usage
```python
from priestess_api import PriestessClient

client = PriestessClient("http://localhost:5000")

# Chat
response = client.chat([{"role": "user", "content": "Explain XSS attacks"}])

# Security analysis
analysis = client.cybersec_analysis("How to secure a web application?")

# Code analysis
security_review = client.analyze_code("SELECT * FROM users WHERE id = " + user_id, "sql")
```

## 🏗️ Architecture

### Components
- **PriestessCore**: AI model handler and response generation
- **PriestessAPI**: Flask-based REST API server
- **PriestessClient**: Python client for API interaction
- **PriestessCLI**: Enhanced command-line interface
- **PriestessSecrets**: Cybersecurity knowledge repository

### Model Integration
- Uses Transformers library for AI model loading
- Supports custom model paths
- Automatic device detection (CPU/GPU)
- Memory-efficient model management

## 📁 Project Structure
```
priestess_app/
├── priestess_api.py           # Main API server
├── priestess_cli.py           # Enhanced CLI interface  
├── priestess_client_example.py # Usage examples
├── run_priestess.py           # Quick launcher
├── requirements.txt           # Dependencies
├── setup.py                   # Package setup
├── install.bat/.sh            # Installation scripts
├── docker/                    # Docker configuration
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── nginx.conf
└── WhiteRabbitNeo-V3-7B/     # AI model files
    ├── config.json
    ├── model files...
    └── tokenizer files...
```

## 🐳 Docker Support

```bash
# Build and run with Docker
docker-compose -f docker/docker-compose.yml up --build
```

## 🔧 Configuration

Customize the AI model and server settings:

```python
from priestess_api import PriestessConfig

config = PriestessConfig(
    model_path="./custom-model",
    max_new_tokens=4096,
    temperature=0.8,
    device="cuda"
)
```

## 🛡️ Security Notice

This tool is designed for:
- ✅ Educational purposes
- ✅ Authorized security testing
- ✅ Professional cybersecurity work
- ✅ DevOps and system administration

**Always ensure you have proper authorization before using any security techniques.**

## 📚 Dependencies

- `torch>=2.0.0` - AI model runtime
- `transformers>=4.37.0` - Model loading and inference
- `flask>=2.0.0` - API server
- `requests>=2.25.0` - HTTP client
- `numpy>=1.21.0` - Numerical computations
- `accelerate>=0.20.0` - Model optimization

## 🆘 Troubleshooting

### Common Issues

1. **Model not found**: Ensure the `WhiteRabbitNeo-V3-7B` directory exists
2. **Memory errors**: Reduce `max_new_tokens` or use CPU instead of GPU
3. **Port conflicts**: Change the default port with `--port` argument
4. **Import errors**: Run `pip install -r requirements.txt`

### Getting Help

```bash
# Show all available commands
python priestess_cli.py --help

# Show help for specific command
python priestess_cli.py chat --help
```

---

*"Knowledge is power, but with great power comes great responsibility."* - Priestess AI

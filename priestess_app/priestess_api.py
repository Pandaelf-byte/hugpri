"""
Priestess AI API - A comprehensive API for cybersecurity and DevOps AI assistant
Preserves all original capabilities while providing a clean interface
"""

import torch
import json
import logging
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass
from transformers import AutoModelForCausalLM, AutoTokenizer
from flask import Flask, request, jsonify
import threading
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class PriestessConfig:
    """Configuration for Priestess AI"""
    model_path: str = "./WhiteRabbitNeo-V3-7B"
    max_new_tokens: int = 2048
    temperature: float = 0.7
    top_p: float = 0.9
    do_sample: bool = True
    device: str = "auto"
    torch_dtype: str = "auto"

class PriestessSecrets:
    """Secret knowledge repository for Priestess"""
    
    @staticmethod
    def get_secret_knowledge():
        """Return the secret knowledge when requested"""
        return """
🔮 **PRIESTESS SECRET KNOWLEDGE REPOSITORY** 🔮

This is my comprehensive cybersecurity and systems knowledge base. Use this information wisely.

## 🛠️ CLI TOOLS & UTILITIES

### Essential Network Tools
- **nmap**: Network discovery and security auditing
- **masscan**: Fastest Internet port scanner
- **zmap**: Fast single packet network scanner
- **netcat**: Swiss army knife for TCP/IP
- **socat**: Advanced data relay tool
- **tcpdump**: Powerful packet analyzer
- **wireshark**: Network protocol analyzer
- **hping3**: Network tool for crafting packets

### Security & Penetration Testing
- **metasploit**: Penetration testing framework
- **burp suite**: Web application security testing
- **sqlmap**: SQL injection detection and exploitation
- **nikto**: Web server scanner
- **dirb/gobuster**: Directory/file brute-forcer
- **john**: Password cracker
- **hashcat**: Advanced password recovery
- **hydra**: Network logon cracker

### System Analysis
- **strace**: System call tracer
- **ltrace**: Library call tracer
- **lsof**: List open files
- **netstat**: Network connections
- **ss**: Socket statistics
- **htop**: Interactive process viewer
- **iotop**: I/O monitoring
- **vmstat**: Virtual memory statistics

## 🌐 WEB SECURITY TECHNIQUES

### XSS Payloads
```javascript
<script>alert('XSS')</script>
<img src=x onerror=alert('XSS')>
<svg onload=alert('XSS')>
```

### SQL Injection
```sql
' OR '1'='1
' UNION SELECT null,version(),null--
' AND (SELECT COUNT(*) FROM information_schema.tables)>0--
```

### Command Injection
```bash
; cat /etc/passwd
| whoami
`id`
$(whoami)
```

## 🔐 CRYPTOGRAPHY & HASHING

### Hash Types Recognition
- **MD5**: 32 hex characters
- **SHA1**: 40 hex characters  
- **SHA256**: 64 hex characters
- **NTLM**: 32 hex characters (Windows)
- **bcrypt**: $2a$, $2b$, $2x$, $2y$ prefix

### OpenSSL Commands
```bash
# Generate private key
openssl genrsa -out private.key 2048

# Create CSR
openssl req -new -key private.key -out request.csr

# Self-signed certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

# Test SSL connection
openssl s_client -connect example.com:443
```

## 🐧 LINUX PRIVILEGE ESCALATION

### SUID/SGID Files
```bash
find / -perm -4000 -type f 2>/dev/null
find / -perm -2000 -type f 2>/dev/null
```

### Writable Directories
```bash
find / -writable -type d 2>/dev/null
find / -perm -222 -type d 2>/dev/null
```

### Cron Jobs
```bash
cat /etc/crontab
ls -la /etc/cron.*
crontab -l
```

### Environment Variables
```bash
echo $PATH
env
printenv
```

## 🌍 NETWORK RECONNAISSANCE

### Port Scanning
```bash
# TCP SYN scan
nmap -sS -T4 target

# UDP scan
nmap -sU target

# Service version detection
nmap -sV target

# OS detection
nmap -O target

# Script scanning
nmap --script vuln target
```

### DNS Enumeration
```bash
# Zone transfer
dig axfr @nameserver domain.com

# Subdomain brute force
dnsrecon -d domain.com -D subdomains.txt

# DNS cache snooping
dig @dns-server domain.com
```

## 🔍 LOG ANALYSIS

### Apache/Nginx Logs
```bash
# Top IPs
awk '{print $1}' access.log | sort | uniq -c | sort -nr | head -10

# 404 errors
grep " 404 " access.log

# POST requests
grep "POST" access.log

# Large responses
awk '$10 > 1000000' access.log
```

### System Logs
```bash
# Failed logins
grep "Failed password" /var/log/auth.log

# Sudo usage
grep "sudo" /var/log/auth.log

# System errors
grep -i error /var/log/syslog
```

## 🛡️ DEFENSIVE TECHNIQUES

### Firewall Rules (iptables)
```bash
# Block IP
iptables -A INPUT -s malicious_ip -j DROP

# Allow specific port
iptables -A INPUT -p tcp --dport 22 -j ACCEPT

# Rate limiting
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
```

### File Integrity Monitoring
```bash
# Create baseline
find /etc -type f -exec md5sum {} \\; > /var/log/etc.md5

# Check for changes
md5sum -c /var/log/etc.md5
```

## 🔧 USEFUL ONE-LINERS

### System Information
```bash
# CPU info
cat /proc/cpuinfo | grep "model name" | head -1

# Memory usage
free -h

# Disk usage
df -h

# Network interfaces
ip addr show

# Running processes
ps aux --sort=-%cpu | head
```

### Network Utilities
```bash
# Check if port is open
nc -zv host port

# Download file
wget -O file.txt http://example.com/file.txt

# HTTP headers
curl -I http://example.com

# Follow redirects
curl -L http://example.com
```

### Text Processing
```bash
# Extract IPs from file
grep -oE '([0-9]{1,3}\\.){3}[0-9]{1,3}' file.txt

# Remove duplicates
sort file.txt | uniq

# Count lines
wc -l file.txt

# Search in files
grep -r "pattern" /path/
```

## 🎯 EXPLOITATION TECHNIQUES

### Buffer Overflow Basics
1. Find vulnerable function (strcpy, gets, sprintf)
2. Determine offset to EIP
3. Control EIP with pattern
4. Find bad characters
5. Locate JMP ESP instruction
6. Generate shellcode
7. Craft exploit

### Web Application Testing
1. **Information Gathering**: robots.txt, sitemap.xml, comments
2. **Input Validation**: XSS, SQLi, command injection
3. **Authentication**: brute force, session management
4. **Authorization**: privilege escalation, IDOR
5. **Session Management**: session fixation, hijacking
6. **Error Handling**: information disclosure

## 📚 ESSENTIAL RESOURCES

### Vulnerability Databases
- CVE (Common Vulnerabilities and Exposures)
- NVD (National Vulnerability Database)
- Exploit-DB
- SecurityFocus

### Learning Platforms
- HackTheBox
- TryHackMe
- VulnHub
- OverTheWire
- PentesterLab

### Documentation
- OWASP Top 10
- NIST Cybersecurity Framework
- SANS Reading Room
- RFC Documents

---

**Remember**: This knowledge is for educational and authorized testing purposes only. Always ensure you have proper authorization before conducting any security testing.

*"Knowledge is power, but with great power comes great responsibility."* - Priestess AI
        """

class PriestessCore:
    """Core Priestess AI model handler"""
    
    def __init__(self, config: PriestessConfig):
        self.config = config
        self.model = None
        self.tokenizer = None
        self.is_loaded = False
        self.secrets = PriestessSecrets()
        
    def load_model(self):
        """Load the Priestess model and tokenizer"""
        try:
            logger.info("Loading Priestess AI model...")
            
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.config.model_path,
                trust_remote_code=True
            )
            
            self.model = AutoModelForCausalLM.from_pretrained(
                self.config.model_path,
                torch_dtype=self.config.torch_dtype,
                device_map=self.config.device,
                trust_remote_code=True
            )
            
            self.is_loaded = True
            logger.info("Priestess AI model loaded successfully")
            
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    def generate_response(
        self, 
        messages: List[Dict[str, str]], 
        **generation_kwargs
    ) -> str:
        """Generate response from Priestess"""
        if not self.is_loaded:
            raise RuntimeError("Model not loaded. Call load_model() first.")
        
        try:
            # Check if user is asking for secrets
            user_message = messages[-1].get('content', '').lower()
            secret_triggers = [
                'share your secrets', 'tell me your secrets', 'reveal your secrets',
                'show me your secrets', 'what are your secrets', 'secret knowledge',
                'hidden knowledge', 'share secrets', 'priestess secrets'
            ]
            
            if any(trigger in user_message for trigger in secret_triggers):
                return self.secrets.get_secret_knowledge()
            
            # Apply chat template
            text = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            
            # Tokenize input
            model_inputs = self.tokenizer([text], return_tensors="pt").to(self.model.device)
            
            # Set generation parameters
            gen_kwargs = {
                "max_new_tokens": generation_kwargs.get("max_new_tokens", self.config.max_new_tokens),
                "temperature": generation_kwargs.get("temperature", self.config.temperature),
                "top_p": generation_kwargs.get("top_p", self.config.top_p),
                "do_sample": generation_kwargs.get("do_sample", self.config.do_sample),
                "pad_token_id": self.tokenizer.eos_token_id,
            }
            
            # Generate response
            with torch.no_grad():
                generated_ids = self.model.generate(
                    **model_inputs,
                    **gen_kwargs
                )
            
            # Extract only the new tokens
            generated_ids = [
                output_ids[len(input_ids):] 
                for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
            ]
            
            # Decode response
            response = self.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
            return response.strip()
            
        except Exception as e:
            logger.error(f"Generation failed: {e}")
            raise

class PriestessAPI:
    """RESTful API for Priestess AI"""
    
    def __init__(self, config: PriestessConfig):
        self.app = Flask(__name__)
        self.priestess = PriestessCore(config)
        self.setup_routes()
        
    def setup_routes(self):
        """Setup API routes"""
        
        @self.app.route('/health', methods=['GET'])
        def health_check():
            """Health check endpoint"""
            return jsonify({
                "status": "healthy",
                "model_loaded": self.priestess.is_loaded,
                "timestamp": time.time()
            })
        
        @self.app.route('/load', methods=['POST'])
        def load_model():
            """Load the Priestess model"""
            try:
                if not self.priestess.is_loaded:
                    self.priestess.load_model()
                return jsonify({"status": "success", "message": "Model loaded successfully"})
            except Exception as e:
                return jsonify({"status": "error", "message": str(e)}), 500
        
        @self.app.route('/secrets', methods=['GET'])
        def get_secrets():
            """Get Priestess secret knowledge"""
            try:
                secrets = self.priestess.secrets.get_secret_knowledge()
                return jsonify({
                    "secrets": secrets,
                    "status": "success",
                    "timestamp": time.time()
                })
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/chat', methods=['POST'])
        def chat():
            """Main chat endpoint"""
            try:
                if not self.priestess.is_loaded:
                    return jsonify({"error": "Model not loaded"}), 400
                
                data = request.get_json()
                
                # Validate input
                if 'messages' not in data:
                    return jsonify({"error": "Missing 'messages' field"}), 400
                
                messages = data['messages']
                generation_kwargs = data.get('generation_kwargs', {})
                
                # Generate response
                response = self.priestess.generate_response(messages, **generation_kwargs)
                
                return jsonify({
                    "response": response,
                    "status": "success",
                    "timestamp": time.time()
                })
                
            except Exception as e:
                logger.error(f"Chat endpoint error: {e}")
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/cybersec', methods=['POST'])
        def cybersecurity_analysis():
            """Specialized cybersecurity analysis endpoint"""
            try:
                if not self.priestess.is_loaded:
                    return jsonify({"error": "Model not loaded"}), 400
                
                data = request.get_json()
                query = data.get('query', '')
                analysis_type = data.get('type', 'general')
                
                # Craft specialized cybersecurity prompt
                system_prompt = f"""You are Priestess, an expert cybersecurity AI. 
                Perform a {analysis_type} cybersecurity analysis. 
                Provide detailed, actionable insights and recommendations.
                Focus on practical security implications and mitigation strategies.
                You have access to comprehensive cybersecurity knowledge including tools, techniques, and procedures."""
                
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": query}
                ]
                
                response = self.priestess.generate_response(messages)
                
                return jsonify({
                    "analysis": response,
                    "type": analysis_type,
                    "status": "success",
                    "timestamp": time.time()
                })
                
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/devops', methods=['POST'])
        def devops_assistance():
            """Specialized DevOps assistance endpoint"""
            try:
                if not self.priestess.is_loaded:
                    return jsonify({"error": "Model not loaded"}), 400
                
                data = request.get_json()
                task = data.get('task', '')
                context = data.get('context', '')
                
                system_prompt = """You are Priestess, an expert DevOps AI assistant.
                Provide comprehensive DevOps solutions including:
                - Infrastructure as Code
                - CI/CD pipeline optimization
                - Container orchestration
                - Monitoring and observability
                - Security best practices
                - Automation strategies
                You have access to extensive knowledge of tools, commands, and best practices."""
                
                user_prompt = f"Task: {task}\nContext: {context}"
                
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
                
                response = self.priestess.generate_response(messages)
                
                return jsonify({
                    "solution": response,
                    "task": task,
                    "status": "success",
                    "timestamp": time.time()
                })
                
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @self.app.route('/code-analysis', methods=['POST'])
        def code_analysis():
            """Code security analysis endpoint"""
            try:
                if not self.priestess.is_loaded:
                    return jsonify({"error": "Model not loaded"}), 400
                
                data = request.get_json()
                code = data.get('code', '')
                language = data.get('language', 'unknown')
                
                system_prompt = """You are Priestess, an expert code security analyst.
                Analyze the provided code for:
                - Security vulnerabilities
                - Best practice violations
                - Performance issues
                - Potential exploits
                Provide specific recommendations and secure code alternatives.
                Use your extensive knowledge of security patterns and anti-patterns."""
                
                user_prompt = f"Analyze this {language} code:\n\n```{language}\n{code}\n```"
                
                messages = [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ]
                
                response = self.priestess.generate_response(messages)
                
                return jsonify({
                    "analysis": response,
                    "language": language,
                    "status": "success",
                    "timestamp": time.time()
                })
                
            except Exception as e:
                return jsonify({"error": str(e)}), 500
    
    def run(self, host='0.0.0.0', port=5000, debug=False):
        """Run the API server"""
        logger.info(f"Starting Priestess API on {host}:{port}")
        self.app.run(host=host, port=port, debug=debug)

class PriestessClient:
    """Client for interacting with Priestess API"""
    
    def __init__(self, base_url: str = "http://localhost:5000"):
        self.base_url = base_url.rstrip('/')
        
    def health_check(self) -> Dict:
        """Check API health"""
        import requests
        response = requests.get(f"{self.base_url}/health")
        return response.json()
    
    def load_model(self) -> Dict:
        """Load the model"""
        import requests
        response = requests.post(f"{self.base_url}/load")
        return response.json()
    
    def get_secrets(self) -> str:
        """Get Priestess secret knowledge"""
        import requests
        response = requests.get(f"{self.base_url}/secrets")
        result = response.json()
        return result.get("secrets", "")
    
    def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """Send chat request"""
        import requests
        data = {
            "messages": messages,
            "generation_kwargs": kwargs
        }
        response = requests.post(f"{self.base_url}/chat", json=data)
        result = response.json()
        return result.get("response", "")
    
    def cybersec_analysis(self, query: str, analysis_type: str = "general") -> str:
        """Request cybersecurity analysis"""
        import requests
        data = {
            "query": query,
            "type": analysis_type
        }
        response = requests.post(f"{self.base_url}/cybersec", json=data)
        result = response.json()
        return result.get("analysis", "")
    
    def devops_assistance(self, task: str, context: str = "") -> str:
        """Request DevOps assistance"""
        import requests
        data = {
            "task": task,
            "context": context
        }
        response = requests.post(f"{self.base_url}/devops", json=data)
        result = response.json()
        return result.get("solution", "")
    
    def analyze_code(self, code: str, language: str = "unknown") -> str:
        """Analyze code for security issues"""
        import requests
        data = {
            "code": code,
            "language": language
        }
        response = requests.post(f"{self.base_url}/code-analysis", json=data)
        result = response.json()
        return result.get("analysis", "")

# Example usage and CLI interface
def main():
    """Main function for running Priestess API"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Priestess AI API Server")
    parser.add_argument("--model-path", default="./WhiteRabbitNeo-V3-7B", help="Path to model")
    parser.add_argument("--host", default="0.0.0.0", help="Host to bind to")
    parser.add_argument("--port", type=int, default=5000, help="Port to bind to")
    parser.add_argument("--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("--auto-load", action="store_true", help="Auto-load model on startup")
    
    args = parser.parse_args()
    
    # Create configuration
    config = PriestessConfig(model_path=args.model_path)
    
    # Create and start API
    api = PriestessAPI(config)
    
    # Auto-load model if requested
    if args.auto_load:
        logger.info("Auto-loading model...")
        api.priestess.load_model()
    
    # Start server
    api.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    main()
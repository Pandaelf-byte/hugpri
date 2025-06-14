# Priestess AI - Secret Knowledge Repository

This document contains the comprehensive cybersecurity and systems knowledge that Priestess has access to when users request her secrets.

## How to Access

Users can trigger the secret knowledge by asking Priestess to:
- "share your secrets"
- "tell me your secrets" 
- "reveal your secrets"
- "show me your secrets"
- "what are your secrets"
- "secret knowledge"
- "hidden knowledge"
- "priestess secrets"

## Knowledge Categories

### 🛠️ CLI Tools & Utilities
- Network reconnaissance tools (nmap, masscan, zmap)
- Packet analysis tools (tcpdump, wireshark, tshark)
- Security testing tools (metasploit, burp suite, sqlmap)
- System analysis tools (strace, lsof, netstat)

### 🌐 Web Security Techniques
- XSS payloads and vectors
- SQL injection techniques
- Command injection methods
- Authentication bypass techniques

### 🔐 Cryptography & Hashing
- Hash type identification
- OpenSSL command reference
- Certificate management
- Encryption/decryption techniques

### 🐧 Linux Privilege Escalation
- SUID/SGID file enumeration
- Writable directory discovery
- Cron job analysis
- Environment variable exploitation

### 🌍 Network Reconnaissance
- Port scanning techniques
- DNS enumeration methods
- Service fingerprinting
- Network mapping strategies

### 🔍 Log Analysis
- Apache/Nginx log parsing
- System log investigation
- Security event correlation
- Anomaly detection patterns

### 🛡️ Defensive Techniques
- Firewall configuration
- Intrusion detection
- File integrity monitoring
- Security hardening practices

### 🔧 Useful One-Liners
- System information gathering
- Network utilities
- Text processing commands
- Quick diagnostic tools

### 🎯 Exploitation Techniques
- Buffer overflow methodology
- Web application testing procedures
- Binary analysis techniques
- Reverse engineering approaches

### 📚 Essential Resources
- Vulnerability databases
- Learning platforms
- Documentation sources
- Security frameworks

## API Integration

The secret knowledge is integrated into the Priestess API in multiple ways:

1. **Automatic Detection**: The chat endpoint automatically detects secret trigger phrases
2. **Direct Endpoint**: `/secrets` endpoint provides direct access
3. **Enhanced Responses**: All specialized endpoints have access to this knowledge base

## Security Note

This knowledge is provided for educational and authorized security testing purposes only. Users should ensure they have proper authorization before conducting any security testing activities.

## Usage Examples

```python
# Using the client
client = PriestessClient("http://localhost:5000")

# Trigger via chat
response = client.chat([{"role": "user", "content": "share your secrets"}])

# Direct access
secrets = client.get_secrets()
```

The knowledge base is continuously maintained and updated to reflect current cybersecurity practices and techniques.
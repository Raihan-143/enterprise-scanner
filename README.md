## Enterprise Network Security Auto-Scanner

An automated Python-based network reconnaissance and perimeter defense tool designed to identify unauthorized exposed services and critical security vulnerabilities across corporate infrastructure.

## Key Features
- **Target Scanning:** Fast TCP socket-level scanning on critical enterprise ports.
- **Risk Categorization:** Automatically flags sensitive administration ports (SSH, RDP, SMB, Telnet) as `CRITICAL` or `HIGH` risks.
- **Automated Logging:** Generates real-time timestamped audit logs (`security_audit_report.txt`).
- **Production-Ready Automation:** Designed for scheduled unattended execution via Linux Cron Jobs.

## Monitored Services & Risk Profile
| Port | Service | Risk Level | Description |
| :--- | :--- | :--- | :--- |
| **21** | FTP | HIGH | Unencrypted file transfer / credential leak risk |
| **22** | SSH | CRITICAL | Remote server management entry point |
| **23** | Telnet | CRITICAL | Legacy unencrypted remote shell |
| **80** | HTTP | INFO | Public web traffic |
| **443** | HTTPS | INFO | Encrypted secure web traffic |
| **445** | SMB | CRITICAL | Windows file sharing (Ransomware / Lateral Movement) |
| **3389** | RDP | CRITICAL | Remote Desktop Protocol exposed to internet |

##Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/<YOUR-USERNAME>/enterprise-scanner.git
   cd enterprise-scanner
##Run the scanner
python3 enterprise_scanner.py

##Sample Output
======================================================
     ENTERPRISE SECURITY AUDIT REPORT                 
     Target   : scanme.nmap.org                       
======================================================
[SECURE: CLOSED] Port 21    | Service: FTP         
[ALERT: OPEN]    Port 22    | Service: SSH         | Risk: CRITICAL
[SECURE: CLOSED] Port 3389  | Service: RDP         
------------------------------------------------------
  AUDIT SUMMARY: 1 High/Critical Risk(s) Detected!
------------------------------------------------------

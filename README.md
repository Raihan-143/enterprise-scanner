# 🛡️ Enterprise Network Security Auto-Scanner

An automated Python-based network reconnaissance and perimeter defense engine designed to identify exposed administrative services, detect misconfigurations, and maintain continuous compliance across corporate infrastructure.

---

## 🚀 Key Features
- **Socket-Level Reconnaissance:** Direct TCP socket probing for high-accuracy port state detection.
- **Enterprise Risk Profiling:** Automatically categorizes exposed ports by threat severity (`CRITICAL`, `HIGH`, `WARNING`, `INFO`).
- **Automated Audit Logging:** Real-time timestamped audit trails stored in `security_audit_report.txt`.
- **Headless Automation:** Engineered for unattended execution via Linux Cron Jobs.

---

## 🛡️ Security Hardening & Fault Tolerance (v1.1 Updates)
In production enterprise environments, defensive scripts must be resilient against network failures and tampering. The following hardening measures have been implemented:

- **DNS Failure Resilience:** Implemented `socket.gaierror` exception handling to prevent runtime crashes during transient network drops or malformed target hostnames.
- **Graceful Signal Termination:** Added `KeyboardInterrupt` handling to safely close active TCP sockets and release system resources upon manual termination.
- **Host-Level Access Control (Least Privilege):** 
  - Script execution restricted strictly to authorized administrative owners (`chmod 700`).
  - Audit log reports locked against unauthorized tampering or modification (`chmod 600`).

---

## 📋 Monitored Services & Risk Matrix
| Port | Service | Risk Level | Threat Vector / Rationale |
| :--- | :--- | :--- | :--- |
| **21** | FTP | HIGH | Unencrypted file transfer; credential leakage risk |
| **22** | SSH | CRITICAL | Remote server management entry point; brute-force target |
| **23** | Telnet | CRITICAL | Legacy unencrypted remote shell |
| **80** | HTTP | INFO | Standard public web traffic |
| **443** | HTTPS | INFO | Encrypted secure web traffic |
| **445** | SMB | CRITICAL | Windows file sharing; lateral movement & ransomware vector |
| **3389** | RDP | CRITICAL | Remote Desktop Protocol exposed directly to the internet |
| **8080** | HTTP-Proxy | WARNING | Alternate web service / unverified proxy service |

---

## 🛠️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Raihan-143/enterprise-scanner.git
   cd enterprise-scanner

##Apply OS-level hardening permissions:
chmod 700 enterprise_scanner.py

##Run the security audit:
python3 enterprise_scanner.py

##Sample Output
======================================================
     ENTERPRISE SECURITY AUDIT REPORT                 
     Target   : scanme.nmap.org                       
     Time     : 2026-09-25 21:13:22                   
======================================================

[SECURE: CLOSED] Port 21    | Service: FTP         
[ALERT: OPEN]    Port 22    | Service: SSH         | Risk: CRITICAL (Remote Admin Access)
[SECURE: CLOSED] Port 23    | Service: Telnet      
[ALERT: OPEN]    Port 80    | Service: HTTP        | Risk: INFO (Public Web Server)
[SECURE: CLOSED] Port 443   | Service: HTTPS       
[SECURE: CLOSED] Port 445   | Service: SMB         
[SECURE: CLOSED] Port 3389  | Service: RDP         
[SECURE: CLOSED] Port 8080  | Service: HTTP-Proxy  

------------------------------------------------------
  AUDIT SUMMARY: 1 High/Critical Risk(s) Detected!
------------------------------------------------------
[+] Audit successfully saved to: security_audit_report.txt

##Author 
Md. Raihan Hasan Rana - Cybersecurity Enthusiast

from datetime import datetime
import socket

TARGET = "scanme.nmap.org"

PORTS_TO_CHECK = {
    21: ("FTP", "HIGH RISK (Cleartext File Transfer)"),
    22: ("SSH", "CRITICAL (Remote Admin Access)"),
    23: ("Telnet", "CRITICAL (Unencrypted Remote Shell)"),
    80: ("HTTP", "INFO (Public Web Server)"),
    443: ("HTTPS", "INFO (Secure Web Server)"),
    445: ("SMB", "CRITICAL (Windows File Share - Ransomware Vector)"),
    3389: ("RDP", "CRITICAL (Remote Desktop Exposed)"),
    8080: ("HTTP-Proxy", "WARNING (Alternate Web Service)"),
}

REPORT_FILE = "security_audit_report.txt"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def run_security_audit(target):
  timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  header = (
      f"\n======================================================\n"
      f"     ENTERPRISE SECURITY AUDIT REPORT                 \n"
      f"     Target   : {target}                              \n"
      f"     Time     : {timestamp}                           \n"
      f"======================================================\n"
  )
  print(f"{BLUE}{header}{RESET}")
  report_lines = [header]
  critical_alerts = 0

  for port, (service, risk) in PORTS_TO_CHECK.items():
    try:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(1.2)
      result = s.connect_ex((target, port))

      if result == 0:
        log_entry = (
            f"[ALERT: OPEN]   Port {port:<5} | Service: {service:<12} | Risk:"
            f" {risk}"
        )
        print(f"{RED}{log_entry}{RESET}")
        report_lines.append(log_entry + "\n")
        if "CRITICAL" in risk or "HIGH" in risk:
          critical_alerts += 1
      else:
        log_entry = f"[SECURE: CLOSED] Port {port:<5} | Service: {service:<12}"
        print(f"{GREEN}{log_entry}{RESET}")
        report_lines.append(log_entry + "\n")
      s.close()

    except socket.gaierror:
      print(
          f"{RED}[-] Hostname could not be resolved! Check domain or"
          f" network.{RESET}"
      )
      break
    except KeyboardInterrupt:
      print(f"\n{YELLOW}[!] Scan interrupted by user. Exiting safely...{RESET}")
      break

  summary = (
      f"\n------------------------------------------------------\n"
      f"  AUDIT SUMMARY: {critical_alerts} High/Critical Risk(s) Detected!\n"
      f"------------------------------------------------------\n"
  )
  if critical_alerts > 0:
    print(f"{YELLOW}{summary}{RESET}")
  else:
    print(f"{GREEN}{summary}{RESET}")
  report_lines.append(summary)

  with open(REPORT_FILE, "a") as f:
    f.writelines(report_lines)
  print(f"{BLUE}[+] Audit successfully saved to: {REPORT_FILE}{RESET}\n")


if __name__ == "__main__":
  run_security_audit(TARGET)

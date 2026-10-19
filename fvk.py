
#!/usr/bin/env python3

import base64
import hashlib
import ipaddress
import socket
import urllib.request
import urllib.error
from getpass import getpass
from pathlib import Path


def pause():
    input("\nEnter press cheythu continue cheyyuka...")


def dns_lookup():
    host = input("Domain name: ").strip()
    try:
        results = socket.getaddrinfo(host, None)
        ips = sorted({item[4][0] for item in results})
        print("\nIP addresses:")
        for ip in ips:
            print(" -", ip)
    except Exception as e:
        print("Lookup failed:", e)
    pause()


def ip_calculator():
    value = input("IP address/CIDR (example 192.168.1.0/24): ").strip()
    try:
        net = ipaddress.ip_network(value, strict=False)
        print("Network:", net.network_address)
        print("Netmask:", net.netmask)
        print("Broadcast:", net.broadcast_address)
        print("Total addresses:", net.num_addresses)
        if net.version == 4:
            print("Usable hosts:", max(0, net.num_addresses - 2))
    except ValueError as e:
        print("Invalid input:", e)
    pause()


def password_checker():
    password = getpass("Enter password (hidden): ")
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(not c.isalnum() for c in password):
        score += 1

    print("Length:", len(password))
    print("Basic strength:", ["Very weak", "Weak", "Fair", "Good", "Strong", "Strong"][score])
    print("Tip: use a unique, long password or passphrase.")
    print("Never share your real password.")
    pause()


def file_hash():
    filename = input("File path: ").strip()
    try:
        digest = hashlib.sha256(Path(filename).read_bytes()).hexdigest()
        print("SHA-256:", digest)
    except Exception as e:
        print("Could not read file:", e)
    pause()


def base64_tool():
    mode = input("1 Encode text  2 Decode text: ").strip()
    value = input("Text: ")
    try:
        if mode == "1":
            result = base64.b64encode(value.encode()).decode()
            print("Encoded:", result)
        elif mode == "2":
            result = base64.b64decode(value, validate=True).decode()
            print("Decoded:", result)
        else:
            print("Invalid choice.")
    except Exception as e:
        print("Could not process input:", e)
    pause()


def security_headers():
    url = input("Public website URL (https://example.com): ").strip()
    if not url.startswith("https://"):
        print("Please use an HTTPS URL.")
        pause()
        return

    request = urllib.request.Request(
        url,
        headers={"User-Agent": "FVK-Security-Learning-Toolkit/1.0"},
        method="GET"
    )
    try:
        with urllib.request.urlopen(request, timeout=10) as response:
            headers = response.headers
            print("HTTP status:", response.status)
            checks = {
                "Strict-Transport-Security": "HSTS",
                "Content-Security-Policy": "CSP",
                "X-Content-Type-Options": "X-Content-Type-Options",
                "X-Frame-Options": "X-Frame-Options",
                "Referrer-Policy": "Referrer-Policy",
            }
            for header, label in checks.items():
                print(f"{label}: {'Present' if headers.get(header) else 'Missing'}")
    except Exception as e:
        print("Request failed:", e)
    pause()


def log_analyzer():
    filename = input("Log file path: ").strip()
    try:
        lines = Path(filename).read_text(errors="replace").splitlines()
        print("Total lines:", len(lines))
        terms = ("error", "failed", "warning", "denied")
        for term in terms:
            matches = [line for line in lines if term in line.lower()]
            print(f"\n{term.upper()}: {len(matches)}")
            for line in matches[:5]:
                print(" ", line[:250])
    except Exception as e:
        print("Could not read log:", e)
    pause()


def lessons():
    print("""
FVK SECURITY LESSONS

1. Use unique passwords and enable MFA.
2. Keep Android and apps updated.
3. Never open suspicious links or files.
4. Only test systems you own or have permission to test.
5. HTTPS encrypts data in transit; it does not prove a site is trustworthy.
6. Base64 is encoding, not encryption.
7. A missing security header alone does not prove a website is vulnerable.
""")
    pause()


def main():
    while True:
        print("""
====================================
       FVK CYBERSECURITY TOOLKIT
====================================
1. DNS Lookup
2. IP / Subnet Calculator
3. Password Strength Checker
4. SHA-256 File Hash
5. Base64 Encode / Decode
6. HTTPS Security Headers Check
7. Local Log Analyzer
8. Security Lessons
0. Exit
""")
        choice = input("FVK > ").strip()

        actions = {
            "1": dns_lookup,
            "2": ip_calculator,
            "3": password_checker,
            "4": file_hash,
            "5": base64_tool,
            "6": security_headers,
            "7": log_analyzer,
            "8": lessons,
        }

        if choice == "0":
            print("FVK closed. Stay safe!")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Choose 0-8.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# ╔══════════════════════════════════════════════════════╗
# ║           NmapScanner — by LatenT                   ║
# ║     github.com/HargosAktif | Network Pentest Tool   ║
# ╚══════════════════════════════════════════════════════╝

import subprocess
import sys
import datetime

BANNER = """
\033[95m
  _      _  _______ _   _ _______
 | |    / \|__   __| \ | |__   __|
 | |   / _ \  | |  |  \| |  | |
 | |__/ ___ \ | |  | |\  |  | |
 |____/_/   \_\|_|  |_| \_|  |_|
        NmapScanner — by LatenT
\033[0m"""

def check_nmap():
    try:
        subprocess.run(["nmap", "--version"], capture_output=True)
        return True
    except FileNotFoundError:
        print("\033[91m[!] Nmap bulunamadı. Yükle: sudo apt install nmap\033[0m")
        return False

def run_scan(target, scan_type):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\033[96m[*] Hedef  : {target}\033[0m")
    print(f"\033[96m[*] Tarama : {scan_type['name']}\033[0m")
    print(f"\033[96m[*] Zaman  : {timestamp}\033[0m")
    print("\033[93m" + "─" * 50 + "\033[0m")

    cmd = ["nmap"] + scan_type["flags"] + [target]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"\033[91m[!] Hata: {result.stderr}\033[0m")
    except KeyboardInterrupt:
        print("\n\033[91m[!] Tarama iptal edildi.\033[0m")
        sys.exit(0)

def menu():
    scan_types = {
        "1": {"name": "Hızlı Tarama",          "flags": ["-F", "-T4"]},
        "2": {"name": "Servis & Versiyon",      "flags": ["-sV", "-T4"]},
        "3": {"name": "OS Tespiti",             "flags": ["-O", "-T4"]},
        "4": {"name": "Tam Port Tarama",        "flags": ["-p-", "-T4"]},
        "5": {"name": "Agresif Tarama",         "flags": ["-A", "-T4"]},
        "6": {"name": "UDP Tarama",             "flags": ["-sU", "--top-ports", "100"]},
    }

    print("\033[95m[?] Tarama türü seçin:\033[0m")
    for k, v in scan_types.items():
        print(f"  \033[92m[{k}]\033[0m {v['name']}")

    choice = input("\n\033[93m> Seçim: \033[0m").strip()
    if choice not in scan_types:
        print("\033[91m[!] Geçersiz seçim.\033[0m")
        sys.exit(1)

    return scan_types[choice]

def main():
    print(BANNER)

    if not check_nmap():
        sys.exit(1)

    if len(sys.argv) < 2:
        target = input("\033[93m[?] Hedef IP veya domain: \033[0m").strip()
    else:
        target = sys.argv[1]

    if not target:
        print("\033[91m[!] Hedef boş olamaz.\033[0m")
        sys.exit(1)

    scan_type = menu()
    print()
    run_scan(target, scan_type)

    print("\033[92m[+] Tarama tamamlandı.\033[0m")
    print(f"\033[90m    github.com/HargosAktif\033[0m\n")

if __name__ == "__main__":
    main()

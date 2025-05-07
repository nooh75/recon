#!/usr/bin/env python3
import os
import shutil
import subprocess
from datetime import datetime

# === Logo ===
def print_logo():
    logo = """
 _   _ ______ 
| \ | |___  /
|  \| |  / / 
| |\  | / /_ 
|_| \_|/____|   Recon Tool

Powered by Nooh Zidan - NZ
    """
    print(logo)

# === Tools and Commands ===
tools_commands = {
    "subfinder": "subfinder -d {domain} -all --recursive -o subfinder.txt",
    "bbot": "bbot -d {domain} -o bbot.txt",
    "chaos": "chaos -d {domain} -key CHAOS_API_KEY -o chaos.txt",
    "findomain": "findomain -t {domain} -o findomain",
    "crtsh": "crtsh -d {domain} -o crtsh.txt",
    "github-subdomains": "github-subdomains -d {domain} -t GITHUB_TOKEN -o github_subs.txt",
    "assetfinder": "assetfinder --subs-only {domain} > assetfinder.txt"
}

# === Check if tool is installed ===
def check_tool(tool):
    return shutil.which(tool.split()[0]) is not None

# === Run a single command ===
def run_tool(tool, command, domain):
    print(f"[+] Running {tool}...")
    try:
        os.system(command.format(domain=domain))
        return True
    except Exception as e:
        print(f"[-] Error running {tool}: {e}")
        return False

# === Merge all output into one file ===
def merge_results():
    print("[+] Merging results...")
    os.system("cat *.txt | sort -u > final_result.txt")
    print("[+] Final results saved to final_result.txt")

# === Main ===
def main():
    print_logo()
    domain = input("Enter target domain: ").strip()

    used_tools = []
    skipped_tools = []

    for tool, command in tools_commands.items():
        if check_tool(command):
            success = run_tool(tool, command, domain)
            if success:
                used_tools.append(tool)
        else:
            print(f"[-] {tool} not found.")
            choice = input(f"Do you want to install {tool} now? (y/n): ").lower()
            if choice == 'y':
                print(f"[!] Please install {tool} manually and re-run the script.")
                skipped_tools.append(tool)
            else:
                print(f"[-] Skipping {tool}...")
                skipped_tools.append(tool)

    merge_results()

    print("\nScan Summary:")
    print("Tools Executed:", ", ".join(used_tools))
    print("Tools Skipped:", ", ".join(skipped_tools))
    print("\nThank you for using NZ Recon Tool!")

if __name__ == '__main__':
    main()



# 🔍 Recon Script

A powerful Bash script for domain reconnaissance and information gathering. This tool combines multiple popular utilities and online sources to gather data such as WHOIS information, subdomains, DNS records, certificate transparency logs, and more.

---

## 📌 Features

* ✅ WHOIS lookup with important fields extraction
* ✅ Reverse WHOIS lookup using registrant email
* ✅ DNS lookups using `dig` and `nslookup`
* ✅ Reverse IP lookup using [viewdns.info](https://viewdns.info)
* ✅ Certificate Transparency log search via `crt.sh`
* ✅ Subdomain enumeration using:

  * `assetfinder`
  * `subfinder`
  * `gobuster`
* ✅ Merges and deduplicates subdomains
* ✅ Resolves subdomains to IP addresses
* ✅ Color-coded terminal output

---

## 🛠️ Dependencies

Ensure the following tools are installed on your system:

* `whois`
* `dig`
* `nslookup`
* `curl`
* `jq`
* `assetfinder`
* `subfinder`
* `gobuster`

You can install most of them via:

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install whois dnsutils curl jq gobuster -y

# Install assetfinder
go install github.com/tomnomnom/assetfinder@latest

# Install subfinder
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
```

> Ensure your `$GOPATH/bin` is in your `PATH` to use `assetfinder` and `subfinder`.

---

## 📦 Output Structure

All results are saved in the `recon_output` directory, organized as:

```
recon_output/
│
├── whois/
│   ├── whois_example.com.txt
│   ├── whois_example.com_important.txt
│   └── reverse_whois_example.com.html
│
├── dns/
│   ├── nslookup_example.com.txt
│   ├── reverse_ip_example.com.html
│   └── cert_sh_example.com.json
│
└── subdomains/
    ├── assetfinder_example.com.txt
    ├── subfinder_example.com.txt
    ├── gobuster_example.com.txt
    ├── all_subs_example.com.txt
    ├── resolved_example.com.txt
    └── crtsh_example.com.txt
```

---

## 🚀 Usage

```bash
./recon.sh <domain>
```

### Example:

```bash
./recon.sh example.com
```

This will run all recon modules and save the results in the structured `recon_output/` directory.

---

## ⚠️ Notes

* This script queries external services (like `crt.sh`, `viewdns.info`) — ensure you're allowed to do so in your environment.
* Make sure `gobuster` has access to the wordlist used:
  `/usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt`

---

## 📃 License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---


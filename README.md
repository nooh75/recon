

## 📘 README.md

````markdown
# 🕵️‍♂️ Subdomain Enumeration Script

This script collects subdomains using multiple tools and organizes the results efficiently.

---

## ✅ Features

- 🔍 Subdomain discovery using:
  - `subfinder`
  - `assetfinder`
  - `crt.sh` (via `curl` + `jq`)
- 🧾 Results saved and merged into `allsubdomains.txt`
- 🗃️ Runs `bbot` separately and saves its raw JSON output in `bbot_output.json`

---

## ⚙️ Requirements

Ensure the following tools are installed and accessible in your `$PATH`:

- `subfinder`
- `assetfinder`
- `bbot`
- `curl`
- `jq`

Installation commands:

```bash
# subfinder
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# assetfinder
go install github.com/tomnomnom/assetfinder@latest

# bbot
pip install bbot

# jq
sudo apt install jq -y
````

---

## 🚀 Usage

```bash
chmod +x collect_subs.sh
./collect_subs.sh example.com
```

---

## 📂 Output

```text
subs_example.com/
├── assetfinder.txt
├── bbot_output.json   👈 bbot result (not merged)
├── crtsh.txt
├── subfinder.txt
└── allsubdomains.txt  ✅ merged, deduplicated list
```

---

## 📝 Notes

* `bbot_output.json` contains full structured output and is not merged with the others.
* The file `allsubdomains.txt` is merged from:

  * subfinder
  * assetfinder
  * crt.sh (removes wildcards)
* Duplicates are removed using `sort -u`.

---


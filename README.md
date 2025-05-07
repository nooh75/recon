###  `README.md`

````markdown
# NZ Recon Tool 

A powerful and modular **Bug Bounty Subdomain Enumeration** automation tool developed by **Nooh Zidan (Na7na7)**. It automates multiple subdomain discovery tools, checks installation, executes scans, and merges the results into a single output file.

---

##  Features

- Logo and branding (NZ)
- Tool auto-detection
- Interactive tool installation prompts
- Aggregated subdomain enumeration
- Result merging into `final_result.txt`
- Full scan summary report

---

##  Tools Used

- [subfinder](https://github.com/projectdiscovery/subfinder)
- [bbot](https://github.com/blacklanternsecurity/bbot)
- [chaos](https://github.com/projectdiscovery/chaos-client)
- [findomain](https://github.com/Findomain/Findomain)
- [crtsh](https://github.com/nahamsec/crtsh)
- [github-subdomains](https://github.com/gwen001/github-subdomains)
- [assetfinder](https://github.com/tomnomnom/assetfinder)

---

##  Requirements

Make sure you install the following tools before running the script:

```bash
sudo apt install -y findomain
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/projectdiscovery/chaos-client/cmd/chaos@latest
pip install -r requirements.txt
````

Manual installs (or use precompiled binaries):

* bbot
* github-subdomains
* crtsh


---

##  Installation

```bash
git clone https://github.com/yourusername/nz-recon-tool
cd nz-recon-tool
chmod +x nz-recon.py
```

---

##  Usage

```bash
./nz-recon.py
```

Enter the target domain when prompted. The tool will check for each recon utility, prompt to install if missing, run the scan, and finally merge all output into a single file called `final_result.txt`.

---

##  Output

* All individual tool outputs are saved as `.txt` files
* Final results are stored in `final_result.txt`

---

##  Powered By

```
NZ - Na7na7 Recon Tool
Developed by Nooh Zidan
```

---

##  Contributions

Pull requests are welcome. For major changes, open an issue first to discuss what you would like to change.

---



---

###  `requirements.txt`

If your script has Python-specific needs (like for `dnscan`, `argparse`, etc.), include this:

```txt
requests
argparse
````



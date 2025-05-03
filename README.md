
#  Recon Methodology

##  Phase 1: Scope Definition & Asset Profiling

###  1. Company Research

Use platforms:

- [Crunchbase](https://www.crunchbase.com/)
- [Dealroom](https://dealroom.co/)
- [TechCrunch](https://techcrunch.com/)

###  2. ASN Enumeration

```bash
amass intel -org "Target Inc" -whois
asnmap -t target.com -silent -o asnmap.txt
````

###  3. CIDR to IPs to Domains

```bash
mapcidr -cidr 192.0.2.0/24 -o ips.txt
cat ips.txt | hakrevdns -o domains.txt
```

###  4. Chaos Enumeration

```bash
chaos -d target.com -key CHAOS_API_KEY -o chaos_domains.txt
```

---

##  Phase 2: Subdomain Enumeration

### 1. Passive Enumeration

```bash
subfinder -d target.com -all -silent > subs.txt
assetfinder --subs-only target.com >> subs.txt
findomain -t target.com -o >> subs.txt
crtsh -d target.com >> subs.txt
github-subdomains -d target.com -t GITHUB_TOKEN >> subs.txt
```

### 2. Active Enumeration

```bash
amass enum -active -brute -d target.com -o amass.txt
dnsx -l subs.txt -a -resp-only -silent -o resolved.txt
```

### 3. Permutations & Wordlists

```bash
dnsgen subs.txt -w permutations.txt | \
massdns -r resolvers.txt -t A -o S -w massdns_output.txt
```

### 4. Final Consolidation

```bash
cat subs.txt amass.txt chaos_domains.txt massdns_output.txt | \
sort -u > all_subs.txt
```

---

##  Phase 3: Live Host Discovery

```bash
httpx -l all_subs.txt -silent -title -status-code -tech-detect -o live_subs.txt
```

---

## 🕸 Phase 4: Web Content Discovery & Crawling

### 1. URL Harvesting

```bash
cat live_subs.txt | waybackurls > wayback.txt
cat live_subs.txt | gau > gau.txt
waymore -i all_subs.txt -mode U > waymore.txt

sort -u wayback.txt gau.txt waymore.txt > all_urls.txt
```

### 2. Crawling & Endpoint Discovery

```bash
katana -list live_subs.txt -jc -o katana.txt
hakrawler -subs -insecure -depth 3 < live_subs.txt > hakrawler.txt

sort -u katana.txt hakrawler.txt > endpoints.txt
```

### 3. JS File Analysis

```bash
subjs -i live_subs.txt > jsfiles.txt

cat jsfiles.txt | xargs -n1 -I{} curl -s {} | \
LinkFinder -i stdin -o cli > js_endpoints.txt

github-endpoints.py -d target.com -t GITHUB_TOKEN > github_js_endpoints.txt
```

### 4. Parameter Discovery

```bash
paramspider -d target.com -o params.txt
arjun -i live_subs.txt -t 20 -oT arjun_params.txt
```

---

##  Phase 5: Vulnerability Probing

### 1. Fuzzing

```bash
ffuf -w wordlist.txt -u https://target.com/FUZZ -mc 200
```

### 2. XSS Testing

```bash
cat params.txt | qsreplace '"'><script>alert(1)</script>' | \
while read url; do
  curl -s "$url" | grep -q '<script>alert(1)</script>' && echo "$url VULNERABLE"
done

kxss -i params.txt -o kxss.txt
```

### 3. Nuclei Scanning

```bash
nuclei -l live_subs.txt -t cves/ -o nuclei_cves.txt
nuclei -l all_urls.txt -tags xss,ssrf,sqli -o nuclei_web_vulns.txt
```

### 4. Subdomain Takeover

```bash
subzy run --targets live_subs.txt
```

### 5. Broken Link Hijacking

```bash
socialhunter -f live_subs.txt
```

### 6. Port & Service Scanning

```bash
naabu -list all_subs.txt -o ports.txt
nmap -iL ports.txt -sV --script vuln -oN nmap_results.txt
```

---

## 📊 Phase 6: Post-Recon Analysis & Reporting

### 1. Filtering & Triage

```bash
unfurl -u all_urls.txt -o parsed.txt
filter-resolved -i all_subs.txt -o valid.txt
```

### 2. Screenshotting

```bash
gowitness file -f live_subs.txt -P ./screenshots/
aquatone -list live_subs.txt -out screenshots/
```

### 3. Directory Management

```bash
mkdir -p recon/target.com/{subs,urls,js,screenshots,vulns}
```

### 4. Periodic Refresh

```bash
# Automate recon weekly/monthly via cron
```

---

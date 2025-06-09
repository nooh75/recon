#!/bin/bash

# Colors
GREEN="\033[0;32m"
YELLOW="\033[1;33m"
RED="\033[0;31m"
NC="\033[0m"

# Check input
if [ -z "$1" ]; then
    echo -e "${YELLOW}[!] Usage: $0 <domain>${NC}"
    exit 1
fi

domain=$1
output_dir="subs_$domain"
mkdir -p "$output_dir"

echo -e "${GREEN}[+] Collecting subdomains for: $domain${NC}"

# 1. Subfinder
echo -e "${YELLOW}[*] Running subfinder...${NC}"
subfinder -d "$domain" -silent -o "$output_dir/subfinder.txt"

# 2. Assetfinder
echo -e "${YELLOW}[*] Running assetfinder...${NC}"
assetfinder --subs-only "$domain" > "$output_dir/assetfinder.txt"

# 3. bbot
echo -e "${YELLOW}[*] Running bbot...${NC}"
bbot -t "$domain" -m subdomain-enum -o "$output_dir/bbot.json" --no-interaction >/dev/null 2>&1
jq -r '.results[] | select(.module=="subdomain-enum") | .data' "$output_dir/bbot.json" > "$output_dir/bbot.txt"

# 4. crt.sh
echo -e "${YELLOW}[*] Fetching from crt.sh...${NC}"
curl -s "https://crt.sh/?q=${domain}&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u > "$output_dir/crtsh.txt"

# 5. Merge all
echo -e "${YELLOW}[*] Merging results...${NC}"
cat "$output_dir/"*.txt | sort -u > "$output_dir/allsubdomains.txt"

echo -e "${GREEN}[✓] All subdomains saved in: $output_dir/allsubdomains.txt${NC}"

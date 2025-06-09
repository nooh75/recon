#!/bin/bash

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Check for domain argument
if [ -z "$1" ]; then
    echo -e "${RED}[!] Usage: $0 domain.com${NC}"
    exit 1
fi

domain=$1
output_dir="subs_$domain"
mkdir -p "$output_dir"

echo -e "${GREEN}[+] Running subfinder...${NC}"
subfinder -d "$domain" -silent -all -o "$output_dir/subfinder.txt"

echo -e "${GREEN}[+] Running assetfinder...${NC}"
assetfinder --subs-only "$domain" > "$output_dir/assetfinder.txt"

echo -e "${GREEN}[+] Running bbot (JSON only)...${NC}"
bbot -t "$domain" -f json -o "$output_dir/bbot_output.json"

echo -e "${GREEN}[+] Getting subdomains from crt.sh...${NC}"
curl -s "https://crt.sh/?q=%25.$domain&output=json" | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u > "$output_dir/crtsh.txt"

echo -e "${GREEN}[+] Merging subdomain results...${NC}"
cat "$output_dir/subfinder.txt" "$output_dir/assetfinder.txt" "$output_dir/crtsh.txt" | sort -u > "$output_dir/allsubdomains.txt"

echo -e "${GREEN}[✔] Done! All subdomains saved in $output_dir/allsubdomains.txt${NC}"
echo -e "${GREEN}[✔] bbot raw output saved in $output_dir/bbot_output.json${NC}"

"""Simple IOC extractor for markdown-based case files.

Purpose:
- scan offense or report markdown files
- extract likely IPs, usernames, domains, and hashes
- help convert analyst notes into a reusable IOC list

This is intentionally lightweight and portfolio-friendly.
"""

import re
import sys
from pathlib import Path

IP_RE = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
HASH_RE = re.compile(r'\b[a-fA-F0-9]{32,64}\b')
USER_RE = re.compile(r'\b(?:root|admin|administrator|[A-Za-z][A-Za-z0-9._-]{2,})\b')

def extract(text: str):
    return {
        "ips": sorted(set(IP_RE.findall(text))),
        "hashes": sorted(set(HASH_RE.findall(text))),
        "usernames": sorted(set(USER_RE.findall(text))),
    }

def main():
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    files = list(target.rglob("*.md")) if target.is_dir() else [target]
    combined = {"ips": set(), "hashes": set(), "usernames": set()}

    for f in files:
        try:
            data = extract(f.read_text(encoding="utf-8", errors="ignore"))
            for k, vals in data.items():
                combined[k].update(vals)
        except Exception as e:
            print(f"[!] Skipped {f}: {e}")

    print("=== Extracted IOCs ===")
    for key in ("ips", "usernames", "hashes"):
        print(f"\n{key.upper()}:")
        for item in sorted(combined[key]):
            print(f"- {item}")

if __name__ == "__main__":
    main()

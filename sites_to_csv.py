#!/usr/bin/env python3
import csv
import sys

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sites.txt"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sites.csv"

    def scheme_and_key(site):
        if site.startswith("http://"):
            return "http", site[len("http://"):]
        if site.startswith("https://"):
            return "https", site[len("https://"):]
        return None, site

    rows = {}
    with open(input_path, encoding="utf-8") as infile:
        for line_num, line in enumerate(infile, start=1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                print(f"Skipping malformed line {line_num}: {line!r}", file=sys.stderr)
                continue
            site, login, password = parts[0], parts[1], parts[2]
            scheme, key = scheme_and_key(site)

            existing = rows.get(key)
            if existing is not None and existing[0] == "https" and scheme == "http":
                continue
            rows[key] = (scheme, site, login, password)

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["site", "login", "password"])
        for key in sorted(rows):
            _, site, login, password = rows[key]
            writer.writerow([site, login, password])

    print(f"Done: {output_path}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import csv
import socket
import sys
import xmlrpc.client

TIMEOUT = 60

def build_endpoint(site):
    return site.rstrip("/") + "/xmlrpc.php"

def check_login(site, login, password):
    endpoint = build_endpoint(site)
    server = xmlrpc.client.ServerProxy(endpoint)
    socket.setdefaulttimeout(TIMEOUT)
    server.wp.getUsersBlogs(login, password)

def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "sites.csv"

    with open(csv_path, encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if "valid" not in fieldnames:
        fieldnames = fieldnames + ["valid"]
    if "error" not in fieldnames:
        fieldnames = fieldnames + ["error"]

    def save():
        with open(csv_path, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

    for row in rows:
        site = row["site"]
        login = row["login"]
        password = row["password"]
        try:
            check_login(site, login, password)
            row["valid"] = "true"
            row["error"] = ""
            print(f"OK   {site}")
        except Exception as e:
            row["valid"] = "false"
            row["error"] = str(e)
            print(f"FAIL {site} -> {e}", file=sys.stderr)
        save()

if __name__ == "__main__":
    main()

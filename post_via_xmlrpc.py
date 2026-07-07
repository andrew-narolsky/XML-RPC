#!/usr/bin/env python3
import csv
import sys
import xmlrpc.client

def build_endpoint(site):
    return site.rstrip("/") + "/xmlrpc.php"

def create_post(site, login, password, title, description):
    endpoint = build_endpoint(site)
    server = xmlrpc.client.ServerProxy(endpoint)
    content = {"title": title, "description": description}
    post_id = server.metaWeblog.newPost(0, login, password, content, True)
    post = server.metaWeblog.getPost(post_id, login, password)
    return post["link"]

def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "sites.csv"

    with open(csv_path, encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    if "url" not in fieldnames:
        fieldnames = fieldnames + ["url"]

    for row in rows:
        site = row["site"]
        login = row["login"]
        password = row["password"]
        title = row["title"]
        description = row["description"]
        try:
            url = create_post(site, login, password, title, description)
            row["url"] = url
            print(f"OK   {site} -> {url}")
        except Exception as e:
            row["url"] = ""
            print(f"FAIL {site} -> {e}", file=sys.stderr)

    with open(csv_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    main()

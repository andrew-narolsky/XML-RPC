#!/usr/bin/env python3
import csv
import sys

TITLE = "Test Post"
DESCRIPTION = "This is a test post."

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sites.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sites.csv"

    with open(input_path, encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        rows = list(reader)

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["site", "login", "password", "title", "description"])
        for row in rows:
            writer.writerow([row["site"], row["login"], row["password"], TITLE, DESCRIPTION])

    print(f"Done: {output_path}")

if __name__ == "__main__":
    main()

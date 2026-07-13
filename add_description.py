#!/usr/bin/env python3
import csv
import json
import sys

def main():
    input_path = sys.argv[1] if len(sys.argv) > 1 else "sites.csv"
    output_path = sys.argv[2] if len(sys.argv) > 2 else "sites.csv"
    data_path = sys.argv[3] if len(sys.argv) > 3 else "data.json"

    with open(input_path, encoding="utf-8", newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        rows = list(reader)

    with open(data_path, encoding="utf-8") as datafile:
        data = json.load(datafile)

    if len(data) < len(rows):
        sys.exit(f"Not enough entries in {data_path}: need {len(rows)}, got {len(data)}")

    with open(output_path, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames + ["description"])
        writer.writeheader()
        for row, entry in zip(rows, data):
            row["description"] = entry["Content"]
            writer.writerow(row)

    print(f"Done: {output_path}")

if __name__ == "__main__":
    main()
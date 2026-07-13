#!/usr/bin/env python3
"""Compare sites.csv and sites_2.csv, write rows from sites_2.csv missing in sites.csv to sites_res.csv."""
import csv

SITES_1 = "sites.csv"
SITES_2 = "sites_2.csv"
RESULT = "sites_res.csv"


def read_rows(path):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)
    return header, rows


def main():
    header1, rows1 = read_rows(SITES_1)
    header2, rows2 = read_rows(SITES_2)

    known_sites = {row[0] for row in rows1 if row}
    missing = [row for row in rows2 if row and row[0] not in known_sites]

    with open(RESULT, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header2)
        writer.writerows(missing)

    print(f"sites.csv: {len(rows1)} rows")
    print(f"sites_2.csv: {len(rows2)} rows")
    print(f"missing in sites.csv: {len(missing)} rows -> {RESULT}")


if __name__ == "__main__":
    main()
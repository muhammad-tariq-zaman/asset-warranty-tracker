"""Track asset warranties from a CSV (serial,asset,warranty_end).

Usage: python3 main.py assets.csv --within-days 90 --today 2026-10-29
"""
import argparse
import csv
import sys
from datetime import date


def status(end, today, within):
    days = (end - today).days
    if days < 0:
        return "EXPIRED"
    if days <= within:
        return "EXPIRING SOON"
    return "OK"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", help="CSV with serial,asset,warranty_end columns")
    parser.add_argument("--within-days", type=int, default=90)
    parser.add_argument("--today", default=None)
    args = parser.parse_args(argv)
    today = date.fromisoformat(args.today) if args.today else date.today()
    rows = []
    with open(args.path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            end = date.fromisoformat(row["warranty_end"])
            rows.append((end, row, status(end, today, args.within_days)))
    rows.sort()
    for end, row, state in rows:
        print(f"{row['serial']} ({row['asset']}): {state} (ends {end.isoformat()})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

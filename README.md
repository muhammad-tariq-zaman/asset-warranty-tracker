# asset-warranty-tracker

List assets by warranty expiry: expired, expiring within N days, or OK, soonest expiry first.

## How to run

```sh
python3 main.py assets.csv --within-days 90
```

## Example output

```
SN-100 (Laptop): EXPIRED (ends 2026-01-01)
SN-101 (Monitor): EXPIRING SOON (ends 2026-12-01)
```

Standard library only. Run the tests with `python3 -m unittest discover`.

# Invoice Generator — P2P Crypto Market

Single-file Python script that generates clean, professional HTML invoices.  
Designed for P2P crypto traders — edit the `DATA` dict, run, get an invoice.

## Features

- Clean, modern design (dark text, purple accent)
- P2P Market badge
- Multi-asset support (USDT, BTC, ETH, custom)
- Network fee included
- Payment info section
- Mobile responsive
- No dependencies — Python 3 only
- Single file output, ready to print/send

## Usage

```bash
# 1. Edit gen.py — change DATA section
# 2. Generate
python3 gen.py

# 3. Open invoice-output.html
```

## Customize

Edit the `DATA` dictionary in `gen.py`:

```python
DATA = {
    "invoice_no": "INV-2026-001",
    "date": "July 9, 2026",
    "due_date": "July 16, 2026",

    "seller": {
        "name": "Your Brand",
        "subtitle": "P2P Crypto Market",
        "address": "City, Country",
        "email": "you@email.com",
        "phone": "+62 812-3456-7890"
    },

    "buyer": {
        "name": "Client Name",
        "company": "",
        "email": ""
    },

    "items": [
        {"asset": "USDT (ERC-20)", "qty": 1000, "rate": 1.00},
        {"asset": "BTC", "qty": 0.05, "rate": 85000},
    ],

    "payment": {
        "bank": "Bank BCA",
        "account": "123-456-7890",
        "name": "Your Name"
    },

    "note": "Market rate applied. Wallet shared after payment."
}
```

## Output

Opens in any browser — ready to print or send to clients.

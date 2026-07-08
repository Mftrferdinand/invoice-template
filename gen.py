import json, sys, os
from datetime import datetime

# ════════════════════════════════════════════
#  Invoice Generator — P2P Crypto Market
#  Edit DATA below, run: python3 gen.py
# ════════════════════════════════════════════

DATA = {
    "invoice_no": "INV-2026-001",
    "date": "July 9, 2026",
    "due_date": "July 16, 2026",

    "seller": {
        "name": "Your Name / Brand",
        "subtitle": "P2P Crypto Market",
        "address": "Jakarta, Indonesia",
        "email": "you@example.com",
        "phone": "+62 812-3456-7890"
    },

    "buyer": {
        "name": "Client Name",
        "company": "",
        "email": ""
    },

    "items": [
        {"asset": "USDT (ERC-20)", "qty": 1000, "rate": 1.00},
        {"asset": "BTC - Bitcoin",   "qty": 0.05, "rate": 85000},
        {"asset": "ETH - Ethereum",  "qty": 2,    "rate": 3200},
    ],

    "payment": {
        "bank": "Bank BCA",
        "account": "123-456-7890",
        "name": "Your Name"
    },

    "note": "Price based on real-time market rate. Wallet address shared after payment confirmed."
}

# ════════════════════════════════════════════
#  DO NOT EDIT BELOW (template rendering)
# ════════════════════════════════════════════

def generate(data):
    subtotal = sum(i["qty"] * i["rate"] for i in data["items"])

    items_html = ""
    for item in data["items"]:
        amount = item["qty"] * item["rate"]
        q = f"{item['qty']:,.2f}" if item["qty"] < 1 else f"{item['qty']:,.0f}"
        items_html += f"""  <tr><td>{item['asset']}</td><td>{q}</td><td>${item['rate']:,.2f}</td><td>${amount:,.2f}</td></tr>\n"""

    S = data["seller"]; B = data["buyer"]; P = data["payment"]

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Invoice {data['invoice_no']} — {S['name']}</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Inter',-apple-system,sans-serif;background:#f5f5f5;display:flex;justify-content:center;padding:40px 12px;color:#1a1a1a}}
.invoice{{max-width:680px;width:100%;background:#fff;border-radius:16px;padding:44px 36px;box-shadow:0 1px 4px rgba(0,0,0,.06),0 8px 32px rgba(0,0,0,.08)}}
.header{{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:36px}}
.brand{{font-size:1.5rem;font-weight:800;color:#111}}
.brand span{{color:#8b5cf6}}.brand .tag{{font-size:.7rem;color:#aaa;font-weight:500;margin-top:2px}}
.ilabel{{text-align:right}}.ilabel h2{{font-size:1.3rem;font-weight:700;color:#8b5cf6}}
.ilabel p{{font-size:.82rem;color:#888;margin-top:2px}}
.grid{{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-bottom:32px}}
.sec h4{{font-size:.68rem;text-transform:uppercase;letter-spacing:.08em;color:#aaa;margin-bottom:6px}}
.sec p{{font-size:.88rem;line-height:1.65;color:#333}}.sec.right{{text-align:right}}
.badge{{display:inline-block;background:#f3f0ff;color:#7c3aed;font-size:.7rem;font-weight:600;padding:3px 10px;border-radius:6px;margin-bottom:8px}}
table{{width:100%;border-collapse:collapse;margin-bottom:28px}}
thead th{{text-align:left;font-size:.7rem;text-transform:uppercase;letter-spacing:.06em;color:#999;padding-bottom:10px;border-bottom:2px solid #eee}}
thead th:last-child,tbody td:last-child{{text-align:right}}
tbody td{{padding:12px 0;font-size:.87rem;color:#333;border-bottom:1px solid #f5f5f5}}
.totals{{margin-left:auto;width:240px}}
.totals .r{{display:flex;justify-content:space-between;padding:6px 0;font-size:.87rem;color:#555}}
.totals .r.t{{border-top:2px solid #333;padding-top:12px;margin-top:4px;font-size:1.1rem;font-weight:700;color:#111}}
.pay{{margin-top:28px;padding:20px;background:#fafafa;border-radius:10px}}
.pay h4{{font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;color:#aaa;margin-bottom:8px}}
.pay p{{font-size:.83rem;color:#555;line-height:1.75}}
.note{{margin-top:16px;padding:12px 16px;background:#fff8e1;border-radius:8px;border-left:3px solid #ffc107}}
.note p{{font-size:.78rem;color:#8d6e00;line-height:1.6}}
.foot{{margin-top:28px;text-align:center;font-size:.74rem;color:#ccc}}
@media(max-width:480px){{.invoice{{padding:28px 18px}}.grid{{grid-template-columns:1fr;gap:16px}}.header{{flex-direction:column;gap:16px}}.ilabel{{text-align:left}}.sec.right{{text-align:left}}}}
</style></head><body>
<div class="invoice">
<div class="header">
<div><div class="brand">{S['name'].split()[0]}<span>{''.join(S['name'].split()[1:])}</span></div><div class="tag">{S['subtitle']}</div></div>
<div class="ilabel"><span class="badge">P2P MARKET</span><h2>INVOICE</h2><p># {data['invoice_no']}</p></div>
</div>
<div class="grid">
<div class="sec"><h4>From</h4><p>{S['name']}<br>{S['address']}<br>{S['email']}<br>{S['phone']}</p></div>
<div class="sec right"><h4>To</h4><p>{B['name']}<br>{B['company']}<br>{B['email']}</p></div>
<div class="sec"><h4>Date</h4><p>{data['date']}</p></div>
<div class="sec right"><h4>Due</h4><p>{data['due_date']}</p></div>
</div>
<table><thead><tr><th>Asset</th><th>Qty</th><th>Rate (USD)</th><th>Amount</th></tr></thead><tbody>
{items_html}</tbody></table>
<div class="totals"><div class="r"><span>Subtotal</span><span>${subtotal:,.2f}</span></div><div class="r"><span>Network Fee</span><span>Included</span></div><div class="r t"><span>Total</span><span>${subtotal:,.2f}</span></div></div>
<div class="pay"><h4>Payment</h4><p>{P['bank']}<br>{P['account']}<br>a/n {P['name']}</p></div>
<div class="note"><p>{data['note']}</p></div>
<div class="foot">{S['name']} — {S['subtitle']}</div>
</div></body></html>"""

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "invoice-output.html"
    with open(out, "w") as f:
        f.write(generate(DATA))
    print(f"✅ Invoice saved: {out} | Total: ${sum(i['qty']*i['rate'] for i in DATA['items']):,.2f}")

#!/usr/bin/env python3
"""The calls our wallets showed as ⚠️ (nothing could read them), most seen first: the descriptors to write next.

    python3 tools/misses.py

Reads wedgie.dev/api/misses (both wallets report there; chain, contract, function only). Names each function
(Sourcify's signature list) and each contract (Sourcify). "has a descriptor": one here or in the EF registry names
the contract (it may lack this function, or have landed since).
"""
import glob, json, os, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, "..", "clear-review", "registry")


def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "clear-descriptors"}), timeout=15) as r:
            return json.load(r)
    except Exception:
        return None


def covered():
    """chain:address of every calldata descriptor here and in the EF checkout clear-review keeps."""
    out = set()
    for d in (os.path.join(ROOT, "registry"), os.path.join(REG, "registry")):
        for p in glob.glob(os.path.join(d, "**", "calldata-*.json"), recursive=True):
            try:
                j = json.load(open(p))
            except Exception:
                continue
            for x in ((j.get("context") or {}).get("contract") or {}).get("deployments") or []:
                out.add(f"{x.get('chainId')}:{str(x.get('address', '')).lower()}")
    return out


def main():
    rows = get("https://wedgie.dev/api/misses") or []
    if not rows:
        print("No misses.")
        return
    have = covered()
    for r in rows:
        f = get(f"https://api.4byte.sourcify.dev/signature-database/v1/lookup?function={r['sel']}&filter=true")
        fn = " or ".join(x["name"] for x in ((f or {}).get("result", {}).get("function", {}).get(r["sel"]) or [])[:2]) or r["sel"]
        c = get(f"https://sourcify.dev/server/v2/contract/{r['chain']}/{r['addr']}?fields=compilation")
        name = ((c or {}).get("compilation") or {}).get("name") or "unverified"
        print(f"{r['n']:>4}  chain {r['chain']:<6} {r['addr']}  {name:<24} {fn}  ({r['app']}, last {r['last_at'][:10]})"
              + ("  has a descriptor" if f"{r['chain']}:{r['addr']}" in have else ""))


main()

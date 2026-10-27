#!/usr/bin/env python3
"""Rebuild STATUS.md and show.json from status.json, the registry, and clear-review's grades.

    python3 tools/status.py [--registry <registry checkout>] [--review <clear-review index.json>] [--no-gh]

--registry: default ../clear-review/registry (a checkout clear-review keeps), else a shallow clone in $TMPDIR.
--review:   default ../clear-review/index.json, else clear-review's on GitHub.
--no-gh:    don't ask GitHub for PR states (offline); stages stay as status.json has them.

status.json is the only file people (and agents) edit by hand. This writes:
  status.json  PR stages refreshed from GitHub (open -> pr, merged -> merged, closed -> closed)
  show.json    what wedgie.dev's clear-signing build reads: our descriptors to add, the functions to hide
  STATUS.md    all of it as tables
"""
import glob, json, os, subprocess, sys, tempfile, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPSTREAM = "ethereum/clear-signing-erc7730-registry"
REVIEW_URL = "https://raw.githubusercontent.com/clawdbotatg/clear-review/main/index.json"
CYFRIN = "0x3846c3A30E62075Fa916216b35EF04B8F53931f6"
STAGES = ("draft", "pr", "merged", "closed")


def arg(name, default=None):
    a = sys.argv[1:]
    return a[a.index(name) + 1] if name in a else default


def registry():
    r = arg("--registry", os.path.join(ROOT, "..", "clear-review", "registry"))
    if os.path.isdir(os.path.join(r, "registry")):
        return r
    r = os.path.join(tempfile.gettempdir(), "erc7730-registry-status")
    if not os.path.isdir(r):
        subprocess.run(["git", "clone", "-q", "--depth", "1", "https://github.com/%s.git" % UPSTREAM, r], check=True)
    return r


def review():
    p = arg("--review", os.path.join(ROOT, "..", "clear-review", "index.json"))
    if os.path.isfile(p):
        return json.load(open(p))["functions"]
    with urllib.request.urlopen(REVIEW_URL, timeout=60) as r:
        return json.load(r)["functions"]


def deployments(path):
    """[(chainId, address lowercase)] a descriptor file binds (no includes followed: ours are self-contained)."""
    try:
        d = json.load(open(path))
    except (OSError, ValueError):
        return []
    return [(int(x["chainId"]), x["address"].lower()) for x in (d.get("context", {}).get("contract", {}).get("deployments") or [])]


def pr_state(n):
    r = subprocess.run(["gh", "pr", "view", str(n), "--repo", UPSTREAM, "--json", "state", "--jq", ".state"],
                       capture_output=True, text=True)
    return {"OPEN": "pr", "MERGED": "merged", "CLOSED": "closed"}.get(r.stdout.strip())


def main():
    sp = os.path.join(ROOT, "status.json")
    st = json.load(open(sp))
    reg = registry()
    grades = review()

    # ---- ours: refresh PR stages, check each row points at a real file
    for f, o in st["ours"].items():
        assert os.path.isfile(os.path.join(ROOT, f)), "status.json names %s, which isn't here" % f
        assert o["stage"] in STAGES, "%s: stage %r (one of %s)" % (f, o["stage"], ", ".join(STAGES))
        if o.get("pr") and "--no-gh" not in sys.argv:
            s = pr_state(o["pr"])
            if s:
                o["stage"] = s
    with open(sp, "w") as fh:
        json.dump(st, fh, indent=2)
        fh.write("\n")

    # ---- the registry: audited files (a Cyfrin attestation file; wedgie.dev's build checks its signature)
    files = sorted(os.path.relpath(p, reg) for d in ("registry", "ercs")
                   for p in glob.glob(os.path.join(reg, d, "**", "calldata-*.json"), recursive=True)
                   if not {"tests", "testsv2", "sigs"} & set(p.split(os.sep)))
    audited = {f for f in files if glob.glob(os.path.join(reg, os.path.dirname(f), "sigs",
                                                          os.path.basename(f)[:-5] + ".*%s.json" % CYFRIN))}

    # ---- hidden: clear-review F's (unless unhidden by hand), then hand-picked ones
    unhide = st.get("unhide", {})
    hide, auto = [], {}
    for k, v in sorted(grades.items()):
        if v["grade"] == "F" and k not in unhide:
            hide.append({"key": k, "file": v["file"], "why": "clear-review F (truth %s, clarity %s)" % (v["truth"], v["clarity"])})
            auto.setdefault(v["file"], []).append(k)
    for f, h in st.get("hide", {}).items():
        for c, a in deployments(os.path.join(reg, f)):
            for sel in h["selectors"]:
                hide.append({"key": "%d:%s:%s" % (c, a, sel), "file": f, "why": h["why"]})

    # ---- show.json: our files not in the registry yet (and not given up on), the hidden functions
    add = [f for f, o in st["ours"].items() if o["stage"] in ("draft", "pr") and o.get("show", True)]
    with open(os.path.join(ROOT, "show.json"), "w") as fh:
        json.dump({"add": add, "hide": hide}, fh, indent=1)
        fh.write("\n")

    # ---- STATUS.md
    L = ["# Status", "",
         "Made by `tools/status.py` from `status.json`. Don't edit by hand.", "",
         "Stages: **draft** (here only) → **pr** (open on the registry) → **merged** (in the registry; wedgie.dev "
         "then takes the registry's copy) · **closed** (PR closed unmerged).", "",
         "## Ours", "",
         "| Descriptor | What | Stage | PR | On the wedgie |", "|---|---|---|---|---|"]
    for f, o in st["ours"].items():
        pr = " ".join("[#%d](https://github.com/%s/pull/%d)" % (n, UPSTREAM, n) for n in [o.get("pr")] if n)
        if o.get("builds_on"):
            pr += " (on %s)" % ", ".join("#%d" % n for n in o["builds_on"])
        on = "ours" if f in add else "registry's" if o["stage"] == "merged" else "no"
        L.append("| `%s` | %s | %s | %s | %s |" % (f, o["what"], o["stage"], pr or "—", on))
    L += ["", "## Hidden by hand", ""]
    if st.get("hide"):
        L += ["| Descriptor | Selectors | Why |", "|---|---|---|"]
        L += ["| `%s` | %s | %s |" % (f, " ".join(h["selectors"]), h["why"]) for f, h in st["hide"].items()]
    else:
        L.append("None.")
    L += ["", "## Hidden: clear-review F", "",
          "A function graded F (its screen says something untrue or unreadable) isn't shown: the wedgie says it "
          "can't read it. Undo one with `unhide` in status.json.", "",
          "%d functions in %d files (%d chain:address:function entries in show.json)." % (
              sum(len({k.rsplit(":", 1)[1] for k in v}) for v in auto.values()), len(auto), sum(len(v) for v in auto.values())), "",
          "| Descriptor | F functions | Chains | Audited |", "|---|---|---|---|"]
    fn = lambda f: len({k.rsplit(":", 1)[1] for k in auto[f]})
    for f in sorted(auto, key=lambda f: (-fn(f), f)):
        L.append("| `%s` | %d | %d | %s |" % (f, fn(f), len({k.split(":")[0] for k in auto[f]}), "yes" if f in audited else ""))
    if unhide:
        L += ["", "## Unhidden by hand", "", "| Function | Why |", "|---|---|"]
        L += ["| `%s` | %s |" % (k, w) for k, w in unhide.items()]
    graded = {v["file"] for v in grades.values()}
    L += ["", "## The registry", "",
          "| | Files |", "|---|---|",
          "| calldata descriptors | %d |" % len(files),
          "| audited (Cyfrin) | %d |" % len(audited),
          "| graded by clear-review | %d |" % len(graded),
          "| with an F function | %d |" % len(auto), ""]
    with open(os.path.join(ROOT, "STATUS.md"), "w") as fh:
        fh.write("\n".join(L))
    print("%d ours (%d added on the wedgie), %d hidden functions" % (len(st["ours"]), len(add), len(hide)))


if __name__ == "__main__":
    main()

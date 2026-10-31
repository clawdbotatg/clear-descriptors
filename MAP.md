# Clear signing map

Every repo that touches clear signing (ERC-7730), all checked out side by side in `~/clawd/clawd-harness/projects/`.

## The rule

**A call no one can read gets a descriptor, never new code.** Write it here (clear-descriptors), add it to
`show.json` (`tools/status.py`), then PR it to the EF registry. Never teach describe.ts, `ours()` or the kit to
decode a contract. (Austin, 10-31.)

## The repos

| Repo | Job |
|---|---|
| `onchain-clear-signing-erc7730-registry` | Our fork of the EF registry (GitHub: clawdbotatg/clear-signing-erc7730-registry). Branches = our PRs. Only touch our own PRs. |
| `clear-descriptors` | Our descriptors, at the registry's paths. `show.json` adds them on top of the EF registry before they merge. `status.json` = PR stages. `STATUS.md` = what's where. |
| `clear-review` | Robot second look at every EF descriptor (truth + clarity). Signs passes per round (🤖 checked, never "audited"). Its `registry/` is a fresh EF checkout. `docs/FIXING.md` = fix PRs. |
| `clear-signing-safe-kit` | Shared code for both wallets. `explain.ts`: a call → words (Uniswap swap code, else 7730 via Sourcify's formatter, EF registry + ours). Sets `src` on each answer. `marks.ts`: the emoji per source. |
| `clear-signing-skill` | Tool for contract teams: deploy → descriptor PR. |
| `wedgie-dev` | wedgie.dev /safe (`src/safe/describe.ts`, `explain.ts`, `api/explain.ts`) and the wedgie itself. `wire/` builds descriptors into Safe Signer (a new build = a Safe Signer release Austin signs). |
| `instant-wallet` | The app. `web/lib/safe/describe.ts`, `web/components/safe/WhatItDoes.tsx`, `web/app/api/explain/route.ts`. |

## How a tx gets its words (both wallets)

1. Our own code first, only for our own stuff: relay fee, approvals, sends, Safe settings (describe.ts).
2. Else `/api/explain` → kit `explain()`: a Uniswap Universal Router swap from its commands, else the 7730
   descriptor (ours over the EF's). A multicall shows its inner calls' words.
3. Else wedgie.dev only: a 🤖 one-line guess.
4. Else ⚠️ raw.

Every address in the words is drawn with the address component (blockie), never bare hex.

## The marks (kit `MARKS`, same on both sites, in place of the step number)

| | Means |
|---|---|
| 🛡️ | EF registry descriptor an auditor signed (its `sigs/` file exists; the registry drops it when the descriptor changes) |
| 🔏 | EF registry descriptor, not audited |
| 📝 | Our descriptor (clear-descriptors), not merged yet |
| 🛠️ | Our own code read it |
| 🤖 | A robot's guess (wedgie.dev) |
| ⚠️ | Nothing could read it → write a descriptor |

## Gotchas

- Sourcify's formatter drops a whole call if any field has an empty `label` (`INVALID_DESCRIPTOR`): shows as ⚠️.
- The kit's server caches the descriptor index for an hour: a new descriptor here shows up within the hour, no deploy.
- A kit change reaches the apps only when each pins the new commit in its `package.json`.

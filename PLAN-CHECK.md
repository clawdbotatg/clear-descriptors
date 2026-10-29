# Plan: check our descriptors before a registry PR

First up: Candide recovery (7d, 14d, 60d) and the passkey signer factory. Another session wrote them on
10-27, with no tests. Nobody has checked them.

## Checks, in order

1. **The contracts are real.** Every deployment (16 per file): code at that address on that chain (Alchemy
   `eth_getCode`), and the ABI matches the selectors. The registry lints with `--require-verified`, so each one
   must be verified on Sourcify. The 14d and 60d modules are our own deployments (10-15): check they're
   verified, and verify them if not.
2. **The registry's own checks**, at the versions pinned in its `.github/`: `erc7730 lint --require-verified
   <file>` and the Sourcify test runner. Never run `erc7730 format` with no path.
3. **Tests from real txs.** `testsv2/*.tests.json` for each file, from mined txs: a recovery helper added,
   removed, a recovery cancelled; a passkey signer created. Find them on Base and Ethereum. Every function needs
   at least one.
4. **Read every screen as a user.** For each test: does the screen say what the tx does, and nothing false?
   Labels short and plain? Missing functions? (Candide: `confirmRecovery`, `executeRecovery`,
   `finalizeRecovery` are called by the helpers, not the Safe. Leave them out, or add them?)
5. **Robot review.** Run clear-review on each file. Fix every finding, or write down why not.
6. **On a real wedgie** (Austin): turn on recovery, add a helper, cancel one. Screen matches step 4.
7. **Registry fit.** The three Candide files show the same thing: use one shared file with `includes`, the way
   the registry does it. Follow the registry's CONTRIBUTING (paths, metadata, owner).

Then open the PR, put its number in `status.json`, and run `tools/status.py`.

## Done when

All 7 pass. Anything that didn't pass is written down here with the reason.

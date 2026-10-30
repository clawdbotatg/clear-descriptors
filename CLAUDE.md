# clear-descriptors: for Claude

Goals, in order (README): people see what they sign; the registry is accurate; we PR in what's needed or missing.
On the EF registry, only open and close our own (clawdbotatg) PRs. Never touch anyone else's.

Read `STATUS.md` first. It answers: what's ours, where each one is (draft / PR / merged), what the wedgie hides and
why, what's audited.

## Files

- `status.json`: the only hand-edited file.
  - `ours`: `{registry path: {what, stage, pr, builds_on, blocked_on, show, note}}`. stage: draft | pr | merged | closed.
    `blocked_on`: what a PR waits for besides review (drop it when that's done).
  - `hide`: `{registry path: {selectors: ["0x…"], why}}`: functions to hide besides clear-review's F's.
  - `unhide`: `{"chain:address:selector": why}`: a clear-review F we show anyway.
- `registry/<entity>/calldata-*.json` + `registry/<entity>/testsv2/*.tests.json`: ours, at the registry's own paths.
  Self-contained (no `includes`), so wedgie.dev's build can read them alone.
- `tools/status.py`: refreshes PR stages from GitHub, writes `STATUS.md` and `show.json`. Run it after any change
  here, and commit all three.
- `show.json`: generated. `add` = our files not merged yet (wedgie.dev builds them in, root a; Instant Wallet's
  `/api/explain` reads them live from GitHub);
  `hide` = `chain:address:selector` keys left out of the build (the wedgie says it can't read that call).

## Adding a descriptor

1. Write it in a checkout of the registry, on a branch. Tests from real mined txs (set `from` if a field reads `@.from`).
2. Run the registry's own checks: `erc7730 lint <file>` and the Sourcify runner, at the versions in the registry's
   `.github/` (pinned there). Never run `erc7730 format` with no path: it rewrites every file.
3. Check it on a wedgie: build test data with `wedgie-dev/wire/release.py` from that branch, then
   `wedgie-dev/tools/safechip.mjs --app <copy> --clear <dir> --txs <txs> --shots <dir>` (wedgie-dev `wire/README.md`).
   One safechip run per test file: same-named cases overwrite each other's screens.
   Put the screens on wedgie.dev/clear: `wedgie-dev/tools/clear_page.py <slug> "<title>" <txs> <shots> "<note>"`,
   commit and push wedgie-dev (only those files). The note says the PR and whether wedgies have it yet.
4. Copy the descriptor and its tests here, add a row to `ours`, open the PR (fork: `clawdbotatg`), put its number in
   `pr`, run `tools/status.py`, commit.

When a PR merges, `status.py` marks it merged and wedgie.dev takes the registry's copy from then on. Keep the file
here as the record.

## Putting a change on wedgies

`show.json` only changes what the next clear-signing build contains. A build changes Safe Signer's roots, so it's a
new Safe Signer version that Austin signs (`wedgie-dev/wire/README.md`, "Make a release"). Say so; don't sign.

# clear-descriptors

Our ERC-7730 clear-signing descriptors, and which descriptors the [wedgie](https://wedgie.dev) shows.

- **Ours:** descriptors we wrote, on their way into the [registry](https://github.com/ethereum/clear-signing-erc7730-registry).
  Same paths as the registry (`registry/<entity>/…`), tests included, so a PR is a copy.
- **Hidden:** registry descriptors the wedgie won't show. Every function [clear-review](https://github.com/clawdbotatg/clear-review)
  grades F, plus any we pick by hand.
- **Audited:** registry descriptors with a Cyfrin attestation. The wedgie shows the rest as "not audited".

**[STATUS.md](STATUS.md)** has all of it in tables. `status.json` is the one file edited by hand;
`python3 tools/status.py` rebuilds `STATUS.md` and `show.json` (what wedgie.dev's clear-signing build reads:
`wedgie-dev/wire/release.py --ours`).

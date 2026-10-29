# clear-descriptors

Our ERC-7730 clear-signing descriptors, and which descriptors the [wedgie](https://wedgie.dev) shows.

- **Ours:** descriptors we wrote, on their way into the [registry](https://github.com/ethereum/clear-signing-erc7730-registry).
  Same paths as the registry (`registry/<entity>/…`), tests included, so a PR is a copy.
- **Hidden:** registry descriptors the wedgie won't show. Every function [clear-review](https://github.com/clawdbotatg/clear-review)
  grades F, plus any we pick by hand.
- **Audited:** registry descriptors with a Cyfrin attestation. The wedgie shows the rest as "not audited".

**[STATUS.md](STATUS.md)** has all of it in tables. `status.json` is the one file edited by hand;
`python3 tools/status.py` rebuilds `STATUS.md` and `show.json`. Who reads `show.json`'s `add`:

- **The wedgie:** wedgie.dev's clear-signing build (`wedgie-dev/wire/release.py`, a checkout of this repo beside
  wedgie-dev). Shows up on wedgies only with the next data release, a new Safe Signer Austin signs.
- **Instant Wallet's pages:** `/api/explain` reads it from GitHub (cached an hour, no deploy).

## Notes on ours

Moved here from wedgie-dev `descriptors/` (10-29); wedgie.dev's build (`wire/release.py`) reads this repo's
`show.json` now. Some can't go to the registry as they are: `registry/safe/calldata-ThisSafe.json` binds to the
stand-in `0x5afe…5afe` (a Safe calling itself), and the Universal Router and MultiSend files use the ERC-8362 draft.
Those go up when the spec takes them, or as a proposal.

- `registry/uniswap/calldata-UniversalRouter-v2.{0,1}.json`: the Universal Router, written to the ERC-8362 draft
  (Custom Encoding Layout, [ERCs PR #1925](https://github.com/ethereum/ERCs/pull/1925)) as it is: `commands` a
  `customEncoding` sequence, `inputs[]` a `switch` on `commands[$index]` masked `0x3f`, V4 actions a switch in a
  switch. v2.0 and v2.1 differ only in V4 swaps (`minHopPriceX36`, `maxHopPriceX36`). Made from Safe Signer's old
  `safe_ur.py` address list. V4 amounts are standard (`wire/README.md`, "Standard only"): one-pool swaps
  name their tokens by an ERC-8362 switch on `zeroForOne`, and v4's 0 (`OPEN_DELTA`) is hidden, the intent saying
  what it means ("Take out what the swap gives", "Pay in what the swap costs"). No optional pool/direction or "From"
  fields: the bundle Instant Wallet sends is at most 6600 B, and a two-token swap must fit with both tokens.

- `registry/uniswap/calldata-SwapRouter02.json`: the router before it. The registry's swaps (our words), plus `multicall`
  with each call in it, unwrap/sweep (and their fee versions), refund, wrap, on 5 chains.

- `registry/lifi/calldata-LIFIDiamond-swaps.json`: the registry's LI.FI same-chain swaps (6) plus `swapTokensGeneric`, with
  `senderAddress: "@.from"` on the receiver (ours, `wire/README.md`): red when it isn't this Safe. Bridges stay the
  registry's. Made by `tools/make_lifi.py` from the registry file.

The 0x..01 and 0x..02 recipients are Uniswap's "the caller" (this Safe) and "the router" (a step in the middle,
hidden). Fields a small screen can skip are `"visible": "optional"`.

A new or changed descriptor ships with a new data release (new roots), so a new Safe Signer version.

# Status

Made by `tools/status.py` from `status.json`. Don't edit by hand.

Stages: **draft** (here only) → **pr** (open on the registry) → **merged** (in the registry; wedgie.dev then takes the registry's copy) · **closed** (PR closed unmerged).

## Ours

| Descriptor | What | Stage | PR | On the wedgie |
|---|---|---|---|---|
| `registry/uniswap/calldata-UniswapV3NonfungiblePositionManager.json` | Uniswap V3 positions: add/remove liquidity, collect, multicall, on Ethereum, Optimism, Polygon, Base, Arbitrum | pr | [#3157](https://github.com/ethereum/clear-signing-erc7730-registry/pull/3157) (on #3075) | ours |

## Hidden by hand

None.

## Hidden: clear-review F

A function graded F (its screen says something untrue or unreadable) isn't shown: the wedgie says it can't read it. Undo one with `unhide` in status.json.

243 functions in 68 files (2543 chain:address:function entries in show.json).

| Descriptor | F functions | Chains | Audited |
|---|---|---|---|
| `registry/ekubo/calldata-VeToken.json` | 35 | 2 |  |
| `registry/ekubo/calldata-Ve33Positions.json` | 23 | 2 |  |
| `registry/ekubo/calldata-Positions.json` | 22 | 7 |  |
| `registry/ekubo/calldata-Orders.json` | 19 | 7 |  |
| `registry/ekubo/calldata-MEVCaptureRouter.json` | 13 | 18 |  |
| `registry/okx/calldata-OkxDexRouterV1.0.7-multi-commission.json` | 13 | 24 |  |
| `registry/okx/calldata-OkxDexRouterV1.0.8-suffix-compat.json` | 13 | 25 |  |
| `registry/1inch/calldata-AggregationRouterV6.json` | 7 | 13 |  |
| `registry/quickswap/calldata-QuickSwap.json` | 6 | 1 |  |
| `registry/uniswap/calldata-UniswapV3Router02.json` | 6 | 1 |  |
| `registry/1inch/calldata-AggregationRouterV5.json` | 4 | 6 |  |
| `registry/gondi/calldata-MultiSourceLoan-v3_0.json` | 4 | 1 |  |
| `registry/lens/eip712-lens-lenshub.json` | 4 | 1 |  |
| `registry/1inch/calldata-AggregationRouterV4-eth.json` | 2 | 1 | yes |
| `registry/ekubo/calldata-Ve33Periphery.json` | 2 | 2 |  |
| `registry/ethena/calldata-ethena.json` | 2 | 1 | yes |
| `registry/flyingtulip/calldata-PftMarketplace.json` | 2 | 1 |  |
| `registry/gondi/calldata-MultiSourceLoan-v3_1.json` | 2 | 3 |  |
| `registry/lens/eip712-lens-token-handle-registry.json` | 2 | 1 |  |
| `registry/lifi/calldata-LIFIDiamond.json` | 2 | 55 |  |
| `registry/morpho/calldata-VaultBundlesV1.json` | 2 | 46 |  |
| `registry/morpho/calldata-clearstar-CSUSDC-8453.json` | 2 | 1 |  |
| `registry/ondo-finance/calldata-GMTokenManager.json` | 2 | 2 |  |
| `registry/opencover/calldata-Quote.json` | 2 | 5 |  |
| `registry/paraswap/calldata-AugustusSwapper-v6.2.json` | 2 | 10 |  |
| `registry/safe/calldata-Safe-1.3.0.json` | 2 | 8 |  |
| `registry/safe/calldata-Safe-1.5.0.json` | 2 | 68 |  |
| `registry/safe/calldata-SafeL2-1.3.0.json` | 2 | 8 |  |
| `registry/safe/calldata-SafeL2-1.4.1.json` | 2 | 7 |  |
| `registry/safe/calldata-SafeL2-1.5.0.json` | 2 | 65 |  |
| `registry/safe/calldata-SafeMigration-1.4.1.json` | 2 | 7 | yes |
| `registry/safe/calldata-SafeMigration-1.5.0.json` | 2 | 65 | yes |
| `registry/1inch/calldata-AggregationRouterV3.json` | 1 | 3 | yes |
| `registry/1inch/calldata-AggregationRouterV4.json` | 1 | 2 | yes |
| `registry/HyperDiscipline/eip712-CommitIntent.json` | 1 | 1 |  |
| `registry/aave/calldata-lpv2.json` | 1 | 3 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4_1-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4_2-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4_3-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4_4-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-exhibition-v4_5-0.json` | 1 | 1 |  |
| `registry/feral-file/calldata-feralfile-vault-v2-0.json` | 1 | 1 |  |
| `registry/flyingtulip/eip712-LeverageRfqEngine.json` | 1 | 2 |  |
| `registry/gondi/calldata-PurchaseBundler-v3_1.json` | 1 | 1 |  |
| `registry/kyberswap/calldata-MetaAggregationRouterV2.json` | 1 | 18 |  |
| `registry/lido/calldata-wstETH-referral-staker.json` | 1 | 1 | yes |
| `registry/morpho/calldata-MorphoBundlerV3.json` | 1 | 2 |  |
| `registry/morpho/calldata-VaultExitBundlesV1.json` | 1 | 46 |  |
| `registry/opensea/eip712-opensea.json` | 1 | 1 |  |
| `registry/paraswap/eip712-Velora-DeltaV2.json` | 1 | 6 |  |
| `registry/permit/eip712-permit-polygon-bridged-usdc.json` | 1 | 1 |  |
| `registry/permit/eip712-permit-polygon-usdt.json` | 1 | 1 |  |
| `registry/rarible/eip712-rarible-exchange-v2-meta-tx.json` | 1 | 1 |  |
| `registry/rarible/eip712-rarible-exchange-v2.json` | 1 | 2 |  |
| `registry/safe/calldata-BatchExecutor.json` | 1 | 6 |  |
| `registry/safe/calldata-Safe-1.4.1.json` | 1 | 7 |  |
| `registry/safe/eip712-Safe-1.3.0.json` | 1 | 8 |  |
| `registry/safe/eip712-Safe-1.4.1.json` | 1 | 7 |  |
| `registry/safe/eip712-Safe-1.5.0.json` | 1 | 68 |  |
| `registry/safe/eip712-SafeL2-1.3.0.json` | 1 | 8 |  |
| `registry/safe/eip712-SafeL2-1.4.1.json` | 1 | 7 |  |
| `registry/safe/eip712-SafeL2-1.5.0.json` | 1 | 65 |  |
| `registry/smartcredit/eip712-smartcredit.json` | 1 | 1 |  |
| `registry/swissborg/calldata-NttManager.json` | 1 | 1 |  |
| `registry/threshold/calldata-Bridge.json` | 1 | 1 |  |
| `registry/yieldxyz/calldata-yieldxyz-pol-validator.json` | 1 | 1 | yes |
| `registry/yieldxyz/calldata-yieldxyz-usde-vault.json` | 1 | 1 |  |

## The registry

| | Files |
|---|---|
| calldata descriptors | 589 |
| audited (Cyfrin) | 163 |
| graded by clear-review | 709 |
| with an F function | 68 |

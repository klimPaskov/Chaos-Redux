# Event 006 setup-receipt category and cost-layout repair

Date: 2026-08-30

## Scope

This bounded repair covers the four signature package decision categories that were the only Event 006 package categories without their own setup receipt in the visibility trigger, plus the shared standard security cost text used by those and other post-release decisions.

## Source changes

- `common/decisions/categories/006_independence_wave_categories.txt` now requires `independence_wave_iw043_setup_complete`, `independence_wave_iw058_setup_complete`, `independence_wave_iw093_setup_complete`, and `independence_wave_iw098_setup_complete` in the matching category visibility blocks.
- `localisation/english/006_independence_wave_decisions_l_english.yml` now places the four standard security costs in two compact icon-first lines for both available and blocked variants.

## Behavior

IW-043, IW-058, IW-093, and IW-098 remain unavailable until their package setup effects have written the generation-specific setup receipt. Their existing active-origin, package-identity, and Event 012 exclusion predicates remain unchanged. The cost layout changes only line grouping; every dynamic resource token and icon is preserved, and no cost amount or payment effect changes.

The pre-event Independence Wave surface remains absent. These category gates cannot create a category, mission, pressure label, queue, history entry, or event; they only narrow already post-release package visibility.

## Evidence

The package trigger definitions and setup effects already use the four corresponding `*_setup_complete` flags as post-setup receipts. All other Event 006 package categories use the same visibility pattern. The allocator, strict flag, country API, and Statehood Ledger source-matrix validators passed after the change. The localization file retains its UTF-8 BOM, and a token comparison confirms that both standard security variants preserve all four resource tokens and icons.

## Limitations

The user-reported zero-country runtime symptom still needs live transaction receipts or candidate-specific engine evidence. Event MCP inspection remains partial, and the named probability-auditor route is unavailable. No admission gate was relaxed and no fallback country or pre-event surface was introduced.

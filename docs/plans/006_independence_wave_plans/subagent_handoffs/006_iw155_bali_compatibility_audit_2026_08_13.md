# IW-155 BLI compatibility audit (2026-08-13)

## Disposition

IW-155 Bali remains fail-closed and is not admitted to the Event 006 runtime. This audit makes no gameplay, central dispatcher, content-attestation, Join Wave, flag, portrait, or localisation change.

The registry row permits a registered `BLI` reuse when a unique current-map state exists, but the accepted research row still requires a sourced period institution or incumbent and a provenance-cleared regional or civic symbol. The package must not invent a royal claimant, generic dynasty member, sacred emblem, or pan-Balinese identity. The current evidence therefore does not support a bounded playable package.

## Vanilla preservation contract

Vanilla registers `BLI` as `countries/Bali.txt` in `common/country_tags/00_countries.txt`. Its history file is `history/countries/BLI - Bali.txt`, with capital state 1052, two research slots, the vanilla starting technology block, neutrality at 90 percent, and `recruit_character = INS_dewa_geg`.

The installed state history is `history/states/1052-Bali.txt`. State 1052 is owned by `INS` at the 1936 start, carries the `BLI` core, and is the compact Bali anchor. Vanilla Indonesia includes `BLI` in the `INS_releasables` array in `history/countries/INS - Indonesia.txt`.

The vanilla character definition is `INS_dewa_geg` in `common/characters/INS.txt`. It is a despotism country leader with the `INS_lord_of_the_nine_kingdoms` trait and an Indonesian political-advisor surface. The Event 006 adapter must preserve that character and its role-transfer semantics rather than create a second unsourced royal consumer.

Vanilla `common/scripted_effects/INS_scripted_effects.txt` defines the `indonesia_transfer_BLI` path used by the Indonesian princely-advisor logic. Any future BLI adapter must prove that the transfer remains available when BLI is absent, that the Event 006 origin is the only context that changes it, and that cleanup restores ordinary Indonesia/Bali behavior.

## Current Chaos Redux source

The Region 13 loader and planner currently expose `can_plan_independence_wave_package_iw_155` with `BLI` and state 1052, reservation group `RG-EAST-INDONESIA`, and an automatic-if-unique-state disposition. That map readiness is not content readiness.

There is no BLI-specific setup, final-validation, cleanup, force receipt, idea lifecycle, decision/mission surface, AI profile, focus hook, character checkpoint, symbol manifest, or central Event 006 adapter. The central adapter and attestation lists intentionally do not include IW-155, so the package remains fail-closed even when the planner sees the bound state.

The existing generic registry trigger only proves that `BLI` is a registered reuse tag. It does not prove state 1052 ownership/control, the vanilla `INS_releasables` membership, the `INS_dewa_geg` role, or `indonesia_transfer_BLI` preservation.

## Required admission boundary

Before runtime implementation, research must identify a period-valid Balinese institutional authority or incumbent that can be represented without inventing a dynasty member, and must clear the chosen civic or regional symbol for the 1936 alternate-history baseline. The package then needs an origin-gated adapter that proves `original_tag = BLI`, package id `iw_155`, state 1052 ownership/control, host survival, the vanilla leader and core, the Indonesian releasable row, and the character-transfer contract.

The eventual setup must use the shared Event 006 framework with a local-guard/coastal-defense force profile and explicit island-supply costs. Cleanup must clear only Event 006 flags, ideas, variables, route cosmetics, event targets, and force receipts; it must leave BLI history, state 1052 core, `INS_releasables`, `INS_dewa_geg`, and Indonesian transfer behavior unchanged outside the Event 006 origin.

## Validation and blockers

The offline Paradox wiki pages and vanilla documentation/history/scripted-effect references required by `AGENTS.md` were consulted. Current HOI4 MCP map, event, focus, and probability calls are blocked before source inspection by `ARTIFACT_MANIFEST_INVALID` for workspace `mod_chaos_redux_ea3b2d67c2c0`; no engine receipt is claimed.

The historical pre-IW-044 static Event 006 authority at this audit was 30 content-attested selectable packages, 27 compatible reservation groups, 163 unattested selectable rows, and 38 central adapters; current routing is 31/28/162/39. IW-155 remains outside those admitted lists.

No fallback tag, generic leader, synthetic flag, copied portrait, or broad automatic package was introduced.

## Closure evidence (2026-08-13)

The asset ledgers still block this package. `asset_research/006_package_asset_coverage.md:110,138` places IW-155 in the attested-symbol group but marks it as a source gap pending an exact-route subject; `asset_research/006_generated_flag_blockers.md:23-25` requires a source that proves symbol owner, date, function, route, and license; and `asset_research/006_real_portrait_and_symbol_sources.md:112` supplies only the REG-SEAO research route, not a cleared Bali symbol or portrait manifest. Vanilla BLI flag files exist, but their presence does not clear an Event 006 route identity or permit a synthetic sacred/pan-Balinese substitute.

Static package checks confirm the only BLI-owned Chaos Redux surfaces are the Region-13 planner/loader and registry constants/triggers; no BLI setup, final-validation, cleanup, force receipt, AI strategy, decision/mission, idea lifecycle, focus hook, character checkpoint, portrait/symbol manifest, or central runtime adapter/attestation exists. The central dispatcher therefore remains correctly fail-closed for IW-155.

Fresh read-only MCP attempts in workspace `mod_chaos_redux_ea3b2d67c2c0` produced no engine artifacts: bounded state-map inspection returned `ARTIFACT_MANIFEST_INVALID` (an initial explicit allocation request also exposed `MAP_STATE_ID_COLLISION` for already-scanned vanilla state 1052); Event 006 inspect and render returned `ARTIFACT_MANIFEST_INVALID`; the Region-13 weighted-source probability inspect returned `ARTIFACT_MANIFEST_INVALID`; and a BLI national-focus inspect returned `FOCUS_TREE_NOT_FOUND`. These are tool/provenance blockers, not evidence of runtime readiness. No probability compare, focus render, or live-game claim is made.

Disposition remains fail-closed. Do not widen the central adapter/content-attestation lists or Join Wave, and do not add a fallback leader, dynasty, broad Balinese identity, sacred flag, copied portrait, or generic AI/force package until the exact-route identity, symbol ownership/license, portrait provenance, host-survival/force, and vanilla transfer/cleanup gates are separately source-backed and parent-reviewed.

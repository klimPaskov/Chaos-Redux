# Event 014 localisation post-remediation regression — 2026-08-25

## Scope

This regression reviewed Event 014 localisation after commits `7df06971f`, `cb6a6667f`, `b8304e0f6`, and `42f04ca5a`. The bounded writable surfaces were `localisation/english/014_cannibalism_l_english.yml` and this handoff. Gameplay, GUI, assets, scripted localisation, and shared localisation remained read-only.

## Patch

- Changed `cannibalism_unified_player_mission_slots_tt` in `localisation/english/014_cannibalism_l_english.yml`.
- Before: `Only two paid Unified missions may be active at once. Finish or cancel an existing Unified mission before opening this route.`
- After: `Only two paid Unified missions may be active at once. Complete or cancel an active Unified mission before starting another.`
- Reason: the tooltip is consumed by mission-start decisions across the command, Larder, war-machine, and counterwar families. “Opening this route” described neither the gated action nor the slot consequence. The revised sentence preserves the two-slot limit and paid-operation distinction while naming the actual recovery action.
- Dynamic localisation added or changed: none. The cap is a fixed two-slot contract implemented by four active-family flags, not a display variable.

## Texticon regression

All five inline tokens use the HOI4 `£token` to `GFX_token` naming contract, resolve to a registered sprite in `interface/014_cannibalism_texticons.gfx`, and point to an existing 18×18 DDS under `gfx/texticons/014_cannibalism/`.

| Inline token | Uses | Registered sprite | Player-facing ledger | Semantic evidence |
| --- | ---: | --- | --- | --- |
| `£cannibalism_larder_texticon` | 35 | `GFX_cannibalism_larder_texticon` | Larder | Every use labels Larder; contact sheet shows a locked stores chest. |
| `£cannibalism_state_population_texticon` | 23 | `GFX_cannibalism_state_population_texticon` | State population | Every use labels population; contact sheet shows a damaged dwelling and population ledger. |
| `£cannibalism_victory_receipt_texticon` | 1 | `GFX_cannibalism_victory_receipt_texticon` | Victory Receipt | The battlefield-consumption cost labels one Victory Receipt; contact sheet shows a sealed battle document and broken shield. |
| `£cannibalism_convoy_hunt_receipt_texticon` | 1 | `GFX_cannibalism_convoy_hunt_receipt_texticon` | Convoy-Hunt Receipt | The convoy-harvest cost labels one Convoy-Hunt Receipt; contact sheet shows a ship, plotted route, and anchor receipt. |
| `£cannibalism_enemy_loss_receipt_texticon` | 1 | `GFX_cannibalism_enemy_loss_receipt_texticon` | Enemy-Loss Receipt | The Wendigo muster cost labels one Enemy-Loss Receipt; contact sheet shows a casualty tally and helmet. |

The source/processed/DDS-roundtrip contact sheet inspected was `docs/assets/014_cannibalism/cost_texticons/contact_sheets/cost_texticons_contact.png`. The local image viewer cannot decode DDS directly, so DDS visual parity relies on the committed roundtrip columns and header checks rather than direct DDS display.

## Localisation integrity

- Parsed Event 014 keys: 2,034.
- Missing keys: none found in the bounded consumer and scripted-localisation checks.
- Duplicate keys: none inside the Event 014 file and none among its keys across `localisation/english/`.
- Invalid `:0` keys: none.
- Empty values: none.
- File encoding: UTF-8 BOM remains present (`EF BB BF`).
- Scripted localisation: all 18 `GetCannibalismAchievement*TrackerStatus` calls in the Event 014 file resolve. The Event 014 scripted-localisation file contains 43 unique `GetCannibalism*` definitions, no duplicate definition names, no missing referenced localisation keys, and no direct `§` or `£` format characters.
- Scripted-localisation issues: none proven.
- Dynamic-text opportunities: none required for this regression. Existing costs retain their live variable and script-constant tokens.

## Secrecy regression

- None of the four named commits added a `Hannibal` or `Lecter` string to the Event 014 English file.
- The repaired mission-slot tooltip and all five cost texticons contain no identity-bearing text.
- The public reveal event remains gated by `has_global_flag = cannibalism_reveal_complete` in `events/014_cannibalism.txt`; the Hannibal submission, Wendigo reveal, subsequent transformation, captured-leader, and news consumers inspected retain the same reveal gate.
- Reveal-named achievements remain visible only after `cannibalism_reveal_complete`, while the deliberately pre-reveal convergence achievement requires the reveal flag to be absent.
- Protected post-reveal spelling remains `Hannibal Lecter`.
- Result: no pre-reveal identity regression was found.

## Cross-surface and prose audit

- The new mission-slot tooltip exists and is consumed by the four slot-aware mission families. Its wording now matches the mission-start behavior.
- Texticon terms match their cost-ledger mechanics. No icon is used for a different resource or receipt.
- Cross-surface mismatches: none proven after the tooltip repair.
- Vagueness: repaired “opening this route,” which did not identify the gated action.
- Bloat, obvious explanation, repetition, and overcomplication: no additional proven defect in the post-remediation lines.
- Style-rule violations: no semicolons or em dashes remain in the Event 014 English file.
- Sourced quotations: no quotation-bearing text was changed. No attributed quotation was encountered in the patched surface.
- Dynamic tokens and formatting codes: preserved without exception.

## MCP evidence and limits

- Event lint: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e5209e4684e5ee442963dfa3af12b3fc35e15145bad770f70721e68497841463/7b7163d9e672943db8c7e6098289567f27b142931d19df26f1079bfa402160c0/event-lint-59143acd4a23.json`.
- Network GUI inspection: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4374389cba975e7e04def59e438f98d8ace4794f9177b585d0248a6bee1b5af8/b53a40177479746191188d05ef51c0e4cc2b414ec1f2d00efc2d21726fe26cc8/gui-inspect.2aa66d9ab1319255.json`.
- The event tool returned `EVENT_INSPECTED_PARTIAL` because its linked full lint carries global graph evidence. The GUI tool completed the selected window inspection, but global source-graph diagnostics exceeded its fixed ceiling and included unrelated repository collisions. These artifacts are not treated as a clean repository-wide validation pass; the bounded localisation, sprite, consumer, and secrecy conclusions come from the task-specific checks above.

## Completion state

- Changed files: `localisation/english/014_cannibalism_l_english.yml` and this handoff.
- Changed keys: `cannibalism_unified_player_mission_slots_tt` only.
- Unresolved wording decisions: none.
- Simplifications or omissions: no in-scope localisation work was omitted. Direct DDS viewing was unavailable, with committed roundtrip PNG evidence used as documented above.

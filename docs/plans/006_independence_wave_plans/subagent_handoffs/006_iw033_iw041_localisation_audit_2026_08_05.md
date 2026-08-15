# IW-033 / IW-041 localisation audit

Date: 2026-08-05

Mode: read-only audit. No gameplay, localisation, scripted localisation, AI, or interface source was changed.

## Current owner-patch status (2026-08-05)

The owner patch is recorded in `006_documentation_curator_iw033_iw041_owner_patch_reconciliation_current_2026_08_05.md`. The current package localisation contains the four referenced Frontier Command and Coastal Command party-name families, all eight package-specific normal/blocked/hover cost families, corrected icon markers, and dynamic founding-mission ledger values. The findings below are retained as a pre-owner-patch baseline and no longer describe the current cost or ledger localisation. Remaining localisation scope is limited to broader package naming policy, concise trigger-gate wording, and any parent-requested player-facing polish; these findings remain visible after the central IW-033/IW-041 attestation promotion and do not revoke that promotion.

## Pre-owner-patch result (superseded)

The Karelia and Crimean Tatar State package is not ready for localisation admission. The package has four directly referenced missing party-name keys, sixteen missing implicit custom-cost companion keys, eight malformed cost icon markers, no player-facing display for its four founding ledgers, and several tooltips that expose implementation language instead of concrete consequences.

The target localisation file is UTF-8 with BOM and has no duplicate key inside the mod. All 22 decision or mission names and descriptions, all 12 idea name and description pairs, the category name and description, and the five reused shared Event 006 cost families resolve. The six AI strategy identifiers do not require localisation.

## Files inspected

- `localisation/english/006_independence_wave_karelia_crimea_l_english.yml`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `common/decisions/006_independence_wave_karelia_crimea_decisions.txt`
- `common/decisions/categories/006_independence_wave_karelia_crimea_categories.txt`
- `common/ideas/006_independence_wave_karelia_crimea_ideas.txt`
- `common/ai_strategy/006_independence_wave_karelia_crimea.txt`
- `common/script_constants/006_independence_wave_karelia_crimea_constants.txt`
- `common/scripted_effects/006_independence_wave_karelia_crimea_package_effects.txt`
- `common/scripted_triggers/006_independence_wave_karelia_crimea_package_triggers.txt`
- `docs/events/006_independence_wave/karelia_crimea_packages.md`
- `localisation/english/006_independence_wave_super_event_l_english.yml` and the matching shared super-event selectors, only to verify ordinary numbering
- Vanilla `countries_l_english.yml` for the existing `KAR` and `CRI` country-name families

## Missing keys

### Direct party-name references

The emergency-government installation effects reference these absent keys:

- `KAR_independence_wave_frontier_command`
- `KAR_independence_wave_frontier_command_long`
- `CRI_independence_wave_coastal_command`
- `CRI_independence_wave_coastal_command_long`

The package file instead defines unused `KAR_independence_wave_emergency_directorate`, `KAR_independence_wave_emergency_directorate_long`, `CRI_independence_wave_emergency_directorate`, and `CRI_independence_wave_emergency_directorate_long`. The parent should either rename those four localisation keys to match the effects or change the effect references. The route and idea names favor `Frontier Command` and `Coastal Command`, so matching the localisation to those established identities is the more consistent repair.

### Implicit custom-cost companions

HOI4 resolves `<custom_cost_text>_blocked` when `custom_cost_trigger` fails and `<custom_cost_text>_tooltip` on hover. Both companions are absent for all eight package-specific cost families:

- `independence_wave_iw033_railheads_cost_blocked`
- `independence_wave_iw033_railheads_cost_tooltip`
- `independence_wave_iw033_ski_guard_cost_blocked`
- `independence_wave_iw033_ski_guard_cost_tooltip`
- `independence_wave_iw033_commission_cost_blocked`
- `independence_wave_iw033_commission_cost_tooltip`
- `independence_wave_iw033_transit_cost_blocked`
- `independence_wave_iw033_transit_cost_tooltip`
- `independence_wave_iw041_survey_cost_blocked`
- `independence_wave_iw041_survey_cost_tooltip`
- `independence_wave_iw041_return_cost_blocked`
- `independence_wave_iw041_return_cost_tooltip`
- `independence_wave_iw041_screen_cost_blocked`
- `independence_wave_iw041_screen_cost_tooltip`
- `independence_wave_iw041_customs_cost_blocked`
- `independence_wave_iw041_customs_cost_tooltip`

The five reused shared Event 006 cost keys have both companions and resolve correctly.

## Duplicate keys

No target key is duplicated elsewhere under `localisation/english/`. The bare `KAR` and `CRI` entries are not exact duplicates of vanilla keys, but they do not replace vanilla's ideology-specific map names.

## Scripted localisation issues

- No broken `defined_text` or scripted-localisation reference was found in the package.
- The package has no scripted localisation that exposes `independence_wave_kar_forest_supply_integrity`, `independence_wave_kar_civic_mandate`, `independence_wave_cri_return_capacity`, or `independence_wave_cri_land_settlement`.
- Shared Event 006 cost localisation correctly reads shared script constants and formats them as integers or percentages.
- The package-specific costs are static text even though every value already has a package script constant. This creates a tuning drift risk.

## Dynamic text opportunities

1. Replace the eight hardcoded cost strings with icon-first dynamic constant values and add green or yellow normal, red blocked, and concise hover variants. Follow the vanilla `custom_cost_text`, `_blocked`, and `_tooltip` pattern. Use the correct equipment, train, convoy, manpower, fuel, and command-power text icons rather than prose-only lists.
2. Add a package-aware category description or scripted-localisation summary that shows the two relevant ledgers, their current integer values, and the stable threshold of 65. The current founding missions require those values but the player cannot see or manage them from this package surface.
3. Name the active country dynamically in the shared category title or description. `Karelian and Crimean Statehood` presents both countries to either carrier and makes the category sound like one joint system.
4. Replace generic phrases such as `both regional ledgers`, `shared capacity ledger`, and `forest ledgers` with the actual metric names relevant to the active package.

## Cross-surface mismatches

- Package identity: the file defines `CRI: "Crimean Tatar State"` and the package documentation uses `Crimean Tatar State`, but vanilla ideology-specific names remain `Crimea`, `Crimean People's Republic`, `Crimean Regime`, and `Crimean Khanate`. The bare `CRI` key will not make the runtime country consistently display as the Crimean Tatar State. If that identity is intended in play, add or deliberately override the ideology-specific `_DEF` and `_ADJ` families, or use a package cosmetic tag. Record the intended naming policy before changing vanilla-visible names.
- Emergency route identity: localisation says `Emergency Directorate`, while effects and ideas say `Frontier Command` or `Coastal Command`.
- `independence_wave_karelia_crimea_category` names both packages even though visibility admits one carrier at a time.
- `independence_wave_cri_ratify_constitutional_mandate` is titled `Ratify the Civic Return Union`, while its route idea is the generic `Constitutional Mandate`. This is understandable but weakens Crimean route identity compared with the party name.
- The documentation states exact starting ledger values and the 65 stability threshold, but no player-facing package localisation exposes them.

## File encoding concerns

- `006_independence_wave_karelia_crimea_l_english.yml` begins with the required `EF BB BF` UTF-8 BOM and contains no NUL or Unicode replacement characters.
- Eight cost strings contain the two-character sequence `U+00C2 U+00A3` (`Â£`) instead of the single HOI4 text-icon marker `U+00A3` (`£`). These will not resolve as intended and must be repaired.
- The file mostly uses LF line endings with one CRLF. This is not an engine blocker, but normalizing it when the file is next edited will avoid noisy diffs.

## Prose-quality findings

### Vagueness

- `opening force`, `surviving anchor`, `regional ledgers`, and `shared capacity ledger` do not tell the player which troops, state, or metric matters.
- `independence_wave_kc_foundation_failure_effect_tt` says the next crisis becomes harder without naming the concrete losses or affected values.
- `independence_wave_kc_host_settlement_effect_tt` says the ledgers are settled but does not say what improves or what concession the country makes.

### Bloat

- Most descriptions are concise. The longest shared Event 006 cost strings are mechanically complete but too sentence-like for compact decision cost presentation. The package-specific replacements should remain icon-first and short.

### Obvious explanation

- `independence_wave_kc_route_effect_tt` restates that selecting a government route makes it active, then adds opaque ledger language. It should state the concrete public authority and the visible tradeoff instead.

### Repetition

- `opening force` recurs across founding, security, and idea text without becoming clearer.
- `public authority`, `recognition`, and generic ledger improvement recur across route tooltips, making distinct political routes read alike.

### Overcomplication

- `A stable compact, a recognized border, and a functioning forest force can turn liberation into durable sovereignty` is readable, but its three abstract prerequisites should be tied to the visible ledger and settlement requirements in the tooltip.
- `Trade a controlled transit regime for a less hostile former host` is awkward and obscures the actual transit agreement.

### Style-rule repairs required

- `independence_wave_cri_services_effect_tt` ends with `without creating a free formation loop`. This is implementation and exploit-prevention language and must be removed from player-facing text.
- `independence_wave_kc_route_effect_tt` mentions `the selected government route` and `shared Event 006 ledgers`. Both are implementation-facing labels.
- No em dash, semicolon, staged contrast formula, staccato chain, prompt fragment, working label, TODO, or placeholder was found in the target localisation.

## Raw trigger and tooltip clarity

The eight package projects provide custom cost text, but their other availability conditions can still expose long raw trigger output for capital control, active-project exclusion, former-host survival or peace, route selection, founding settlement, and ledger thresholds. Add concise custom trigger tooltips for these non-obvious gates, especially the two durable-sovereignty decisions and the former-host settlement. The tooltip should name the capital or state and the required ledger values rather than printing internal trigger names.

## Ordinary super-event numbering

The Karelia/Crimea package contains no super-event visibility, image, audio, or localisation references. Shared Event 006 ordinary slots 23 and 24 each retain exactly one `.t`, `.d`, `.a`, and `.q` key, and the shared selectors contain all four mappings for each slot. This package does not regress ordinary super-event numbering.

The slot 23 Woodrow Wilson quotation and slot 24 Hosea quotation were inspected only for numbering and were left verbatim. Attribution accuracy was not re-researched in this bounded audit.

## MCP evidence and limitations

- `hoi4.probability_inspect` scanned `common/decisions/006_independence_wave_karelia_crimea_decisions.txt` with the `decision_ai_will_do` adapter. Source revision: `c801bd53f4ec877922c2dbe2809c45c5a8fa9a62888c81bd535aa84ee58bf703`. Artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c52a0b3758d1593bd760b7ec81792a4a183087a0d9e8b61b20b0e78e85983309/ab9bdda04039df1b76acc48b4527dce8eba8c4e7b5d8618e36e4610c2b977d48/probability-inspect-43d279a452b6.json`.
- The probability inspector reported an incomplete pool and discovered only two candidates from the decision file. This is not complete balance evidence for the 22 decisions or missions.
- The `ai_strategy_factor` adapter returned `PROBABILITY_SURFACE_EMPTY` for `common/ai_strategy/006_independence_wave_karelia_crimea.txt`. Source inspection confirms six AI strategy identifiers, but MCP could not inspect that surface.
- The installed HOI4 MCP exposes no dedicated decision-category localisation inspector or renderer. Decision-list overflow, blocked-cost rendering, raw-trigger presentation, and source-linked visual layout therefore remain unverified. Source review is not treated as equivalent visual evidence.
- No linked focus, scripted GUI, map, event-chain, technology, or doctrine surface is introduced by this package, so no additional MCP renderer applied.

## Recommended fixes

1. In `localisation/english/006_independence_wave_karelia_crimea_l_english.yml`, add the four referenced command-party keys or rename the four unused emergency-directorate keys to the established command identities.
2. In the same file, rebuild all eight package cost families with dynamic constant tokens and their `_blocked` and `_tooltip` companions. Repair every `Â£` marker and use correct text icons.
3. Add package-aware dynamic ledger text and a 65-threshold explanation, then connect it to the category or founding-mission tooltip through scripted localisation.
4. Rewrite `independence_wave_cri_services_effect_tt` and `independence_wave_kc_route_effect_tt` to remove implementation language. Make the remaining generic ledger tooltips name the affected metrics and concrete consequences.
5. Add custom trigger tooltips for capital control, package ledger thresholds, settlement state, former-host availability, and the one-active-project rule.
6. Decide whether runtime country names should remain vanilla or identify `CRI` consistently as the Crimean Tatar State. Align `_DEF`, `_ADJ`, ideology variants or a cosmetic tag with that decision.
7. After patching, re-run key/reference coverage, custom-cost companion coverage, UTF-8 code-point checks, and the available MCP probability scan. A decision renderer remains unavailable and should stay listed as skipped visual validation.

## Sourced quotation preservation

No sourced or attributed quotation appears in the Karelia/Crimea package localisation. The shared slot 23 and 24 quotations were not altered. Their exact wording and punctuation must remain untouched unless a dedicated source-verification task authorizes a correction.

## Unresolved decisions

- Whether `Crimean Tatar State` is intended as a runtime country identity or only a package label.
- Whether the emergency parties should be named `Emergency Directorate` or should follow the established `Frontier Command` and `Coastal Command` route identities.
- Which package UI surface should own the four dynamic ledger values, because no package-specific GUI exists and the current decision category description is static.

## Changes made

Only this audit handoff was added. No source keys, identifiers, dynamic localisation, behavior, or display were changed.

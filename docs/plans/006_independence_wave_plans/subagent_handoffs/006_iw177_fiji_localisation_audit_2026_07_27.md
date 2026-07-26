# Event 006 IW-177 Fiji localisation audit v20

## Scope

This audit covers only the Fiji localisation tranche in `localisation/english/006_independence_wave_pacific_l_english.yml` and the directly referenced FIJ decision, focus, category, idea, party, and leader identifiers. It does not audit or claim completion for the whole Event 006 chain.

The required Chaos Redux event, decision and mission, focus-tree, and subagent guidance was read before the audit. The offline Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, National focus modding, and AI modding pages were consulted alongside the installed vanilla localisation, dynamic-variable, localisation-formatter, localisation-object, script-concept, effects, and triggers documentation.

## Key coverage

The Fiji block contains 57 keys covering four short and long party names, the founding-congress chair name and description, three ideas with descriptions, the founding-congress category and dynamic description, the founding mission and failure tooltip, six decisions with descriptions and completion tooltips, and six focuses with descriptions and completion tooltips.

The six decisions in `common/decisions/006_independence_wave_pacific_decisions.txt`, the category in `common/decisions/categories/006_independence_wave_pacific_categories.txt`, the six shared focuses in `common/national_focus/006_independence_wave_pacific_focus.txt`, the three ideas in `common/ideas/006_independence_wave_pacific_ideas.txt`, the FIJ chair in `common/characters/006_independence_wave_pacific_characters.txt`, and the four party-name assignments in `common/scripted_effects/006_independence_wave_pacific_package_effects.txt` resolve to existing English localisation keys.

### Missing key list

None found. A targeted scan found 30 FIJ `name`, `desc`, and custom-tooltip references in the decision, category, focus, and character files, with zero unresolved keys. The idea ids and focus ids also have their expected automatic name and `_desc` keys.

### Duplicate key list

None found in the target file. A scan of all English localisation files also found no duplicate key for any FIJ or `independence_wave_fij_*` key.

### Scripted localisation issue list

None found. The Fiji tranche does not call a Fiji-specific `defined_text` or scripted-localisation selector. Its category text uses ordinary scoped variables and a script constant, which is consistent with the installed vanilla dynamic-variable and script-constant documentation.

## Dynamic text opportunities

The category description already exposes live congress pressure, the pressure maximum, communal authority, shipping access, colonial accounts, and defense readiness at `localisation/english/006_independence_wave_pacific_l_english.yml:263`.

The generic decision cost keys in `localisation/english/006_independence_wave_decisions_l_english.yml` expose the constants consumed by the Fiji decisions, so no Fiji-specific duplicate cost strings are needed.

The Fiji completion tooltips remain qualitative. If the owning gameplay tranche later publishes exact ledger deltas, a follow-up could add the existing `minor_gain`, `standard_gain`, `major_gain`, and `standard_loss` constants to the relevant tooltips, but no new dynamic localisation was added here because that would broaden the repeated Pacific tooltip design.

## Cross-surface mismatch notes

Three narrow wording mismatches were fixed in the target file.

- `independence_wave_fij_founding_crisis_failure_tt` previously claimed that Fiji defense readiness fell and that the release remained exposed to the former host. The failure effect lowers the shared legitimacy, capacity, and security values, raises instability, and subtracts Fiji congress pressure without changing the Fiji defense-readiness ledger. The text now names the shared values and the congress-pressure loss.
- `independence_wave_fij_charter_coastal_guard_tt` previously claimed that the coastal-guard decision unlocked the final island compact. The decision is visible before the labor and shipping board is complete, while the final decision also requires that board. The text now says that the coastal guard prepares the final compact.
- `independence_wave_fij_ratify_island_compact_tt` previously claimed that the action published Fiji's regional ambition to the Independence Network. The current effect sets the compact flag, Fiji ledger deltas, and the shared major-settlement values, but it does not call a network or ambition reward. The text now describes completion of Fiji's regional settlement.

The remaining description at `independence_wave_fij_ratify_island_compact_desc` still uses the phrase "regional ambition" as in-world route language. If the owning gameplay tranche intends this action to open a live ambition or network receipt, that effect and its dynamic tooltip should be added by the parent before the phrase is treated as a mechanic guarantee.

The Fiji former-host strings refer to the English host because the IW-177 package binding and current tranche explicitly use an English former host. The Sukuna leader key resolves, but the existing source handoff still records a circa-1940s image against the event's 1936-centered baseline. That source-date gate is outside localisation scope and remains unresolved.

## File encoding concerns

`localisation/english/006_independence_wave_pacific_l_english.yml` begins with the UTF-8 BOM bytes `EF BB BF`. The Fiji keys omit version suffixes, use valid ASCII key names, and keep each value on one physical line with escaped `\\n` sequences where needed. Git reports its normal LF-to-CRLF warning for this working copy, but the BOM remained intact after the narrow patch.

## Patch handoff

### Changed files

- `localisation/english/006_independence_wave_pacific_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_iw177_fiji_localisation_audit_2026_07_27.md`

### Changed keys

- `independence_wave_fij_founding_crisis_failure_tt`
- `independence_wave_fij_charter_coastal_guard_tt`
- `independence_wave_fij_ratify_island_compact_tt`

### Display before and after

The founding-crisis failure tooltip now reports the shared legitimacy, administrative-capacity, security, instability, and Fiji congress-pressure changes instead of claiming a defense-readiness change that the effect does not make.

The coastal-guard decision tooltip now describes preparation for the final compact instead of claiming that this decision alone unlocks it.

The island-compact completion tooltip now describes the current regional settlement effect instead of promising a network or ambition publication that is not currently called.

No dynamic localisation block was added or removed. Existing dynamic category values and generic dynamic cost strings were verified in place.

## Validation

Meaningful checks completed were a targeted FIJ reference-to-localisation scan with zero missing keys, a duplicate-key scan across the target and all English files with zero FIJ collisions, a custom-tooltip reference scan confirming all 13 Fiji decision and focus tooltip keys resolve, and a byte-level BOM check confirming `EF BB BF`.

In-game testing was skipped because agents must not launch Hearts of Iron IV and the parent owns live-consumer validation. No broad Event 006 completion audit, focus render, decision render, or runtime source-date acceptance was attempted because those surfaces are outside this localisation-only tranche.

## Unresolved wording decisions and risks

The phrase "regional ambition" in `independence_wave_fij_ratify_island_compact_desc` remains a deliberate in-world description but should be revisited if the parent adds or rejects a corresponding ambition receipt.

The Sukuna portrait source-date uncertainty remains in the existing visual and country-package handoffs and is not resolved by this localisation patch.

No other Fiji localisation simplification or omission was introduced. This handoff is an actionable localisation audit and patch record, not a claim that IW-177 or Event 006 is complete.

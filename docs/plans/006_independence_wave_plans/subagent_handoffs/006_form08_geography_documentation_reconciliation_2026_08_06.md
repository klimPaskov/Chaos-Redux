# FORM-08 geography documentation reconciliation

Date: 2026-08-06.

Scope: documentation-only reconciliation of the current FORM-08 geography wording in the named source-of-truth system and registry documents; no gameplay, localisation, asset, or spreadsheet files were changed.

## Current authority

The current FORM-08 geography guard admits selectable TRA state 84 with optional North Transylvania state 76 and AXX state 82. Vojvodina remains the vanilla HUN-origin dynamic overlay, Slavonia remains unbound because no unique installed-map anchor is attested, and MAC state 106 remains a separate Event 006 package anchor rather than a current FORM-08 selectable member. FORM-08 therefore remains fail-closed pending a third in-scope member and anchor plus the required three-member, three-anchor, and three-consent proof.

## Files changed

- `docs/systems/006_independence_wave_form08_danubian_confederation.md` now separates current TRA/AXX selectable anchors from the Vojvodina overlay, unbound Slavonia, and separate MAC package readiness.
- `docs/events/006_independence_wave/systems/formable_registry.md` now carries the same current geography and admission wording in its status, policy, and adapter sections.

## Validation

- Read-only source evidence was checked in `common/scripted_triggers/006_independence_wave_form08_triggers.txt:4-40`, including the TRA/AXX geography branches and absence of a MAC branch.
- `rg -n -i 'FORM-08|TRA|AXX|MAC|Vojvodina|Slavonia|anchor|unbound|selectable'` was run against both changed source-of-truth docs and this handoff.
- `git diff --check -- docs/systems/006_independence_wave_form08_danubian_confederation.md docs/events/006_independence_wave/systems/formable_registry.md` was run after the edits.

## Remaining risk

Separate MAC package readiness must not be interpreted as FORM-08 admission, and the Vojvodina overlay or unbound Slavonia must not be counted as a third selectable member without an explicit geography and package decision. This handoff makes no runtime or gameplay-completion claim.

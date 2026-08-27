# Event 006 localisation audit

Date: 2026-08-27

## Scope and authority

This bounded audit reviewed the current Event 006 English localisation set after commits `010333a4c`, `4f6e9689b`, and `9adebbe20`. It traced event, decision and mission, focus, scripted-localisation, scripted-GUI, and GUI consumers, rechecked all active custom-cost keys, and verified that the retired pre-event crisis surface has no active category, mission, cost, queue, callback, or history writer.

The current source and `docs/plans/006_independence_wave_plans/006_source_of_truth_map.md` were treated as authority. Existing dirty Event 006 edits owned by other agents were preserved and were not folded into this patch.

## Audit results

### Missing keys

None remain after the patch.

The source trace resolved 3,334 unique explicit or implicit event, decision, focus, scripted-localisation, and GUI references. The only apparent extra reference was the focus-tree database id `independence_wave_focus_tree`, which is not a focus node and therefore does not require a `_desc` key.

### Duplicate keys

None. The 37 Event 006 English localisation files contain 8,764 parsed keys after the patch, with no duplicate Event 006 key and no Event 006 key duplicated elsewhere in the English localisation database.

### Scripted localisation issues

None found in active selectors. The consolidated Event 006 registry defines 58 unique `defined_text` names. All 48 Event 006 localisation calls to `GetIndependenceWave*` selectors resolve, and every `localisation_key` target used by the registry exists.

The retired `GetIndependenceWaveCrisisHistoryCause` and `GetIndependenceWaveCrisisResolution` compatibility selectors remain defined, but no active Event 006 source records their reserved payload values `6003` through `6012`. Their shared Event Log branches therefore have no current writer and do not create a pre-event row. They were not removed because the current source deliberately retains inert compatibility definitions.

### Dynamic text opportunities

No new dynamic selector is needed. Existing convoy-or-train, provisional-capital, formable commitment, status, scenario, formable, and focus-title selectors resolve correctly.

The active decision inventory contains 690 `custom_cost_text` consumers using 190 unique keys. After the patch, every active key has a base string, `_tooltip` alias, and `_blocked` string.

### Cross-surface mismatches and no-pre-event boundary

The FER administration cost was the one concrete mismatch. `independence_wave_fer_restore_railway_administration` consumes command power, manpower, and one civilian-factory commitment through `independence_wave_fer_cost_administration_standard`, but that custom-cost key lacked the tooltip alias and red blocked-state string expected by the decision UI.

No active pre-event localisation surface was found. The old crisis category and decision files are absent, `can_independence_wave_open_crisis` remains hard-disabled, the annex callback is absent, `chaosx.nr6.1` is hidden and triggered-only, and the public `chaosx.nr6.2` report requires a committed non-empty presentation count. Searches found no active `independence_wave_crisis_category`, `independence_wave_open_host_crisis`, or `independence_wave_cost_pre_wave_crisis` consumer.

### File encoding concerns

All 37 Event 006 English localisation files have UTF-8 BOM and the `l_english:` header. The patched FER file retains its BOM.

Eight older Event 006 localisation files contain 1,878 indented key lines, contrary to the repository's no-leading-space convention. They currently parse as localisation definitions in the source audit, and normalising 1,878 unrelated lines would create a broad mechanical diff, so this audit records the concern without changing them.

### Prose-quality findings

- Vagueness: no directly provable vague wording was introduced by the three audited cost commits. The corrected formable and FER strategic rows now distinguish spendable resources from gate-only War Support.
- Bloat: `independence_wave_ice_north_atlantic_category_desc` exposes a dense multi-ledger block with substantially more than the preferred visible-value budget. `independence_wave_afx_codify_basin_government_tt` is a 109-word route matrix. Both need owner-side presentation decisions rather than a localisation-only deletion of gameplay information.
- Obvious explanation: no additional safe removal was proved in clean files. Existing cost descriptions already use their adjacent custom-cost rows as the authoritative payment surface where prior handoffs repaired repetition.
- Repetition: several package effect tooltips enumerate the same ledger family across sequential settlement effects. The values differ by action, so they were not merged without an owning gameplay/display decision.
- Overcomplication: the Iceland category description and the Wallonia/Frisia government settlement tooltip are the strongest current examples. The Wallonia/Frisia file is also dirty from another agent, so this audit did not overwrite it.
- Style-rule repair: no em dash, sentence semicolon, update-history phrase, staged contrast formula, or prompt fragment was found in the Event 006 English set by the focused pattern scan.

### Sourced quotation preservation

The quote-bearing keys `chaosx_super_event.23.q` and `chaosx_super_event.24.q` were inspected and left byte-for-byte unchanged. No sourced or attributed quotation was altered.

## Patch

### Changed files

- `localisation/english/006_independence_wave_far_eastern_l_english.yml`
- `docs/plans/006_independence_wave_plans/subagent_handoffs/006_event6_localisation_audit_2026-08-27.md`

### Changed keys

- `independence_wave_fer_cost_administration_standard_tooltip`
- `independence_wave_fer_cost_administration_standard_blocked`

### Dynamic localisation added or fixed

No selector was added or changed. The tooltip alias nests the existing dynamic base key, and the blocked row preserves the same constants and texticons while using red amount formatting.

### Display before and after

Before, the FER railway-administration decision had only its normal custom-cost row. The UI had no package-local tooltip alias or red blocked rendering for its command power, manpower, and civilian-factory commitment.

After, the normal, tooltip, and blocked surfaces form a complete triplet. No trigger, payment effect, duration, AI weight, route gate, or cost value changed.

### Prose before-and-after summary

- Vagueness: unchanged.
- Bloat: unchanged.
- Obvious explanation: unchanged.
- Repetition: the tooltip aliases the existing cost instead of copying a second normal-state string.
- Overcomplication: unchanged.
- Style repair: the new rows are compact icon-first cost strings and contain no prose-style violation.

All dynamic tokens, constants, texticons, colour closures, and sourced quotations were preserved without exception.

## Validation

- Re-enumerated all 690 active Event 006 custom-cost consumers and confirmed complete base, tooltip, and blocked coverage for all 190 unique keys after the patch.
- Re-traced 3,334 unique player-facing source references and found no unresolved key.
- Rechecked all 58 Event 006 scripted-localisation names and 48 Event 006 selector calls with no duplicate or unresolved selector.
- Rechecked the retired pre-event identifiers and found no active category, decision, cost, annex callback, or history writer.
- Current mandatory MCP attempts for `chaosx.nr6.1`, `independence_wave_focus_tree`, `independence_wave_status_window`, and `chaosx_independence_wave_formable_state_puzzle_window` all failed in workspace `mod_chaos_redux_ea3b2d67c2c0` with `ARTIFACT_MANIFEST_INTEGRITY_FAILED: Artifact provenance manifest does not match its immutable address`. No current overflow, hierarchy, click-region, event-flow, or focus-layout artifact is claimed.

## Skipped meaningful validation and blockers

The installed MCP package has no dedicated decision-cost renderer. Decision-row wrapping and cost overflow therefore remain unverified. The mandatory event, focus, and GUI routes were attempted but produced no artifact because of the immutable artifact-manifest failure. Hearts of Iron IV was not launched, as required by repository policy.

## Unresolved wording decisions

- Whether to redesign the Iceland ledger category into a smaller visible summary requires owner-side gameplay and presentation input.
- Whether to split the Wallonia/Frisia route-settlement tooltip by selected route requires coordination with its current dirty source owner.
- The eight files with indented localisation keys should be normalised only as a separate mechanical cleanup with a reviewed diff.

No plan addendum was written. No gameplay, asset, spreadsheet, specification, or unrelated localisation file was changed.

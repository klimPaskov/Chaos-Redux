# Event 006 localisation audit and narrow patch handoff — 2026-08-24

## Scope and references

Audited Event 006 event/report text, event-log and event-details text, decisions and missions, the national focus tree, ideas, formables, super-events, dynamic cost bundles, scripted localisation, and character/portrait-facing name keys against current source and the Event 006 specifications.

The audit followed `AGENTS.md`, the Event, Decisions and Missions, Focus Trees, Super Events, Improvement Loop, and Subagents skills, the required offline Paradox localisation and system pages, and the corresponding vanilla documentation.

## Changed files and keys

- `localisation/english/006_independence_wave_iw059_mesopotamia_l_english.yml`
  - `independence_wave_iw059_cabinet_cost`
  - `independence_wave_iw059_cabinet_cost_blocked`
  - `independence_wave_iw059_cabinet_cost_tooltip`
  - `independence_wave_iw059_depot_cost`
  - `independence_wave_iw059_depot_cost_blocked`
  - `independence_wave_iw059_depot_cost_tooltip`
  - `independence_wave_iw059_officer_cost`
  - `independence_wave_iw059_officer_cost_blocked`
  - `independence_wave_iw059_officer_cost_tooltip`
  - `independence_wave_iw059_constitutional_cost`
  - `independence_wave_iw059_constitutional_cost_blocked`
  - `independence_wave_iw059_constitutional_cost_tooltip`
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml`
  - `independence_wave_rival_bloc_cost_invitation`, `independence_wave_rival_bloc_cost_accept`, `independence_wave_rival_bloc_cost_reserve`, `independence_wave_rival_bloc_cost_host`, `independence_wave_rival_bloc_cost_patron`, `independence_wave_rival_bloc_cost_leadership`
  - the matching six `_blocked` keys
  - the matching six `_tooltip` keys
- `localisation/english/006_independence_wave_form05_l_english.yml`
  - `independence_wave_form05_ratify_common_defense_protocol_desc`
- `localisation/english/006_independence_wave_wallonia_frisia_l_english.yml`
  - added `independence_wave_afx_basin_industry_bonus`
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
  - added `independence_wave_rhi_rail_industry_bonus`
  - added `independence_wave_bay_finance_industry_bonus`

All five changed localisation files remain UTF-8 with BOM.

## Display and prose before and after

- **Bloat and obvious explanation:** the rival-bloc custom cost repeated “Commits”, resource names, conjunctions, and, for the invitation, decision timing inside the cost line. It now displays only four or fewer dynamic amount-icon groups. Timing remains in the decision description and scripted duration.
- **Repetition:** IW059 and rival-bloc tooltip variants repeated their base cost lists with extra labels such as “Baghdad cabinet commitment” or “Requires”. Tooltip keys now reuse the authoritative base key. Blocked variants retain the same dynamic tokens with red amounts.
- **Overcomplication:** all patched cost bundles now use one consistent amount-before-icon pattern, without sentence structure around the spend.
- **Vagueness:** the FORM-05 common-defense description promised Army Experience although `independence_wave_decision_pay_security_material_standard` does not spend it. The description now names manpower, infantry equipment, support equipment, and the civilian-industry allocation actually required by the decision.
- **Style-rule repair:** removed prose and punctuation from cost-only strings. No event narrative was flattened or rewritten.

No new dynamic localisation selector was required. Existing constants, colour codes, icons, state tokens, scripted localisation calls, and country-name calls were preserved. The tooltip aliases reduce duplicate dynamic text without changing payment behavior.

## Audit findings

### Missing keys

The audit found three missing localisation keys used as `add_tech_bonus.name` values:

- `independence_wave_afx_basin_industry_bonus`
- `independence_wave_rhi_rail_industry_bonus`
- `independence_wave_bay_finance_industry_bonus`

All three were added. The 82 focus ids have title and `_desc` coverage, and all 68 Event 006 character `name =` references inspected have localisation coverage.

### Duplicate keys

No duplicate keys were found across 73 `006_independence_wave*_l_english.yml` files (8,741 keys after this patch).

### Scripted localisation issues

No broken scripted-localisation key target was found. All 44 `GetIndependenceWave...` calls found in Event 006 localisation resolve to a `defined_text` name, and all `localisation_key =` targets in Event 006 scripted-localisation files exist.

The remaining `independence_wave.history.crisis.*` namespace is internally stale terminology, but its visible strings are post-release “Release Record” text and its selectors still use those identifiers. Renaming it would be a multi-surface migration, not a narrow prose fix.

### Dynamic text opportunities and unresolved cost design

`independence_wave_formable_commit_cost_civic` displays five spend groups, while the revolutionary and military variants display eight. Localisation accurately mirrors the current payment bundles, so shortening those strings alone would conceal real costs. The gameplay owner should reduce or consolidate the bundles before a four-group localisation rewrite.

Other older package cost families still contain resource prose or redundant tooltip copies. This round changed only the two directly evidenced, bounded families above; a repository-wide cost-palette rewrite remains outside this subagent scope.

### Cross-surface mismatches and pre-event wording

- Current Transcaucasus IW-070/071/072 cost strings already use the corrected package Command Power amounts, and their descriptions no longer promise Army Experience. No patch was needed.
- FORM-05 reopening no longer mentions War Support and matches its current stability/Command Power/shipping/factory spend. No patch was needed there.
- No player-facing pre-event crisis category, mission, cost, queue, or pressure string was found in the Event 006 localisation set. The post-release Transcaucasian “oil-security crisis”, rival-bloc “patron pressure/host pressure”, and danger-milestone “coordinated pressure” describe active post-release systems and were retained.
- `common/script_constants/006_independence_wave_crisis_constants.txt` still contains a stale header saying a host-facing pre-wave crisis can request a Wave and has visible consequences. This is non-player-facing source commentary and was not patched under localisation ownership, but it contradicts the superseding spec and should be cleaned by the gameplay/documentation owner.

### File encoding concerns

None in the Event 006 localisation set. All 73 inspected files have a UTF-8 BOM.

### Prose-quality issues not patched

- **Vagueness/bloat:** several category descriptions are deliberately ledger-dense and remain long, especially the Transcaucasian charter and FORM-05 charter category. They communicate real thresholds and requirements, so a safe shortening pass needs GUI overflow evidence.
- **Obvious explanation/repetition:** older package `_tooltip` and `_blocked` cost variants still repeat base bundles. They are candidates for the same alias pattern after consumer verification.
- **Overcomplication:** the selected-formable commitment bundles remain too wide because gameplay currently charges five or eight spend groups.
- **Style violations:** no em dash or semicolon was introduced. Existing sourced quotations were excluded from style normalization.

### Sourced quotation preservation

`chaosx_super_event.23.q` (Woodrow Wilson, Fourteen Points, Point XIV) and `chaosx_super_event.24.q` (Hosea 8:7, King James Version) were inspected and preserved byte-for-byte. This audit did not independently re-research the source editions, so source wording certainty remains limited to the existing attributed text and Event 006 super-event documentation.

## MCP evidence and limitations

- `hoi4.event_inspect` for `chaosx.nr6.1` completed as `EVENT_INSPECTED_PARTIAL` and returned `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/ec30f9de8eeff9f7e7676cf849b2d46439e48dfdf0406ced03205638e01d7c97/569c454df4d693b9fa522eea2bdb072695cac3f4ea23640033bed94f99bf4ee9/event-trace-2ff7afa1197e.json`.
- `hoi4.event_render` completed as `EVENT_RENDERED_PARTIAL`; manifest: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/4cc3ae4d7b4908ad19a5d7113e8a3bcf8fc47b444a1ada2b33e6c2f7a446adea/4c271d0dba1688d8233f1b1f4a6913f9132000fc64aaeb372d469f8cb6fadebe/event-neighborhood-2ff7afa1197e-manifest.json`.
- Focus inspection of `common/national_focus/006_independence_wave_focus.txt` / `independence_wave_focus_tree` timed out after 180 seconds. A focus-render retry returned no artifact within 90 seconds and was terminated. Source coverage is not treated as equivalent visual evidence.
- GUI inspection of `events_log_history_details_window` first returned an input-validation blocker requiring `windowName` and `scenario` together. A scenario-id request then returned no artifact and stalled until terminated. No GUI overflow or live tooltip acceptance claim is made.
- The installed Technology Tree Viewer is unavailable, as noted in the localisation-agent contract. The three technology-bonus names were verified against source references only.

## Meaningful validation

- Re-ran Event 006 explicit localisation-reference coverage after the patch. The only initially unresolved literal `name` references were the three technology bonuses, and all are now present. Scripted-localisation function names were separated from literal localisation keys to avoid false missing-key reports.
- Compared each patched custom-cost key with its decision `custom_cost_text`, current cost trigger/payment effect, factory modifier, and duration fields. Dynamic token identities and spend-group counts are unchanged.
- Rechecked duplicate keys, BOMs, scripted-localisation targets/calls, focus title/description coverage, and character name-key coverage.

Skipped meaningful validation: no in-game or live tooltip test was performed, and no GUI/focus render artifact was available because of the MCP blockers above.

## Unresolved wording decisions and recommendations

1. Reduce or consolidate selected-formable gameplay payment bundles before shortening the five/eight-group cost strings.
2. Decide whether to migrate the internal `history.crisis` namespace to release-record terminology across scripted localisation and log consumers.
3. Clean the stale pre-wave crisis constants header in its owning source change.
4. Re-run focus and Event Details long-text/missing-localisation renders when the MCP routes return artifacts, then revisit the threshold-heavy category descriptions.

No mechanic plan handoff was created beyond this localisation audit because the unresolved items already belong to existing Event 006 gameplay/spec ownership.

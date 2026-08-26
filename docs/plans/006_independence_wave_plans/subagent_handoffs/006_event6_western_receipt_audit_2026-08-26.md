# Event 006 western founding-mission receipt audit

Date: 2026-08-26

Owner: `/root/event6_western_receipt_audit`

Status: Source audit complete with three minimal gameplay guards applied. Event 006 remains HOLD / PARTIAL and no live or save/load completion is claimed.

## Scope and verdict

This bounded pass audited every `days_mission_timeout` founding mission in `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt` and `common/decisions/006_independence_wave_iberian_decisions.txt` against the setup-receipt lifecycle contract.

The four audited blocks are AFX / IW-006 Wallonia, AGX / IW-007 Frisia, NAV / IW-013 Basque, and GLC / IW-015 Galicia.

No separate `FR` package predicate or `FR` founding mission exists in the two owned decision files or the package trigger/effect registries. The western file's second package is AGX / Frisia.

Three confirmed cancellation omissions were repaired with one existing-guard line each.

AGX / IW-007 already had the complete contract and was left unchanged.

No cost, AI-weight, admission, route, balance, localisation, or GUI behavior was changed.

## Severity-sorted findings

### High: stale mission lifecycle risk repaired

- `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:30` in `independence_wave_afx_prevent_industrial_stoppage.cancel_trigger` now cancels when `independence_wave_iw_006_setup_complete` is absent.
- `common/decisions/006_independence_wave_iberian_decisions.txt:21` in `independence_wave_nav_hold_fueros_together.cancel_trigger` now cancels when `independence_wave_iw_013_setup_complete` is absent.
- `common/decisions/006_independence_wave_iberian_decisions.txt:213` in `independence_wave_glc_hold_council_together.cancel_trigger` now cancels when `independence_wave_iw_015_setup_complete` is absent.

Before these lines, each mission already required its receipt in `activation`, but its cancellation OR block could leave an active mission alive while setup was being retried or had failed before restoring the receipt.

After these lines, receipt loss enters each mission's existing cancellation path, which preserves the existing package failure branch and removes the mission through normal engine cancellation.

### Pass: AGX / IW-007 was already symmetric

`common/decisions/006_independence_wave_wallonia_frisia_decisions.txt:321` requires `independence_wave_iw_007_setup_complete` in activation and `:331` already contains `NOT = { has_country_flag = independence_wave_iw_007_setup_complete }` in cancellation.

No duplicate guard or unrelated edit was added.

### No additional confirmed omissions

All four founding missions retain package identity, stable-ledger success, capital-control cancellation, timeout, existing failure effects, urgent AI weighting, and their existing category/localisation references.

## Exact patch inventory

Changed file: `common/decisions/006_independence_wave_wallonia_frisia_decisions.txt`.

- Identifier: `independence_wave_afx_prevent_industrial_stoppage.cancel_trigger`.
- Current line: 30.
- Added line: `NOT = { has_country_flag = independence_wave_iw_006_setup_complete }`.

Changed file: `common/decisions/006_independence_wave_iberian_decisions.txt`.

- Identifier: `independence_wave_nav_hold_fueros_together.cancel_trigger`.
- Current line: 21.
- Added inline guard: `NOT = { has_country_flag = independence_wave_iw_013_setup_complete }`.
- Identifier: `independence_wave_glc_hold_council_together.cancel_trigger`.
- Current line: 213.
- Added inline guard: `NOT = { has_country_flag = independence_wave_iw_015_setup_complete }`.

No files were staged or committed by this subagent.

## Lifecycle audit

The contract requires activation to have the package setup receipt, setup to clear that receipt before rebuilding, setup to restore it only in the prepared-success branch, and cancellation to test absence of the same receipt.

| Package and mission | Activation receipt and requirement | Setup clear / prepared restore evidence | Cancellation receipt guard | Existing outcome |
| --- | --- | --- | --- | --- |
| AFX / IW-006 `independence_wave_afx_prevent_industrial_stoppage` | Decision file `:18-24` requires `is_independence_wave_afx_package`, `independence_wave_iw_006_setup_complete`, unstable continuity, and unset resolved/failed receipts. | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:763` starts `independence_wave_setup_iw_006_wallonia`, `:765` clears the receipt, and `:806-807` checks `has_prepared_independence_wave_iw_006_package_setup` and restores it. | Decision file `:30`, added in this pass. | Existing `:34-47` marks resolved only for stable continuity, otherwise marks failed and applies the NWE project-failure effect. Timeout remains at `:26`. |
| AGX / IW-007 `independence_wave_agx_hold_the_waterline` | Decision file `:319-325` requires `is_independence_wave_agx_package`, `independence_wave_iw_007_setup_complete`, unstable waterline, and unset resolved/failed receipts. | `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:814` starts `independence_wave_setup_iw_007_frisia`, `:816` clears the receipt, and `:857-858` checks `has_prepared_independence_wave_iw_007_package_setup` and restores it. | Decision file `:331`, already present and preserved. | Existing `:335-349` marks resolved only for stable waterline, otherwise marks failed and applies the NWE project-failure effect. Timeout remains at `:327`. |
| NAV / IW-013 `independence_wave_nav_hold_fueros_together` | Decision file `:18` requires `is_independence_wave_nav_package`, `independence_wave_iw_013_setup_complete`, unset compact resolved/failed receipts, and no active founding mission. | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:428` starts `independence_wave_setup_iw_013_basque`, `:430` clears the receipt, and `:470` restores it only inside the prepared-success condition. | Decision file `:21`, added in this pass. | Existing `:21` cancellation effect marks resolved only for a stable compact, otherwise marks failed and applies `independence_wave_iberian_apply_project_failure`. Timeout remains at `:20`. |
| GLC / IW-015 `independence_wave_glc_hold_council_together` | Decision file `:210` requires `is_independence_wave_glc_package`, `independence_wave_iw_015_setup_complete`, unset compact resolved/failed receipts, and no active founding mission. | `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:474` starts `independence_wave_setup_iw_015_galicia`, `:476` clears the receipt, and `:515` restores it only inside the prepared-success condition. | Decision file `:213`, added in this pass. | Existing `:213` cancellation effect marks resolved only for a stable compact, otherwise marks failed and applies `independence_wave_iberian_apply_project_failure`. Timeout remains at `:212`. |

The prepared predicates are package-specific and remain source-backed at `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:174-231` for IW-006/IW-007 and `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:153-237` for IW-013/IW-015.

The corresponding complete predicates retain both the prepared proof and setup receipt at `common/scripted_triggers/006_independence_wave_wallonia_frisia_package_triggers.txt:294-309` and `common/scripted_triggers/006_independence_wave_iberian_package_triggers.txt:239-254`.

Package cleanup also clears the receipt for AFX at `common/scripted_effects/006_independence_wave_wallonia_frisia_package_effects.txt:968`, AGX at `:1018`, NAV at `common/scripted_effects/006_independence_wave_iberian_package_effects.txt:555`, and GLC at `:608`. No cleanup change was needed.

## Decision-category lifecycle notes

`independence_wave_afx_industrial_category` and `independence_wave_agx_waterline_category` contain the passive western founding missions and their package-local follow-on projects.

`independence_wave_nav_iberian_category` and `independence_wave_glc_iberian_category` contain the passive Iberian founding missions and their package-local follow-on projects.

Each founding mission uses `available = { always = no }`, so it is an automatic mission rather than a player-click cost surface.

Each founding mission has a package-specific `days_mission_timeout` constant and existing `cancel_effect` plus `timeout_effect` failure handling.

The new guards only make cancellation symmetric with the already-required activation receipt.

## Cognitive-load and mission-quality notes

The audited decision files expose no new visible action from this patch. Founding missions are automatic passive entries with existing names, descriptions, icons, and concise category structures.

There is one audited founding mission per package, and NAV/GLC retain their explicit shared active-founding-mission exclusion. No simultaneous mission expansion was introduced.

The setup receipt is an internal boolean lifecycle value and is not presented as a raw player-facing number.

Existing package ledgers and stability values carry the gameplay meaning through their existing tooltips and effects. This audit did not alter those values or add unexplained value dumps.

The mission requirements are readable from the existing package predicate, receipt, unresolved/failed receipt, stability, and capital-control checks. No long raw trigger tooltip was added.

Mission owners, categories, regions, requirements, duration, success, failure, and duplicate risk are as follows.

- AFX / IW-006 is the Wallonia industrial-continuity mission in the Northern Western Europe package category, with package-plus-receipt activation, dynamic NWE industrial-crisis duration, stable-continuity success, existing failure penalty, and one package-local founding mission identity.
- AGX / IW-007 is the Frisia waterline mission in the Northern Western Europe package category, with package-plus-receipt activation, dynamic NWE waterline-crisis duration, stable-waterline success, existing failure penalty, and one package-local founding mission identity.
- NAV / IW-013 is the Basque compact mission in the Iberian adapter category, with package-plus-receipt activation, dynamic Iberian founding-crisis duration, stable-compact success, existing failure penalty, and shared active-founding-mission protection.
- GLC / IW-015 is the Galicia compact mission in the Iberian adapter category, with package-plus-receipt activation, dynamic Iberian founding-crisis duration, stable-compact success, existing failure penalty, and shared active-founding-mission protection.

## Cost and requirement clarity

The founding missions have zero spendable cost types because `available = { always = no }` and none defines `cost`, `custom_cost_text`, or a paid completion effect.

The cost-count audit is therefore zero for AFX, AGX, NAV, and GLC, and no texticon coverage change is applicable.

Existing paid follow-on projects in the same files were outside this receipt-only scope and were not changed.

## AI validity and route-lock notes

All four missions retain `ai_will_do = { base = constant:independence_wave_decision_ai.urgent }` at AFX `:50`, AGX `:353`, NAV `:25`, and GLC `:217`.

No AI weight, probability modifier, package admission, route gate, or target predicate changed.

The required direct read-only MCP probability inspection was run after the patch with the `mission_ai_will_do` adapter for both owned decision files.

- Wallonia / Frisia artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/3896f17595834584e1e7bf6f7b596548ba7be54203be95c4dc3710de9233e6cc/73d60510cae5525187f9ed658cf11aafa08734a155398b4295a61cda32bac665/probability-inspect-2f6f029767d8.json`. Status is `PROBABILITY_SOURCE_INSPECTED` with empty diagnostics, 20 candidates, 14 required inputs, 0 unresolved, an incomplete pool, and 0 available candidates.
- Iberian artifact: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/542cc98c42a9d89e78ba005ac42611a03492f8879c9c8662dadfcbb9a96c1a80/537e16528b58d1b491b5241426cb5d2b06260c74db0769efbba936b15c10f4b8/probability-inspect-56cc0cefe28c.json`. Status is `PROBABILITY_SOURCE_INSPECTED` with empty diagnostics, 22 candidates, 12 required inputs, 0 unresolved, an incomplete pool, and 0 available candidates.

The first concurrent Wallonia inspection returned a transient MCP `INTERNAL_ERROR`. The serial retry succeeded with the artifact above and no source diagnostics.

No probability comparison was warranted because this patch does not change a weighted surface.

The installed tool surface exposed direct `hoi4_probability_inspect` but no callable `chaosx_ai_probability_auditor` route. This is recorded as a tooling limitation, not as equivalent live balance evidence.

No GUI inspection or render was run because these two decision files contain no in-scope scripted GUI surface.

## Localisation, tooltip, cleanup, and exploit notes

No visible key, icon, tooltip, or localisation string changed, and the internal receipt guard is not player-facing.

Existing cancellation and timeout tooltips remain attached to the existing effects, so receipt loss uses the established failure explanation.

Existing package cleanup clears missions and receipt flags through the package cleanup dispatch. No stale-flag cleanup gap was confirmed.

The repair closes a stale-mission generation gap and does not add a new activation loop, free equipment, war goal, core, unit, or cooldown path.

## Evidence and validation

Required offline references were read before editing, including the core Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding pages under `paradox_wiki/`.

The directly relevant offline references are `paradox_wiki/Decision modding - Hearts of Iron 4 Wiki.md:338,453-463`, `paradox_wiki/Triggers - Hearts of Iron 4 Wiki.md:286-287`, `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md:115-117`, and `paradox_wiki/Effects - Hearts of Iron 4 Wiki.md:282-283,525-527`.

Vanilla documentation was consulted in `C:/Program Files (x86)/Steam/steamapps/common/Hearts of Iron IV/documentation/triggers_documentation.md:3624+`, `effects_documentation.md` mission/flag entries, and `dynamic_variables_documentation.md:238-239`. Vanilla decision mission precedents were also inspected.

A corrected focused source assertion passed for all four missions and all four setup effects, proving activation receipt presence, matching cancellation guard, timeout presence, clear-before-prepared ordering, and prepared-only receipt restoration.

The six relevant Event 006 static validators all passed: `.tools/audit_event6_allocator.py`, `.tools/audit_event6_country_api.py`, `.tools/audit_event6_flags.py --strict`, `.tools/audit_event6_form16.py`, `.tools/audit_event6_gui_matrix.py`, and `.tools/audit_event6_scenario_matrix.py`.

The validator results include 149 publishers and 40 adapters, zero missing/duplicate country API entries, 102 complete flag families, FORM-16 contract pass, Statehood Ledger GUI semantic matrix pass, and SCN-008 scenario matrix pass.

No live game, save/load, or runtime consumer validation is claimed.

## Remaining risks and simplifications

The MCP probability artifacts report incomplete runtime candidate pools with zero available candidates, so they support source inspection only and do not provide numeric balance evidence.

The custom probability-auditor route was unavailable from the installed MCP surface, and no compare artifact was fabricated.

The Event 006 validators are repository-wide static checks and do not prove live mission cancellation or save/load behavior.

No separate FR package was inferred or invented, and no broad mechanic, cost redesign, AI rebalance, route change, localisation rewrite, or GUI work was performed.

No separate plan handoff was written because the requested repairs were narrow one-line guards. This file is the unique handoff for the tranche.

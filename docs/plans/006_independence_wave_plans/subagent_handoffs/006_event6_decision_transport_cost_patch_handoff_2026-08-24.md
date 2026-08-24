# Event 006 decision transport-cost branch patch handoff

Date: 2026-08-24.

Owner: `/root/event6_decision_gap_audit`.

## Result

I found and patched one concrete shared decision-surface gap: the Event 006 diplomatic cost strings showed one convoy amount beside both the convoy and train icons, while the payment helper consumes exactly one transport branch.

The patch is limited to the shared Event 006 scripted-localisation registry and its shared English decision-cost localisation file.

## Issue list, sorted by severity

1. **High — misleading transport cost disclosure across the shared decision map.** `common/scripted_effects/006_independence_wave_decision_effects.txt:156-170` and `:199-214` pay convoys when the actor has the threshold reserve and otherwise pay trains. `common/scripted_triggers/006_independence_wave_decision_triggers.txt:241-255` admits either branch. Before this patch, `independence_wave_cost_diplomatic_light` and `independence_wave_cost_diplomatic_standard` rendered the convoy amount followed by both `£convoy_texticon` and `£GFX_train_texticon`, so a player could not tell which stockpile or amount would be consumed.

2. **Medium — package-owned Event 006 cost strings remain outside this bounded patch.** Country/formable package files such as `006_independence_wave_form05_l_english.yml`, `006_independence_wave_form03_l_english.yml`, and the country package localisations contain similar static transport pairs, but their payment helpers and route-specific costs are not the shared decision surface audited here. Those packages need their own owner-scoped branch audit before changing them.

3. **Unresolved evidence — mandatory GUI and weighted MCP routes did not return engine artifacts.** `hoi4.gui_inspect` and `hoi4.gui_render` for `independence_wave_status_scripted_gui` with scenario `E6_SHARED_DECISION_PROVISIONAL_2026_08_24` each timed out with `tool call failed ... timed out awaiting tools/call after 180s`. `hoi4.probability_inspect` for `decision_ai_will_do` on `common/decisions/006_independence_wave_decisions.txt` returned the same timeout. No source-only result is presented as equivalent engine evidence.

## Changed files and identifiers

- `common/scripted_localisation/006_independence_wave_scripted_localisation_registry.txt` adds `GetIndependenceWaveDiplomaticLightTransportCostText`, `GetIndependenceWaveDiplomaticLightTransportCostBlockedText`, `GetIndependenceWaveDiplomaticStandardTransportCostText`, and `GetIndependenceWaveDiplomaticStandardTransportCostBlockedText`.
- `localisation/english/006_independence_wave_decisions_l_english.yml` adds twelve branch-localisation keys for light/standard convoy, train, either-branch fallback, and blocked variants.
- Shared cost IDs rewired to the selectors are `independence_wave_cost_diplomatic_light`, `independence_wave_cost_diplomatic_standard`, `independence_wave_cost_diplomatic_standard_factory_standard`, `independence_wave_cost_diplomatic_standard_factory`, `independence_wave_cost_patron_balance`, `independence_wave_cost_strategic`, `independence_wave_cost_strategic_major`, `independence_wave_cost_agx_coastal_conference`, `independence_wave_cost_corridor`, `independence_wave_cost_rescue_aid`, `independence_wave_cost_breakaway_sponsorship`, and `independence_wave_cost_reclamation_front`, including their blocked variants.
- Thirty-five shared decisions/missions use these cost IDs, covering the nine light diplomatic uses, five standard diplomatic uses, three standard-factory uses, ten strategic uses, three strategic-major uses, and the patron, corridor, rescue, breakaway, and reclamation actions.

## Before and after behavior

Before the patch, a light action could display `5 £convoy_texticon £GFX_train_texticon` even when the effect would consume `5 train_equipment`, and a standard action could display `10 £convoy_texticon £GFX_train_texticon` even when the effect would consume `10 train_equipment`.

After the patch, the scripted selector checks the same strict threshold as the available trigger and payment effect. If convoys satisfy the threshold, the cost shows the convoy amount and convoy icon. If convoys do not satisfy it but trains do, the cost shows the train amount and train icon. If neither branch is currently satisfied, the fallback shows both exact alternatives with their matching icons. Blocked variants apply the same branch selection in red.

Strategic, corridor, rescue, patron-balance, breakaway, and reclamation cost strings now reuse the same branch selector, so their civilian-factory, fuel, infantry, and support costs remain visible while the transport branch is no longer ambiguous.

## Decision category lifecycle notes

The shared category remains gated by `is_independence_wave_active_country = yes` in `common/decisions/categories/006_independence_wave_categories.txt:48-53`, so this patch does not introduce a pre-event player surface.

No category, activation, duration, target, cooldown, AI, or cleanup logic was changed.

## Cognitive-load notes

The shared decision map has thirty-five cost call sites using the affected transport family, but each call now communicates one selected transport branch rather than two icons attached to one amount.

The affected strategic and factory variants remain at four spendable cost groups at most: stability, command power, one transport branch, and civilian-factory burden. Rescue remains command power, one transport branch, infantry equipment, and support equipment.

The shared category and scripted GUI still expose the Event 006 state values through their existing surfaces; this patch only reduces cost ambiguity and does not redesign the panel.

## Mission quality notes

The audited DM-01 owner is the active Event 006 country in the founding category, with the capital state as its objective region. Its material gate requires capital control, the force-tier garrison, infantry/support equipment, and the conditional isolated-capital transport burden. Its duration is the existing dynamic 30-to-75-day band, and its success, cancellation, failure, and cleanup effects are already present in `common/decisions/006_independence_wave_decisions.txt:23-81` and the linked helper files.

The DM-01 mission is not a passive checklist: its normal activation is closed and `independence_wave_start_provisional_capital_mission` opens it only after the country-scoped commitment gate. Duplicate activation is blocked by the existing secured/failed/reserved flags and active-mission checks.

The existing open DM-01 disclosure concern remains that the opening commitment is reserved before the automatic mission appears; it was not widened into this transport-localisation patch.

## Cost, requirement, and icon audit

The source payment palette remains unchanged: command power plus one transport alternative for diplomatic actions, with any existing factory, stability, fuel, infantry, or support requirements shown separately.

All twelve new cost keys use the matching `£convoy_texticon` or `£GFX_train_texticon` for the displayed amount. No literal resource name replaces an icon.

The selector thresholds are `constant:independence_wave_decision_cost.convoy_light`, `train_light`, `convoy_standard`, and `train_standard`, matching the trigger and effect branches rather than duplicating magic numbers.

## AI validity, route locks, localisation, cleanup, and exploit risk

No AI weight or target route was edited, so no new AI validity or route-lock claim is made. The existing AI helpers continue to call the same payment effects as human decisions.

No effect, mission, flag, target, cooldown, or cleanup path was edited, so the patch adds no free-equipment loop, duplicate payment, reserve duplication, or stale-target risk.

The new scripted-localisation IDs are unique and all twelve branch keys are present in the shared English file. The modified YAML retains its UTF-8 BOM.

## Validation and skipped checks

`python .tools/audit_event6_allocator.py` passed and reported the Event 006 pre-event crisis surface retired.

A targeted static check confirmed all four new scripted-localisation names are defined, all twelve `independence_wave_cost_transport_*` keys are present, and the old ambiguous convoy-plus-train pattern is absent from the shared decision-cost file.

The GUI inspect/render checks were attempted and skipped after the exact 180-second MCP timeout described above.

The probability inspect route was attempted and skipped after the exact 180-second MCP timeout described above; no AI or probability patch was made.

HOI4 was not launched, in accordance with the repository instructions.

## Remaining issues

The package-localisation duplicates listed above remain for their package owners, and the prior Event 006 handoffs still contain the separate DM-01 disclosure, formable cost-budget, GUI evidence, and broad probability evidence gaps.

No separate plan was written because this was a narrow local cost-disclosure correction; this file is the complete patch handoff.

# Event 026 Black Friday Current Localisation Final Audit

Audit date: 2026-08-30.
Documentation refresh: 2026-09-02 against the current worktree; the current localisation evidence is supplemented by `localisation_patch_audit_2026-09-02.md`.

> Current-snapshot note: the 2026-09-02 patch handoff supersedes the stale visual/MCP and terminal-Fury statements formerly presented as current in this retained bounded audit; this file remains a historical scoped record and does not claim universal or live acceptance.

## Outcome

Event 026 has source-level localisation coverage for the audited scope, but universal consumption and Fury terminal sale-price proof remain incomplete.
Key coverage, namespaces, shared Event Log mappings, stale-identity cleanup, dynamic adapter wording, and UTF-8 BOM encoding are recorded for the audited scope after the parent applied the nine source fixes identified below.
Bounded visual proof was refreshed on 2026-09-02: selected GUI renders contain glyph paths and were rasterized and visually inspected, while full runtime visual proof and ordinary decision-tooltip rendering remain unavailable.
Hearts of Iron IV was not launched.

## Scope and references

This pass read `AGENTS.md`, every file under `docs/specs/026_black_friday_specs/`, the current Event 026 implementation and handoffs, the required offline Paradox wiki pages, relevant installed vanilla documentation, and the `chaos-redux-events`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents` skills.
The audit covered Event 026 presentation, Fury costs, the Japanese chemical campaign, biological medical capacity, CBRN civilian shelters, Japanese biological campaigns, shared Event Log and Event Details mappings, settings/debug name mappings, stale desert identity, status/cost-source text, and localisation encoding.
No design-depth gap was found, so no improvement-loop plan was written.

## Files and keys checked

### Event 026 and shared presentation

- `localisation/english/026_black_friday_l_english.yml`: all 44 keys, especially `chaosx.nr26.1.t`, `chaosx.nr26.1.d`, `black_friday.event_detail.premise`, `black_friday.status.*`, `black_friday.event_detail.evolution`, `black_friday.evolution.*`, `black_friday.history.50`, `black_friday.history.75`, `black_friday.scope.global`, `black_friday.cost_source.*`, `universal_cost.quote.*`, `black_friday.event_list.*`, and `achievement_black_friday_*`.
- `common/scripted_localisation/026_black_friday_scripted_localisation.txt`: `GetBlackFridayEventDetailStatusLine`, `GetBlackFridayEventListStatus`, every Fury normal/blocked selector, `GetBlackFridayJapanChemicalCampaignAttackCost`, `GetBlackFridayJapanChemicalCampaignAttackCostBlocked`, `GetBlackFridayJapanChemicalCampaignCylinderRequirement`, `GetBlackFridayBioExpandMedicalCapacityCost`, `GetBlackFridayJapanBioAnthraxCost`, `GetBlackFridayJapanBioAnthraxCostBlocked`, `GetBlackFridayJapanBioPlagueCost`, and `GetBlackFridayJapanBioPlagueCostBlocked`.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`: Event 26 scope, event-name, evolution type/title/body/summary, history ratio, Event-list state/weight, and Event Details description branches.
- `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`: Event ID 26 to `chaosx.event_name.26` at lines 125-126.
- `common/scripted_localisation/chaosx_scripted_localisation_settings.txt`: settings Event ID 26 and last-fired Event ID 26 to `chaosx.event_name.26` at lines 1747-1748 and 5748-5749.
- `localisation/english/chaosx_event_names_l_english.yml`: `chaosx.event_name.26`.
- `localisation/english/chaosx_gui_l_english.yml`: shared Event Details title, metadata, status, history, and body consumers, including the Event 26 status selector appended to `chaosx.events_log.window.event_details.entry_meta_cluster`.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt`: actorless history visibility at lines 581-594 and Event Details tertiary-row visibility at lines 1559-1577.
- `events/026_black_friday.txt`, `common/scripted_effects/026_black_friday_effects.txt`, `common/scripted_effects/chaosx_events_log_effects.txt`, `common/scripted_triggers/026_black_friday_triggers.txt`, and the Event 026 constants were read to compare the wording with activation, percentage, lifetime, eligibility, rounding, history payload, and cost behavior. This specialist audit did not edit gameplay files; the parent follow-up did.

### Fury adapters

- `common/decisions/007_fury_decisions.txt`: all 17 Event 026 custom-cost consumers for target, reinforcement, settlement, registers, rail registry, administrative core, march core, cooperation, rivalry, survey, terminal reserves, terminal fronts, border watch, emergency aid, staff talks, supply denial, and recognition denial.
- `localisation/english/007_random_expansion_l_english.yml`: `fury_*_cost_text`, their `_blocked` and `_tooltip` companions, and every `_sale`, `_sale_evolution`, `_sale_blocked`, and `_sale_evolution_blocked` variant; the corresponding anti-Fury key families were also checked.
- `common/script_constants/007_fury_constants.txt`: ordinary values used to verify the displayed 50-percent and 75-percent payable amounts and upward rounding.

The four Fury terminal normal and blocked branches use the defined positive `terminal_reserves_cp_gate` and `terminal_fronts_cp_gate` constants for quotes, with the corresponding negative spend constants retained for payment; sale-price confidence remains blocked only by owner-level and live display/payment evidence.
The displayed values follow the implemented upward-rounding rule where the required owner constants are available, including minimum positive units.
No static effect tooltip was found that contradicts the selected payment outside that unresolved constant blocker.

### Japanese chemical adapter

- `common/decisions/japan_chemical_campaign_decisions.txt`: attack cost and stockpile requirement consumers.
- `localisation/english/chaosx_decisions_l_english.yml`: `japan_chemical_campaign_attack_cost`, `_blocked`, `_stockpile_tt`, all `japan_chemical_campaign.attack_cost.*` variants, and all `japan_chemical_campaign.attack_cylinder_requirement.*` variants.

The ordinary and optimized command-power values, cylinder requirement, 50-percent variants, and 75-percent variants agree with the implementation and round upward correctly.
The readiness requirement remains distinct from the discounted payment.

### Biological medical adapter

- `common/decisions/biowarfare_disease_containment_decisions.txt`: `bio_expand_medical_capacity` cost, availability, and effect-tooltip consumers.
- `localisation/english/chaosx_decisions_l_english.yml`: `bio_expand_medical_capacity_cost`, `bio_expand_medical_capacity.cost.normal`, `.sale`, `.evolution`, `bio_expand_medical_capacity_cost_blocked`, `bio_expand_medical_capacity_available_tt`, and `bio_expand_medical_capacity_effect_tt`.

The payable selector, blocked selector, and effect tooltip are dynamic and correct.

### CBRN shelter adapter

- `common/decisions/cbrn_protection_decisions.txt`: `cbrn_move_civilians_to_shelters` custom cost and completion tooltip.
- `common/scripted_triggers/026_black_friday_triggers.txt`: the temporary payable political-power, Support Equipment, and Train values assigned for the custom-cost display.
- `localisation/english/cbrn_protection_l_english.yml`: `cbrn_move_civilians_to_shelters`, `_desc`, and `_complete_tt`.

The custom cost uses the calculated payable variables and the completion tooltip refers to the displayed payable costs rather than repeating ordinary values.
Source-level localisation is complete for this adapter.

### Japanese biological adapters

- `common/decisions/japan_biological_campaign_decisions.txt`: Anthrax and Plague requirements, custom costs, blocked costs, and effect tooltips.
- `localisation/english/japan_biological_campaign_l_english.yml`: `japan_bio_campaign_anthrax_target_tt`, `japan_bio_campaign_plague_target_tt`, both `*_requirements_tt`, both `*_cost`, both `*_cost_blocked`, both `*_cost_tooltip`, and both `*_effect_tt`.

The custom-cost selectors and the supporting requirements, cost, and effect strings display the correct ordinary, 50-percent, and 75-percent values.

## Missing-key list

No missing Event 026 or audited adapter key was found.
Every `localization_key` referenced by `common/scripted_localisation/026_black_friday_scripted_localisation.txt` resolves in English localisation, and every selector called by the audited decision custom-cost fields is defined.

## Duplicate-key list

No Event 026 or audited adapter key is duplicated under `localisation/english/`.
The repository-wide parser encountered unrelated duplicates for other event-name IDs, but none belongs to Event 026 or the six localisation-audited adapter scopes and none was changed in this bounded audit.

## Scripted-localisation issue list

- `GetBlackFridayEventListStatus` remains unconsumed outside its definition. This is dead helper text rather than a broken active surface; the shared Event-list selector is the current consumer and correctly handles Event 26.
- The parent follow-up added the matching dynamic selector for `bio_expand_medical_capacity_cost_blocked`.
- No broken `localization_key`, missing selector, namespace collision, or malformed Event 026 scripted-localisation reference was found.

## Source fixes applied after the specialist audit

1. The parent replaced `black_friday.event_detail.premise` with direct global one-day, baseline-rate, Friday-wait, and Evolution I wording and mirrored it in `Events!C27` before export.
2. The parent replaced the fixed ordinary `bio_expand_medical_capacity_cost_blocked` string with an icon-first normal, baseline-sale, and evolution-sale blocked selector showing `50/120/40`, `25/60/20`, and `13/30/10`.
3. The parent changed the three Anthrax supporting strings and the three Plague supporting strings to consume the existing dynamic cost selectors while preserving the non-cost requirements and consequences.

## Dynamic-text opportunities

- The blocked medical-capacity selector and the Anthrax and Plague dynamic references are now wired at source level.
- `black_friday.cost_source.line`, `.rounding`, and `.requirements` are consumed by the active sale idea description. `black_friday.cost_source.name` and `universal_cost.quote.*` remain generic shared copy rather than proof of universal transaction-level display; the six localisation-audited adapter scopes use their own current-cost selectors, while the broader registry records ten bounded source-adapter families.

## Shared Event Log and Event Details mappings

- Event ID 26 resolves to `chaosx.event_name.26: "Black Friday"` in debug, settings, last-fired, source-event, and Event-list mappings.
- The Event-list shared selector presents `Active`, `Reserved`, `Disabled`, `Fired`, below-threshold `N/A`, or the live event weight as appropriate.
- Actorless Event 26 history maps to `black_friday.scope.global`.
- Payment-ratio payloads 5000 and 2500 map to `black_friday.history.50` and `.75`.
- Evolution type, title, body, and summary mappings resolve to the Event 26 keys.
- The former shared-GUI visibility blockers are fixed in current source: Event 26 explicitly makes the actor row visible despite zero actors, and explicitly makes the Event Details tertiary status row visible even before a history sequence or evolution stage exists.

No remaining source-level shared mapping blocker was found.

## Stale desert identity

No active Event 026 source, localisation, spec, mapping, or asset registration contains `026_industry_to_desert`, `Industry to Desert`, `Move Industry to desert`, `Operation Desert Forge`, the former desert report sprite, or equivalent Event 26 desert wording.
The old desert event/localisation/assets are deleted in the current worktree and the Black Friday replacements are present.
Unrelated references to geographic deserts and desert forces elsewhere in the repository were excluded from this bounded finding.

## Status, cost-source, and debug text

The active Event Details status preserves the dynamic discount percentage and expiry.
Reserved, disabled, fired, unavailable, and eligible states are all present and ordered coherently.
The debug, settings, and last-fired mappings all resolve Event ID 26 to Black Friday.
The generic cost-source copy correctly distinguishes ordinary requirements from payable discounts and explains upward rounding, and the active sale idea description consumes the line, rounding, and requirement strings. The six localisation-audited adapter scopes use owner-specific dynamic selectors, while universal consumption by every custom owner remains unproven.
No player-facing Event 26 text exposes variable names, debug labels, implementation history, tuning notes, payment ratios, or basis points.

## Cross-surface mismatch notes

- The parent follow-up replaced the earlier vague Event Details premise with direct global-sale wording and mirrored it in the authoritative workbook before export.
- The parent follow-up added the dynamic blocked medical-capacity selector and changed all six Japanese biological supporting strings to reference the current dynamic cost line.
- Fury, Japanese chemical, and CBRN shelter wording matches the current source behavior at source level.

## File encoding concerns

The following audited English localisation files begin with `EF BB BF` and are UTF-8 with BOM:

- `localisation/english/026_black_friday_l_english.yml`
- `localisation/english/007_random_expansion_l_english.yml`
- `localisation/english/chaosx_decisions_l_english.yml`
- `localisation/english/cbrn_protection_l_english.yml`
- `localisation/english/japan_biological_campaign_l_english.yml`
- `localisation/english/chaosx_event_names_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

No `:0` suffix was found in the audited keys.
No encoding corruption was found.

## Prose-quality issue list

- The previously reported premise, medical blocked-cost, and Japanese biological repetition defects were corrected in the parent follow-up.
- The audited surfaces contain no em dash, sentence semicolon, prompt fragment, staged contrast formula, or implementation-history wording requiring repair.

## Sourced-quotation preservation

No inspected Event 026 or adapter surface contains a sourced or attributed quotation.
No quotation, dynamic token, formatting code, actor token, state token, cost value, requirement, or consequence was edited by this audit.

## MCP evidence and visual-proof blocker

- Event 26 trace, completed with partial expansion: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/e20cbe892828fb771b2f1dcbca41d4e3812972a0640d01defa138226de34f19b/00f438ba7e8705067c27f4272c1b78a5229a0db08fd9feb0d0681e6f2d2eb3c6/event-trace-bc205a20fdb8.json`.
- Event-list inspect for Event ID 26: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/925caea84510b474ce5f0d9a2dd111b12b50ad62431819b9dae7f8564c445d7c/256b8054edbb073a9f2a27b51125cc70f1140a4ed59d94819b63de5418643211/gui-inspect.698476fb3005544a.json`.
- Event-list render at 1920 by 1080 and 1366 by 768 in normal, long-text, and missing-localisation states: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/63e6551826bbf0610eb795dd14099c254bdbc3a38b872b93db1eed7685f6e873/3c055b1b0fdf473dcd4d48410f4511ea3c6a77af2cddf972efb66a527a466f19/events_log_events_content_window-full.svg`.
- Event Details inspect for Event ID 26 with active state and 75-percent discount variables: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/88671a4eefee316b5a0e353b21a430669ca8e1030c422c9e0173f0a15ded8bbd/db7a41ddec932ff7dfd43e1d254023d3c31d0919a625cea8141585a61982ec06/gui-inspect.4b2d998bb3117224.json`.
- Event Details render at both resolutions and all three states: `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/5830bbe2a44f7b99a8178b7bf654f3b0c75d4c30d8da596429527db33bae8eb1/fe738e73cbe7d1835d1ca56e9d852cd40f7a164c8abfc08a1321d0250afe9034/events_log_event_details_window-full.svg`.

The generated-GUI interpretation and Event Chain failure statements from this 2026-08-30 audit are historical and are superseded for the current snapshot by `localisation_patch_audit_2026-09-02.md`.
That current patch handoff records glyph-path and rasterized visual inspection for the selected Event Log and Event Details states, while full runtime visual proof and ordinary decision-tooltip rendering remain unavailable.
The installed HOI4 MCP package still exposes no decision-tooltip renderer for ordinary decision custom-cost surfaces, so Fury, Japanese chemical, biological, CBRN shelter, and Japanese biological tooltip overflow cannot be visually certified through the required MCP route.
Source inspection and partial render artifacts are not treated as equivalent to full live visual proof.

## Edits made by this audit

- Updated only `docs/plans/026_black_friday_plans/subagent_handoffs/localisation_final_audit_current.md` during the specialist audit.
- Parent follow-up then edited the Event Details premise, medical blocked-cost selector, Japanese biological supporting strings, and the authoritative catalog mirror identified in this handoff.
- No Git commit was created because this audit changed only the permitted untracked handoff in a worktree containing unrelated concurrent changes.

## Completion classification

- Source-level key/reference/encoding coverage: complete for the audited scope.
- Source-level player-facing localisation correctness: complete for the audited adapters after the nine identified keys were corrected and the catalog premise was mirrored.
- Shared Event Log/Event Details mapping source coverage: complete.
- Stale Event 26 desert-key cleanup: complete in active source.
- Bounded visual evidence: refreshed on 2026-09-02, but full runtime visual proof and ordinary decision-tooltip rendering remain unavailable; HOI4 was not launched, as required.
- Remaining wording blocker: live tooltip and full rendered-text proof remain unavailable through the installed tools; the Fury terminal quote constants are defined and aligned with their payment constants in the current worktree.
- Simplifications or fallbacks introduced by this audit: none.

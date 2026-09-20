# Event 006 FORM-03 body-level decision crosswalk

Date: 2026-09-20

Disposition: IMPLEMENTED SOURCE AUDIT / NO SOURCE-SAFE PATCH

This parent-owned crosswalk resumes the previously incomplete FORM-03 body scan in `common/decisions/006_independence_wave_form03_decisions.txt`. It is a source-structure audit, not native decision-row, probability, live-runtime, or save/load evidence.

## Scope and method

The scan covered all 23 child rows under `independence_wave_form03_low_countries_category`, including the two core-delegation votes, two Belgian delegation votes, autonomous membership, the language and works progression, the development compact mission, sovereign-corridor invitation, ratification, recovery, associate-member, and withdrawal surfaces.

Every row was checked for its title and description identifiers, icon, visible or activation gate, availability gate, terminal effect, cancellation trigger, and AI willingness block. Paid rows were also checked for a custom affordability trigger, custom cost key, and base/blocked/tooltip localisation triplet. The ratification row was checked as the deliberate prepaid selectable mission exception with timeout and cancellation resolution.

## Results

All 23 rows have the required structural lifecycle fields. The 22 ordinary decisions have a `complete_effect`, `remove_effect`, `cancel_trigger`, and `ai_will_do` block. The ratification mission has `activation`, `selectable_mission`, `complete_effect`, `timeout_effect`, `cancel_trigger`, `cancel_effect`, `fire_only_once`, and `ai_will_do` instead of an ordinary custom cost row.

All 23 rows have a defined title, description, and effect-tooltip localisation key. All 22 paid rows have a matching `custom_cost_trigger` and `custom_cost_text`, and each cost family has base, blocked, and tooltip definitions. The prepaid ratification mission intentionally has no custom cost key because its convergence work is paid before the mission begins.

The source-specific cancellation contracts remain aligned with their intended consequences. The language convention applies its accommodation cancellation result, the Sambre-Meuse and Frisian waterway projects apply their state-loss integration results, the Development Compact mission handles its committed reserve cancellation, and ratification resolves through its timeout or cancellation helper. No payment effect, AI weight, route lock, admission gate, or package boundary was changed.

The 23 rows are:

| Row | Source line | Surface | Cost contract |
| --- | ---: | --- | --- |
| `independence_wave_form03_authorize_core_delegation` | 15 | decision | diplomatic standard |
| `independence_wave_form03_withhold_core_delegation` | 63 | decision | diplomatic light |
| `independence_wave_form03_belgium_authorize_founding_delegation` | 105 | decision | diplomatic standard |
| `independence_wave_form03_belgium_withhold_founding_delegation` | 142 | decision | diplomatic light |
| `independence_wave_form03_join_as_autonomous_member` | 178 | decision | diplomatic standard |
| `independence_wave_form03_convene_language_convention` | 207 | decision | administration standard plus factory |
| `independence_wave_form03_open_multilingual_service_examinations` | 240 | decision | administration standard plus factory |
| `independence_wave_form03_publish_member_language_codes` | 282 | decision | administration light |
| `independence_wave_form03_establish_federal_language_appeals` | 325 | decision | administration standard plus factory |
| `independence_wave_form03_extend_protected_local_services` | 357 | decision | protected services composite |
| `independence_wave_form03_reconnect_sambre_meuse_corridor` | 394 | decision | Sambre-Meuse project composite |
| `independence_wave_form03_coordinate_frisian_waterway_standards` | 436 | decision | Frisian waterway project composite |
| `independence_wave_form03_standardize_rail_and_customs_manifests` | 478 | decision | diplomatic standard plus factory |
| `independence_wave_form03_request_development_compact_technical_mission` | 507 | decision | compact technical mission composite |
| `independence_wave_form03_invite_sovereign_corridor_partners` | 550 | decision | corridor invitations composite |
| `independence_wave_form03_ratify_confederal_charter` | 587 | selectable mission | prepaid convergence work; timeout/cancellation resolver |
| `independence_wave_form03_resubmit_confederal_charter` | 615 | decision | diplomatic standard |
| `independence_wave_form03_reopen_charter_talks` | 641 | decision | strategic composite |
| `independence_wave_form03_repair_language_settlement` | 670 | decision | administration standard plus factory |
| `independence_wave_form03_repair_industrial_compact` | 700 | decision | industrial repair composite |
| `independence_wave_form03_implement_member_language_guarantees` | 730 | decision | member language composite |
| `independence_wave_form03_fund_associate_corridor_share` | 758 | targeted decision | member corridor composite |
| `independence_wave_form03_withdraw_from_autonomous_membership` | 795 | decision | diplomatic standard |

## Remaining evidence limits

This crosswalk does not prove simultaneous native visibility, rendered cost-row fit, AI balance, typed probability, dynamic GUI fidelity, live execution, or save/load behavior. The installed probability fixtures remain incomplete for decision and mission weighting, and the native decision-row rendering gate remains open. No central admission, formable identity, cost, or AI change follows from this receipt.

Changed files: this handoff only.

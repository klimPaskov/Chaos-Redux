# Event 006 player-facing route wording cleanup handoff

Date: 2026-08-29

Mode: bounded localisation-only patch

## Outcome

The scoped Event 006 player-facing tooltips no longer expose implementation-facing `package` terminology. The wording now names the bilateral settlement, government, route spirit, state authority, or concrete transport and arms resource that the player sees and uses.

## Changed localisation files

- `localisation/english/006_independence_wave_balkan_l_english.yml`
- `localisation/english/006_independence_wave_iw093_iw098_l_english.yml`
- `localisation/english/006_independence_wave_rhineland_bavaria_l_english.yml`
- `localisation/english/006_independence_wave_rival_bloc_l_english.yml`
- `localisation/english/006_independence_wave_scotland_wales_l_english.yml`

## Changed keys

- `independence_wave_mnt_host_ledgers_effect_tt` now says `Bilateral settlement`.
- `independence_wave_iw093_ratify_post_crisis_settlement_failure_tt` now refers to the Asante government.
- `independence_wave_iw098_ratify_post_crisis_settlement_failure_tt` now refers to the Sokoto government.
- `independence_wave_rhi_route_government_effect_tt` and `independence_wave_bay_route_government_effect_tt` now refer to the selected route spirit.
- `independence_wave_rhi_rhine_congress_effect_tt` now refers to the Rhenish government.
- `independence_wave_rival_bloc_invite_member_desc` now names transport capacity and arms.
- `independence_wave_scotland_wales_administrative_project_effect_tt` now refers to the state's civil authority.

No decision trigger, payment effect, amount, AI weight, package gate, category visibility, event id, character, portrait, asset, or pre-event surface changed. Internal localisation keys and comments that use `package` as an implementation identifier remain unchanged.

## Evidence

The scoped search across dedicated Event 006 English localisation no longer finds player-facing `package` wording in the five repaired route families. Remaining matches are internal keys, scenario identifiers, comments, or other non-player-facing source labels. The broader audit indicator still reports 95 cost-key rows containing numeric literals without a dynamic constant token; the separate Event 006 localisation cleanup handoff records the 140 audited dynamic-cost repairs.

The required HOI4 production event, GUI, and visible-consumer render routes remain unavailable in this runtime, so this handoff makes no production overflow or live-display claim. Existing allocator, GUI semantic, scenario, and FORM-16 static validators remain the applicable source-level evidence.

## Simplifications, omissions, and blockers

No fallback, gameplay simplification, or unapproved asset was used. Broader route-by-route prose review and production rendering remain open, as does the broader Event 006 HOLD / PARTIAL disposition.

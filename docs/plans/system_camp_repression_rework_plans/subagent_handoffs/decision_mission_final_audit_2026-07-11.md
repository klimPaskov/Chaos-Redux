# Decision and Mission Final Audit Handoff

## Status

PASS. The final decision/mission audit found no remaining blocker in the requested scope after the cooldown-parity patch.

## Files changed

- `common/decisions/camp_repression_major_country_decisions.txt`
- `common/decisions/camp_repression_colonial_country_decisions.txt`

The patch adds the matching `camp_gui_country_action_N_cooldown` exclusion to the normal decision `available` block for each of the 32 actions exposed through the four country-action slots in the Repression Ledger. This prevents a normal decision click from bypassing a cooldown created by the equivalent Ledger button.

## Exact slot mapping

| Country kit | Slot 1 | Slot 2 | Slot 3 | Slot 4 |
| --- | --- | --- | --- | --- |
| Germany | `germany_route_prisoner_labor_to_war_construction` | `germany_increase_guard_allocation_to_ss_sites` | `germany_destroy_auschwitz_evidence_before_retreat` | `germany_dismantle_auschwitz_complex` |
| Japan | `japan_submit_to_army_review` | `japan_shut_down_prisoner_experiments` | `japan_evacuate_pingfang_research_staff` | `japan_open_epidemic_containment_office` |
| Soviet Union | `sov_reduce_paranoia_through_party_review` | `sov_emergency_famine_relief` | `sov_release_prisoners_for_military_service` | `sov_dismantle_overextended_gulags` |
| United Kingdom | `uk_reform_colonial_labor_administration` | `uk_release_political_prisoners_for_negotiations` | `uk_dismantle_raj_detention_network` | `uk_allocate_additional_colonial_guards` |
| United States | `usa_allow_court_review` | `usa_release_detainees_under_supervision` | `usa_terminate_relocation_authority` | `usa_establish_redress_commission` |
| France/Vichy | `fr_inspect_camp_legacy` | `fr_support_refugee_and_rescue_networks` | `fr_open_colonial_labor_review` | `fr_dismantle_north_africa_labor_network` |
| Italy | `ita_close_desert_camps` | `ita_compensate_local_communities` | `ita_expand_desert_transport_guard` | `ita_raise_colonial_security_battalions` |
| Belgium | `bel_open_international_inspection` | `bel_reform_concession_system` | `bel_recognize_local_administration` | `bel_negotiate_colonial_strike_settlement` |

## Final audit evidence

- Inventory is exactly 84 player actions, 41 missions, and four Ledger controls. Action parity is GER 7, JAP 13, SOV 9, ENG 10, USA 8, FRA/VIC 9, ITA 8, BEL 8, and generic 12.
- All 84 action ids are unique. Eighty-three route once through `camp_repression_action_dispatcher_effects.txt`; `camp_repression_close_dormant_legacy_site` routes once through the shared action bus. No action has a missing or duplicate route.
- Every player action has a centralized cost and an `ai_will_do` block. All 41 missions have a resolved positive timeout token.
- The obsolete `genocide_dismantle_extermination_camp` gameplay route is absent. The surviving dormant-legacy closure performs its actual closure in `remove_effect` after `days_remove`.
- `camp_rework_germany_start_occupied_poland_expansion_mission_in_from` and `camp_rework_germany_start_laboratory_annex` call `camp_rework_apply_ai_cap` immediately after mission activation, so Germany's one-project AI cap is current.
- `camp_rework_france_support_refugee_networks` applies `fr_refugee_aid_commitment` as a timed idea; `camp_rework_belgium_negotiate_colonial_strike_settlement` applies `bel_strike_settlement_commitment` as a timed idea. Both ideas carry the advertised civilian burden.
- `is_generic_player_selectable_camp_pool_state` includes the political-opposition tier before core fallback. The AI priority target and final generic dispatcher validation use the same selector, so political-opposition targets are reachable without suppressing all fallbacks.
- The cooldown validator found all 32 exact mapped decisions with one correct slot gate and zero unexpected gated decisions.
- Shared Ledger expansion, labor-project, and inspection buttons retain `camp_rework_country_uses_generic_kit`; dismantlement retains the reform/state checks; chemical and biological buttons retain the restricted-route and AI-cap checks. Country-action clicks rebuild availability before dispatch and use the same country action bus as decisions.

## Skipped validation and remaining risks

No runtime session was part of this read/audit-and-patch handoff. No remaining static decision/mission blocker, omission, fallback, or simplification was found in the requested scope.

## Skills used

- `hoi4-decisions-missions`
- `chaos-redux-subagents`

No skill was created or changed.

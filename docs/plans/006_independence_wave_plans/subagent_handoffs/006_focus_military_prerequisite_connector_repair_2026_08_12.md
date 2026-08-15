# Event 006 military focus prerequisite connector repair

## Scope

This bounded repair adds missing visible prerequisite connectors in `common/national_focus/006_independence_wave_focus.txt`.

## Change

The two military choices already required completion of `independence_wave_adopt_military_archetype_program` in their `available` blocks. Each now also declares that prerequisite, matching the sibling military choices.

Eleven adjacent branch roots received the same source-equivalent connector treatment: `independence_wave_map_internal_power_centers` → `independence_wave_complete_founding_settlement`, `independence_wave_establish_emergency_revenue` → `independence_wave_inventory_the_state`, `independence_wave_integrate_militia_commands` → `independence_wave_bind_the_first_oath`, `independence_wave_establish_foreign_office` → `independence_wave_name_provisional_authority`, `independence_wave_prepare_first_assembly` → `independence_wave_complete_founding_settlement`, `independence_wave_organize_popular_councils` → `independence_wave_complete_founding_settlement`, `independence_wave_define_former_host_policy` → `independence_wave_complete_founding_settlement`, `independence_wave_inherit_successor_ledger` → `independence_wave_define_former_host_policy`, `independence_wave_survey_regional_ambition` → `independence_wave_complete_founding_settlement`, `independence_wave_recognize_fellow_new_states` → `independence_wave_complete_founding_settlement`, and `independence_wave_sponsor_further_ruptures` → `independence_wave_survey_regional_ambition`.

The change does not alter the underlying availability trigger, route flags, mutual exclusion, reward, or AI score. It makes the authored military, founding, former-host, ambition, network, and high-chaos routes visible in the focus graph and removes trigger-only branches identified by the focus audit.

## Evidence and limits

The offline focus-tree guidance and vanilla prerequisite structure were reviewed before editing. A fresh `hoi4.focus_inspect`/`hoi4.focus_render` pass could not run because the installed MCP returned `ARTIFACT_MANIFEST_INVALID: Artifact provenance manifest is invalid` for workspace `mod_chaos_redux_ea3b2d67c2c0`. Prior valid Event 006 focus evidence remains historical; no new engine-layout claim is made here.

The broader Event 006 focus audit still records available-only roots elsewhere in the generic tree. Distant former-host, ambition, network, and high-chaos roots were left unchanged because a direct connector would create a long cross-lane detour; they remain a documented layout follow-up rather than an invented prerequisite.

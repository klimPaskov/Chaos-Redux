# Event 012 Africa Created-Country Advisor Pool Audit Handoff

Date: 2026-06-17

Scope: `africa_generate_created_country_role_staff` in `common/scripted_effects/012_africa_effects.txt`, matching advisor localisation in `localisation/english/012_african_union_l_english.yml`, and stale wording directly tied to the created-country generated advisor pool.

## Summary

No gameplay or localisation patch was needed. The helper generates exactly two generated advisor characters for each of the 21 Event 012 created actor tags: one `role_staff` advisor and one `support_staff` advisor. Token bases are unique, support advisor token bases begin with `africa_staff_`, all generated advisor idea keys and `_desc` keys are localised, and every advisor trait used by the helper resolves to a vanilla country-leader/advisor trait.

This remains the intended bounded setup surface. It is not a full bespoke minister or commander roster.

## Changed Files

- Added this handoff: `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_advisor_pool_audit_handoff.md`

No changes were made to:

- `common/scripted_effects/012_africa_effects.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- earlier Event 012 handoffs named in the parent prompt

## Country Package Coverage Checklist

- Tag list checked: `WAC SAH MAG NHR EAC GLK CBC ZSC SLC IOC GHP BBS TDM ANW OVN CRR CTL OKP TRM HGD GHC`
- Generated advisor count checked: 42 total advisor blocks.
- Per-tag advisor count checked: every listed tag appears exactly twice in the helper.
- Role split checked: 21 `role_staff` advisors and 21 `support_staff` advisors.
- Support advisor naming checked: every support advisor uses `idea_token = support_staff`, a token base beginning `africa_staff_`, and a resulting localisation key ending `_support_staff`.
- Duplicate token bases checked: none found among the 42 generated `token_base` values.
- Idempotence checked at helper level: the helper sets and gates on `africa_created_country_role_staff_generated`.

## File Surface Checklist

- `common/scripted_effects/012_africa_effects.txt`: checked helper structure, tag gating, `generate_character` syntax pattern, `idea_token`, advisor slots, ledger use, costs, allowed tag gates, and traits.
- `localisation/english/012_african_union_l_english.yml`: checked 84 generated advisor localisation keys, consisting of 42 idea names and 42 `_desc` entries.
- `localisation/english/012_african_union_l_english.yml`: confirmed UTF-8 with BOM by file header bytes `EF BB BF`.
- Vanilla references: checked `generate_character` documentation in `~/projects/Hearts of Iron IV/documentation/effects_documentation.md` and advisor trait definitions in `~/projects/Hearts of Iron IV/common/country_leader/00_traits.txt`.
- Scoped docs/handoffs: searched the named Event 012 documentation and handoffs for advisor-pool wording. No directly stale wording tied to this pool was found.

## Advisor IDs And Keys Checked

| Tag | Role advisor key | Support advisor key |
| --- | --- | --- |
| `WAC` | `africa_staff_wac_port_union_organizers_role_staff` | `africa_staff_wac_lagos_guard_captains_support_staff` |
| `SAH` | `africa_staff_sah_oasis_route_quartermasters_role_staff` | `africa_staff_sah_caravan_treaty_brokers_support_staff` |
| `MAG` | `africa_staff_mag_port_pilots_role_staff` | `africa_staff_mag_harbor_rebuilders_support_staff` |
| `NHR` | `africa_staff_nhr_nile_horn_surveyors_role_staff` | `africa_staff_nhr_highland_pass_commanders_support_staff` |
| `EAC` | `africa_staff_eac_railway_supply_engineers_role_staff` | `africa_staff_eac_track_security_command_support_staff` |
| `GLK` | `africa_staff_glk_lake_muster_staff_role_staff` | `africa_staff_glk_lake_supply_organizers_support_staff` |
| `CBC` | `africa_staff_cbc_river_forest_quartermasters_role_staff` | `africa_staff_cbc_congo_gate_pilots_support_staff` |
| `ZSC` | `africa_staff_zsc_stone_city_builders_role_staff` | `africa_staff_zsc_enclosure_captains_support_staff` |
| `SLC` | `africa_staff_slc_mine_port_strike_staff_role_staff` | `africa_staff_slc_gold_belt_organizers_support_staff` |
| `IOC` | `africa_staff_ioc_monsoon_convoy_pilots_role_staff` | `africa_staff_ioc_island_assembly_stewards_support_staff` |
| `GHP` | `africa_staff_ghp_highland_sanctuary_guides_role_staff` | `africa_staff_ghp_forest_boundary_mediators_support_staff` |
| `BBS` | `africa_staff_bbs_baobab_memory_speakers_role_staff` | `africa_staff_bbs_root_record_keepers_support_staff` |
| `TDM` | `africa_staff_tdm_tidemark_harbor_voices_role_staff` | `africa_staff_tdm_tide_gate_tally_keepers_support_staff` |
| `ANW` | `africa_staff_anw_ananse_signal_weavers_role_staff` | `africa_staff_anw_counterfeit_treaty_readers_support_staff` |
| `OVN` | `africa_staff_ovn_omen_keepers_role_staff` | `africa_staff_ovn_grove_boundary_speakers_support_staff` |
| `CRR` | `africa_staff_crr_river_marshals_role_staff` | `africa_staff_crr_ferry_law_tally_support_staff` |
| `CTL` | `africa_staff_ctl_telegraph_operators_role_staff` | `africa_staff_ctl_canopy_cipher_callers_support_staff` |
| `OKP` | `africa_staff_okp_shadow_couriers_role_staff` | `africa_staff_okp_forest_discretion_court_support_staff` |
| `TRM` | `africa_staff_trm_citadel_builders_role_staff` | `africa_staff_trm_tunnel_defence_captains_support_staff` |
| `HGD` | `africa_staff_hgd_route_finders_role_staff` | `africa_staff_hgd_hidden_depot_guides_support_staff` |
| `GHC` | `africa_staff_ghc_pathbreakers_role_staff` | `africa_staff_ghc_migration_vanguard_support_staff` |

Each key above also has the matching `_desc` key in `localisation/english/012_african_union_l_english.yml`.

## Advisor Roles And Traits Checked

Advisor slots used:

- `political_advisor`: 15 advisors
- `army_chief`: 7 advisors
- `high_command`: 11 advisors
- `navy_chief`: 4 advisors
- `theorist`: 5 advisors

Traits checked against vanilla `common/country_leader/00_traits.txt`:

- `silent_workhorse`
- `army_logistics_2`
- `navy_chief_maneuver_2`
- `military_theorist`
- `captain_of_industry`
- `army_chief_organizational_2`
- `war_industrialist`
- `navy_chief_decisive_battle_2`
- `army_infantry_2`
- `quartermaster_general`
- `army_chief_offensive_2`
- `army_regrouping_2`
- `armaments_organizer`
- `army_chief_defensive_2`
- `smooth_talking_charmer`
- `army_entrenchment_2`
- `army_cavalry_2`

All listed trait ids exist in vanilla advisor/country-leader trait definitions. The advisor-role syntax follows the documented `generate_character` pattern where the full idea token is `token_base` plus `idea_token`.

## Missing Or Stale Country Package Surfaces

No missing or stale advisor-pool surfaces were found in the scoped helper, localisation, or named documentation/handoff files.

Broader country-package gaps remain out of scope and are already described in the existing Event 012 country-package handoffs: full bespoke minister rosters, named commander pools, deeper country-specific focus trees, and deeper naval/air country branches.

## Map And State Setup Issues

Not audited in this pass. No advisor-pool issue depends on map or state setup.

## Politics, Leader, Portrait, Flag, Advisor, And Party Issues

Advisor pool result: no issue found.

This audit did not inspect country leaders, portraits, flags, parties, or gendered personal-name pools because these generated advisors are institutional staff bodies with explicit `name =` strings, not random one-person leaders or full minister rosters.

## Focus, Decision, Idea, And Asset Issues

No focus, decision, or asset issue was found for this advisor pool.

The generated advisor ideas rely on generated-character advisor idea tokens and localisation. This pass found matching localisation for all 42 generated idea ids and descriptions. No dedicated advisor icons were expected or added in this bounded setup.

## Starting Military, Technology, Industry, Supply, And Production Issues

Not audited in this pass. No starting military, technology, industry, supply, or production issue was found that is directly tied to the generated advisor pool.

## AI And Playability Issues

No advisor-pool AI issue was found. The helper gives each created actor two hireable advisors with valid slots and traits, which supports playability without expanding into full country-specific minister rosters.

## Validation

Meaningful checks run:

- Counted helper tag gates inside `africa_generate_created_country_role_staff`: every expected tag appears exactly twice.
- Counted generated advisor token bases: 42 total, with no duplicates.
- Counted generated idea tokens: 21 `role_staff` and 21 `support_staff`.
- Built expected generated advisor idea ids from `token_base` plus `idea_token` and checked every id plus `_desc` in `localisation/english/012_african_union_l_english.yml`.
- Checked localisation file header bytes and confirmed the BOM is present.
- Checked all advisor traits used by the helper against vanilla `common/country_leader/00_traits.txt`.
- Searched the named Event 012 docs/handoffs for advisor-pool wording and found no directly stale wording requiring a narrow doc patch.

Skipped validation:

- No live game load was run. The task was a scoped file audit and no gameplay or localisation patch changed runtime behavior.

## Remaining Gaps

- None inside the scoped generated advisor pool.
- Remaining broader country-package depth gaps are out of scope for this pass: full bespoke minister rosters, named commander pools, deeper country-specific focus trees, deeper production histories, and deeper naval/air behavior.

# Event 012 Africa Created-Country Advisor Pool Parent Handoff

Date: 2026-06-17

Scope: parent implementation and audit note for the bounded created-country advisor pool. This is not a completion claim for Event 012 Africa or the full country-package suite.

## Files changed

- `common/scripted_effects/012_africa_effects.txt`
- `localisation/english/012_african_union_l_english.yml`
- `docs/events/012_africa_foundation.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_country_package_audit_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-16_012_africa_completion_audit_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_production_parent_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_created_country_focus_ai_capstones_parent_handoff.md`
- `docs/plans/012_africa_plans/subagent_handoffs/2026-06-17_012_africa_bestiary_role_spirit_cleanup_parent_handoff.md`

## Gameplay surface

`africa_generate_created_country_role_staff` now gives each Event 012 created actor two generated advisor characters instead of one shared role-only surface:

- one existing role-family advisor using `idea_token = role_staff`;
- one distinct support advisor using `idea_token = support_staff`.

The support advisors are separate generated advisor identities, not smaller copies of focus or goal icons and not reused role-staff names. They are scoped to the same 21 Event 012 created actors:

`WAC`, `SAH`, `MAG`, `NHR`, `EAC`, `GLK`, `CBC`, `ZSC`, `SLC`, `IOC`, `GHP`, `BBS`, `TDM`, `ANW`, `OVN`, `CRR`, `CTL`, `OKP`, `TRM`, `HGD`, `GHC`.

## New support advisor token bases

- `africa_staff_wac_lagos_guard_captains`
- `africa_staff_sah_caravan_treaty_brokers`
- `africa_staff_mag_harbor_rebuilders`
- `africa_staff_nhr_highland_pass_commanders`
- `africa_staff_eac_track_security_command`
- `africa_staff_glk_lake_supply_organizers`
- `africa_staff_cbc_congo_gate_pilots`
- `africa_staff_zsc_enclosure_captains`
- `africa_staff_slc_gold_belt_organizers`
- `africa_staff_ioc_island_assembly_stewards`
- `africa_staff_ghp_forest_boundary_mediators`
- `africa_staff_bbs_root_record_keepers`
- `africa_staff_tdm_tide_gate_tally_keepers`
- `africa_staff_anw_counterfeit_treaty_readers`
- `africa_staff_ovn_grove_boundary_speakers`
- `africa_staff_crr_ferry_law_tally`
- `africa_staff_ctl_canopy_cipher_callers`
- `africa_staff_okp_forest_discretion_court`
- `africa_staff_trm_tunnel_defence_captains`
- `africa_staff_hgd_hidden_depot_guides`
- `africa_staff_ghc_migration_vanguard`

## Validation

Task-specific checks run by the parent:

- `africa_generate_created_country_role_staff` contains 42 generated advisor blocks: 21 `role_staff` and 21 `support_staff`.
- All 21 expected actor tags appear once in each advisor layer.
- All 42 `token_base` values are unique.
- Every generated advisor idea key and matching `_desc` key exists in `localisation/english/012_african_union_l_english.yml`.
- The localisation file still has a UTF-8 BOM.
- Advisor traits used by the generated roles resolve against the vanilla/mod country leader trait definitions.
- The touched effect and localisation files remain brace-balanced.

## Remaining gaps

- This tranche is still a bounded generated-advisor setup, not a full named minister, commander, and high-command roster for every created actor.
- The created actors still use shared companion focus trees with tag-specific capstones rather than full bespoke country trees.
- The broader country-package gaps remain open: richer per-tag route decisions, deeper package aftermath, fuller scripted AI behavior, and scenario validation.

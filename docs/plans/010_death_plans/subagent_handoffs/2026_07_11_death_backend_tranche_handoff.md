# Event 010 Death Maritime, Spatial, and Custodial Backend Handoff

Date: 2026-07-11

Role: `chaosx_scripted_system_architect`

Mode: bounded patch. Gameplay ownership was limited to Event 010 constants, scripted triggers, scripted effects, and state dynamic modifiers. Decisions, events beyond the approved evidence hook, localisation, GUI, assets, and broader documentation remained parent-owned.

## Reference Pass

Required project guidance was read before inspecting or patching the backend:

- `AGENTS.md`
- `.agents/skills/chaos-redux-events/SKILL.md`
- `.agents/skills/chaos-redux-subagents/SKILL.md`
- `.agents/skills/hoi4-decisions-missions/SKILL.md`
- `docs/plans/010_death_plans/2026_07_11_death_improvement_loop_addendum.md`
- the current Event 010 specs, matrices, README, and `docs/events/010_death/overview.md`

The required offline wiki pages were consulted: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, and AI modding. Relevant official vanilla documentation and precedents were checked for script constants, variables, meta triggers, `distance_to`, dynamic modifiers, event targets, state control changes, and targeted decisions.

## Files Changed

- `common/script_constants/010_death_constants.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `docs/plans/010_death_plans/subagent_handoffs/2026_07_11_death_backend_tranche_handoff.md`

No shared dynamic helper was added. These helpers are Event 010-specific, so `common/scripted_effects/chaosx_dynamic_effects.txt` and its markdown contract did not need changes.

## Implemented Outcome

### Country-scoped maritime evidence

The quiet-origin case file is held on each country, not inferred from hidden global Death state:

- variable: `death_maritime_evidence`
- durable country confirmation flag: `death_maritime_case_confirmed`
- one-time ledger flags:
  - `death_maritime_first_report_evidence_recorded`
  - `death_maritime_second_report_evidence_recorded`
  - `death_maritime_coastal_warning_evidence_recorded`
- policy-history flag: `death_maritime_case_closed_under_weather`

Central constants:

| Constant | Value |
| --- | ---: |
| `death_maritime_evidence.minimum` | 0 |
| `death_maritime_evidence.maximum` | 12 |
| fragmentary / pattern / probable / confirmed thresholds | 1 / 4 / 7 / 10 |
| first / second report gains | 2 / 3 |
| telegraph / quiet-quarantine gains | 2 / 1 |
| survey / confirmed-warning gains | 5 / 5 |
| weather / decay losses | -3 / -1 |

Public trigger API:

- `death_has_country_confirmed_maritime_case`
- `death_has_confirmed_maritime_case`
- `death_maritime_evidence_band_none`
- `death_maritime_evidence_band_fragmentary`
- `death_maritime_evidence_band_pattern`
- `death_maritime_evidence_band_probable`
- `death_maritime_evidence_band_confirmed`

Public effect API:

- `death_initialize_maritime_evidence`
- `death_clamp_maritime_evidence`
- `death_refresh_maritime_case_confirmation`
- `death_add_maritime_evidence`, consuming temp `death_maritime_evidence_delta`
- `death_confirm_maritime_case`
- `death_decay_maritime_evidence`
- `death_record_first_missing_report_evidence`
- `death_record_second_missing_report_evidence`
- `death_record_confirmed_coastal_warning_evidence`

Existing decision effects now feed the same evidence ledger:

- survey boat: +5 and country confirmation
- telegraph office: +2
- quiet quarantine: +1
- file under weather: -3, clamped, while preserving any remaining evidence

The first and second missing-route events call the one-time report helpers. `death_declare_war_on_current_state_owner` now snapshots the pre-transfer owner and controller, grants the confirmed-warning helper once to each existing normal-civilian non-Death country, and then performs the existing war declarations. A country that is both owner and controller cannot double-claim because the helper's ledger flag deduplicates the second call. This covers the first mainland revelation and later consumed coasts without a global knowledge scan.

Global public revelation remains a separate override only in `death_has_confirmed_maritime_case`; it does not backfill hidden country evidence.

### Spatial ordinary spread

Central route bands:

| Constant | Distance |
| --- | ---: |
| `death_spatial_route.short_distance` | 750 |
| `death_spatial_route.wide_distance` | 1500 |
| `death_spatial_route.maximum_distance` | 2500 |

`distance_to` requires literal numeric text. `death_initialize_global_state` mirrors the three authoritative script constants into:

- `global.death_ordinary_route_short_distance`
- `global.death_ordinary_route_wide_distance`
- `global.death_ordinary_route_maximum_distance`

The three distance triggers inject those initialized values through `meta_trigger`, avoiding an invalid effect assignment inside a trigger and avoiding duplicated file-scoped tuning.

Reusable target API:

- `death_is_within_short_ordinary_route`
- `death_is_within_wide_ordinary_route`
- `death_is_within_maximum_ordinary_route`
- `death_coast_is_warned_or_investigating`
- `death_is_ordinary_route_tier_one_target`
- `death_is_ordinary_route_tier_two_target`
- `death_is_ordinary_route_tier_three_target`
- `death_has_spatial_mainland_reveal_target`
- `death_has_spatial_triggerable_mainland_reveal_target`
- `death_has_spatial_coastal_jump_target`

Tier order is:

1. any otherwise-valid coast within the short band
2. a locally warned or investigating coast within the wide band, with global public revelation counting as a public warning
3. an otherwise-valid coast within the maximum band while spread pressure is high

`death_try_mainland_pressure_spread`, its living-war bypass variant, and `death_attempt_coastal_jump` all select the first tier that has a candidate and randomize only inside that tier. There is no unrelated global coast fallback.

If an ordinary coastal jump has no spatial candidate, its existing cooldown is applied and spread pressure is left intact. Coastal Watch interception remains ahead of a successful jump. Quarantine remains an absolute exclusion. Coastal Watch remains authoritative except for the already-established No Ferry Returns and world-end bypasses.

The strict, relaxed, defended, and last-resort world-end foothold triggers and `death_create_world_end_footholds` remain unchanged. Their continent-by-continent supernatural escalation is not constrained by the ordinary route tiers.

### Irreversible custodianship

Country throughput:

- variable: `death_custodial_capacity`
- range: 0 to 12
- completed survey gain: 1
- completed outpost gain: 1
- Living Compact contribution at defeat: 2
- qualifying participation in Death's defeat: 2

Capacity helper API:

- `death_initialize_custodial_capacity`
- `death_clamp_custodial_capacity`
- `death_add_custodial_capacity`, consuming temp `death_custodial_capacity_delta`
- `death_spend_custodial_capacity`, consuming temp `death_custodial_capacity_cost`
- `death_grant_defeat_custodial_capacity`
- `death_has_custodial_capacity`

State progression and candidate API:

- `death_is_valid_wasteland_survey_target`
- `death_has_wasteland_survey_candidate`
- `death_is_valid_dead_zone_outpost_target`
- `death_has_dead_zone_outpost_candidate`
- `death_is_valid_custodial_policy_target`
- `death_has_custodial_policy_candidate`
- `death_transit_custodianship_needs_maintenance`
- `death_has_transit_custodianship_maintenance_candidate`

Survey and outpost progression now has explicit state validation, payment inside the state effect, and retained one-time capacity claim flags:

- `death_custodial_survey_capacity_claimed`
- `death_custodial_outpost_capacity_claimed`
- `death_dead_zone_outpost_achievement_counted`

The retained claim flags are deliberately not cleared by renewed consumption. A recaptured state may need new survey and outpost work, but it cannot mint the one-time project capacity or achievement count again.

Final policies are mutually exclusive and cannot be switched while the state remains under custodianship:

| Policy | Capacity | Additional opening cost | Persistent state flag | Persistent modifier |
| --- | ---: | --- | --- | --- |
| Sealed Exclusion | 1 | none | `death_custodial_sealed_exclusion` | `death_custodial_sealed_exclusion_state` |
| Memorial Stewardship | 2 | none | `death_custodial_memorial_stewardship` | `death_custodial_memorial_stewardship_state` |
| Transit Custodianship | 3 | 20 CP, 200 support equipment, 100 trucks, 6 trains, 400 fuel | `death_custodial_transit_custodianship` | `death_custodial_transit_custodianship_state` |

Selection API, called from the targeted state:

- `death_select_sealed_exclusion_policy`
- `death_select_memorial_stewardship_policy`
- `death_select_transit_custodianship_policy`

Country cost gates:

- `can_pay_death_sealed_exclusion_policy_cost`
- `can_pay_death_memorial_stewardship_policy_cost`
- `can_pay_death_transit_custodianship_policy_cost`

Memorial Stewardship grants its one-time 3% stability and up to 2 mourning-debt relief through retained state flag `death_custodial_memorial_benefit_claimed`.

Transit Custodianship starts a 180-day `death_custodial_transit_maintenance_state`. Renewal costs 10 CP, 100 support equipment, 50 trucks, 3 trains, and 250 fuel through:

- `can_pay_death_transit_custodianship_upkeep`
- `death_start_transit_custodianship_maintenance`
- `death_maintain_transit_custodianship`

The underlying transit policy is permanent. The timed maintained-corridor benefit is deliberately removed on controller transfer; the new controller must fund its own service cycle.

Lifecycle safety:

- `death_remove_custodial_policy_modifiers` enforces modifier exclusivity.
- `death_clear_custodial_projects_for_reconsumption` removes active survey, outpost, policy, and maintenance state while retaining the anti-duplication ledger flags.
- `death_apply_active_wasteland_state` calls that cleanup before restoring the active wasteland package.
- `death_refresh_custodial_policy_state` repairs the selected permanent policy on control transfer.
- `death_apply_recaptured_wasteland_state` calls the refresh through the existing `on_state_control_changed` path.
- `death_finish_defeat` grants compact/participation capacity before compact membership flags are cleared.

## Permanent Wasteland Boundary

No policy restores population, state category, buildings, factories, or resources.

All three permanent policy modifiers add another `local_factories = -0.15` and `local_resources = -0.10` on top of the existing recaptured-wasteland values of -0.85 and -0.90. The combined values remain -1.00. Transit maintenance improves only limited movement, supply, organisation, and attrition; it does not make the state productive.

## Parent-facing AI Constants

The following centralized factors were added for the decision owner:

- `death_decision_tuning.ai_maritime_investigate_factor = 3`
- `death_decision_tuning.ai_maritime_strong_case_factor = 5`
- `death_decision_tuning.ai_maritime_quarantine_factor = 4`
- `death_decision_tuning.ai_maritime_low_evidence_close_factor = 2`
- `death_decision_tuning.ai_maritime_close_file_suppression_factor = 0.1`
- `death_decision_tuning.ai_custodial_exposed_sealed_factor = 5`
- `death_decision_tuning.ai_custodial_strategic_transit_factor = 5`
- `death_decision_tuning.ai_custodial_secure_memorial_factor = 4`
- `death_decision_tuning.ai_custodial_default_factor = 1`
- `death_decision_tuning.ai_custodial_unfit_factor = 0`

## Meaningful Validation

- Every new public trigger, effect, and modifier has exactly one top-level definition across `common/`.
- Every reference to the added Death script-constant groups and keys resolves.
- The report, confirmed-warning, policy-selection, transit-upkeep, re-consumption, control-transfer, and defeat-capacity helper call sites were traced.
- Both quiet-origin and Instant Outbreak launch paths call `death_initialize_global_state`, so the three spatial distance mirrors exist before ordinary spread evaluation.
- The target-selection call graph was checked for all three ordinary paths: standard mainland, living-war mainland bypass, and coastal jump.
- The world-end foothold target definitions and continent selection effect have no changed lines in this tranche.
- The confirmed-warning path snapshots both event targets before state transfer and deduplicates a shared owner/controller.
- The defeat-capacity grant occurs before compact flags are cleared.
- The four new dynamic modifiers contain no positive manpower, factory, or resource restoration.
- No daily, weekly, or monthly all-country scan was added.

Skipped:

- No live engine session was available for runtime evaluation of the spatial meta-trigger output, timed modifier expiry, or targeted-decision scope chain.
- No decisions, localisation, GUI, assets, spreadsheets, event-detail docs, or specs were edited by this backend tranche. The late parent-requested evidence integration stayed inside the owned scripted-effect helper.
- No Git commit was created because the parent owns the combined tranche and mandatory audit pass in the shared dirty worktree.

## Risks and Parent/Audit Follow-up

- Keep the weather action's player-facing wording aligned with its actual `-3` evidence downgrade; it does not always reset evidence to zero.
- The distance meta-triggers depend on the normal Event 010 initializers. Any future direct Death launch helper must call `death_initialize_global_state` first.
- Transit maintenance removal on control transfer is intentional; audit decision visibility so the new controller immediately sees the upkeep option.
- Policy dynamic modifiers currently reuse the approved existing outpost icon. No new asset is required by this tranche, but any later icon split needs the asset workflow before sprite identifiers change.
- The parent decision and localisation wiring should remain the source of player-visible costs and AI route preferences and must stay synchronized with the constants above.

## Simplifications, Omissions, and Blockers

No backend fallback or gameplay simplification was used. All three approved backend parts are implemented, including the explicit confirmed-warning call surface, spatial failure behavior, permanent policies, capacity accounting, duplicate prevention, controller-transfer repair, re-consumption cleanup, and unchanged world-end exception.

The backend tranche has no known implementation blocker. Runtime behavior still requires the parent-owned mandatory Event 010 completion and decision/mission audits before the combined tranche can be called complete.

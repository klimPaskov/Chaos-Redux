# Event 005 Completion Gap Audit Sidecar

Date: 2026-05-28  
Scope: read-only completion-gap audit for Event 005 Soviet Collapse. This report does not claim completion.

## Inspected Inputs

- Spec package: `tmp/soviet_collapse_final_clean_merged_spec_package/specs/005_soviet_union_collapse_part_1.md` through `part_7.md`.
- Recent handoffs in `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/`, especially:
  - `2026_05_28_event005_balance_mtth_low_threat_follow_on_sidecar.md`
  - `2026_05_28_event005_decision_mission_balance_tooltip_sidecar.md`
  - `2026_05_28_event005_breakaway_category_tooltip_sidecar.md`
  - `2026_05_28_event005_duplicate_payoff_cleanup_sidecar.md`
  - `2026_05_28_republic_industry_reward_variety_sidecar.md`
  - `2026_05_27_event005_council_leader_name_surface_sidecar.md`
  - `2026_05_28_event005_super_event_audio_unique_tracks_sidecar.md`
  - `2026-05-28_event005_generated_visual_sidecar_blocked.md`
  - `generated_asset_evidence_pass_2026_05_28.md`
- Current implementation files inspected:
  - `common/script_constants/005_soviet_collapse_constants.txt`
  - `common/mtth/005_soviet_collapse_mtth.txt`
  - `common/scripted_effects/005_soviet_collapse_effects.txt`
  - `common/scripted_triggers/005_soviet_collapse_triggers.txt`
  - `common/decisions/005_soviet_collapse_decisions.txt`
  - `common/decisions/categories/005_soviet_collapse_categories.txt`
  - `common/national_focus/005_soviet_collapse_republics.txt`
  - `common/national_focus/005_soviet_collapse_custom_splinters.txt`
  - `common/national_focus/005_soviet_collapse_factory_successors.txt`
  - `common/national_focus/005_soviet_collapse_ancient_restorations.txt`
  - `localisation/english/005_soviet_collapse_l_english.yml`
  - `history/countries/ALN - Alan Pass Principality.txt`
  - `history/countries/BAC - Black Sea Anarchist Confederation.txt`
  - `history/countries/KHW - Khwarazmian Oasis Authority.txt`
  - `history/countries/KZR - Khazar Toll Khaganate.txt`
  - `history/countries/NLC - Northern Lights Commune.txt`
  - `history/countries/OGB - Old Great Bulgaria.txt`
  - `history/countries/SOG - Sogdian City League.txt`
  - `history/countries/TSC - Trans-Siberian Cartel.txt`
  - `history/countries/UDC - Ural Defence Committee.txt`
  - `history/countries/UWD - United Women's Division.txt`
  - `music/chaosx_super_event_music.txt`
  - `music/chaosx_super_event_music.asset`
  - `sound/chaosx_sound.asset`
  - `docs/events/005_soviet_collapse_balance_audit.md`
  - `docs/events/005_soviet_collapse_validation_report.md`
  - `docs/events/005_soviet_collapse_focus_tree_audit.md`
  - `docs/events/005_soviet_collapse_final_completion_report.md`
  - `docs/events/005_soviet_collapse_full_implementation_ledger.md`
  - `docs/assets/005_soviet_union_collapse/manifest.md`
  - `docs/assets/005_soviet_union_collapse/gfx_handoff.md`
  - `docs/super_events/005_soviet_union_collapse_super_event_research.md`
  - `docs/super_events/super_event_audio_packages.md`

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Balance | Source-side partial | Low-threat and cap changes are present, but `docs/events/005_soviet_collapse_validation_report.md:153` says validation is source-level only, not a live playthrough. |
| Focus duplicate and quality | Partial | Current recount found 1696 focus `icon` fields, 1501 unique sprite names, 135 duplicate groups, and 195 duplicate extra assignments. |
| MTTH republic releases | Source-side partial | Low-threat follow-on release changes are reflected in constants, MTTH, triggers, and effects, but cadence still needs month 2-6 scenario validation. |
| Decision tooltips | Mostly reflected | Categories and mission failure tooltips are present; static regional cost text remains a drift risk. |
| Gender-safe leader names | Reflected | Single-person leader randomizer uses female/male portrait flags; council tags retain institutional names. |
| Super-event unique tracks | Reflected for active slots | Active slots 14-18 use unique tracks; retired archived slots still reuse the Union Unmade track. |
| Assets, flags, portraits | Partial | Focus icons remain incomplete. Generated visual sidecar was blocked. Some sidecar-only portrait outputs are not promoted. Stale/inactive duplicate flag families need parent reconciliation. |
| Docs and ledgers | Partial | Several docs correctly record source-only validation and focus icon blockers, but completion wording and stale counts remain inconsistent. |

## Priority Findings

### 1. Balance Is Still Source-Proven, Not Fully Validated

The recent low-threat follow-on balance changes are present:

- `common/script_constants/005_soviet_collapse_constants.txt:285-293` has `low_threat_follow_on_pressure_monthly_add = 2`, `low_threat_follow_on_release_add = 6`, `low_threat_follow_on_roll_release_add = 4`, `low_threat_follow_on_miss_factor = 0.85`, and `low_threat_follow_on_miss_floor = 12`.
- `common/script_constants/005_soviet_collapse_constants.txt:390-394` has `scheduler_low_threat_follow_on_days = 30`.
- `common/mtth/005_soviet_collapse_mtth.txt:17-20` applies the low-threat release add.
- `common/scripted_effects/005_soviet_collapse_effects.txt:1521-1526` uses the low-threat scheduler days.
- `common/scripted_effects/005_soviet_collapse_effects.txt:16280-16282` applies low-threat monthly pressure.
- `common/scripted_effects/005_soviet_collapse_effects.txt:16587-16592` applies the low-threat release roll add, miss factor, and miss floor.
- `docs/events/005_soviet_collapse_balance_audit.md:11` records calm strong USSR Authority 62 / Threat 7.25, which matches the spec target range much better than the former runaway-threat state.

Remaining blocker: `docs/events/005_soviet_collapse_validation_report.md:153` explicitly says the current validation is source-level only. The sidecar also left month 2-6 live scenario validation unresolved. The parent should not convert this into a completion claim until the calm/low-threat, mid-pressure, and collapse-pressure scenario cadence is verified or the docs explicitly keep the claim source-only.

### 2. Focus Duplicate Cleanup Is Only Partial

The recent payoff cleanup is reflected in the focus files and the visible repeated `remove_ideas` problem appears addressed:

- `common/national_focus/005_soviet_collapse_factory_successors.txt:1077` has `remove_ideas` inside `hidden_effect`.
- `common/national_focus/005_soviet_collapse_custom_splinters.txt:1353`, `1867`, `2253`, `2682`, `3110`, `3539`, and `19315` have `remove_ideas` in hidden effects or hidden blocks.
- `docs/events/005_soviet_collapse_focus_tree_audit.md:229-260` records multiple duplicate cleanup passes.

The larger focus quality blocker remains:

- Direct recount of the four Event 005 focus files found 1696 `icon` fields but only 1501 unique sprite names, leaving 135 duplicate icon groups and 195 duplicate extra assignments.
- `docs/events/005_soviet_collapse_validation_report.md:184` marks the focus icon scenario as `source_partial` for the same 1696 / 1501 / 195 blocker.
- `docs/assets/005_soviet_union_collapse/manifest.md:41` and `:972` also record focus icon uniqueness as incomplete.
- `docs/events/005_soviet_collapse_final_completion_report.md:56-58` records the 1696 / 1501 / 195 blocker, but later lines contain stale inconsistent counts. That report should be reconciled before any parent completion report.

Quality risk: `docs/events/005_soviet_collapse_focus_tree_audit.md:230` still records 163 base-only AI blocks outside scaffold in `005_soviet_collapse_custom_splinters.txt`, mostly bespoke late branches. That is not the same as duplicate payoff spam, but it is still a route-quality and AI-depth gap against the clean spec's depth standard.

### 3. MTTH Republic Release Follow-On Changes Are Reflected, But Cadence Is Unproven

The low-threat follow-on MTTH lane exists in current script:

- `common/scripted_triggers/005_soviet_collapse_triggers.txt:802` defines `has_soviet_collapse_low_threat_follow_on_release_lane`.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt:1435-1442` includes the low-threat lane in sustained MTTH release pressure.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt:1517-1530` excludes the low-threat lane from the calm MTTH release block.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt:1717-1752` permits progressive release rolls through the low-threat lane when pressure and pacing are ready.
- `common/scripted_triggers/005_soviet_collapse_triggers.txt:1902-1926` includes the low-threat lane in progressive release pacing readiness.

Remaining risk: `common/mtth/005_soviet_collapse_mtth.txt:174-190` and `:224-234` deliberately exclude the low-threat follow-on lane from some high-authority / high-obedience and strong-center dampeners. That may be intended by the recent handoff, but it is exactly the branch that needs practical month 2-6 validation to prove calm games do not over-release after one legitimate low-threat follow-on signal.

### 4. Asset, Flag, Portrait, And Generated Visual State Is Incomplete

Generated visual production remains blocked:

- `docs/plans/005_soviet_union_collapse_plans/subagent_handoffs/2026-05-28_event005_generated_visual_sidecar_blocked.md` reports no generated output because the asset request lacked exact asset list, paths, dimensions, and source mode.

Portrait state is mixed:

- `docs/assets/005_soviet_union_collapse/manifest.md:1208-1223` records the live MOL/UZB/TAJ/TMS/FER replacement portrait pass and validates the five promoted files.
- Sidecar-only generated portrait files exist for UKR/BLR/KAZ/LIT/GEO/AZR/KYR/TAT under `docs/assets/005_soviet_union_collapse/generated_republic_council_portraits_2026_05_26/`, but no live `gfx/leaders/005_soviet_collapse/<TAG>_leader.dds` files exist for those tags. This is not automatically a gameplay blocker if those tags intentionally use vanilla leaders, but it is an unresolved parent decision.

Flag state needs reconciliation:

- `generated_asset_evidence_pass_2026_05_28.md` reports byte-identical generated/custom flag families for BEC/BLT/COU/ILU/IRA/TRS.
- Direct repo scan found those flag files present under `gfx/flags/`, `gfx/flags/medium/`, and `gfx/flags/small/`.
- Direct repo scan found no active references to BEC/BLT/COU/ILU/IRA/TRS in `common/country_tags`, `history/countries`, or `interface`, so these appear inactive/stale rather than live Event 005 blockers. The parent should either exclude/remove them from Event 005 completion evidence or restore/regenerate them if they are meant to remain active.

## Explicit Recent-Change Checks

- MTTH low-threat follow-on release changes: reflected in current constants, MTTH, triggers, and effects. Live cadence validation remains missing.
- Decision tooltip changes: reflected. `common/decisions/categories/005_soviet_collapse_categories.txt:8-52` uses `visible_when_empty = yes` for the relevant categories, and `localisation/english/005_soviet_collapse_l_english.yml:2432`, `:2438`, and `:2498` include mission failure tooltips. Static regional faction cost strings at `localisation/english/005_soviet_collapse_l_english.yml:140-161` remain a drift risk.
- Focus duplicate-payoff cleanup: partly reflected. Exact repeated payoff packets and visible `remove_ideas` spam appear improved, but focus icon uniqueness and some route-quality / AI-depth gaps remain.
- Gender-safe leader names: reflected. `common/scripted_effects/005_soviet_collapse_effects.txt:8195` defines the single-person leader randomizer, female/male pools branch on `soviet_collapse_female_single_person_leader_portrait`, and `:8577` defines the council leader application path. BAC/NLC/TSC/UDC/UWD histories set female leader state before randomization; ALN/KHW/KZR/OGB/SOG retain institutional council names.
- Super-event unique track handoffs: reflected for active slots 14-18. `music/chaosx_super_event_music.txt:84-122`, `music/chaosx_super_event_music.asset:427-569`, and `sound/chaosx_sound.asset:249-270` wire unique active tracks. Retired slots still reuse the Union Unmade track by documented archival intent.
- Generated visual blockers: still present. The generated visual sidecar is blocked and focus icon uniqueness remains incomplete.

## Accepted Handoffs And Disposition

- `2026_05_28_event005_balance_mtth_low_threat_follow_on_sidecar.md`: implemented in source; unresolved live validation.
- `2026_05_28_event005_decision_mission_balance_tooltip_sidecar.md`: implemented in source; remaining live tuning and tooltip-density risks.
- `2026_05_28_event005_breakaway_category_tooltip_sidecar.md`: implemented for the category description; static regional faction cost text remains queued.
- `2026_05_28_event005_duplicate_payoff_cleanup_sidecar.md`: implemented in source; broader focus quality and AI-depth cleanup remains.
- `2026_05_28_republic_industry_reward_variety_sidecar.md`: implemented for the named republic industry duplicate set; broader repeated patterns remain outside that patch.
- `2026_05_27_event005_council_leader_name_surface_sidecar.md`: reflected in current history and scripted effects.
- `2026_05_28_event005_super_event_audio_unique_tracks_sidecar.md`: reflected for active super-event slots; retired slot duplication is documented as archival.
- `2026-05-28_event005_generated_visual_sidecar_blocked.md`: not implemented; blocked pending exact asset work order.
- No separate non-handoff accepted plan addenda were found under `docs/plans/005_soviet_union_collapse_plans/`. The clean merged spec remains the strict requirement source.

## Validation Performed

- Static unsupported-operator scan on Event 005 constants, MTTH, effects, triggers, decisions, and focus files found no `<=` or `>=`.
- Brace-depth scan returned `depth=0` and `neg=0` for the inspected Event 005 constants, MTTH, effects, triggers, decisions, category, and four national focus files.
- Static focus icon recount performed across the four Event 005 focus files.
- Static reference scan performed for stale BEC/BLT/COU/ILU/IRA/TRS flag families.
- Static existence checks performed for active super-event audio files and sidecar-only portrait files.

Validation not performed:

- No live HOI4 playthrough validation.
- No Clausewitz parser run beyond brace-depth and string scans.
- No visual inspection of DDS assets in-game.
- No AI simulation or balance run for month 2-6 republic release cadence.

## Remaining Blockers

1. Balance and release pacing remain source-validated only; low-threat follow-on republic release cadence is still unproven in practical month 2-6 scenarios.
2. Focus icon uniqueness is still incomplete: 1696 focus icon fields, 1501 unique sprite names, 195 duplicate extra assignments.
3. Focus route quality is improved but not fully at spec depth; documented base-only AI blocks and lighter shared-tree branches remain.
4. Generated visual production remains blocked; exact asset list, dimensions, target paths, and source mode are still needed.
5. Asset documentation is inconsistent: focus icon counts and completion language need reconciliation, and inactive duplicate flag families need explicit parent disposition.
6. Static regional faction cost localisation still embeds numeric costs, creating future drift risk against constants.

## Recommended Parent-Owned Patches

1. Run or explicitly record the missing live balance scenarios for calm strong USSR, low-threat follow-on month 2-6, mid-pressure, and collapse-pressure release cadence. If live validation is unavailable, keep the docs source-only and remove completion-style wording.
2. Finish focus icon uniqueness by replacing the remaining 135 duplicate icon groups / 195 duplicate extra assignments, or explicitly relax the spec and update the manifest, validation report, and completion report.
3. Patch or triage the remaining focus-quality issues: base-only AI blocks in bespoke late branches, lighter shared-tree branches, and any route payoffs still relying on helper-heavy generic rewards.
4. Consider routing `chaosx_improvement_loop_planner` for the remaining focus-tree depth and AI-quality gap, because the event can technically function while still falling short of the clean spec's intended depth, and no unresolved planner addendum was found.
5. Convert static regional faction cost localisation to scripted or constant-backed wording where possible, or document the cost strings as intentionally static with a maintenance note.
6. Reconcile `docs/assets/005_soviet_union_collapse/manifest.md`, `docs/assets/005_soviet_union_collapse/gfx_handoff.md`, and `docs/events/005_soviet_collapse_final_completion_report.md` against the latest asset evidence and current focus icon recount.
7. Decide whether sidecar-only UKR/BLR/KAZ/LIT/GEO/AZR/KYR/TAT council portraits should be promoted to live files or documented as unused alternates.
8. Decide whether inactive BEC/BLT/COU/ILU/IRA/TRS generated/custom flag families should be removed/excluded from Event 005 evidence or regenerated and restored as active content.

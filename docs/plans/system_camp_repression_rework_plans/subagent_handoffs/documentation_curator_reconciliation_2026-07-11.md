# Camp Repression Documentation Curator Handoff

Date: 2026-07-11

Status: **superseded checkpoint**. This handoff records the earlier 81-action reconciliation and is retained as implementation history. Current status lives in `../source_of_truth_and_completion_tracker.md`, `../completion_report.md`, `../scenario_contract_validation_report.md`, and `documentation_curator_final_reconciliation_2026-07-11.md`. Counts and open gates below are not current.

Mode: documentation patch only. No gameplay, localisation, workbook, spreadsheet, image, audio, or runtime asset file was edited by this pass.

## Changed Files

- `docs/plans/system_camp_repression_rework_plans/source_of_truth_and_completion_tracker.md`
- `docs/plans/system_camp_repression_rework_plans/major_country_kit_implementation_map.md`
- `docs/plans/system_camp_repression_rework_plans/colonial_country_kit_implementation_map.md`
- `docs/plans/system_camp_repression_rework_plans/repo_explorer_file_map.md`
- `docs/plans/system_camp_repression_rework_plans/core_contract_audit.md`
- `docs/plans/system_camp_repression_rework_plans/core_script_architecture_handoff.md`
- `docs/plans/system_camp_repression_rework_plans/completion_report.md`
- `docs/specs/system_camp_repression_rework_specs/README.md`
- `docs/specs/system_camp_repression_rework_specs/package_index.md`
- `docs/specs/system_camp_repression_rework_specs/continuation/continuation_prompt.md`
- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_2_country_systems_major_powers.md`
- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_5_country_decision_kits_focus_hooks.md`
- `docs/specs/system_camp_repression_rework_specs/specs/system_camp_repression_rework_spec_part_7_implementation_checklist_validation.md`
- `docs/systems/genocide_crisis_system.md`
- `docs/super_events/system_camp_repression_rework_super_event_research.md`
- this handoff.

## Promoted Live Identifiers and Surfaces

- Consolidated shared runtime, major-country, colonial-country, generic, Ledger, presentation, and workbook files are named in the tracker and completion report.
- The verified action baseline is 29 major, 41 colonial, and 11 generic actions: 81 total. The accepted final-audit target is 29 major, 43 colonial, and 12 generic: 84 total after France refugee aid, Belgium strike negotiation, and generic site inspection are confirmed live.
- Subject-controlled and direct selected-state actions use `camp_rework_action_state_id`, `camp_rework_prepare_selected_action_state`, `camp_rework_dispatch_prepare_colonial_selection`, `camp_rework_dispatch_restore_colonial_selection`, and `camp_rework_route_country_specific_action`.
- France and Italy pool helper and selector names are recorded from the live scripted trigger/effect files.
- Italy's homeland emergency detention and desert transport guard actions are called out explicitly.
- Restricted methods are documented as strict fixed-country/explicit-doctrine routes with matching technology, facility, and stockpile capacity, not a generic ideology inheritance.
- Ledger tabs are reconciled to Overview, State Pools, Active Sites, Country System, and Discovery & Reform.
- Super-event slots `12`, `74`, `75`, `76`, and `77`, audio ids `45`, `44`, `46`, `47`, and `48`, and their live helper/file ownership are recorded.
- Static UI, icon, report/news, super-event, achievement, and audio package status is reconciled; optional frame animation remains queued behind live static presentation.
- Workbook status remains attached to the existing Soviet Collapse Event Log row. No standalone camp-rework event identity was invented.

## Status Corrections

- `repo_explorer_file_map.md`, `core_contract_audit.md`, and `core_script_architecture_handoff.md` are retained but visibly marked as superseded preimplementation or frozen audit snapshots.
- Parts 2, 5, and 7 now distinguish live identifiers from proposed names and retain older design material as historical contract evidence.
- The system document's stale Ledger tab labels were replaced with the exact live five-tab contract.
- The super-event research file now distinguishes final live wiring from its archived proposed-text and original subagent ownership-boundary sections.
- A structured completion report now exists with files, systems, route coverage, assets, documentation, workbook, validation evidence, and remaining-gate sections.

## Validation Performed

- Recounted the live player decision blocks in all three package decision files, excluding mission blocks and the four Ledger controls.
- Read the action dispatcher path and confirmed the normal country state pointer and subject prepare/restore bridge.
- Read France and Italy pool helpers and selectors in live triggers/effects.
- Read fixed-country and explicit-doctrine restricted-method gates plus capacity checks.
- Reconciled Ledger names across scripted GUI, scripted localisation, interface, and player-facing localisation.
- Reconciled super-event slots, audio ids, helpers, localisation ownership, art registration, and sound registration.
- Compared asset-manifest totals with live GFX consumers and workbook Event Details with live localisation.

## Remaining Risks and Parent Follow-up

1. Promote the target count to 84 only after the three accepted audit additions exist with exact decision, dispatcher, localisation, icon, and AI parity. Until then, the documents intentionally retain an 81 verified / 84 target distinction.
2. The final decision/mission audit remains open while maintained-logistics behavior, mission outcome wiring, and control-sensitive dismantlement semantics are corrected.
3. The Part 7 scenario suite and final parent completion gate remain open.
4. `docs/assets/system_camp_repression_rework/manifest_icons.md` contains stale producer prose saying final registration is pending even though live GFX registrations exist.
5. `docs/assets/system_camp_repression_rework/manifest_report_super_event.md` contains a stale note saying the Auschwitz discovery report identity is not consumed; `GFX_report_event_auschwitz_discovery` is consumed by `chaosx_genocide.56`.

No fallback or unapproved simplification was used. Optional frame animation remains an accepted queued enhancement, not a runtime blocker.

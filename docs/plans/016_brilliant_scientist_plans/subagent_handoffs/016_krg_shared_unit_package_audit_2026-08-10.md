# Event 016 KRG shared-unit package audit handoff

Date: 2026-08-10.

Status: the KRG/Event 016 shared clone and Portal Raider integration is source-coherent and load-safe at the identifier level, with one unresolved technology-viewer sprite diagnostic and the intentionally unwired Portal Raider model package documented below.

## Scope and result

This audit covers KRG access to `portal_raider`, `teleportation_equipment_1`, the locked six-battalion `Quantum Transit Raiders` template, project completion and weaponization grants, Event 019 provider reuse, shared clone and Mengele refinement consumers, counters, GFX registrations, and runtime model/entity/action/sound references.

No obsolete runtime identifiers `kruger_portal_raider` or `kruger_portal_equipment` remain outside documentation, and no new Portal Raider model, entity, action, or sound fallback was created.

The only local load-safety edit in this tranche is lowercase `texturefile` normalization in `interface/clone_system.gfx` and `interface/portal_raider_system.gfx`.

## Country package coverage checklist

- KRG is registered as the dormant Event 016 formation tag and has the expected fixed leader and institutional characters in `history/countries/KRG - Kruger State.txt`.
- KRG starts with no research slots, no OOB units, and no portal or clone stockpile in `history/units/016_brilliant_scientist_dormant.txt`; formation setup materializes only from recorded project history.
- Formation setup in `common/scripted_effects/016_brilliant_scientist_country_effects.txt` inherits the verified host snapshot, calls the carried-portfolio importer, applies the history-gated project-force package, and then loads `brilliant_scientist_kruger_state_focus_tree`.
- The ordinary KRG portal and clone decisions remain gated by project operational triggers, site/network state, costs, and bounded batch limits.
- No politics, leader, portrait, flag, party, advisor, focus-tree, map, or state data was changed by this audit.

## Runtime file surface required for a safe commit

The canonical Event 016 consumers are `common/units/016_brilliant_scientist_project_forces.txt`, `common/units/equipment/016_brilliant_scientist_project_force_equipment.txt`, `common/technologies/016_brilliant_scientist_project_technologies.txt`, and `common/technologies/016_brilliant_scientist_project_force_technologies.txt`.

The shared clone consumers are `common/units/clone_infantry.txt`, `common/units/equipment/clone_equipment.txt`, `common/technologies/clone_technologies.txt`, and `common/scripted_effects/clone_system_effects.txt`.

The KRG and rebuild integration is in `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt`, `common/scripted_effects/016_brilliant_scientist_project_effects.txt`, `common/scripted_effects/016_brilliant_scientist_custom_technology_api_effects.txt`, `common/scripted_effects/016_brilliant_scientist_country_effects.txt`, `common/scripted_effects/016_brilliant_scientist_effects.txt`, and `common/scripted_effects/016_brilliant_scientist_kruger_state_decision_effects.txt`.

The KRG decision and trigger consumers are `common/decisions/016_brilliant_scientist_kruger_state_portal_temporal_decisions.txt`, `common/decisions/016_brilliant_scientist_kruger_state_clone_machine_decisions.txt`, `common/scripted_triggers/016_brilliant_scientist_focus_triggers.txt`, and `common/scripted_triggers/016_brilliant_scientist_project_force_triggers.txt`.

Event 019 provider registration and dynamic template reuse are in `common/script_constants/016_brilliant_scientist_project_force_constants.txt` and `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt`.

The expected counter and shared presentation assets are `gfx/interface/counters/divisions_large/unit_portal_raider_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_portal_raider_icon.dds`, `gfx/interface/counters/divisions_large/unit_clone_infantry_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_clone_infantry_icon.dds`, `gfx/interface/counters/divisions_large/unit_aryan_clone_infantry_icon.dds`, `gfx/interface/counters/divisions_small/onmap_unit_aryan_clone_infantry_icon.dds`, `gfx/interface/archetypes/archetype_clone_equipment.dds`, and `gfx/interface/technologies/clone_infantry_access_tech.dds`.

The shared clone runtime presentation is `gfx/entities/clone_infantry.gfx`, `gfx/entities/clone_infantry.asset`, `gfx/models/units/clone_infantry/`, `sound/clone_infantry_sound.asset`, and `sound/shared_clone_system/clone_infantry/`.

There must be no Portal Raider path under `gfx/entities/`, `gfx/models/units/`, or `sound/`; the model/entity/actions/sounds package remains rejected and intentionally unwired pending approved paid recovery.

## Templates, battalions, and duplicate-reward checks

`Quantum Transit Raiders` is defined once in `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` with six `portal_raider` regiments and is always locked by `set_division_template_lock`.

Its cap and recruiting authorization require teleportation deployment history or the explicit external portal operational flag, and the rebuild first revokes the cap and recruiting authorization before reapplying history-backed state.

`Replicated Guard Cadre` is defined once in the same file with ten shared `clone_infantry` regiments and follows the analogous locked and capped rebuild path.

`Clone Infantry Division` is defined once by `clone_ensure_infantry_template` in `common/scripted_effects/clone_system_effects.txt` as the shared editable ten-battalion template.

Event 019 provider 509 intentionally creates a dynamic locked `Portal Raider Formation [TEMPLATE_UID]` with four `portal_raider` battalions for derivative training; this is a provider-specific dynamic template and is not a duplicate of KRG's canonical six-battalion template.

Mengele ordinary clone and Aryan paths use their dedicated refinement helpers and existing German-model Aryan presentation; no duplicate KRG template or Portal Raider runtime ID is introduced.

## Technology and equipment grants

`brilliant_scientist_portal_warfare_tech` enables `portal_raider` and `teleportation_equipment_1`, while the portal weaponization technology depends on it and only supplies the intended combat and raid bonuses.

`clone_infantry_access_tech` enables shared `clone_infantry` and `clone_equipment_1`, while Event 016's `brilliant_scientist_clone_formations_tech` intentionally enables the same shared consumer through a separate project ledger; `clone_select_kruger_refinement` revokes Mengele refinements before selecting the Event 016 clone refinement.

`brilliant_scientist_rebuild_project_force_runtime_package` grants portal operational technology only when `brilliant_scientist_has_teleportation_force_history_deployment` is true and grants portal weaponization only when the corresponding history weaponization trigger is true.

The same rebuild path selects Kruger clone refinement and weaponization only from persisted cloning force history, while Mengele uses `clone_select_mengele_refinement` and `clone_select_mengele_aryan_refinement` under its own project and country gates.

The KRG portal batch decision grants only physical `teleportation_equipment_1` stockpile through `brilliant_scientist_krg_complete_portal_transit_batch`; it does not grant hidden technology or a formation.

The Event 016 custom technology API remains the only external grant surface and explicitly documents that it introduces no new player-facing technology object or icon requirement.

## Event 019 provider reuse

Provider 509 is registered as the Event 016 portal family and is exposed only when `brilliant_scientist_event19_portal_provider_unlocked` is true.

Its eligibility, dynamic four-battalion template, spawn callback, and sustainment profile all consume the canonical `portal_raider` and `teleportation_equipment_1` identifiers.

Provider 522 is the Mengele Aryan clone family and requires Germany scope, an active Mengele program, completed cloning project, the master-race claim, and `mengele_aryan_clone_refinement_tech`.

No provider callback references `kruger_portal_raider` or `kruger_portal_equipment`.

## KRG inheritance and causal rebuild

`brilliant_scientist_snapshot_kruger_state_portfolio` records the former host's project stage arrays, damage and suspension state, breakthrough state, and carried capacity before the verified formation transfer.

`brilliant_scientist_inherit_kruger_carried_portfolio` restores the exact snapshot for fixed-tag sovereignty and falls back to portable personal history for ordinary transfers without fabricating project sites or replaying completion rewards.

`brilliant_scientist_validate_inherited_project_physical_state` invalidates retained deployment stages when the required quantum transit network or cloning growth site is absent.

`brilliant_scientist_apply_project_inheritance_outputs` restores persistent ledger outputs while excluding one-shot sites, stockpiles, incidents, commitments, and force packages, after which `brilliant_scientist_apply_project_force_package_from_history` performs the independent history and physical-state-gated runtime rebuild.

This preserves the causal chain from formation snapshot to project history to technology and template materialization.

## MCP technology evidence

The mandatory `hoi4_tech_inspect` scan and explain route ran against workspace `mod_chaos_redux_ea3b2d67c2c0`.

The post-patch explain artifact for `clone_infantry_access_tech` is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/16af73344266e56f24705be95287a70aa8ab5478d10294605e277b5eb7108855/e3b076c608d705c5053380954f431a181ae0ec8eefb5d5f062b1d723805376c9/technology-explain-79a91cb13867.json`.

The route returned `TECH_INSPECTED_PARTIAL`, found no blockers, and still classified `GFX_clone_infantry_access_tech_medium` as `missing_sprite` despite the registered runtime DDS and lowercase `texturefile` key.

The five other hidden Event 016 or Mengele technology IDs likewise produced `GFX_<id>_medium` missing-sprite diagnostics; no `GFX_tech_<id>` names were requested by the definitions or MCP.

Event 016 documentation maps only the existing clone access DDS and states that the hidden custom technology API introduces no new player-facing icons.

The missing hidden-tech sprite diagnostics are therefore routed to the dedicated icon artist for review rather than filled with an unapproved fallback.

## Validation and remaining risks

The runtime obsolete-ID search returned `NO_OBSOLETE_RUNTIME_IDS` when excluding docs and wiki snapshots.

The runtime asset search returned `NO_PORTAL_RUNTIME_ASSETS`, while clone entity, mesh, animation, and sound assets were present in the shared paths listed above.

Counter and technology DDS paths were enumerated directly and matched the registered GFX paths.

The installed technology viewer returned partial helper projections for the large workspace, so source inspection and linked MCP evidence remain necessary until a complete Technology Tree Viewer route is available.

No Hearts of Iron IV process was launched, and no live save or in-game validation was performed because live consumer testing belongs to the user.

No probability or AI weight was changed, so no probability-auditor baseline or compare pass was required for this audit.

An older documentation-only map at `docs/plans/016_brilliant_scientist_plans/subagent_handoffs/016_project_reuse_identifier_map.md` still mentions obsolete Kruger Portal Raider names; runtime files are clear, but the stale historical handoff should be cleaned or superseded by the documentation curator.

Simplifications and blockers are limited to the unresolved hidden-tech sprite diagnostics and the intentionally unwired Portal Raider model/entity/action/sound package; no fallback asset or broad country-content change was made.

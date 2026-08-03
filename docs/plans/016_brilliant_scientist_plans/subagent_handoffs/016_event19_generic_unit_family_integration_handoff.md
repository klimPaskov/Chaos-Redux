# Event 016 to Event 019 Generic Unit-Family Provider Handoff

## Outcome

Event 016 now exposes seven generic Event 019 provider families after the history-derived runtime package is rebuilt.

The provider IDs and family IDs are 504 clone infantry, 505 autonomous robots, 506 paleogenetic creatures, 507 xenobiological organisms, 508 alien-interface infantry, 509 portal raiders, and 510 temporal guards.

The registration call is country-scoped at the end of `brilliant_scientist_rebuild_project_force_runtime_package`, so no all-country on-action or world iteration was added.

Existing Event 016 native materialisation remains authoritative and unchanged.

## Files changed

- `common/script_constants/016_brilliant_scientist_project_force_constants.txt` adds the provider-kind enum and seven generic registry tuning rows.
- `common/scripted_triggers/016_brilliant_scientist_project_force_event19_triggers.txt` gates each provider on its completed Event 016 history/runtime flag or its exact Event 019 derivative family/provider pair.
- `common/scripted_effects/016_brilliant_scientist_project_force_event19_effects.txt` owns registration, eligibility, generic template building, spawn dispatch, provider-owned management costs, refunds, manpower obligations, derivative setup, public-package receipt/removal, and cleanup callbacks for IDs 504-510.
- `common/scripted_effects/016_brilliant_scientist_project_force_effects.txt` calls the idempotent provider registration after runtime templates are rebuilt.
- `common/ideas/016_brilliant_scientist_project_force_ideas.txt` adds seven hidden provider-owned family ideas used by generic derivative public packages.
- `events/019_infantry_spawn.txt` adds generic Event 019 provider release and defeat presentation events 918 and 919.
- `localisation/english/019_infrantry_spawn_l_english.yml` localizes the generic provider reports and neutral host commander name.
- `docs/systems/chaos_unit_family_registry.md` records the five rows, neutral visual contract, provider-owned custom equipment accounting, and generic derivative receipt behavior.
- `docs/plans/016_brilliant_scientist_plans/016_event19_generic_unit_family_3d_model_backlog.md` records the deferred reusable model packages and runtime consumers.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `brilliant_scientist_register_event19_project_force_providers` | Country scope; current Event 016 active flags. | Calls exact registration rows once per active family; shared registry makes repeat calls idempotent and conflicting rows fail closed. | End of `brilliant_scientist_rebuild_project_force_runtime_package`. |
| `chaos_unit_family_provider_504..510_register` | Country scope; registry temporary registration fields. | Appends or verifies one family/provider row with contract version 4 and neutral visual profile 999. | Registration helper only. |
| `chaos_unit_family_provider_N_event19_evaluate_eligibility` | Country scope; provider-kind wrapper plus project history or derivative marker. | Sets `chaos_unit_family_candidate_eligible` and `chaos_unit_family_candidate_native`. | Generic Event 019 registry dispatch. |
| `chaos_unit_family_provider_N_event19_build_template` | Country scope; current Event 019 template UID/family. | Creates a locked generic Event 019 template using the existing Event 016 battalion token and appends the component manifest. | Event 019 generation/derivative template dispatch. |
| `chaos_unit_family_provider_N_event19_spawn_unit` | Country scope; current template and origin state. | Delegates to Event 019's authoritative unit spawn helper. | Event 019 generation/scenario/derivative spawn dispatch. |
| `chaos_unit_family_provider_N_event19_evaluate_management` | Country scope; live family count, stockpiles, and provider unlock gate. | Reports exact train/spawn/sustainment availability and training mode. | Event 019 Muster Board management dispatch. |
| `chaos_unit_family_provider_N_event19_pay_management_action` and `_refund_management_action` | Country scope; selected Event 019 management action. | Pays or restores provider-owned PP/CP/army XP, manpower, and exact project equipment without touching Event 019 shared costs. | Event 019 management transaction. |
| `chaos_unit_family_provider_N_event19_reconcile_sustainment` | Country scope; current generated unit factors. | Records the shared manpower obligation only; provider equipment remains provider-owned and is checked by the management callback. | Event 019 materialization obligation dispatch. |
| `chaos_unit_family_provider_N_event19_setup_derivative` | New derivative country scope; stored exact family/provider pair and parent isolation boundary. | Calls the common Event 019 private package, installs a neutral host commander, one provider-owned hidden family idea, a route variable, and a generic release report, then records a provider-owned package receipt. | Event 019 derivative setup dispatch. |
| `chaos_unit_family_provider_N_event19_remove_public_additions` and `_cleanup_derivative` | New derivative country scope; stored exact family/provider pair and defeat/final phase. | Clears the provider package receipt and family variable, then proves cleanup only after exact pair and phase checks. | Event 019 cleanup dispatch. |

## Constants and tuning

The seven rows live in `chaos_unit_family_event16_*` categories and use IDs 504-510, source event 16, neutral visual profile 999, family-only lot policy, and contract version 4.

Clone infantry uses standard `infantry_equipment` for the provider-owned material payment.

Robots, paleogenetic creatures, xenobiological organisms, alien-interface infantry, portal raiders, and temporal guards use their exact Event 016 equipment variants in their provider callbacks.

No shared Event 019 equipment-profile enum was expanded for these project-only equipment lines.

The provider-kind enum centralizes branch selection for the reusable callback bodies and prevents magic provider-kind values in the script.

## Event targets and cleanup

The bridge does not create a new global event target.

It relies on Event 019's existing regular event targets and ledgers for live divisions, generation context, templates, lots, and obligations.

The provider derivative marker and public-package family variable are country-scoped and cleared by `chaos_unit_family_provider_N_event19_remove_public_additions` before cleanup proof.

The common Event 019 cleanup retains ownership of shared ledgers, common flags, missions, and tracked-formation absence proofs.

## Icons and presentation assets

No new icon family is required for the provider bridge.

The generic release and defeat events use the existing `GFX_report_event_infantry_spawn_evolution_iii` report sprite, and the neutral provider commander uses the existing `GFX_portrait_infantry_spawn_unassigned_muster` portrait sprite.

Bespoke unit entity assets remain deferred in the durable 3D backlog and are not represented by the current neutral presentation.

## Migration from duplicated logic

Native Event 016 spawn helpers remain untouched.

Event 019 now reaches all seven families only through the generic registry row and provider-ID meta-effect dispatch, so no Event 019 family-list or provider-file edit was required.

Template construction, manpower ledger recording, eligibility, management, payment, refund, derivative setup, and cleanup branches are centralized in the Event 016 provider integration surface and exposed through seven thin provider wrappers.

## Validation

Offline Paradox wiki core pages, Unit Modding, Entity Modding, and Scripted GUI Modding were consulted before the edit.

Vanilla `script_concept_documentation.md`, `common/script_constants/documentation.md`, `effects_documentation.md`, and `triggers_documentation.md` were consulted for constants, `meta_effect`, `create_unit`, `set_variable`, `check_variable`, and event-target behavior.

The changed script files have balanced braces, no unsupported `<=` or `>=` tokens, no `add_army_experience` effect, and all seven provider wrappers expose the 11 required Event 019 callbacks including `remove_public_additions`.

The registration caller is present in the runtime rebuild and no daily, weekly, monthly, or other world-iteration action was added.

HOI4 was not launched.

## Risks and known limitations

The current engine presentation uses the already-defined Event 016 unit tokens and neutral Event 019 visual profile 999; no bespoke 3D entity binding is claimed.

The generic derivative installs a provider-owned hidden family idea, a neutral host commander using the existing Event 019 muster portrait, a provider route variable, a generic release report, and an auditable package receipt; cleanup removes those additions before proving the stored family/provider lifecycle.

The durable 3D backlog records that unsupported visual and presentation work for later approval and production.

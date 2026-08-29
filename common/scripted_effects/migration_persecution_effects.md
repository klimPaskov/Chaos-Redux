# Migration persecution projection

`common/scripted_effects/migration_persecution_effects.txt` owns the state-scoped `migration_persecution_active` projection. The flag describes only a currently proven targeted-persecution owner. It is not an ideology, war state, regime, occupation law, site/building presence, quota, famine-pressure value, evidence value, death amount, or generic occupation inference.

## Helper map

| Helper | Scope and inputs | Outputs and side effects | Call sites |
| --- | --- | --- | --- |
| `migration_persecution_issue_generation` | State scope after an accepted owner action has passed its concrete state, actor, and action guards. | Increments the state-local `migration_persecution_generation_counter`. | Internal to `migration_persecution_record_state`. |
| `migration_persecution_record_state` | State scope; `migration_persecution_pending_owner` must be a non-zero owner class and `migration_persecution_pending_actor` must be an existing country scope equal to `ROOT`. An owner may supply `migration_persecution_pending_generation`; otherwise the helper allocates one. | Allocates one state-local generation when no owner generation was supplied and forwards it to the idempotent class marker. Clears one-shot pending fields. A missing or mismatched actor fails closed. | Accepted detention, expanded labor, generic labor project, Soviet Gulag/extreme repression, concrete extermination/genocide, Germany/Japan experiment, and accepted CBRN operation seams. |
| `migration_persecution_mark_state` | State scope; pending owner class and pending generation. | Stores separate class-active flag, generation, actor country ID, and cause class. A newer generation replaces an older one, an equal active generation is a no-op, a lower generation is ignored, and a generation already ended cannot be replayed. | Internal. |
| `migration_persecution_recompute_state` | State scope; exact owner-class markers and metadata. | Selects metadata from the highest-priority currently active class while preserving every overlapping class marker. Sets the canonical flag only when at least one complete owner proof remains. | Internal after every mark and clear. |
| `migration_persecution_prepare_camp_terminal` | State scope before evidence resolution or inactive-site unregister; the current camp site profile is refreshed at this exact owner seam. | Maps detention, expanded labor, Gulag, radicalized, or experiment site type to one camp owner class and snapshots its current generation. Contaminated and generic profile-only states produce no request. | `camp_rework_resolve_site_evidence`, `camp_rework_unregister_inactive_site`. |
| `migration_persecution_prepare_camp_dismantlement` | State scope before a complete camp dismantlement clears site flags. | Snapshots every camp-owned class generation so a newer overlapping owner cannot be cleared by the older terminal path. | `camp_rework_complete_dismantlement`. |
| `migration_persecution_clear_owner_state` | State scope; pending owner class and a matching generation snapshot from its exact terminal callback. | Records the last ended generation, clears only that class, then recomputes aggregate ownership. A lower/stale generation cannot clear a newer class. | Exact evidence/site invalidation, generic labor project completion/failure, dismantlement, Soviet Gulag dismantlement through the shared dismantlement owner, CBRN control loss, and the CBRN active-window boundary callback. |
| `migration_persecution_clear_camp_owners` | State scope; snapshots created by the dismantlement preparation helper. | Clears detention, expanded labor, labor project, Gulag, and extermination classes one at a time; leaves CBRN ownership untouched; recomputes after the terminal sequence. | `camp_rework_complete_dismantlement`. |

## Owner classes and metadata

`migration_persecution_owner_class` in `common/script_constants/migration_persecution_constants.txt` is the shared class enum. The active class fields are state variables, not flags used as inferred inputs:

- detention: `migration_persecution_detention_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.
- expanded labor: `migration_persecution_expanded_labor_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.
- generic labor project: `migration_persecution_labor_project_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.
- Soviet Gulag/extreme repression: `migration_persecution_gulag_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.
- extermination/genocide and concrete experiment operations: `migration_persecution_extermination_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.
- accepted CBRN coercive nerve-suppression operation: `migration_persecution_cbrn_active`, `..._generation`, `..._actor_id`, and `..._cause_class`.

The canonical projection stores the selected current metadata in `migration_persecution_active_generation`, `migration_persecution_active_actor_id`, and `migration_persecution_active_cause_class`. Consumers must continue to use the boolean as a state-safety projection and must not infer actor or cause from it.

## Accepted writer contracts

Every writer sets a pending owner class and actor pointer in the exact state scope, then calls `migration_persecution_record_state = yes` only after its accepted action/state guard and concrete owner mutation have succeeded. The actor pointer must resolve to the action country (`ROOT`). A generation is allocated on the target state, so two different actors cannot collide merely because they have independent country counters.

The generic camp writer seams are detention activation, expanded labor assignment, generic construction/resource labor project start, and successful radicalization. The project uses a separate owner class so project completion cannot erase a still-active expanded-labor site.

The Soviet writers are the accepted industrial-Gulag transfer and extreme-repression state branches. Country quota, famine pressure, missions, active-site counts, and buildings alone never write the projection.

Concrete accepted German and Japanese prisoner/experiment operations may write the extermination/genocide class. The Auschwitz-layer and Japanese experiment writers require the concrete `genocide_camp_conversion_succeeded` result; a profile or laboratory registration without that accepted conversion remains blocked. Generic `genocide_register_*_site_for_root` APIs, inherited/static/test registration, and profile refreshes remain API-only and do not write the projection.

The CBRN writer is limited to the accepted nerve-suppression operation whose state target, actor, supplied payload proof, coercive route, exact record, timed active window, and control-loss cleanup are already owned by `cbrn_occupation_effects.txt`. Protected administration and protective-aid paths never write this class.

## Terminal and overlap contract

Evidence resolution and inactive-site unregister snapshot the class represented by the exact current camp profile before mutating that profile. Complete dismantlement snapshots every camp-owned class before clearing the concrete site flags. Generic labor project completion/failure snapshots and clears only the project class. CBRN operational control loss snapshots and clears only the CBRN class. The exact state-scoped backlash event is scheduled at the current operation's active-window boundary and invokes the existing expiry helper; that helper clears only when the timed active flag is absent, then recomputes overlap ownership.

Each clearer supplies the generation captured at the start of its exact owner callback. `migration_persecution_clear_owner_state` compares that value with the currently stored class generation; a lower or stale callback therefore fails closed. The last-ended generation is retained so a replay of a completed operation cannot reactivate the class. After one class is cleared, recomputation leaves the canonical flag set whenever another exact class still has complete current proof.

No terminal helper scans the world. The existing bounded active-site registry cleanup remains the owner of its own registry and only calls the exact state-local unregister path.

## No population or pressure side effects

These helpers never call Deaths, change population, mutate a cohort, apply famine pressure, issue migration pressure, or reuse a Deaths amount as persecution. The existing camp and chemical aftermath adapters remain the only owner-to-famine/migration pressure bridges. The canonical flag alone is never a pressure request.

## Example

```txt
var:camp_rework_action_state_id = {
	set_variable = {
		migration_persecution_pending_owner = constant:migration_persecution_owner_class.detention
	}
	set_variable = { migration_persecution_pending_actor = ROOT }
	migration_persecution_record_state = yes
}
```

The caller must place this example after the exact detention action succeeds. It must not be copied into a site registration helper, occupation-profile resolver, ordinary occupation-law path, test setup, generic genocide register, or forced-movement-only path.

## Unsupported or deliberately excluded branches

Generic occupation-law transitions lack a callback carrying changed state, responsible actor, action generation, and replay identity. Generic occupation-repression mortality, strategic bombing, war/front pressure, ideology, passive site presence, quota-only changes, famine pressure, evidence, and forced movement alone are not writers. If an owner cannot provide an exact terminal generation match, it remains blocked rather than inventing a fallback.

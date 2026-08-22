# Famine and Migration Achievement Hook Closure

## Scope and evidence

This closure review covers the eight achievement predicates in `common/scripted_triggers/famine_migration_achievement_triggers.txt` and their persistent evidence writers in `common/scripted_effects/famine_migration_achievement_effects.txt`.

Required offline references were reviewed before the patch: the Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Achievement modding pages under `paradox_wiki/`. Vanilla documentation reviewed for the touched behavior includes `documentation/effects_documentation.md`, `documentation/triggers_documentation.md`, and `documentation/script_concept_documentation.md`.

The achievement registry remains in `common/achievements/chaos_redux_achievements.txt`; all eight stable IDs still point to the same eight scripted predicates. No AI or probability weight changed, so the probability-auditor route was not required for this patch.

## Changed files and identifiers

- `common/scripted_effects/famine_migration_achievement_effects.txt`
  - `famine_migration_achievement_process_state`
  - `famine_migration_achievement_record_blockade_wasteland`
  - `famine_migration_achievement_record_blockade_self_route_exploit`
  - `famine_migration_achievement_record_predatory_requisition`
  - `famine_migration_achievement_record_corridor_started`
  - `famine_migration_achievement_record_tag_switch`
- `common/decisions/famine_migration_decisions.txt`
  - `fm_requisition_safer_state` exact donor-state transaction
- `common/scripted_effects/chaosx_famine_migration_effects.txt`
  - `famine_migration_resolve_route`
  - `famine_migration_transfer_civilians_exact`
  - `famine_migration_cleanup_state_registration`
- `common/scripted_effects/fallout_consolidated_effects.txt`
  - `fallout_commit_current_player_primary_target`
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/achievement_hook_closure.md`

## Before and after behavior

Before this patch, the blockade wasteland, blockade self-route, corridor manufactured-crisis, transfer-cycle/ledger, and tag-switch flags were predicate-only flags with no owner-local producer in the famine/migration source. The internment and protected forced-labor recorders also had no active owner call site.

After this patch:

- A route whose destination is the exact origin state is rejected before any population debit. If the origin has the proven blockade contract or the persistent blockade-achievement state, the owner receives `famine_migration_achievement_blockade_self_route_exploit`.
- A non-zero conservation residual after an actual origin debit marks both `famine_migration_achievement_transfer_cycle_detected` and `famine_migration_achievement_return_ledger_failed`. Invalid routes with no debit do not manufacture a failure record.
- A tracked blockade state entering the `wasteland` category records `famine_migration_achievement_blockade_wasteland` before state-registration cleanup can clear the runtime context.
- Starting a corridor from a state carrying the actual `famine_migration_crisis_concealed` or `famine_migration_extraction_active` owner-action flag records `famine_migration_achievement_corridor_manufactured_crisis`. A normal famine/trapped state without one of those explicit actions remains eligible.
- Requisitioning relief from an exact neighboring famine state through `fm_requisition_safer_state` records `famine_migration_achievement_blockade_predatory_requisition` at the existing owner-local decision transaction.
- The supported player tag-switch commit path marks both the previous player country and the target country before `change_tag_from = PREV`, so the current player cannot continue the country achievement after switching tags.

## Lifecycle and cleanup notes

The new evidence is country-scoped and intentionally persistent for the campaign; it is not a second meter and is not cleared by state retirement. The wasteland hook runs before the existing state cleanup clears food and displacement registrations. The self-route rejection happens before `famine_migration_transfer_civilians_exact` can debit population. No new global array, regular/global event target, daily world scan, or mission was introduced.

## Required producer audit and unresolved blockers

### Protected internment

`famine_migration_achievement_record_protected_internment` remains an API-only recorder. The repository has camp/repression and detention decisions, but none accepts or resolves a famine migration cohort, current host, or exact reception transaction. Calling it from generic camp decisions would be a broad inference and could falsely disqualify an unrelated detainee action. A future owner must call it only after an exact cohort-to-internment transaction proves that the protected cohort was interned.

### Protected forced labor

`famine_migration_achievement_record_protected_forced_labor` remains an API-only recorder for the same reason. Existing forced-labor systems use camp or occupation quotas and do not identify a famine cohort. No safe owner-local producer exists in the current source. The recorder must be wired by the owner of a cohort-aware forced-labor transaction, not by a country-wide scan or by the existence of a generic labor idea/decision.

### Corridor attacked

`famine_migration_achievement_corridor_attacked` remains predicate-only. The current corridor decision targets a controlled state, does not persist a corridor target country/state, and the mission has no attack-target event target. The available `on_war_relation_added` callback therefore cannot prove that a player attack hit the protected corridor rather than another front. A broad “any war while the mission exists” hook would be an invalid false-positive producer. Add this flag only after the corridor owner persists the exact protected state/route and the owner-local combat/war callback can compare that target.

### Country annexation

The country achievement has a core-floor disqualifier and the new tag-switch flag, but no famine owner currently receives an exact annexation callback for the tracked country or its active cohort host. `is_subject = no` and `exists = yes` are live eligibility requirements, not durable proof that annexation never occurred. The annexation disqualifier remains an explicit blocker until the country/war owner provides a scoped annexation transaction producer; do not infer it from a daily scan or from current ownership.

### Exact transfer-cycle history

The implementation records actual conservation failures and rejects exact self-routes, but it does not claim a full visit-history cycle detector. The aligned ledger stores the original origin and current host/destination only. A true repeated A→B→A cycle needs an explicit visit-history field or transaction owner contract; adding a broad scan would violate the system’s ledger boundary.

## Achievement-by-achievement closure

- Break the Blockade: blockade proof, relief, recovery, survival, forced-removal/requisition/concealment, wasteland, and self-route checks remain fail-closed. Wasteland and self-route now have owner-local producers.
- No One Left at the Gate: protected-cohort counting remains tied to successful exact transfers. Internment and forced-labor disqualifiers remain waiting for the two blocked cohort-aware owners above.
- Roads Home: return evidence still requires the validated return and exact transfer; a real residual failure now sets the return-ledger disqualifier.
- Bread Across the Front: manufactured pressure now has two real state-action producers. The attack disqualifier remains blocked until an exact corridor target exists.
- They Were Hungry, Not Contagious: medical reception evidence is unchanged; internment/forced-labor remain explicit blockers rather than inferred from quarantine or camp state.
- A Place at the Table: distinct origins and integrated population remain transaction-backed; residual failures now disqualify through the existing transfer-cycle flag.
- The Grain Stayed Home: extraction, suspension, recovery, and alternative logistics are unchanged; no weight or unrelated balance was changed.
- The Country Did Not Empty: severe-state/floor/recovery/major-cohort evidence is unchanged; the supported player tag-switch path now writes its disqualifier.

## Validation and skipped validation

Task-specific static review confirmed that each newly referenced recorder has one matching definition, the eight registry IDs still resolve to the original scripted predicates, the self-route guard precedes the population debit, and the conservation-failure recorder is reached only from the non-zero-residual branch after an actual debit.

The HOI4 live consumer was not launched. GUI inspection/rendering was not applicable because this patch changes no decision-owned GUI surface. Probability inspection/compare was not run because no weight, score, MTTH, or AI factor changed. The protected-internment, protected-forced-labor, and corridor-attack blockers remain intentionally unresolved and are listed above.

# Corridor attack owner receipt patch

> **Superseded historical identifier banner (2026-08-25):** Any `fm_*` or `famine_migration_*` identifier quoted in this historical handoff is source-snapshot terminology only and is superseded; current authorities use separate `famine_*`, `migration_*`, or narrow neutral `civilian_transfer_*`/`humanitarian_*` names; see [source_of_truth_map.md](../source_of_truth_map.md).

## Scope and result

This bounded owner patch connects the existing `famine_migration_corridor_handle_exact_state_attack` State-scoped consumer to the four project-owned biological, chemical, and operative attack resolvers.

Each call is made only after the resolver has an exact actor-country target and exact target-state target, saves the actor as `event_target:famine_migration_corridor_exact_attacker`, and enters the exact target state.

Failure, no-release, rejected-record, attacker-accident, context-loss, recency, victim, pressure, control, and war-status paths do not emit a corridor attack receipt.

## Files changed

- `common/scripted_effects/biological_raid_effects.txt` adds one target-release receipt at `bio_resolve_strategic_raid_outcome:718-724`.
- `common/scripted_effects/biological_battlefield_effects.txt` adds one primary-release receipt at `bio_resolve_battlefield_dissemination:525-531`.
- `common/scripted_effects/cbrn_chemical_raid_effects.txt` adds one accepted-action receipt at `cbrn_resolve_chemical_air_raid_outcome:321-327`.
- `common/scripted_effects/biological_operation_effects.txt` adds partial and full-success receipts at `bio_operative_release_resolve:180-185` and `:204-209`.
- `docs/plans/famine_and_migration_system_plans/subagent_handoffs/corridor_attack_owner_receipt_patch.md` records this handoff.

No paired markdown file exists for the four owner resolver files, so no dynamic-helper documentation file required an update.

No decisions, events, on-actions, mapmodes, GUI, population/death mutation, AI weights, constants, or source specifications were edited.

No commit was created.

## Helper map

| Helper or owner boundary | Scope | Inputs | Outputs | Side effects | Call site |
| --- | --- | --- | --- | --- | --- |
| `famine_migration_corridor_handle_exact_state_attack` | State | Current exact target state plus regular `event_target:famine_migration_corridor_exact_attacker` | Existing exact attack receipt and corridor disqualification only when the active origin/front contract matches | Saves `famine_migration_corridor_attacked_state`, delegates to the existing idempotent disqualifier, and performs the existing bounded sparse registered-country projection | Biological raid `biological_raid_effects.txt:722-724`; biological battlefield raid `biological_battlefield_effects.txt:529-531`; chemical raid `cbrn_chemical_raid_effects.txt:325-327`; operative release `biological_operation_effects.txt:184` and `:208` |
| `bio_resolve_strategic_raid_outcome` target release owner | RAID_INSTANCE-derived resolver | Existing `var:actor_country` and `var:target_state` event targets plus supplied target-release dispatch proof | One exact corridor attack receipt for a successful project biological strategic release | Saves the actor target immediately before entering the exact target state; all existing biological release, contamination, history, and cleanup effects remain owner-controlled | `biological_raid_effects.txt:715-731` |
| `bio_resolve_battlefield_dissemination` primary release owner | RAID_INSTANCE-derived resolver | Existing `var:actor_country` and `var:target_state` event targets plus supplied primary-release dispatch proof | One exact corridor attack receipt for a successful project battlefield dissemination | Saves the actor target immediately before the exact target-state helper; friendly blowback, history, and existing consequence dispatch remain unchanged | `biological_battlefield_effects.txt:522-543` |
| `cbrn_resolve_chemical_air_raid_outcome` accepted action owner | RAID_INSTANCE-derived resolver | Existing actor/target event targets plus `cbrn_action_result = constant:cbrn_action_result.accepted` after the shared preparation contract | One exact corridor attack receipt for an accepted release-bearing chemical action | Saves the actor target and calls the exact target-state helper before the existing shared chemical dispatcher; rejected records still use the existing failed-attempt path | `cbrn_chemical_raid_effects.txt:308-334` |
| `bio_operative_release_resolve` partial/full release owner | Operation scope | `ROOT`, `FROM`, and `FROM.FROM` saved as actor, victim, and exact target state plus supplied seed-dispatch proof | One exact corridor attack receipt for each successful partial or full operative release | Saves the exact actor within the exact target-state scope; existing attempt history, failure conversion, and tooltip branches remain unchanged | `biological_operation_effects.txt:159-221` |

## Exact attack semantics

The biological strategic raid receipt is limited to `bio_strategic_raid_outcome_has_target_release = yes` followed by `bio_raid_release_dispatch_status = constant:bio_lifecycle_proof.supplied`.

The no-release branch records only a failed attempt, the attacker-accident branch is deliberately excluded, and a target-release dispatch failure is deliberately excluded.

The biological battlefield receipt is limited to the non-no-release branch after `bio_battlefield_dispatch_primary_release_internal = yes` returns `bio_battlefield_dispatch_status = constant:bio_lifecycle_proof.supplied`.

The no-release and primary-dispatch-failure branches remain receipt-free.

The chemical receipt is limited to `cbrn_action_result = constant:cbrn_action_result.accepted` after `cbrn_prepare_chemical_action_record = yes` validates the exact actor, target, payload debit, protection, release, and victim contract.

The helper call intentionally precedes the existing `cbrn_dispatch_chemical_action_record` call at this accepted owner boundary, while the dispatcher remains the sole owner of chemical exposure, unit damage, civilian deaths, contamination, evidence, attribution, and history mutation.

Rejected release records continue through `cbrn_chemical_air_raid_convert_rejected_release_to_attempt_internal` and `cbrn_dispatch_failed_chemical_air_raid_attempt` without a receipt.

The operative receipt is limited to the partial and full-success branches after `bio_operative_release_dispatch_seed_internal = yes` supplies `bio_seed_dispatch_status`.

The failure branch, dispatch context loss, and every non-supplied seed dispatch remain receipt-free.

The shared helper itself still compares the exact callback state and saved actor against the persisted active corridor contract before setting proof, reason, date, terminal status, or cleanup.

## Constants and tuning

No new constants or tuning values were added.

The owner gates reuse the existing `bio_lifecycle_proof.supplied`, `bio_lifecycle_result`, and `cbrn_action_result.accepted` contracts.

No probability-bearing value, AI score, random-list weight, MTTH value, threshold, or duration was changed, so no probability inspection was required.

## Event targets and cleanup

The four owners reuse their existing regular event targets: `bio_raid_actor`, `bio_raid_target_state`, `bio_battlefield_actor`, `bio_battlefield_target_state`, `cbrn_action_actor`, `cbrn_action_target_state`, `bio_operation_actor`, and `bio_operation_target_state`.

Each accepted owner branch saves the exact actor to regular `event_target:famine_migration_corridor_exact_attacker` immediately before calling the State-scoped helper.

No global event target, target registry, recurring hook, or manual target clearing was added.

The existing corridor helper owns `famine_migration_corridor_attacked_state` persistence, exact origin/front matching, receipt proof, disqualification, and terminal cleanup.

## Migration from duplicated or missing receipt logic

Before this patch, the four owner resolvers recorded their own successful release or action outcomes but did not notify the shared corridor attack consumer.

The patch adds one narrow owner call per authoritative biological strategic release, biological battlefield release, and chemical accepted action, plus one call for each operative partial/full release branch.

Existing no-release, failed-delivery, rejected-action, attacker-accident, and context-loss logic is unchanged.

Existing `common/on_actions/chaosx_famine_migration_on_actions.txt` native exact callbacks remain unchanged because they already call the same helper for naval invasion, paradrop, and nuclear attack boundaries.

No generic combat, strategic-bombing, war-status, controller-loss, pressure, victim, or date-recency adapter was introduced.

## Validation and evidence

- Read `AGENTS.md`, the complete `chaos-redux-subagents` and `chaos-redux-state-ledgers` skills, all eight famine/migration specification parts, the achievement prompt, the improvement closure review, the corridor attack exploration handoff, and the existing corridor effects/on-actions before editing.
- Read the required offline Paradox wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on-actions, event modding, decision modding, idea modding, AI modding, and the raid/scope/effect references used by this owner boundary.
- Read vanilla `common/raids/_documentation.md`, `common/on_actions/00_on_actions.txt`, `documentation/effects_documentation.md`, and `documentation/triggers_documentation.md` for RAID_INSTANCE variables, exact callback scopes, event targets, and the limits of recency/combat proxies.
- PowerShell source inspection confirmed five new helper call sites, each paired with the actor save and exact target-state scope; no call appears in a failure or no-release branch.
- PowerShell brace accounting returned final depth zero with no underflow for all four changed owner files.
- `git diff --check` returned no whitespace errors for the four changed owner files.
- A narrow read-only `hoi4_event_inspect` state-flow pass for selector `{kind:event,eventId:chaosx.nr19.1}` returned `EVENT_INSPECTED_PARTIAL`, zero blocking diagnostics, and artifact `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c412babbd400c173d2d74f32dae0f3f9442cc138a13c6e02113bbd08b9bc4579/d9a659058d57b12e710bb85447f9a581b4c39fbada1eb7a8deeaf39fb8e7b95d/event-state_flow-655620ee867d.json`.
- The event inspector reported `MCP_INLINE_FILES_TRUNCATED` and deferred workspace-wide helper/lifecycle projections, so the artifact is structural event evidence only and does not validate these raid/operation resolver files.
- The matching narrow `hoi4_event_render` scope request timed out after 180 seconds with no render artifact; raid and operation owner effects have no dedicated event MCP surface.
- No live Hearts of Iron IV run was performed.

## Known gaps and blockers

- Ordinary land combat still has no exact project-owned callback carrying both the attacked state and responsible attacker country, so it remains unwired.
- Ordinary strategic bombing still exposes only state-local recency or victim aftermath, so it remains unwired.
- These owner receipts are conclusive only when the existing corridor contract is active and the shared helper's exact origin/front and requester matching succeeds; they do not create or repair that contract.
- The event MCP route cannot inspect generic RAID_INSTANCE or operation owner effect graphs directly, and the matching event render timed out; parent review must treat the source and owner-scope evidence above as the applicable validation.
- Dynamic `var:<state_or_country_id>` scope resolution and live save/reload behavior still require parent-owned engine validation.

## Parent follow-up

Review the five callsites and the accepted-release semantics against the parent-owned corridor contract, then perform the normal source reload and live consumer validation.

# Stage 7 biological raid decision and mission audit handoff

Date: 2026-07-15
Scope: strategic biological raid staging, native raid definitions, and their owned resolver surface.

## Result

Three bounded resolver defects were corrected in `common/scripted_effects/biological_raid_effects.txt`. No lifecycle, localisation, asset, shared CBRN, or zombie-cure file was changed.

## Changed files and identifiers

| File | Identifiers | Change |
|---|---|---|
| `common/scripted_effects/biological_raid_effects.txt` | `bio_strategic_raid_refund_payload_internal` | Refunds now restore the four exact produced equipment models: `anthrax_bomb_1`, `plague_bomb_1`, `tularemia_bomb_1`, and `smallpox_bomb_1`. |
| `common/scripted_effects/biological_raid_effects.txt` | `bio_strategic_raid_apply_failed_attempt_condemnation_internal` | Chaos Warfare doctrine applies its Condemnation multiplier only after the failed attempt has evidence-based attribution (`suspected`, `discovered`, or `public`). Evidence, deaths, contamination, and history remain untouched. |
| `common/scripted_effects/biological_raid_effects.txt` | `bio_strategic_raid_record_rejected_reservation_loss_internal`, `bio_resolve_strategic_raid_outcome` | Replaced the full-refund context-rejection path. A native raid whose context becomes invalid after creation now records the entire already-collected essential payload as physical loss, with no fabricated release, use history, retaliation trigger, or refund. |

## Before and after behavior

1. A completed native reservation could enter the resolver after a target, policy, or staging-context change and be fully returned. This was a payload-farming path. It is now fail-closed: the payload is lost and recorded in `bio_strategic_raid_payload_consumed_total`, `bio_strategic_raid_context_rejected_payload_lost_total`, and `bio_last_strategic_raid_rejected_payload_lost`.
2. Partial failed-delivery refunds named equipment archetypes, while the produced payloads are level-one equipment models. Refunds now match the precise reservation models.
3. Terminal Hazard or Theater Contamination could lower a hidden failed-attempt Condemnation source before the attempt had generated attribution. The multiplier now remains one for hidden attempts and is considered only after evidence produces attribution.

## Audit findings, sorted by severity

### Critical, fixed

- `bio_strategic_raid_rollback_rejected_reservation_internal` fully refunded native `essential_equipment` after a later context rejection. Native raid documentation states essential equipment is collected at raid creation, so the resolver could not prove that it remained unused. The replacement accounts for total physical loss instead of refunding it.

### High, fixed

- `bio_strategic_raid_refund_payload_internal` passed `*_bomb_equipment` archetypes to `add_equipment_to_stockpile`, despite the equipment definitions producing `*_bomb_1` models. This conflicted with exact reservation/refund accounting.

### Medium, fixed

- `bio_strategic_raid_apply_failed_attempt_condemnation_internal` selected the Chaos Warfare doctrine multiplier before evidence-derived attribution visibility. This allowed doctrine to suppress a hidden source. The multiplier now occurs only after attribution, without changing the evidence record.

### Low, resolved by parent integration

- The initial audit found that a staging-complex flag on a captured state could remain until redesignation. Parent integration added an exact `on_state_control_changed` cleanup. The state is saved as a regular event target before entering the actor scope, so the marker, actor pointer, and loss history are cleared only for the exact transferred state. No periodic scan was added.
- No direct focus-tree unlock reference was found for this surface. The present route is special-project plus CBRN-policy progression. A bespoke focus integration would be a cross-surface design choice, not a bounded raid/decision correction.

## Decision category lifecycle notes

- `bio_designate_strategic_raid_staging_state` selects an exact controlled state, records its owner and designation date, removes the prior actor-owned staging marker on relocation, and applies the 90-day relocation cooldown.
- Availability revalidates the selected staging state. It does not infer an airfield or use an aircraft proxy. It requires a controlled, non-impassable state with the configured air-base and infrastructure floors.
- The category uses existing custom trigger-tooltip keys rather than exposing the long staging requirement directly. Localisation was not edited or reworded under this scope.

## Native raid and mission-quality notes

This surface has no HOI4 mission template. It contains four native raid types, each with the same lifecycle contract:

| Owner and category | Target and region | Requirement and duration | Success / failure | Duplicate risk |
|---|---|---|---|---|
| Actor country, CBRN raid category | Native `var:target_state`, while an attacker accident uses only the actor's designated staging state | Exact essential payload, project, policy, staging, aircraft, and selected-target gates with 21 to 45 preparation days by agent | All four native engine outcomes call `bio_resolve_strategic_raid_outcome` once. Actual releases dispatch once into the biological lifecycle. Failed delivery creates exact-state evidence and Condemnation without use or contamination. Attacker accident dispatches only to staging. | 16 call sites, with four outcomes for each of four raids. No second resolver, aircraft hook, or periodic release path was found. |

The ordinary agents remain distinct from `common/raids/biological_zombie_cure_raid.txt`. The cure raid does not call `bio_strategic_raid_*` or `bio_lifecycle_dispatch_seed`.

## Cost and requirement clarity

- Essential payload requirements are differentiated and match the native raid definitions: anthrax 200, plague 100, tularemia 100, smallpox 50.
- Command-power costs and preparation windows vary by agent (10/28, 15/35, 8/21, and 25/45) rather than forming a flat exchange.
- The staging decision cost and cooldown use named script constants. The intentionally unusual native disaster reliability formula remains `weight = 0` and `start_weight = 0.12`.
- Player and AI gates use exact project, policy, war, subject/faction, selected target-state, staging, and payload conditions. No fallback, proxy, estimator, or broad periodic pulse was found.

## AI validity and route-lock notes

- All four raid `ai_will_do` blocks use `bio_strategic_raid_ai_may_target_from`. That shared gate requires the same preparation route and policy gate as the player, rejects invalid diplomatic targets, and limits routine AI use to safe countermeasure states or the documented desperate exception.
- The route checks retaliation, prior victim use, permitted first use, and Japanese-China context before allowing a target. It does not select dead countries, closed routes, faction partners, subjects, invalid target states, or stale staging locations.

## Localisation, tooltip, GUI, and cleanup notes

- No localisation was changed. Existing decision and raid files reference custom tooltip keys. Wording was not audited or modified because localisation is outside the granted surface.
- No scripted GUI button belongs to this raid surface. The only related interface evidence is the static raid sprite registration, so no GUI inspection or rewrite was applicable.
- Failed-attempt evidence decays through the scheduled state event in the lifecycle event file, not through a country-wide pulse. Rejected native contexts now retain audit variables without creating biological-use history.

## Validation

- Read the accepted Stage 7 specification, biological countermeasure matrix, AI matrix, and lifecycle plan. Consulted the offline Paradox wiki core pages plus Decision Modding and installed vanilla raid/decision documentation and raid precedents.
- Static contract check passed for four exact refund models, context-rejected reservation consumption, 16 resolver calls across four four-outcome raid definitions, preserved disaster reliability constants, zombie-cure separation, absence of a broad periodic pulse, and native exact target and staging gates.
- Reviewed the native essential-equipment contract against the installed raid documentation and the payload model definitions.

## Skipped validation

- No live-engine raid was executed. Exercising a mid-preparation target/staging/policy invalidation requires a running HOI4 session and was not available in this bounded source audit.
- Localisation rendering and GUI rendering were not run: neither surface was in scope and the raid exposes no scripted GUI control.

## Completion and follow-up

No in-scope simplifications were made. Parent integration resolved the staging-marker finding with the exact-state `on_state_control_changed` hook in `common/on_actions/chaosx_on_actions.txt` and `bio_strategic_raid_cleanup_staging_after_control_change`. The helper saves the transferred state as a regular event target before entering the actor scope. It clears the lost state's marker immediately and clears the former actor's stored pointer only when that pointer still names the same state. No periodic country or world scan was added. Direct focus integration is not required because the accepted route is the matching special project plus use-policy authority.

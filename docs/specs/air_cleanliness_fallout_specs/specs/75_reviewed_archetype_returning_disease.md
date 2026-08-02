# Reviewed Fallout archetype chain: The Returning Disease

## Identity and ownership

The Returning Disease is the next dormant Quarantine State chain in the Fallout scheduler. It is candidate 712, transaction key 710073, route 7178, and Event Log history 9179. It owns event ids `chaosx.fallout.712` through `chaosx.fallout.718`, scripted effects and triggers with the `fallout_event_712` namespace, a dedicated report-event sprite, and the cause-memory flags listed below. Fallout itself remains a consequence and does not receive an ordinary Event Log entry, evolution, or super-event registration.

## Admission

The candidate follows a closed Doctor's Coup memory in one current native state. The state must still be controlled by the native country, have durable survival identity, resource, and Supply Access rows, and carry Air Winter Shelter Capacity at least 18, Supply Access at least 12, Adaptation at least 10, Exposure from 8 through 89, Disease Pressure from 22 through 89, and a live Air Winter phase. The state must have population above the minimum contract and must not be in a controlled evacuation project.

The owner must be a current Quarantine State with public health at least 35, grievance at least 1, Medicine at least 8, Cohesion at least 25, Recognition at least 10, and a campaign day from 900 through 5199. The request coordinator rejects reserved, committed, pending, or closed candidate rows and refuses countries that cannot afford at least one branch. State identity, owner, controller, generation, and every delayed receipt are revalidated before resolution.

## Opening choices and costs

1. **Seal the infected district** spends Food 2, Medicine 3, and Recognition 2. It emphasizes shelter and exposure relief while imposing a small Supply Access loss and a larger border-trust cost.
2. **Send targeted care teams** spends Medicine 4, Fuel 2, and Recognition 2. It gives the largest disease reduction and protects treatment capacity at the cost of Fuel, Cohesion, and inspection fatigue.
3. **Request the aid convoy** spends Food 2, Scrap 1, and Recognition 3. It opens a witnessed border compact and raises the chance of medicine and Supply Access recovery while increasing aid dependence when the settlement is partial.
4. **Keep the outbreak off the books** spends Medicine 2, Fuel 1, and Power 2. It can preserve shelter, adaptation, and reclamation in the short term, but it raises the concealment ledger and has the most damaging failure memory.

The human opening is event 712. The hidden AI opening is event 713. AI uses the same affordability, generation, target, and transaction checks as the human lane and ranks targeted care, aid, concealment, and lockdown through the event-specific constants.

## Deterministic result grading

The scheduler snapshots the target state and country ledgers before charging a branch. The grade combines Supply Access, Shelter Capacity, Adaptation, relief from Disease Pressure and Exposure, Medicine, Recognition, Treatment Capacity, and relief from Aid Dependence. A Quarantine State receives the small government match defined in the constants. Branch-specific success and partial thresholds are 55 and 34 for lockdown, 62 and 40 for targeted care, 58 and 36 for aid, and 48 and 30 for concealment. Values below the partial threshold fail.

Event 714 resolves the human result and event 715 resolves the hidden AI result. Success, partial, and failure each write Air Winter changes to the target state, Medicine and Recognition resource changes, public health, grievance, Treatment Capacity, Border Trust, Aid Dependence, Concealment Pressure, and Cause Memory. Failure damages one infrastructure building level and sends a bounded population-loss request through the Deaths system. The request is capped by the Deaths contract and keeps the documented minimum population alive.

## Delayed callback and cleanup

The result is scheduled exactly 24 days after the opening receipt. The result lane records the selected branch and outcome in Event Log history 9179, applies a short-lived dynamic modifier, and schedules the callback exactly 210 days later. Event 716 presents the callback to a human player. Event 717 resolves the same callback for AI countries. The callback score uses public health, Cohesion, Recognition, Treatment Capacity, Border Trust, Cause Memory, Supply Access, Reclamation, Disease Pressure, Grievance, Aid Dependence, and Concealment Pressure.

Callback success, partial, and failure update all five state ledgers, apply another Air Winter disease modifier, and write one of the durable branch memories. Callback failure uses the Deaths system with its own lower loss contract. Event 718 releases the delayed cleanup ticket idempotently, clears reserved and committed state flags, clears receipts and temporary deltas, preserves the durable cause memory, and records a cancelled result when any receipt becomes invalid.

## Durable memory

The chain preserves one of these country flags without changing the country tag or government archetype: `fallout_returning_disease_lockdown_memory`, `fallout_returning_disease_targeted_response_memory`, `fallout_returning_disease_aid_compact_memory`, or `fallout_returning_disease_concealment_memory`. Partial branches use the corresponding `_contested` flag. Failure uses `fallout_returning_disease_outbreak_uncontained`. These memories are intended for later diplomacy, recovery, character, and Year 10 order chains.

## Asset and localisation

The dedicated fictional report illustration is `GFX_report_event_fallout_returning_disease`, registered in `interface/fallout_consolidated.gfx` and backed by `gfx/event_pictures/fallout/report_event_fallout_returning_disease.dds`. Source, processed PNG, DDS hashes, prompt record, and handoff notes live under `docs/assets/712_returning_disease/`. All player-facing text names Ash Ward Hospital, North Gate clinic, the eastern checkpoint, the aid convoy, and the relevant ledger rather than using generic apocalypse wording.

## Dormancy and future links

The row is dormant until the Fallout scheduler opens candidate 712. It is designed to feed a later border-inspection crisis, health certification chain, aid compact, generation-change chain, and recovery-year opening of the sealed city. Those chains remain separate candidates and are not silently bulk-generated here.

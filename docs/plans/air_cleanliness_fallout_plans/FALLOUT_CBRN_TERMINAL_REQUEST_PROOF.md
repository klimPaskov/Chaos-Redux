# Fallout CBRN terminal request proof

## Scope

This proof records the concrete chemical and biological terminal callers that now submit Fallout through the existing idempotent request coordinator. Fallout remains a consequence transition. These callers do not create a Fallout Event Details row, evolution, ordinary super-event, or public scenario-catalog entry.

## Chemical terminal caller

`chem_unleash_stockpile_doomsday` in `common/scripted_effects/chemical_ability_effects.txt` is the stockpile doomsday decision resolver. After it consumes the four chemical payload types, applies the state contamination and unit damage, records the doomsday condemnation source, and completes treaty handling, it saves the releasing country as `fallout_request_actor_input` and submits `fallout_request_source.chemical_saturation` with terminal intensity to `fallout_request_aftermath`.

The caller does not set `world_end`, does not write a public Fallout identity, and does not bypass the shared request ledger. The coordinator validates the explicit chemical source without requiring Air Contamination or Chaos above 1000. A request that races another terminal source is admitted only if the one shared ledger remains free.

## Biological terminal caller

`bio_doomsday_register_batch_consequence` in `common/scripted_effects/biological_doomsday_effects.txt` runs only after the complete doomsday release has seeded the eligible domestic and adjacent enemy-front state array and recorded the public biological consequence. It saves the releasing country as `fallout_request_actor_input` and submits `fallout_request_source.biological_follow_through` with terminal intensity to the same `fallout_request_aftermath` coordinator.

The biological caller shares the same world-end exclusion and idempotent ledger gate. Partial seed resolution is still recorded by the biological subsystem, while Fallout cause memory records the accepted biological request only when the coordinator admits it.

## Boundary and remaining proof

The source enum also retains `mixed_terminal` for a future authored mixed cause. No mixed caller is inferred from two independent requests, because that would make source selection order-dependent. The existing Final Silence, Strategic Singularity, gradual Air Contamination, and manual scenario callers remain unchanged.

Static inspection proves the two CBRN callers enter one coordinator and provide actor, cause, and intensity inputs. Runtime validation of host authority, save recovery, blackout input blocking, and the exact manual native province sweep remains outside this proof. No alternate event path or variable-only Fallout substitute is claimed.

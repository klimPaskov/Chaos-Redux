# Event 006 nested execution counter-frame repair — 2026-09-01

## Disposition

`PATCHED / SOURCE-LEVEL EXECUTION HARDENING`.

The standalone and Event 005 + Event 006 joint callers now seed the Event 006 finalizer counters before invoking nested scripted effects. This preserves the package preparation, activation, validation, and initialization results across the nested return so the commit barrier can evaluate the actual release transaction.

This is a narrow execution-frame repair. It does not widen package admission, change the automatic ladder, alter reservation or host-survival rules, add a fallback country, change costs, or restore any pre-event Independence Wave surface.

## Evidence and reason for the patch

The offline `paradox_wiki/Data structures - Hearts of Iron 4 Wiki.md` temporary-variable section documents that a temporary variable created only inside a nested scripted effect may not remain available to the caller, while a temporary variable seeded by the caller is carried into and back from the nested effect.

`independence_wave_prepare_finalizer_frozen_country_origins` writes `independence_wave_execution_prepared_count`, `independence_wave_execution_activated_count`, and `independence_wave_execution_validated_count` through nested package passes. `independence_wave_finalize_frozen_country_origins` writes `independence_wave_execution_initialized_count` through another nested pass. The standalone caller previously seeded only the instantiated, state-transfer, transfer-failure, and validated counters before calling those effects. The joint caller likewise seeded the validated counter but not the other Event 006 finalizer counters.

When the outer caller tested `independence_wave_execution_initialized_count` after the nested finalizer returned, the value could therefore be undefined in the caller frame even when every package had committed its origin. That leaves the plan in finalization failure instead of reaching the committed release path, which is consistent with a console Event 006 invocation creating no visible countries.

## Source changes

- `common/scripted_effects/006_independence_wave_execution_effects.txt`
  - Seeds `independence_wave_execution_prepared_count`, `independence_wave_execution_activated_count`, and `independence_wave_execution_initialized_count` at the standalone execution barrier before `independence_wave_prepare_finalizer_frozen_country_origins` and `independence_wave_finalize_frozen_country_origins` run.

- `common/scripted_effects/005_006_liberations_collision_effects.txt`
  - Seeds the same three Event 006 finalizer counters in the joint execution caller before the shared finalizer chain.

The existing Event 032 missile-inheritance additions in these files are unrelated concurrent work and are not part of this repair.

## Validation

Focused Event 006 validators passed after the patch:

- allocator: 149 publishers, 40 runtime adapters, 32 content attestations, 29 compatible groups, exact 3/4/5/7/10 ladder, and the 20-package static witness;
- country API: 242 broad tags, 191 resolved carriers, zero missing or duplicate carriers;
- strict flag-family audit: 102 complete families;
- FORM-16 contract audit;
- SCN-008 matrix: all 32 scenario cells and eight edge cases;
- Statehood Ledger GUI semantic source matrix.

No live Hearts of Iron IV process or save/load session was run. Event MCP remains partial and cannot by itself certify nested helper execution or live country materialization.

## Remaining boundary

The source fix does not prove a live release. A user-supplied terminal receipt is still required to distinguish allocator selection, country instantiation, state transfer, and finalization in a running save. The current 32/29/40/161 admission boundary and HOLD / PARTIAL whole-event disposition remain unchanged.

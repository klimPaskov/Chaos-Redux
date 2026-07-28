# Event 006 league expulsion evidence helpers

## `independence_wave_record_league_expulsion_ground`

Country-scope writer for the DM-60 charter case. Callers invoke it only at a
factual transaction point while the country is an active league member under
the anti-puppetry charter and the formal, durable, or reformed league phase.

Inputs:

- temporary `independence_wave_expulsion_ground_input`: one value from
  `constant:independence_wave_expulsion_ground`;
- temporary `independence_wave_expulsion_has_target_input`: zero or one;
- when the target input is one, temporary
  `independence_wave_expulsion_evidence_target_input` is a surviving country
  scope to persist as the secondary witness.

Outputs and side effects:

- increments the accused country's `independence_wave_charter_violation_count`;
- writes `independence_wave_expulsion_ground`,
  `independence_wave_expulsion_ground_date`, and the optional persistent
  country-scope witness variable;
- sets `independence_wave_expulsion_ground_recorded` and clears any prior
  resolved marker;
- promotes the current ground to
  `constant:independence_wave_expulsion_ground.repeated_charter_violation`
  once the threshold in
  `constant:independence_wave_decision_gate.repeated_charter_violation_threshold`
  is reached.

Current call sites:

- patron-client route selection after a strict charter member locks that route;
- `on_annex` before the victim country is removed;
- `on_war_relation_added` when a defensive-charter member starts an external
  war (civil-war participants are excluded);
- DM-43 refusal response;
- DM-44 cancellation while its threatened member remains at war;
- DM-61 sponsored member coup.

## `independence_wave_expel_league_member`

DM-60 resolution helper. It requires the active factual-case flag, marks the
case resolved, unregisters the aligned league member/founder rows, preserves
the network and Event 006 origin, and applies the existing discredited-member
idea lifecycle.

## `independence_wave_clear_league_expulsion_case`

Generation cleanup for the case flag, repeated marker, ground/date, secondary
target pointer, and violation count. It is called by Event 006 generation
reset and origin termination, never by a periodic world action.

## `independence_wave_clear_binding_arbitration_request`

Clears the DM-43 pending requester pointer, request date, pending flag, and
refusal marker. DM-43 uses it on success/cancellation; Event 006 cleanup uses
it as a stale-pointer guard.

## `independence_wave_start_sponsored_member_coup`

Target-country helper for DM-61. It starts a vanilla `start_civil_war` revolt
using the target's current government to select the opposing ideology and a
central `independence_wave_decision_coup.revolt_size` value injected by
`meta_effect`. It does not spawn free sponsor units or run a world scan.

## `independence_wave_revalidate_reclamation_front_operation`

Country-scope lifecycle guard for the active DM-58 operation. It is called after
the generation-matched league row is removed by
`independence_wave_unregister_league_member`.

Inputs:

- the persistent global `independence_wave_reclamation_fronts_coordinated`
  operation flag;
- the aligned `global.independence_wave_league_member_*` registry and its
  current member count;
- the frozen `global.independence_wave_reclamation_front_members` witness array.

Outputs and side effects:

- invokes `independence_wave_cleanup_reclamation_front_operation` when the
  league drops below the formation minimum or the exiting country is a recorded
  witness member;
- clears the shared operation flag, coordinator target, state receipts,
  readiness fields, and frozen witness arrays through the shared cleanup path;
- deliberately leaves already-issued finite `take_state_focus` war goals to
  their own timed expiry and never manufactures replacement targets.

The witness-array membership check is generation-safe for the single active
operation because the array is rebuilt only by the current-generation DM-58
resolver and is cleared by every operation reset path.

# Event 006 league-expulsion grounds handoff

Date: 2026-07-22  
Scope: DM-60 factual expulsion evidence and the accepted grounds that can be
witnessed without a periodic world scan.  This handoff records the narrow
scripted-system implementation; it does not promote Event 006 to overall
completion.

## Implementation result

DM-60 no longer infers a case from client status.  It consumes
`independence_wave_expulsion_ground_recorded`, which is written by
`independence_wave_record_league_expulsion_ground` only at a transaction or
targeted decision surface.  The accused country owns the ground enum, date,
violation count, optional surviving witness pointer, and resolved marker.

| Accepted ground | Factual writer | Evidence owner / witness | Strict charter gates |
| --- | --- | --- | --- |
| host proxy / patron capture | `independence_wave_select_government_route` patron-client branch | accused member; no secondary target survives | anti-puppetry + formal/durable/reformed phase |
| annexing a League member | `on_annex` (`ROOT` winner, `FROM` victim) before victim cleanup | annexer; victim is intentionally not persisted | anti-puppetry + both active member flags |
| refusing binding arbitration | DM-43 completion writes pending requester; `independence_wave_refuse_binding_arbitration` target response records refusal | refusing member; requester pointer is persisted as witness | arbitration pillar + requester still active/compliant |
| abandoned rescue obligation | DM-44 cancel while target remains at war | rescuing member; threatened member pointer | target active member and still at war |
| repeated charter violation | helper promotes the second factual write | same accused member; latest witness replaces prior pointer | threshold `constant:independence_wave_decision_gate.repeated_charter_violation_threshold` |
| sponsoring a coup in another member | DM-61 `independence_wave_sponsor_member_coup` | sponsor; target pointer | anti-puppetry + target active non-client member, no existing civil war/war |
| unauthorized war under defensive charter | `on_war_relation_added` (`ROOT` attacker, `FROM` defender) | attacker; defender pointer | anti-puppetry + mutual-defense pillar + defensive-congress route; civil wars excluded |

The annexation and war hooks are event-driven. No `on_daily`, `on_weekly`, or
world iteration was added.

## Helper map

### `independence_wave_record_league_expulsion_ground`

- Scope: country (the accused member).
- Inputs: temporary `independence_wave_expulsion_ground_input`; temporary
  zero/one `independence_wave_expulsion_has_target_input`; optional temporary
  `independence_wave_expulsion_evidence_target_input` country scope.
- Outputs: increments `independence_wave_charter_violation_count`; writes
  `independence_wave_expulsion_ground` and
  `independence_wave_expulsion_ground_date`; sets
  `independence_wave_expulsion_ground_recorded`; stores/clears the optional
  witness pointer; promotes the enum and marker to repeated violation at the
  central threshold.
- Side effects: clears `independence_wave_expulsion_resolved` so a new factual
  breach opens a new voteable case.
- Call sites: patron route helper, `on_annex`, `on_war_relation_added`, DM-43
  refusal response, DM-44 abandonment branch, DM-61 coup decision.

### `independence_wave_expel_league_member`

DM-60 resolution now requires the factual case flag, marks it resolved, clears
the active-case flag, unregisters the member/founder ledger rows, leaves the
network and Event 006 origin intact, and applies the existing discredited
member lifecycle.  The target trigger additionally rejects resolved cases.

### Cleanup helpers

`independence_wave_clear_league_expulsion_case` clears case flags, ground/date,
violation count, and the witness pointer during generation reset and origin
termination.  `independence_wave_clear_binding_arbitration_request` clears the
DM-43 pending/refusal flags, requester pointer, and request date on success,
cancellation, refusal response, and origin cleanup.

### `independence_wave_start_sponsored_member_coup`

DM-61 pays a security-standard material cost, then invokes the documented
vanilla `start_civil_war` effect through `meta_effect` with a central
`independence_wave_decision_coup.revolt_size` value.  The opposing ideology is
selected from the target's current government.  The effect does not grant
free sponsor units, store political power, or run a world scan.

## Constants and tuning

`common/script_constants/006_independence_wave_decision_constants.txt` adds:

- `independence_wave_expulsion_ground` integer enum (`none`, seven factual
  grounds, and `repeated_charter_violation`);
- `independence_wave_decision_gate.repeated_charter_violation_threshold = 2`;
- `independence_wave_decision_coup.revolt_size = 0.35`.

DM-61 uses the existing security-standard manpower, army-experience,
infantry-equipment, and support-equipment cost helpers and the major decision
cooldown.  DM-43 refusal uses diplomatic-light cost.  AI is very-low for the
coup (with a radical-route modifier) and escalates DM-60's weight for recorded
and repeated cases.

## Target and variable lifecycle

Surviving witnesses are stored as normal country-scope pointers because they
must remain readable after the originating effect block.  The annexed victim
is not stored: the `on_annex` callback runs before removal, but no stable target
exists afterward.  DM-43's requester pointer is held only while the response
decision is visible; the response clears pending/request/date while leaving the
refusal marker for the requester-side cancellation branch, which applies the
league loss and then clears it.  If an origin is destroyed without that branch,
the target marker can remain physically present, but the refusal-target trigger
requires an active/compliant requester, so it is not actionable; generation and
origin cleanup also clear the local request state.

## Rival-bloc boundary

The accepted text mentions a possible rival bloc after expulsion.  The current
`independence_wave_split_league_after_expulsion` helper only changes the
Event-006 phase flags and has no call site or faction-template contract.  No
cosmetic rival flag was added.  A genuine rival bloc still needs an engine-safe,
route-controlled faction template, membership wiring, and cleanup ownership;
that work remains explicitly unresolved rather than being represented by a
cosmetic outcome.

## Files changed

- `common/decisions/006_independence_wave_decisions.txt`
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.md`
- `common/scripted_localisation/006_independence_wave_decision_scripted_localisation.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- this handoff

## Validation and limitations

- Offline wiki and vanilla documentation consulted for event targets,
  `on_annex`, `on_war_relation_added`, decision targets/cancellation, script
  constants, meta effects, and `start_civil_war`.
- Targeted repository searches confirmed one helper definition per new name and
  all seven ground call sites, plus DM-60/DM-61 localisation and matrix rows.
- `hoi4.event_inspect` was attempted against the Event 006 source, but the
  installed analyzer expands the repository to 101,724 event nodes and returns
  its fixed `EVENT_NODE_LIMIT` error before producing an artifact.
- No live HOI4 save/runtime load was available in this subtask; engine parsing
  and dynamic decision visibility therefore remain unverified.  Parent review
  should retain the known rival-bloc blocker and the stale-refusal-marker guard
  in the completion report.

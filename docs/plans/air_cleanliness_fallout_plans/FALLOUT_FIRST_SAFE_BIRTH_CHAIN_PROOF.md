# Fallout First Safe Birth chain proof

## Scope

This tranche implements a dormant country-level generation-change incident in
`events/fallout_world_end_events.txt` under `add_namespace = chaosx.fallout`.
It is owned by candidate `282`, transaction key `710014`, route `7114`, and
Event Log history `9119`.

## Static implementation evidence

- Events `282` through `288` are defined once. The seven blocks are one human
  opening, one hidden-AI opening, one human delayed result, one hidden-AI
  delayed result, one human callback, one hidden-AI callback, and cleanup.
- The candidate producer admits the row only when the Fallout country registry,
  survival identity, durable resource row, campaign window, Cohesion, Medicine,
  Shelter, and one affordable branch are current. It stores no state or actor
  target.
- The opening freezes country Deaths, Cohesion, Medicine, Shelter, Recognition,
  and exposure. The result is due after 21 days. The callback is due after 180
  days. Human visible costs are three for the opening and one for each delayed
  visible receipt. Hidden-AI rows use zero visible cost.
- Four authored branches use public celebration, private protection, civic
  campaign, and elders' rite. Each branch has success, partial, and failure
  results with resource, Cohesion, stability, war support, manpower, exposure,
  generation-count, memory, and modifier consequences.
- Result and callback failure population requests use
  `apply_exact_state_civilian_population_loss` through the shared Deaths
  contract. The result rate is `0.0015` and the callback rate is `0.0008`.
- Result and callback history entries use the shared Event Log writer with
  fifteen payloads. History `9119` is registered in the type selector, name
  selector, and detail selector.
- Cleanup releases the exact issued result and callback receipts, prepares the
  result cleanup after callback release, retains durable memory flags, and
  clears transaction variables and transient flags.
- The dedicated report image is at
  `gfx/event_pictures/fallout_world_end/report_event_fallout_first_safe_birth.dds`.
  Its sprite is `GFX_report_event_fallout_first_safe_birth` in
  `interface/fallout_world_end.gfx`.

## Review boundary

The scheduler activation flags remain without setters. No gameplay caller can
issue this candidate while the numerical contract review lanes are closed.
The event, save-recovery, host-authority, multiplayer, and runtime Event Log
surfaces have not been observed because HOI4 was not launched. The chain is
therefore implemented and statically wired, yet dormant and uncounted toward
the 660-block release floor.

A refreshed read-only `hoi4.event_inspect` lint request targeted
`chaosx.fallout.282` with helper expansion disabled and traversal bounded to 40
nodes, 80 edges, and depth 2. The installed service returned a partial
workspace-wide artifact with code `EVENT_INSPECTED_PARTIAL`. It reported no
source-specific diagnostic, but its evidence inventory was truncated and the
graph reached the service's derived-edge ceiling. This artifact is tooling
evidence only. Direct source inspection remains the authoritative audit for
this dormant chain.

## Files reviewed

- `common/script_constants/fallout_world_end_event_constants.txt`
- `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
- `common/scripted_effects/fallout_world_end_first_safe_birth_event_effects.txt`
- `common/scripted_triggers/fallout_world_end_first_safe_birth_event_triggers.txt`
- `events/fallout_world_end_events.txt`
- `common/dynamic_modifiers/fallout_world_end_first_safe_birth_dynamic_modifiers.txt`
- `common/scripted_localisation/fallout_world_end_first_safe_birth_event_log_scripted_localisation.txt`
- `localisation/english/fallout_world_end_first_safe_birth_l_english.yml`
- `interface/fallout_world_end.gfx`

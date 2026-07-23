# The Door List implementation handoff

Status: dormant implementation complete for the reviewed two-state survival
transaction. The scheduler release gate remains closed. The chain is not yet
release-floor credit until its engine-sensitive surfaces receive a live audit.

## Fixed surfaces

- Human opening: `chaosx.fallout.230`
- Hidden AI opening: `chaosx.fallout.231`
- Human family, specialist, lottery, and refusal results: `232` through `235`
- Hidden AI results: `236` through `239`
- Human callback: `chaosx.fallout.240`
- Hidden AI callback: `chaosx.fallout.241`
- Cleanup: `chaosx.fallout.242`
- Candidate id: `230`
- Transaction key: `710010`
- Route: `7110`
- Event Log history id: `9115`
- Result delay: `12` days
- Callback delay: `180` days
- Visible budget cost: `3`

## Changed gameplay surfaces

- `common/script_constants/fallout_world_end_event_constants.txt` owns branch,
  threshold, viability, cost, movement, result, Event Log, AI, and fixed id
  values.
- `common/scripted_effects/fallout_world_end_event_candidate_effects.txt`
  selects the lowest valid destination and the lowest different source whose
  exposure is at least fifteen points higher. Candidate state ids and the
  source exposure floor are stored as normal country variables.
- `common/scripted_triggers/fallout_world_end_door_list_event_triggers.txt`
  separates opening eligibility from post-result receipt validation. The
  post-result triggers do not reapply the initial population or shelter floor.
- `common/scripted_effects/fallout_world_end_door_list_event_effects.txt`
  freezes the pair and numerical ledgers, reserves delayed scheduler receipts,
  scores AI choices, applies result deltas, performs exact population movement,
  records durable state memories, writes Event Log history, schedules the
  callback, and releases cleanup receipts.
- `events/fallout_world_end_events.txt` owns the human and hidden AI surfaces
  under `add_namespace = chaosx.fallout`.
- `localisation/english/fallout_world_end_door_list_l_english.yml` contains
  concrete shelter and government-aware text with UTF-8 BOM encoding.
- `common/scripted_localisation/fallout_world_end_door_list_event_log_scripted_localisation.txt`
  maps the fifteen Event Log payloads to player-facing detail text.
- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`
  and `interface/fallout_world_end.gfx` contain the central Event Log routes
  and dedicated report sprite registration.

## Exact population proof

The opening freezes source population, destination population, destination
shelter, receiving capacity, arrival pressure, branch, outcome, and resource
rows before the twelve-day result. The result computes moved people and deaths
from the frozen base cohort. Moved people are capped against frozen receiving
capacity. The source request is submitted once to
`apply_exact_state_civilian_population_loss` with Deaths logging disabled.
The returned applied amount is authoritative. Deaths are clamped to that
returned amount, moved people are the remainder, moved people are added to the
destination with `add_manpower`, and the death remainder is recorded once by
`fallout_orientation_record_exact_country_deaths`. No direct population
creation or duplicate death pass is used.

## AI and memory proof

Hidden AI and human results use the same branch thresholds, resource costs,
frozen Air Winter values, source exposure, destination supply, government
archetype adjustments, war adjustment, and deterministic strict-higher tie
order. Durable state flags distinguish admitted families, the service class,
the civic roll, and orderly, fractured, or violent refusal. Cleanup removes
only the live transaction receipt and registry flags, leaving those memories
available to later Fallout scheduling.

## Engine-sensitive surfaces still requiring proof

1. The engine's host identity and input-lock behavior for an ordinary visible
   delayed event are not proven by this chain. The scheduler must remain closed
   until that surface is audited.
2. Cross-effect persistence and rebinding of two state ids is represented by
   country-held ids plus `var:<state_id>` rebinding on every result, callback,
   and cleanup trigger. The live audit must prove that both pointers survive a
   save and reload without scope drift.
3. The reusable migration helper is intentionally not extracted from the
   exact sequence in this tranche. The sequence is explicit so the source loss,
   applied amount, moved remainder, and Deaths record can be audited together.
4. The visible budget cost of three uses the existing ordinary scheduler
   receipt field. Its ledger interpretation still needs a live scheduler audit.

No scheduler activation flag was opened and no runtime test was run.

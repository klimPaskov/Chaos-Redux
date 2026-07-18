# Event 15 Ledger and calling idempotence audit

## Scope and result

This is the final read-only architecture handoff for the live Event 15 Ledger and
calling refactor on 2026-07-15. No gameplay, localisation, specification, asset,
or spreadsheet file was edited by this audit.

The implemented design is idempotent: a refresh projects durable history and
current country state into derived values. Repeating a refresh without changing
an input produces the same totals, severities, bands, flags, and GUI breakdown.

Identifiers are authoritative if later edits move the line anchors below.

## Final state model

### Ledger

For each of Need, Plenty, Concord, and Assignment:

```text
displayed total = clamp(base + durable policy record + live contributions, 0, 100)
```

- `utopia_manifesto_*_from_base` is initialized once at acceptance.
- `utopia_manifesto_*_from_policy` is the durable additive record. All 372
  prepared Ledger mutations route through
  `utopia_manifesto_apply_prepared_ledger_delta` (effects line 600).
- `utopia_manifesto_recalculate_live_ledger_contributions` (line 427) resets and
  derives industry, infrastructure, war, occupation, capital, institutions,
  subject status, named pressure, and territorial-loss components.
- `utopia_manifesto_rebuild_ledger_totals` (line 516) is the sole normal owner
  of the four displayed totals. Repository-wide mutation inspection found no
  other gameplay mutation of `utopia_need`, `utopia_plenty`, `utopia_concord`,
  or `utopia_assignment` outside rebuild/clamp/terminal cleanup.
- `utopia_manifesto_capture_ledger_acceptance_baseline` (line 410) stores only
  owned states that are cores of the accepting actor. Lost members of that
  fixed array produce the live Need/Concord territorial contribution; regaining
  one removes its contribution on the next refresh.
- `utopia_manifesto_refresh_live_pressure_flags` (line 418) clears and derives
  migration, housing, and trade pressure from the pure triggers at trigger
  lines 294, 311, and 320. These flags are therefore reachable state, not dead
  inputs.
- Reserve is a separate durable score. Refresh clamps and bands it but does not
  reconstruct it from the four Ledger axes.

`utopia_manifesto_refresh_ledger` (line 589) has the fixed call graph:

```text
derive pressure flags
-> derive all live Ledger components
-> rebuild the four totals
-> clamp totals
-> derive Ledger and reserve bands
-> refresh callings
-> refresh focus visibility
```

It does not add policy deltas and does not enumerate countries.

### Callings

Each of the six families uses four distinct layers:

```text
effective policy = clamp(raw durable policy, -70, 70)
uncovered severity = clamp(structural pressure + effective policy, 0, 100)
present severity = clamp(uncovered severity + temporary adjustment, 0, 100)
```

- `*_structural_pressure` is reset to its base and re-derived from current
  Ledger bands, stores, equipment, research, infrastructure, war, occupation,
  coast, and live pressure flags on every calling refresh.
- `*_policy_adjustment` is the raw durable history. It is intentionally not
  clamped, so paired changes such as `-8` and `+8` remain exactly reversible
  even when the effective value is already at a display bound.
- `*_effective_policy_adjustment` is the clamped projection consumed by the
  severity calculation.
- `*_temporary_adjustment` is reset to zero and re-derived from
  `utopia_manifesto_emergency_levy_active` plus
  `utopia_manifesto_emergency_levy_family`. Expiry clears those inputs and
  refreshes; it never applies an inverse delta.
- `*_uncommitted_severity` is the material deficit consumed by Necessary Ground
  selection. Emergency coverage therefore cannot erase case justification.
- `*_severity` is the present, temporarily coverable shortage used by calling
  flags and calling missions.
- Shortage flags use hysteresis: enter above 40 and clear below 30. Exact 30 or
  40 preserves the prior flag state by design.
- `utopia_manifesto_selected_calling_has_shortage` and
  `utopia_manifesto_selected_calling_is_ready_for_method` dispatch through the
  selected family. Method decisions therefore cannot use another family's
  shortage, and family-specific `*_method_recent` flags provide cooldowns.

The pure rebuild path is split among
`utopia_manifesto_reset_calling_structural_pressure` (line 632),
`utopia_manifesto_seed_calling_pressure_from_country_conditions` (line 641),
`utopia_manifesto_recalculate_temporary_calling_adjustments` (line 720), and
`utopia_manifesto_rebuild_calling_severities` (line 762).
`utopia_manifesto_refresh_calling_state` (line 836) calls those helpers, clamps
present severity, applies hysteresis, and validates an already-active Necessary
Ground case. It never calls the Ledger refresh, so there is no recursion.

## Calling mutation and caller inventory

Repository-wide direct-mutation inspection found four durable mutation owners,
plus initialization and terminal cleanup:

| Durable mutation owner | Current callers |
| --- | --- |
| `utopia_manifesto_apply_prepared_calling_change` | `utopia_manifesto_clear_selected_calling_shortage` for open call, guaranteed placement, and assignment quota. Emergency levy bypasses durable policy and derives temporary coverage instead. |
| `utopia_manifesto_apply_domestic_review_relief` | Two branches of `utopia_manifesto_resolve_domestic_alternatives` (decision effects lines 1389 and 1404). |
| `utopia_manifesto_relieve_active_case_deficit` | `utopia_manifesto_start_stewardship_from_active_case` and `utopia_manifesto_integrate_stewardship` (effects lines 2790 and 3303). |
| `utopia_manifesto_relieve_stored_case_family` | The settlement-agreement, long-supply-contract, and association-duties wrappers. Each wrapper is called by its start, completion, and failure path: effects lines 2310/2345/2365, 2447/2481/2503, and 2603/2663/2685. |

The raw durable variables are otherwise touched only by
`utopia_manifesto_initialize_callings`, missing-variable initialization inside
the rebuild, and `utopia_manifesto_clear_calling_runtime`. Derived structural,
effective, temporary, uncovered, and present variables are owned only by their
rebuild layer and cleanup. The removed mission outcome and family-filled flags
have no remaining references.

Emergency lifecycle ownership is now explicit:

- success stores the family and sets `utopia_manifesto_emergency_levy_active`;
- the expiry mission represents its public term;
- extension removes and re-arms that mission without invoking its timeout;
- expiry clears active state/family/days and refreshes;
- terminal cleanup clears active/recent/expired flags, family, duration, and
  extension count.

## Bounded refresh cadence

Full Ledger refresh occurs only at these bounded points:

1. acceptance through `utopia_manifesto_initialize_ledger`;
2. National Survey completion through
   `utopia_manifesto_complete_national_survey` (decision effects line 455);
3. every prepared Ledger mutation through the central delta helper: 167 event
   callers, 124 focus callers, 53 decision-effect callers, 16 core-effect
   callers, and 12 direct decision callers;
4. the direct reserve mutation in `decision_utopia_rotate_old_stores`;
5. the scripted-GUI Recount button;
6. the accepted actor's self-scheduling `chaosx.nr15.150` pulse;
7. actor-guarded `on_war`, `on_peace`, `on_capitulation`, `on_annex`,
   `on_peaceconference_ended`, and `on_state_control_changed` hooks.

Calling-only mutation helpers use `utopia_manifesto_refresh_calling_state` so
they do not rebuild the Ledger unnecessarily. Duplicate event delivery is safe
because both refresh functions are projections.

There is no Event 15 daily, weekly, or monthly on-action and no world iteration
in either shared refresh. `utopia_manifesto_prepare_case_candidate_targets`
still uses `every_country`, but only from explicit Necessary Ground preparation,
case resolution/invalidation, and decision/event entry points. Validation from
the calling refresh can reach it only once when an active case becomes invalid;
it is not part of the steady refresh path.

There is no documented `on_capital_changed` hook in the consulted snapshot or
vanilla documentation. Capital and equipment changes are caught by the actor
pulse and manual Recount; state-control changes refresh immediately.

## Cleanup and dynamic localisation

`utopia_manifesto_clear_calling_runtime` (line 5015) clears all shortage and
cooldown flags; emergency state; structural, raw policy, effective policy,
temporary, uncovered, and present values; family methods; selection; and mission
durations. `utopia_manifesto_clear_ledger_runtime` (line 5139) clears the four
totals and bands, reserve state, the acceptance core-state array, derived
pressure flags, durable/base breakdown, all live components, and last deltas.
No additional Ledger/calling cleanup identifier was found.

The GUI breakdown is aligned with the model:

- overview localisation line 35 shows base, public policy record, every live
  contribution, and the core-territory loss component for each applicable axis;
- calling localisation lines 36-37 show uncovered, present, structural,
  effective durable, and temporary values for every family, plus the current
  method;
- the explanatory footer states that Necessary Ground reads uncovered pressure
  while Emergency Levy changes only present pressure.

## Shared Deaths hook for Penal Works

Event 15 should use the existing state-scope
`apply_exact_state_civilian_population_loss`; no Event 15-only Deaths system is
needed.

Evidence:

- implementation: `common/scripted_effects/chaosx_dynamic_effects.txt`, lines
  720-800;
- documented contract: `common/scripted_effects/chaosx_dynamic_effects.md`,
  lines 858-923;
- working caller precedent:
  `common/scripted_effects/018_resources_found_incident_effects.txt`, lines
  12-55;
- shared registrar: `chaos_meter_register_deaths` in
  `common/scripted_effects/chaos_meter_effects.txt`, line 2569;
- suitable existing cause:
  `constant:chaos_meter_deaths_reason.gulag_repression` in
  `common/script_constants/chaos_meter_constants.txt`, line 395, localised as
  "From camps and forced labor".

Every Penal Works invocation must be in the selected project STATE scope and
must set all of these temporary inputs immediately before the call:

```text
state_civilian_population_loss_requested
state_civilian_population_loss_minimum_remaining
state_civilian_population_loss_reason
state_civilian_population_loss_log_deaths
state_civilian_population_loss_target_country
state_civilian_population_loss_has_target_country
state_civilian_population_loss_applied = 0
state_civilian_population_loss_result = 0
state_civilian_population_loss_contract_supplied = 1
```

Use the Event 15 actor, not an assumed state owner, as the target country when
the project scope can differ from ownership. Use the Event 15 protected
population-floor constant, `log_deaths = 1`, and the existing
`gulag_repression` reason. Copy
`state_civilian_population_loss_applied` immediately after the call and derive
all project totals, penalties, and rewards from that applied amount. The helper
removes actual state population exactly once, reconciles recruitable-manpower
credit, and still applies the population loss when the optional Deaths display
is disabled. A separate manpower/equipment project cost must not be described
or counted as civilian deaths.

## Remaining risks

- Acceptance currently initializes the Ledger and then initializes callings;
  the Ledger initializer already performs a calling refresh. The second refresh
  is redundant but idempotent and actor-bounded.
- Raw calling policy can exceed the effective `-70..70` band. This preserves
  exact rollback history but can make several positive reversals produce no
  immediate displayed change while raw history remains beyond the bound. The
  GUI intentionally exposes the effective durable value, not this bookkeeping
  overflow; balance changes should account for it.
- Live equipment/research/capital changes without a dedicated hook have at most
  one actor-pulse interval of latency unless the player presses Recount. No
  global recurring scan should be added to eliminate that bounded latency.

No blocker, fallback, placeholder, or unapproved simplification was found in
the audited Ledger/calling architecture. Penal Works still needs its eventual
project-specific call site, requested-loss formula, protected floor, and
applied-result accounting; this handoff verifies the shared adapter rather than
claiming that Penal Works itself is implemented.

## Sources and skills

Consulted the required offline wiki pages for Data structures, Triggers,
Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision
modding, Idea modding, AI modding, Interface Modding, and Scripted GUI Modding.
Also consulted vanilla effects/triggers/localisation/script-concept/script-
constant documentation, `common/on_actions/_documentation.md`, scripted-GUI and
decision documentation, and vanilla `on_war`/`on_peace` precedents. No online
Paradox wiki was used.

Skills used: `chaos-redux-subagents` and `chaos-redux-events`. No skill was
created or modified.

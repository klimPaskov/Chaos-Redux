# Event 006 League decisions DM-42 through DM-62 - decision and mission audit

Date: 2026-07-22  
Scope: DM-42, DM-43, DM-44, DM-60, DM-61, and DM-62; their shared target
pointer, rescue-equipment lifecycle, charter-war authorization, supporting
triggers, on-action, localisation, constants, and decision matrix.

## Patch made by this audit

| File | Identifier | Before | After |
| --- | --- | --- | --- |
| `common/decisions/006_independence_wave_decisions.txt` | `independence_wave_request_charter_war_mandate` (DM-62) | The timed authorization flag used a temporary-variable token in `set_country_flag = { days = ... }`. That field does not safely parse variable tokens. | Uses the file-scoped `@INDEPENDENCE_WAVE_CHARTER_WAR_MANDATE_DAYS = 365` literal, explicitly mirrored to `constant:independence_wave_decision_cooldown.major`. The mandate continues to last 365 days, but its duration is load-safe. |
| `common/scripted_effects/006_independence_wave_effects.txt` | `independence_wave_select_government_route` patron-client branch | A league member that accepted the client route retained an unspent target-specific war-mandate flag while awaiting charter expulsion. | Calls `independence_wave_decision_clear_charter_war_mandate` immediately after setting `independence_wave_client_route_locked`, clearing the dynamic authorization flag and its metadata. |

The audit did not change the intended material costs, reward magnitudes, AI
weights, decision matrix entries, or player-facing wording.

## Issues, sorted by severity

1. **Resolved - high engine-risk:** DM-62 passed
   `independence_wave_charter_war_mandate_days` to `set_country_flag.days`.
   The decision skill and Event 006 implementation rules identify timed flag
   durations as a field that must receive a literal, not a variable token.
   The patch uses a file-scoped `@` literal mirrored to the global tuning
   constant.
2. **Resolved - medium lifecycle risk:** a patron-client route could leave a
   pre-existing unconsumed mandate on a country that had become charter
   non-compliant. The patron-client route now clears that mandate before the
   country remains in the ledger for its possible expulsion vote.
3. **No remaining confirmed high/medium issue in the assigned surface.** The
   shared target pointer is held for every timed selected-state decision,
   revalidated against the original selected state owner, and cleared on both
   resolve and cancellation.

## Decision category lifecycle

- **DM-42 - collective recognition:** stores the selected member country at
  commitment; resolution raises that stored country's recognition and network
  standing. Cancellation clears the pointer and applies only the campaign
  cohesion loss.
- **DM-43 - border arbitration:** stores the partner and the target-side
  arbitration requester record. Resolution removes reciprocal claims with the
  frozen partner; cancellation clears the pending request and pointer,
  including the refusal branch.
- **DM-44 - rescue threatened member:** reserves 500 infantry and 100 support
  equipment at start. At 75 days it transfers exactly those reserved amounts
  to the frozen member and gives the applicant's guarantee. Peace before
  delivery refunds the reserve. Client-route abandonment while the member is
  still at war records the rescue-abandonment ground and intentionally does
  not refund; other cancellation paths refund.
- **DM-60 - charter expulsion vote:** stores the accused country, then
  rechecks leader authority, original state ownership, member status, and the
  documented ground at resolution. An invalidated case fails rather than
  expelling a redirected target; both paths clear the pointer.
- **DM-61 - sponsored coup:** is immediate, has no timed pointer, saves the
  live target as an event target before beginning the civil war, and records
  the sponsored-coup ground in the sponsor's ledger. The war on-action excludes
  civil wars so this deliberate intervention is not double-recorded as an
  unauthorized external declaration.
- **DM-62 - charter war mandate:** holds the target during the 45-day
  deliberation, replaces any prior unconsumed mandate at resolution, then sets
  one target-specific 365-day flag. `on_war_relation_added` consumes it only
  when `ROOT` declares against that exact `FROM` defender; any other offensive
  declaration records the unauthorized-war ground. Origin cleanup and the new
  patron-client cleanup both clear pending mandate metadata and the dynamic
  flag.

None of these six entries is a mission. DM-42/43/44/60/62 are timed
decisions; DM-61 is immediate. Their single-active-crisis trigger prevents the
shared target variable from being overwritten by another listed League action.

## Cost, requirement, AI, and route-lock notes

- DM-42/43/62 use diplomatic-standard command attention plus convoy-or-train
  capacity; DM-62 also commits one civilian factory during deliberation.
  DM-44 additionally reserves the exact equipment it later delivers. DM-60
  uses the strategic commitment; DM-61 pays its security-standard material
  intervention cost.
- DM-44's availability uses strict `has_equipment >` checks, so it requires a
  one-unit stockpile buffer (501 infantry and 101 support) while still
  spending, transferring, and refunding exactly 500/100. This is conservative
  and prevents a negative stockpile; it is not an equipment-farming loop.
- DM-60 requires an active current leader, aligned member ledger, sufficient
  membership, anti-puppetry authority, and a factual ground that is still
  present when the vote resolves. DM-62 requires the mutual-defense pillar,
  defensive-congress route, a live non-member external target, and a valid war
  declaration target.
- AI is appropriately conservative for enforcement and coup actions: DM-60
  starts very low and prefers repeated/documented breaches; DM-61 is very low
  and rises only for the radical route; DM-62 is low and reduced for neutral
  commissions. Recognition, arbitration, and rescue retain their high/high/
  urgent roles. All are blocked by an active League crisis.
- Focus integration is present: `independence_wave_propose_defensive_congress`
  calls `independence_wave_focus_reward_league_defense`; later League route
  state gates DM-62 through `independence_wave_league_route.defensive_congress`.

## Localisation, tooltip, cleanup, and exploit notes

- DM-42/43/44/60/61/62 names and descriptions are present in
  `localisation/english/006_independence_wave_decisions_l_english.yml`, which
  retains its UTF-8 BOM. DM-44 describes reservation/refund/abandonment, and
  DM-62 describes the exact target, lifetime, consumption, and breach result.
  DM-60 uses the recorded factual-ground scripted text rather than exposing raw
  trigger blocks.
- Dynamic mandate flags use the selected country tag at creation and the
  attacker/defender tag at consumption. The stored target metadata permits
  cleanup before tag reuse. The new client-route cleanup closes the remaining
  stale-authorization path within this route.
- No scripted-GUI decision surface is in scope; no GUI artifact was inspected
  or changed.

## Validation and boundaries

- Read the required offline wiki pages and current vanilla decision,
  on-action, script-constant, effect, and trigger documentation. Verified the
  targeted-decision `ROOT`/`FROM` scope contract, `on_war_relation_added`
  attacker/defender scope, equipment stockpile direction, guarantee direction,
  and timed-flag duration constraint against vanilla precedents.
- Ran a focused diff check on the eight tranche files; it reported no diff
  errors. Confirmed the obsolete DM-62 duration variable token is absent and
  that the new `@` literal equals the `major = 365` script constant. Confirmed
  all six decisions and their name/description localisation keys are present.
- Reviewed the DM-42 through DM-62 rows in
  `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`
  against the implemented lifecycles.
- Skipped runtime execution and a Clausewitz parser because no task-specific
  parser or automated test harness is supplied in this workspace. No in-game
  validation was requested or performed. GUI inspection is not applicable.

## Remaining issues and handoff

No broad mechanic, new decision system, GUI surface, or new formable is
recommended from this audit. No requested mechanic was simplified.

Review files that form the implementation tranche:

- `common/decisions/006_independence_wave_decisions.txt`
- `common/scripted_effects/006_independence_wave_decision_effects.txt`
- `common/scripted_effects/006_independence_wave_effects.txt`
- `common/scripted_triggers/006_independence_wave_decision_triggers.txt`
- `common/on_actions/006_independence_wave_achievement_on_actions.txt`
- `common/script_constants/006_independence_wave_decision_constants.txt`
- `localisation/english/006_independence_wave_decisions_l_english.yml`
- `docs/specs/006_independence_wave_specs/matrices/006_decision_mission_map.csv`

No separate deepening plan was written. This audit handoff is the plan-area
artifact for the two narrow fixes above.

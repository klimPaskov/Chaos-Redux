# Event 010 Death Improvement Loop Addendum

Date: 2026-07-11

Status: reviewed proposal, queued for implementation. No gameplay or localisation change is authorized by this addendum alone.

Disposition: a further bounded pass is justified. The previous focus-depth and remaining-routes plans are implemented and closed. This addendum does not reopen them.

## Verdict

Death already has enough route breadth. The high-value expansion is to make its first signs less self-spoiling, make its movement across the map feel geographically legible, and make victory leave a playable burden instead of ending with one survey and one outpost.

The smallest coherent implementation has three connected parts:

1. a spoiler-safe maritime evidence layer before public revelation
2. spatially coherent mainland and coastal spread selection
3. irreversible post-defeat custodianship for recaptured wastelands

These parts deepen the same story. Governments first interpret missing routes, then learn where the pattern can travel, then inherit land that cannot be made whole.

## Current Evidence

- `events/010_death.txt` already supports hidden launch, two missing-island reports, spread pulses, and census reports.
- `death_send_survey_boat_tt` names Death and exposes mechanical consequences before the world has confirmed what happened.
- `death_try_mainland_pressure_spread` and `death_attempt_coastal_jump` select from every globally valid state. Island spread already prefers nearby targets through `distance_to`, so the inconsistency is local to the mainland and coastal stages.
- Recaptured wastelands retain zero usable population and severe permanent penalties.
- The current aftermath decisions only survey a wasteland and build a dead-zone outpost.
- `docs/events/010_death.md` explicitly queues deeper memorial and reconstruction decisions without restoring erased population.
- The 26-node DTH focus tree, Dark Methods, Black Oath, Herald, Apostolate, Living Compact, Black Atlas, achievements, and super-events are already implemented. They are not missing route work.

## Tranche One: The Maritime Case File

Add a country-scoped evidence value for governments that receive missing-route reports. It should represent confidence in a connected maritime anomaly, not knowledge of Death.

Suggested state:

- `death_maritime_evidence` as a country variable
- flags for one-time discoveries and policy choices
- script constants for evidence thresholds, gains, decay, AI bands, and costs
- scripted localisation that changes only after country-level confirmation or global public revelation

Existing actions should feed the case file:

- receiving the first and second missing-island reports
- checking port and registry records
- issuing a quiet quarantine notice
- sending a survey boat
- closing the file under weather
- later receiving a confirmed coastal warning

Evidence bands should change available information and policy confidence. Before confirmation, tooltips must refer to the missing route, silent islands, anomalous traffic, or an unknown coastal threat. They must not name Death, reveal DTH focus consequences, or explain world-end bypass rules. After confirmation, the same keys may resolve to direct Death terminology through contextual or scripted localisation.

This is an information mechanic, not a second resource economy. It should reuse the existing Maritime Errata category and missing-report flags. The Black Atlas remains unavailable as an omniscient pre-reveal encyclopedia.

## Tranche One: Spatial Spread Logic

Mainland revelation and ordinary coastal jumps should prefer targets connected to the current pattern.

Add reusable target tiers:

1. valid coasts within a short configured distance of an active Death wasteland
2. warned or investigating coasts within a wider configured distance
3. valid coasts within a maximum configured route distance when spread pressure is high

The helper should select the first tier with a candidate and then choose inside that tier. If no spatially coherent target exists, the spread attempt fails, its cooldown behavior is applied as designed, and pressure remains available for a later attempt. It must not jump to an unrelated global coast as a hidden fallback.

World-end footholds remain a separate explicit rule. Their continent-by-continent behavior is already designed as supernatural escalation and should not be constrained by the ordinary route logic.

Implementation requirements:

- reuse the existing `distance_to` precedent from nearby island spread
- centralize distance bands and pressure consequences in script constants
- keep coastal watch and quarantine exclusions authoritative
- preserve No Ferry Returns and world-end bypasses only where the current design explicitly grants them
- expose enough information that a warned player can understand why a coast is at risk without revealing the exact random target
- do not add a daily or weekly world scan

## Tranche One: Custodianship of the Empty Land

Build on the existing state sequence instead of adding a separate reconstruction system.

### State progression

1. `Recaptured Wasteland`: the existing permanent condition
2. `Surveyed Dead Zone`: created by the existing survey decision
3. `Custodial Outpost`: created by the existing outpost decision
4. one permanent custodial policy selected after Death is defeated

The final policy should be a real tradeoff:

- **Sealed Exclusion** favors containment, defense, and lower operating risk, but preserves the harshest access and construction limits.
- **Memorial Stewardship** converts national effort into remembrance, social stability, and mourning-debt relief, but does not make the state productive.
- **Transit Custodianship** restores limited movement and supply utility through maintained corridors, but requires continuing equipment and command investment and never restores local manpower, factories, or resources.

These are direction labels, not final localisation.

Use state flags for the selected policy and a country variable such as `death_custodial_capacity` for limited project throughput. Capacity can come from completed surveys, outposts, Living Compact contribution, and participation in Death's defeat. Costs and gains must be centralized.

The hard boundary is permanent:

- consumed population is never restored
- the state remains a wasteland category
- no custodial policy recreates civilian or military factories stripped by consumption
- no policy recreates erased resources or recruitable population
- control changes do not permit a second country to claim the same one-time project reward
- renewed Death consumption clears custodial project flags before applying the active-wasteland state

## AI And Scenario Behavior

- Coastal AI should investigate when evidence, naval capacity, and local exposure justify the cost.
- AI should not gain confirmed knowledge from hidden global state.
- Death target selection uses the same spatial tiers for human and AI games.
- AI chooses Sealed Exclusion on exposed borders, Transit Custodianship on strategically important supply corridors, and Memorial Stewardship when the state is secure and national mourning pressure is high.
- Instant Outbreak continues to suppress the normal quiet-origin case file where its scenario rules already do so.
- World-end and whole-world-consumed paths keep their current exceptional behavior.

## Later Tranches

These are separate plans and must not be folded into tranche one without a new scope decision:

1. Living Compact obligations, shared missions, leadership disputes, and success or collapse thresholds.
2. Black Atlas regional diagnostics after public revelation, while decisions remain the authoritative action surface.
3. Route-aware aftermath for Compact members, Black Book users, Heralds, and oathbreakers.

## Implementation Surfaces

- `common/script_constants/010_death_constants.txt`
- `common/scripted_effects/010_death_effects.txt`
- `common/scripted_triggers/010_death_triggers.txt`
- `common/decisions/010_death_decisions.txt`
- `common/dynamic_modifiers/010_death_state_modifiers.txt`
- `common/scripted_localisation/010_death_scripted_localisation.txt`
- `localisation/english/010_death_l_english.yml`
- `docs/events/010_death.md`
- relevant Event 010 specs, event-detail text, and spreadsheet fields after final in-game wording exists

No new icon is required for tranche one if the existing survey, outpost, quarantine, coastal watch, and memorial-compatible sprites remain semantically accurate. Any art expansion requires a separate asset handoff before sprite names change.

## Acceptance Scenarios

- A coastal country can receive both missing reports and investigate without any player-facing text naming Death before confirmation.
- Closing the file under weather has a visible information and preparedness cost rather than only removing a category.
- Ordinary mainland revelation occurs near the existing pattern when a valid nearby target exists.
- An ordinary coastal jump does not cross the world to an unrelated valid coast merely because closer coasts are defended.
- World-end footholds still reach uncovered continents under their existing exceptional rules.
- A recaptured wasteland can progress through survey, outpost, and one custodial policy after defeat.
- Each custodial policy has a distinct strategic use while population, factories, resources, and state category remain irreversible.
- Control transfer, reactivation, defeat cleanup, and scenario setup cannot duplicate rewards or leave contradictory state modifiers.

## Do Not Add

- another DTH focus branch
- another forbidden route
- a second scripted GUI
- normal population or industrial reconstruction
- a global random coast as a fallback for ordinary spread
- a broad daily, weekly, or monthly all-country loop
- final localisation, new achievements, super-events, or assets before the gameplay tranche is implemented

No fallback design or simplification is approved in this addendum.

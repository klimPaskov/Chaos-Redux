# Mandatory Near-Completion Improvement Loop Review

> **Superseded process notice (2026-07-16):** This file preserves the manual
> planning-stage review. A later mandatory planner pass produced
> `docs/plans/019_infantry_spawn_plans/019_near_completion_improvement_addendum_2026_07_16.md`.
> Its natural-release, pre-fire reception, documentation, and fixed
> identity-scene findings have been implemented. That addendum and the newest
> audit handoffs are the current authority. The live-final AI, balance,
> performance, isolation, scenario-safety, and exploit reaudit is clean with
> zero P0, P1, or P2 findings. All gameplay specialist gates are closed. The
> owner-approved 7/18 regional candidate now contains 91 raw sources, 91
> deterministic spot masters, and 273 native/runtime output pairs. Visual and
> runtime rows pass. The independent remediation re-audit handoff
> `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
> is PASS and clears the regional asset gate for parent-owned package
> promotion. The machine JSON retains its immutable literal
> `candidate_requires_independent_visual_review` processor-state value. Parent
> workbook/catalog reconciliation and export, the 33-file package inventory,
> and the mandatory final completion audit are complete. Event 19 and SCN-013
> are `Fully Functional`; no closure gate remains.

## Process status

This file preserves the planning-stage manual review that shaped the source
specification. The first required planner run returned a dated closure handoff;
the later planner pass and addendum named above supersede that process status.

## Feature promise

The event promises that armies can appear anywhere, become increasingly useful and strange, create military and political burdens, and eventually introduce Chaos unit families whose mishandling can produce hostile offshoot states.

The design succeeds only if more units can be either salvation or disaster and if the player can deliberately gamble without controlling the result.

## Depth gaps found during review

### Gap 1: A random spawn without persistent generation memory would repeat mechanically

Resolution added:

- generation records
- stacked muster
- prior management affects future quality
- closeout classes

### Gap 2: Fully random templates could become a reroll minigame

Resolution added:

- cost paid before reveal
- escalating request cost and cooldown
- no free cancel-and-reroll
- recombination consumes the same personnel and equipment with loss and failure risk
- weak results retain uses as cadres, garrisons, political liabilities, or achievements

### Gap 3: Claimant generals could remain flavor-only

Resolution added:

- influence values
- archetypes
- demand families
- command districts
- actual loyal formation links
- takeover, negotiation, arrest, and revolt
- one-state handling
- 20 male claimant profile/name-pool plan plus 20 separate regional army/muster identity scenes in the fixed portrait slots

### Gap 4: Chaos units could accidentally duplicate parent events

Resolution added:

- opt-in family registry
- explicit train-versus-spawn mode
- parent isolation fields
- derivative origin flags
- shared classifiers
- family-specific weaker country profiles
- default exclusion of future and advanced units

### Gap 5: Derivative countries could be empty tags

Resolution added:

- starting forces from actual revolt units
- idea lifecycles
- sustainment and reinforcement
- hierarchy choices
- focus-scale route architecture
- expansion and integration
- AI and defeat cleanup

### Gap 6: A global system could create unbounded UI and script load

Resolution added:

- lot-level rather than division-level management
- selected-lot UI
- bounded active claimant presentation
- country-scoped active pulses only
- no permanent daily all-country loop
- explicit closeout and cleanup

## Anti-bloat decisions

### No fifth evolution

Four evolutions already move the event from local infantry musters to anomalous military secession. A fifth evolution would likely duplicate parent world-end systems or turn the event into a universal content aggregator.

### No direct world-end path

The user explicitly rejected a direct world-end scenario. Derivative states remain regional threats.

### No ordinary-country focus tree layer

The decision and GUI system is shared across ordinary countries. Country-specific ordinary focus branches would multiply scope without improving the core global event.

### No super-event

No normal threshold in this event changes the whole campaign’s meaning enough to justify image, quote, and audio production. A globally dominant derivative state can be reconsidered in a later separate plan.

### No one-member cluster

Event 19 stays unclustered until other military manifestation events are reworked and can form a real incident group.

### No animation for every claimant identity scene

Twenty animated army/muster scenes would create asset volume and visual noise. Static identity scenes plus a critical-state panel-border animation communicate the mechanic better.

### No automatic future-family inclusion

Dynamic support means one registry entry is enough. It does not mean every new unit is automatically safe.

## Closure assessment

The planning design is deep enough to hand to implementation. Another broad planning expansion is not recommended now. The remaining work is implementation, local identifier verification, asset production, balance testing, specialist audits, final localisation, documentation, and catalog alignment.

The planning-stage closure recommendation was superseded by the required
project-agent planner after a meaningful implementation tranche. That pass did
produce the accepted near-completion addendum named above. Its natural-release,
first-family reception, fixed identity-scene, and documentation findings were
promoted into implementation and are closed at addendum level; another broad
expansion pass is not warranted unless a current audit finds a concrete gap.

Exactly two engine-constrained substitutes are owner-approved and implemented:
exact recorded-formation recreate/prove/delete and controlled one-formation
combat trials. The owner-approved deterministic spot-colour route is also
implemented for the 7/18 regional candidate. The independent remediation
re-audit handoff
`docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_regional_full_flag_postprocess_remediation_reaudit_2026_07_18.md`
is PASS and clears the regional asset gate. Workbook/catalog reconciliation,
export, the 33-file package inventory, and the final completion audit are
complete. Event 19 and SCN-013 are `Fully Functional`; no closure gate remains.
The current disposition is tracked in
`review/blockers_and_uncertainty.md`.

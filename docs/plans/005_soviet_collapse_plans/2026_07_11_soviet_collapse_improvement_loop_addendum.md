# Event 005 Soviet Collapse Improvement Loop Addendum

Date: 2026-07-11

Status: reviewed proposal, queued for implementation. No gameplay or localisation change is authorized by this addendum alone.

Disposition: the 2026-05-29 focus redesign remains partially implemented and explicitly queued. This addendum does not duplicate that backlog. It defines the missing shared crisis loop and reconciles later Event 005 additions.

## Verdict

Soviet Collapse does not need more raw content volume. It needs connective mechanics that make its existing values, 118 Soviet missions, staged releases, intervention desks, rail and depot language, successor packages, and end states produce one another.

The smallest coherent implementation is a Command and Corridors tranche. It should organize the existing mission pool around four operational values:

- Moscow Authority
- Military Obedience
- Republic Confidence
- Depot Vulnerability

Foreign Appetite, League Cohesion, and Old Movement pressure remain secondary forces that select targets, amplify consequences, and alter available outcomes. Union Collapse Threat remains the public derived severity.

## Source Reconciliation

The canonical June 5 ledger is stale.

- Current Event 005 focus files contain 43 trees and 1,728 focuses.
- The promoted ledger records 41 trees and 1,698 focuses.
- The difference is the later UWR and KMB packages, which have supplemental specs but are not reconciled into the source map.
- UWR has a compact seven-focus package and no dedicated decision category or bespoke AI surface.
- KMB has a compact nine-focus package with decisions, coal-golem units, resource treaties, and concessions, but no bespoke route AI.
- The existing audit still records 1,127 helper-only or nearly helper-only focus rewards and 520 pathline heuristic risks. Those findings remain the separate focus backlog.
- `docs/events/005_soviet_collapse.md` says selected patron desks normalize dynamic targets and check both target and `FROM`.
- Before this reconciliation, `source_of_truth_map.md` still listed Tajikistan-style empty panels as unresolved. It now records the required verification instead of assuming a missing implementation.
- The live scripts contain selected-target variables, flags, event-target activation, array normalization, and checks in both scope directions. This is a verification contradiction, not evidence that another targeting system is needed.
- Reconquest resolution currently clears the crisis and resets its component values. It does not turn the manner of victory into a political settlement or lasting aftermath.

This review updates the source map and documentation ledger with these facts and marks the new addendum as proposed rather than implemented. Future implementation must preserve that disposition until the tranche is actually complete.

## Tranche One: Command And Corridors

### Reclassify the existing mission pool

Do not add a parallel objective board. Classify and prioritize the current 118 Soviet missions through three operational families:

1. **Chain of Command** for Moscow Authority and Military Obedience
2. **Corridors and Depots** for Depot Vulnerability, movement, supply, and regional access
3. **Republic Settlement** for Republic Confidence, negotiated control, and targeted breakaway relations

Foreign, League, Old Movement, legal, and regional missions remain in the existing pool. Their conditions should feed one of the three families or act as escalation modifiers.

At each existing refill:

- calculate which operational values are furthest from the posture's safe band
- prioritize at most one mission from each family before filling remaining allowed slots
- suppress missions whose target or required geography no longer exists
- prefer a family that can change the live crisis state over a low-impact helper-only objective
- preserve the existing active-objective cap and refill events

The first pass should add classification flags or scripted triggers and shared prioritization helpers. It should not renumber the 118 mission ids or rewrite all localisation at once.

### Give objectives three outcome shapes

Reuse common effects so objectives produce connected consequences:

- **Decisive success** improves the primary operational value and reduces the release pressure derived from it.
- **Compromise** prevents immediate deterioration but concedes pressure to another component, such as lower Republic Confidence pressure at the cost of Authority or higher League Cohesion.
- **Failure** worsens the primary value, adds release urgency, and records a cause that the next breakaway episode can inherit.

Not every mission needs a new compromise button. Where HOI4 mission structure makes a third action awkward, expose compromise through an existing decision that resolves the active mission. All outcomes must use shared constants and helpers.

### Turn each release into a crisis episode

The progressive release system already chooses staged, pressure-gated candidates and fires cause-specific reports. Extend that flow by recording the dominant operational cause on the released country:

- command fracture
- corridor or depot loss
- negotiated political break
- foreign or League-backed rupture

The cause should influence existing setup values, Moscow's next prioritized family, foreign sponsor interest, and neighboring successor reactions. It must not replace the existing release gates, force a release because time passed, or add a second release scheduler.

### Bind geography to real state conditions

Corridor objectives should identify a limited state target from original Union territory using supported state and building conditions, existing regional classifiers, and current control. Prefer meaningful rail, depot, port, border, or supply geography over named-state flavor alone.

The implementation must first confirm the exact vanilla-supported railway and supply-node triggers and effects. If a valid geographic target does not exist, do not activate that objective. A hardcoded substitute state is not approved.

### Reuse the selected-republic desks

Moscow and foreign patrons already have human-selected target desks. Tranche one should make the selected republic the preferred target for settlement and intervention outcomes where it is eligible.

Before changing logic, prove the scope path for:

- a base republic
- Tajikistan
- a dynamically released non-base republic
- a high-chaos successor
- a target after Union Unmade

The proof must show decision activation, visibility, availability, completion scope, cleanup, and reopening. If those cases pass, close the stale source-map issue without adding code. If one fails, patch the shared dynamic helper. Do not add tag-specific exceptions.

## Focus And Country Integration

Tranche one adds hooks, not focuses.

- Existing focus rewards that promise command, corridors, settlements, or regional authority should feed the shared operational helpers.
- Helper-only rewards should be converted only when they sit directly on the tranche's route and can expose a visible mission, target, state project, or crisis-value consequence.
- UWR should receive crisis-facing AI and contamination aftermath hooks before receiving more focus nodes.
- KMB should receive route AI and its existing treaties and concessions should affect Depot Vulnerability, sponsor pressure, or corridor control before receiving more focus nodes.
- The May 29 custom-splinter, ancient-restoration, OGB, layout, and broad reward backlog remains queued separately.

## AI Behavior

- Moscow AI prioritizes the family whose operational value is most dangerous relative to its current posture.
- It must account for cost, time remaining, target existence, war state, and whether another active mission already addresses the same pressure.
- Breakaway AI responds to its recorded release cause, local institutions, resilience, depot control, sponsor influence, and League membership.
- Foreign AI continues to evaluate the broad dynamic target list. Human players continue to see one selected desk.
- UWR AI should value facilities, payload readiness, controlled contamination, and expansion targets.
- KMB AI should value basin control, rail access, treaties when isolated, and concessions when militarily superior.
- No unrestricted daily, weekly, or monthly all-country loop is introduced.

## Later Tranches

These require separate acceptance after tranche one works:

1. **Patron Rivalry** uses existing influence and patronage values to create competing offers, dependency resistance, and sponsor conflict around one selected republic.
2. **Successor Relations** adds bounded corridor agreements, border arbitration, League obligations, and visible disputes using existing regional and target helpers.
3. **Reconsolidation And Aftermath** snapshots the surviving crisis values before cleanup and produces distinct Soviet settlements or successor outcomes. Reconquest must stop erasing the manner of victory before those outcomes are evaluated.
4. **UWR And KMB Completion** adds UWR field-release and facility decisions, contamination integration for conquerors, KMB treaty competition, conquered-basin policy, route AI, and final asset work through the proper asset workflow.

These labels are design directions, not final player-facing localisation.

## Implementation Surfaces

- `common/script_constants/005_soviet_collapse_constants.txt`
- `common/mtth/005_soviet_collapse_mtth.txt` only if existing release weights need a new recorded-cause input
- `common/scripted_effects/005_soviet_collapse_effects.txt`
- `common/scripted_triggers/005_soviet_collapse_triggers.txt`
- `common/decisions/005_soviet_collapse_decisions.txt`
- `common/decisions/categories/005_soviet_collapse_categories.txt`
- `events/005_soviet_collapse.txt`
- `common/ai_strategy/005_soviet_collapse.txt`
- the four existing Event 005 focus files only for accepted shared hooks
- `localisation/english/005_soviet_collapse_l_english.yml`
- `docs/events/005_soviet_collapse.md`
- `docs/plans/005_soviet_collapse_plans/source_of_truth_map.md`
- `docs/plans/005_soviet_collapse_plans/documentation_state.md`
- relevant canonical specs and the Event 005 spreadsheet row after final wording exists

## Acceptance Scenarios

- A calm, strong-center start does not produce an early non-base release merely because a timer elapsed.
- High command pressure makes command missions more likely without hiding all corridor and settlement play.
- High depot pressure produces a valid geographic objective tied to current Union territory and control.
- Mission success, compromise, and failure alter connected values and the next refill in distinguishable ways.
- A release records a meaningful cause and that cause changes its setup or the next crisis response without bypassing release gates.
- Selected Moscow and foreign desks work for a base republic, Tajikistan, a dynamic non-base republic, a high-chaos successor, and a post-Union-Unmade target.
- UWR and KMB participate in the shared crisis and AI layers without adding focus nodes.
- Reconquest behavior remains unchanged in tranche one except for any non-destructive data capture explicitly needed by a later aftermath plan.
- Terminal, maximum-chaos, and standalone scenario release paths retain their documented exhaustive behavior.

## Do Not Add

- more focus trees or a new broad focus expansion plan
- a second mission board or another large mission batch
- another release scheduler
- static tag lists for intervention visibility
- instant non-base releases in calm worlds
- hardcoded substitute states when no corridor target exists
- a new scripted GUI before the decision and mission loop is coherent
- fallback trees, placeholder country packages, or unreviewed bulk rewards
- asset work before gameplay identifiers and accepted scope are stable
- a world-scanning recurring on-action

No fallback design or simplification is approved in this addendum. Event 005 remains incomplete until its queued focus backlog, AI parity, presentation alignment, assets, and completion audits are resolved.

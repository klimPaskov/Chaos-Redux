# Event 005 Soviet Collapse Improvement Loop Addendum

Date: 2026-07-11

Status: Command and Corridors, Patron Rivalry, Successor Relations, Reconsolidation and Aftermath, and the UWR/KMB follow-up packages are implemented and reconciled through 2026-08-09. The 43-tree and 1,760-focus package has zero semantic shallow-leaf risks, final assets are installed, workbook/CSV parity is complete, and every supported probability surface has complete scenario inputs with zero unresolved items.

Disposition: the 2026-05-29 focus redesign and its former heuristic risk counts remain historical evidence, while the current 43-tree package and semantic reward audit are resolved. This addendum does not duplicate that backlog. Its first tranche is the implemented shared crisis loop, Patron Rivalry events `chaosx.nr5.50` through `chaosx.nr5.70` are implemented, Successor Relations is implemented through three faction packages and charter events `chaosx.nr5.33`, `chaosx.nr5.34`, and `chaosx.nr5.37`, Reconsolidation and Aftermath events `chaosx.nr5.96` and `chaosx.nr5.97` are implemented, and the UWR/KMB package and final-asset work are implemented.

## Verdict

Soviet Collapse does not need more raw content volume. It needs connective mechanics that make its existing values, 118 Soviet missions, staged releases, intervention desks, rail and depot language, successor packages, and end states produce one another.

The smallest coherent implementation is a Command and Corridors tranche. It should organize the existing mission pool around four operational values:

- Moscow Authority
- Military Obedience
- Republic Confidence
- Depot Vulnerability

Foreign Appetite, League Cohesion, and Old Movement pressure remain secondary forces that select targets, amplify consequences, and alter available outcomes. Union Collapse Threat remains the public derived severity.

## Source Reconciliation

The canonical June 5 ledger is historical and must not be used as the current implementation ledger.

- Current Event 005 focus files contain 43 trees and 1,760 focuses: 515 republic focuses, 1,035 custom-splinter focuses, 134 factory-successor focuses, and 76 ancient-restoration focuses.
- The historical promoted ledger recorded 41 trees and 1,698 focuses.
- The 41-tree and 1,698-focus figures are superseded by the current source count and the later UWR/KMB and focus-depth handoffs.
- UWR and KMB now have their implemented specialist packages, dedicated decisions, route-aware AI, and final focus, decision, idea, and UWR flag assets.
- The historical 1,127 helper-only or nearly helper-only reward count and 520 pathline heuristic count are superseded. Recursive review of all 1,760 completion rewards reports zero semantic shallow-leaf risks.
- `docs/events/005_soviet_collapse/overview.md` says selected patron desks normalize dynamic targets and check both target and `FROM`.
- Before this reconciliation, `source_of_truth_map.md` still listed Tajikistan-style empty panels as unresolved. It now records the required verification instead of assuming a missing implementation.
- The live scripts contain selected-target variables, flags, event-target activation, array normalization, and checks in both scope directions. This is a verification contradiction, not evidence that another targeting system is needed.
- Reconquest resolution clears the crisis and resets its component values, while events `chaosx.nr5.96` and `chaosx.nr5.97` turn the manner of victory into a political settlement and lasting aftermath.

The source map and documentation ledger distinguish the implemented Event005 systems, including Successor Relations, and route the completed probability evidence to the 2026-08-09 probability handoff.

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

This section records the historical tranche-one boundary; the later UWR/KMB follow-up package added the implemented specialist focus surfaces documented in the 2026-08-09 handoffs.

- Existing focus rewards that promise command, corridors, settlements, or regional authority should feed the shared operational helpers.
- Helper-only rewards should be converted only when they sit directly on the tranche's route and can expose a visible mission, target, state project, or crisis-value consequence.
- At tranche-one scope, UWR was to receive crisis-facing AI and contamination aftermath hooks before receiving more focus nodes; the later UWR package is implemented.
- At tranche-one scope, KMB was to receive route AI and make its existing treaties and concessions affect Depot Vulnerability, sponsor pressure, or corridor control before receiving more focus nodes; the later KMB package is implemented.
- The May 29 custom-splinter, ancient-restoration, OGB, layout, and broad reward wording is historical planning evidence. The current semantic reward audit resolves its shallow-leaf risk, while any authored-layout work remains a separate parent decision.

## AI Behavior

- Moscow AI prioritizes the family whose operational value is most dangerous relative to its current posture.
- It must account for cost, time remaining, target existence, war state, and whether another active mission already addresses the same pressure.
- Breakaway AI responds to its recorded release cause, local institutions, resilience, depot control, sponsor influence, and League membership.
- Foreign AI continues to evaluate the broad dynamic target list. Human players continue to see one selected desk.
- UWR AI should value facilities, payload readiness, controlled contamination, and expansion targets.
- KMB AI should value basin control, rail access, treaties when isolated, and concessions when militarily superior.
- No unrestricted daily, weekly, or monthly all-country loop is introduced.

## Implementation Evidence

The implemented tranche preserves all 118 mission identifiers and classifies them exactly once as 37 Chain of Command, 21 Corridors and Depots, and 60 Republic Settlement missions. It reuses the existing active-objective cap, monthly refill cap, refill event, progressive release system, and selected-target categories. All 21 corridor missions are bound to a live qualifying state and cancel into refill without success or failure when that state becomes invalid. The opening posture is applied before the first objective fill.

Release causes are recorded before release setup and affect the released country's package, Moscow's next family, sponsor interest, neighboring breakaways, and AI without forcing a release. The five selected-target scope families use one shared lifecycle, retain cooldowns while hidden, and convert to bounded wartime actions after Union Unmade. UWR contamination and KMB treaty/concession hooks feed the shared crisis values, and both countries receive route-aware AI; later UWR/KMB follow-up work also adds their implemented focus surfaces.

Implementation and audit records:

- `subagent_handoffs/2026_07_11_soviet_command_corridors_backend_handoff.md`
- `subagent_handoffs/2026_07_11_soviet_command_corridors_audit.md`
- `subagent_handoffs/2026_07_11_soviet_selected_target_uwr_kmb_audit.md`
- `subagent_handoffs/2026_07_11_soviet_selected_target_lifecycle_handoff.md`
- `subagent_handoffs/2026_07_11_soviet_command_corridors_completion_audit.md`
- `subagent_handoffs/2026_07_11_soviet_localisation_audit.md`

The Event 005 workbook row, event-detail text, evolution-detail text, and generated CSV exports are in exact wording parity according to the 2026-08-09 spreadsheet handoff. The final focus, decision, idea, and UWR flag assets are covered by the 2026-08-09 asset handoffs. The probability completion handoff records complete decision, mission, event-option, random-list, and focus candidate pools with zero unresolved inputs.

## Later Tranches

The following disposition supersedes the original queued wording:

1. **Patron Rivalry** is implemented by events `chaosx.nr5.50` through `chaosx.nr5.70`; no further Event 005 implementation is required for this chain.
2. **Successor Relations** is implemented through the Black International, Free Soviet Congress, and Iron Production Bloc founding decisions, common faction lifecycle, route-sensitive AI, and charter events `chaosx.nr5.33`, `chaosx.nr5.34`, and `chaosx.nr5.37`.
3. **Reconsolidation And Aftermath** is implemented by events `chaosx.nr5.96` and `chaosx.nr5.97`; no further Event 005 implementation is required for this chain.
4. **UWR And KMB Completion** is implemented, including package decisions, route AI, conquered-basin outcomes, contamination and aftermath handling, final icons, and the final UWR flag family.

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
- `docs/events/005_soviet_collapse/overview.md`
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
- UWR and KMB participate in the shared crisis and AI layers, with their later implemented specialist focus packages and final assets.
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

No fallback design or simplification was used for the implemented tranches. Historical handoffs with older focus, asset, map, parity, and partial-probability dispositions remain preserved as evidence and are routed through the current source map rather than treated as active blockers. The compact MCP focus-layout rewrite remains the terminal source mutation.

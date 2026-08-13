# Event 014 Final Completion Reaudit

> Superseded as current specialist authority by the 2026-07-15 consolidation re-audit set. This pre-consolidation completion checkpoint remains historical evidence only and must not override the current package specifications or consolidation reports.

Date: 2026-07-15

Audit basis: the live shared working tree. Current files, including uncommitted Event 014 closure work, were treated as the implementation authority. Historical reports were used only as navigation and were not accepted as proof without checking the current source, assets, documentation, or workbook.

Audit mode: independent definition-level, control-flow, inventory, media-metadata, visual, documentation, manifest, and workbook review. No gameplay, localisation, asset, or workbook file was changed by this audit.

## Verdict

Event 014 Cannibalism is completion-ready against the accepted specification and the full requested goal.

| Severity | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

Completion-ready: YES.

## Required authority and references

The audit followed `AGENTS.md` and the repository skills `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `chaos-redux-focus-trees`, `chaos-redux-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and `xlsx`.

The required offline Paradox wiki pages were consulted for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, national focuses, interfaces, scripted GUI, graphical assets, countries, achievements, divisions, and units. Relevant vanilla documentation was checked for effects, triggers, script concepts, dynamic variables, modifiers, localisation objects and formatters, script constants, decisions, AI strategy, AI templates, on actions, characters, scripted GUI, and factions. Vanilla precedents were checked for triggered events, timed missions, mutual exclusions, focus-tree loading, unit creation, animated sprites, and achievements.

## Acceptance coverage

### Event identity, selection, and runtime

- `events/014_cannibalism.txt` contains the canonical hidden, triggered-only entry `chaosx.nr14.1` and enters through `cannibalism_begin_from_prefire_context`.
- Event 14 is registered in `global.fire_once_events`, classified as Minor Fire-Once, and absent from the event-cluster registry. The workbook cluster cell is empty.
- Initial host and state selection use scored, dynamic pools. Player status, war duration, stability, casualties, manpower, isolation, supply damage, convoy pressure, occupation, population, and Chaos contribute through central constants.
- The runtime uses a ticketed self-scheduling pulse. Event 014 adds no daily, weekly, or monthly whole-world on-action. The one-shot pre-fire `every_country` selection is not recurring global work.
- The seven accepted public meters are wired: Field Hunger, Command Integrity, Cult Cohesion, Network Reach, Larder Stores, Frenzy, and Network Alignment. Their staged visibility and clamps match baseline, ritual, network, warlord, unified, and Wendigo state.

### Evolutions, gameplay depth, and accounting

- The baseline and three true evolutions are implemented as active transitions and pre-fire-capable starts. Evolution I and II activate their real runtime systems; pre-fire Evolution III enters the real convergence transaction rather than assigning a synthetic completion marker.
- Event Log history records the same evolution type, tier, and stage identities for active and pre-fire paths. Event Details exposes two neutral previews before reveal and the third preview only after `cannibalism_reveal_complete`.
- Baseline containment, maintained objectives, response, concealment, exploitation, terror, spread, local victory, reinfection, worldwide victory, reconstruction, and cleanup surfaces are present.
- Population consumption calls the shared exact civilian-population-loss contract. The exact applied loss drives the consumed-population ledger, the Deaths reason or mixed prisoner ledger, Larder yield, recruitment capacity, and cooldown. Failed or zero loss produces no Larder or unit reward.
- Warlord formation and paid recruitment use population-backed manpower and zero-filled unit shells. Normal queue recruitment remains locked. No free manpower, equipment, starting-strength, or duplicate population transaction was found.

### Countries, origins, reveal, and unification

- CBA through CBH are exactly eight origin-agnostic reusable slots with eight neutral country definitions and eight dormant histories. CBL is separate and reserved for ordinary unification.
- Exactly three origins remain: Island Host, Siege Commune, and March Host. Runtime searches found zero retired Prison Host, `prison_host`, `origin_prison`, `warlord_prison_`, `lockhouse`, or `lock_house` identifier.
- Ordinary unification selects a viable human host before the AI score pass, transfers player control before absorption, unions compatible researched technologies, preserves wars and troops, and supports retained command, disposal, autonomy, resistance, and challenge outcomes.
- Wendigo unification requires the live original-tag ZZZ Event 2 identity. It transforms that same country in place, keeps the original ZZZ country and Pack, preserves its technology, ideas, units, recruitment state, equipment, and special-project state, and adds donor technology and troops without creating a replacement ZZZ.
- Both transactions set `cannibalism_reveal_complete` before exposing the Hannibal country, character, portrait, focus tree, reports, news, super-event, or revealed GUI. Public text uses the requested name Hannibal Lecter. No ancient-general or Carthaginian disclaimer appears in Event 014 player-facing localisation.

### Focuses, decisions, counterplay, AI, and terminal routes

- Exact focus counts are 68 Warlord, 108 Unified, and 28 Wendigo, for 204 total. Every focus has a completion reward and `ai_will_do`; the current focus audit found all 204 exclusion-aware reachable.
- The three origin overlays are mutually origin-gated. No fourth-origin branch or residue remains.
- The eight Event 014 decision files contain 127 entries: 109 operational entries plus 18 read-only staged achievement tracker entries. The operational package includes the accepted maintained missions, paid actions, international response, warlord, unified, counterwar, Wendigo, reconstruction, and achievement-support surfaces.
- Exactly 14 timed mission objects exist across the full package. The incarnation reset helper removes the same exact 14-ID set, guards removal with `has_active_mission`, clears family runtime, and keeps terminal global-target cleanup owner-scoped.
- Two country scorers, two decision-weight MTTH entries, and six unified targeted-decision consumers are present. Separate pre-lock and post-lock Wendigo priority passes match the accepted fixed-first-band design.
- The ordinary and Wendigo terminal routes both require `constant:cannibalism_evolution_threshold.world_end_chaos = 1000` through strict `greater_than` or `>` comparisons. The ordinary route also requires the completed operational package and paid final preparation. The Wendigo route requires living anchors, countdown progression, territory, population, victories, authority, Larder, and an unbroken pre-lock transformation.
- Counterwar remains available before lock. The terminal hunt changes transformation progress but does not set `world_end`; only the pulse-owned final lock can complete the Wendigo terminal form.

### Achievements, scenario, and shared integration

- The achievement registry contains exactly 18 Event 014 definitions: five public and thirteen hidden. Each delegates to its matching completion trigger. The Event Details tracker contains exactly 18 permanently unavailable, effect-free, staged entries using the same completion predicates.
- SCN-010 is registry ID 10 and exposes exactly five types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence, across Low, Medium, High, and Maximum intensity.
- Manual launch builds and validates an exact temporary manifest for actors, opening states, external Island/Siege/March states, origin distribution, and reusable slots before runtime mutation. Commit follows exact equality; failed preflight changes only the launcher failure marker and temporary planning state. Automatic Evolution III pre-fire remains on its separate dynamic path.
- Event name, actor mapping, Event Log history, evolution rows, shared threat, defeat contributors, aftermath, reconstruction, triggerable-scenario registry, and cross-event CBRN, Deaths, disaster, famine, camp, Fallout, and Event 2 Wendigo hooks are wired.
- Event Details terminal registry rows are independent: ID 6 is The World Is the Larder with super-event 50, and ID 7 is No Thaw Will Come with super-event 53. Both are hidden before reveal and use distinct disable-array IDs and active flags.
- Final cleanup clears the live actor, node, route, spread-queue, scenario, convergence, unification, terminal, threat, meter, and scheduler state while retaining historical Event Log snapshots.

## Independent inventory and media proof

| Surface | Independent result |
| --- | --- |
| Focus trees | 68 / 108 / 28; 204 AI blocks; 204 completion rewards |
| Decision entries | 127 total; 109 operational; 18 read-only tracker |
| Timed missions | 14 defined; exact 14-ID reset set |
| Achievements | 18 registry definitions; 18 tracker entries; 54 state sprites |
| Runtime GFX | 812 references; 598 unique paths; 0 missing; 598 unique hashes |
| Flags | 195 TGA files; 65 per tier; 82x52, 41x26, and 10x7; 195 unique hashes |
| Regional portraits | 56 DDS files; all 156x210; 56 unique hashes |
| Nonportrait animations | 12 packages; 114 source frames and 114 processed frames; every package has sheet, fallback, preview, manifest, and unique frames |
| Leader animations | Ordinary 12 unique source and processed frames; Wendigo 16 unique source and processed frames; live 12/16-frame declarations at 12 FPS |
| Super-event images | 4 unique registered 457x328 DDS files |
| Audio | 4 OGG plus 4 WAV; all stereo 44.1 kHz; 8 unique hashes; IDs 49, 50, 52, and 53 |

Direct contact-sheet review confirmed that the 56 warlord portraits are distinct, feral, close-framed HOI4-style male portraits without prison settings. The CBA South America skull-lick composition is present. The 195 flags are flat 2-to-4-color designs rather than physical flag mockups. The four super-event scenes are action-heavy and distinct: pursuit at reveal, a capital overrun, a defender breakthrough and rescue, and a frozen Pack hunt. The animation packages contain semantic frame progression rather than transform-only movement of one still.

The audio registry assigns six settings-aware variants to each of IDs 49, 50, 52, and 53. Metadata checks found Vorbis OGG and PCM s16le WAV at 44.1 kHz stereo, with paired durations of 114.0, 120.0, about 116.1, and 118.0 seconds. Source, license, attribution, excerpt, and processing evidence is present, including the required share-alike attribution for ID 52. Event 014 does not use ID 51.

## Documentation, addenda, manifest, and workbook

- All 12 source specification parts, 10 matrices, 9 prompts, 4 focus graphs, quality files, research files, the canonical event document, and current system documentation agree on the live three-origin, 68/108/28-focus package.
- Both accepted improvement-loop addenda are marked accepted, implemented, audited, and promoted. H-01, H-02, H-03, M-01, the additive technology union, and the 38 distinct unified decision icons are closed. Optional ideas A through C remain explicitly queued and unaccepted, so they are not accepted completion debt.
- `docs/specs/014_cannibalism_specs/PACKAGE_MANIFEST.md` was independently recalculated against every package file: 43 rows, 43 unique paths, 43 actual files, 0 missing, 0 unlisted, 0 byte mismatches, 0 LF-line-count mismatches, and 0 SHA-256 mismatches.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` has SHA-256 `6aa758d699d814599a1011d5f9acc1089bbf42baf053be7a4dbabadd525091a2`. `Events!A15:M15` matches Event 014, its three evolution titles, both terminal descriptions, Minor Fire-Once classification, empty cluster, and `Fully Functional` status. `Scenarios!A10:F10` matches SCN-010, all five type names, four intensity descriptions, and `Fully Functional` status.
- The Events table covers `A1:M1015`; the Manual Scenarios table covers `A1:F11`, preserving concurrent SCN-013. Status validation uses the current `Fully Functional` vocabulary. The workbook contains zero formulas and zero formula-error values. Event 014 and SCN-010 conditional-formatting cells are covered.

## Current specialist audit cross-check

The current 2026-07-15 country-package, decision/mission, focus-tree, localisation/asset, spreadsheet, super-event visual, documentation, improvement-loop, and integration/catalog audits were read after the independent checks. Each reports P0/P1/P2/P3 at zero in its assigned scope. Their inventories and dispositions agree with the live tree and with this audit.

This report is superseded as the current completion authority by the forthcoming Event 014 consolidation completion audit. Its animation-rate statement above was reconciled to the live 12 FPS GFX declarations during the consolidation improvement-loop pass.

## Validation boundary

This is a source, control-flow, asset, media, documentation, and workbook audit. It does not claim that a live HOI4 runtime session was performed. The completion verdict is based on the accepted definition-level contract, reachable scripted control flow, exact inventory reconciliation, direct visual inspection, and current authority alignment.

## Files changed by this audit

- `docs/plans/014_cannibalism_plans/audits/event014_final_completion_reaudit_2026-07-15.md`

No gameplay, localisation, interface, asset, audio, spreadsheet, specification, or existing audit file was changed. No commit was created.

## Simplifications, omissions, fallbacks, and blockers

None. No accepted route, country package, focus branch, decision family, mission cleanup, AI equivalent, achievement, scenario type, terminal row, localisation surface, asset, audio cue, documentation surface, spreadsheet field, or accepted addendum remains missing or simplified. No fallback, placeholder, weaker substitute, or blocker was found.

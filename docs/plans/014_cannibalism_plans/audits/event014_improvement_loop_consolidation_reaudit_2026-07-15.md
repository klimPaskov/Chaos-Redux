# Event 014 Improvement-Loop Consolidation Re-audit

Date: 2026-07-15

Historical-scope notice: this audit and its P0/P1/P2/P3 counts apply only to the frozen 2026-07-15 mechanics and presentation scope. They are not current full-package completion evidence. The 2026-08-26 decision explicitly approves vanilla `sprite = cavalry` for Bone Riders and vanilla `sprite = infantry` for Network Cadre, so their former custom-model work is superseded rather than an open blocker; current portrait, MCP, probability, provenance, live-consumer, super-event image, and catalog gates remain tracked in the current resume packet.

Scope: final recursive improvement-loop and consolidation audit of the implemented Event 014 Cannibalism package. This pass reads the current source rather than treating an earlier completion report as proof. It covers the 23 dedicated merge-safe script, GUI, and localisation loader files, all twelve source-spec parts and their matrices, the canonical Event 014 documentation, both improvement-loop addenda, current asset manifests and production handoffs, and the current country, decision, focus, localisation/asset, spreadsheet, super-event, documentation, integration/catalog, and completion audits.

## Verdict

Event 014 retains its full accepted design after 93 dedicated Event 014 script, GUI, and localisation loader files were consolidated into 23 merge-safe files. The 23 are the practical minimum of one dedicated file per incompatible HOI4 loader schema. Per-tag country and history files, engine flag ladders, binary assets, and shared global registries remain structurally separate and are not counted as merged. Both accepted improvement-loop addenda are implemented and promoted into the source specifications. No accepted mechanic has been silently dropped, no fourth warlord origin has returned, and no material gameplay, AI, integration, localisation, or asset gap remains in the audited scope.

| Priority | Open findings |
| --- | ---: |
| P0 | 0 |
| P1 | 0 |
| P2 | 0 |
| P3 | 0 |

The only correction made by this audit was documentation-only: the older final-completion audit's Hannibal animation row was reconciled from 6 FPS to the live 12 FPS declarations and marked as superseded by the consolidation completion authority. No gameplay or asset file was changed.

## Required references and method

The audit followed `AGENTS.md` and the repository skills `chaos-redux-improvement-loop`, `chaos-redux-event-planning`, `chaos-redux-events`, and `chaos-redux-subagents`.

The required offline Paradox wiki snapshot was consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus modding, AI focuses, Country creation, Division modding, Unit modding, Achievement modding, Interface modding, and Scripted GUI modding. No Paradox wiki web page was used.

Relevant official vanilla documentation was checked for script concepts and script constants, effects, triggers, modifiers, dynamic variables, decisions, on actions, scripted GUIs, characters, AI strategies, and AI templates. Vanilla implementations were used as the structural comparison set.

The current files were traced directly across entry dispatch, the ticketed pulse, evolution scheduling, route effects, exact population loss, state recovery, spread, convergence, both unification branches, both terminal branches, AI, achievements, scenario setup, Event Details, Event Log, world threat, and cleanup. A fresh `hoi4.event_inspect` artifact could not be emitted because the MCP artifact store returned `ARTIFACT_STORAGE_LIMIT`; direct source inspection and the current rendered focus/audit evidence were used instead. This is an audit-tooling limitation, not a source finding, and this report does not claim a live game session.

## Consolidation integrity

The live package has exactly 23 dedicated Event 014 merge-safe files in the normal HOI4 script, GUI, and localisation loader surfaces. They are the practical minimum of one dedicated file per incompatible loader schema. All 23 expected paths exist and no extra pre-consolidation Event 014 loader fragment remains active. Per-tag country and history files, engine flag ladders, binary assets, and shared global registries remain structurally separate and are outside this 93-to-23 count.

### Thirteen merged loaders

1. `common/country_leader/014_cannibalism_traits.txt`
2. `common/decisions/014_cannibalism_decisions.txt`
3. `common/decisions/categories/014_cannibalism_categories.txt`
4. `common/dynamic_modifiers/014_cannibalism_dynamic_modifiers.txt`
5. `common/ideas/014_cannibalism_ideas.txt`
6. `common/national_focus/014_cannibalism_focus.txt`
7. `common/script_constants/014_cannibalism_constants.txt`
8. `common/scripted_effects/014_cannibalism_effects.txt`
9. `common/scripted_localisation/014_cannibalism_scripted_localisation.txt`
10. `common/scripted_triggers/014_cannibalism_triggers.txt`
11. `events/014_cannibalism.txt`
12. `interface/014_cannibalism.gfx`
13. `localisation/english/014_cannibalism_l_english.yml`

### Ten retained singleton loaders

1. `common/ai_strategy/014_cannibalism_warlords.txt`
2. `common/characters/014_cannibalism_characters.txt`
3. `common/country_tags/014_cannibalism_countries.txt`
4. `common/mtth/014_cannibalism_mtth.txt`
5. `common/on_actions/014_cannibalism_on_actions.txt`
6. `common/opinion_modifiers/014_cannibalism_opinion_modifiers.txt`
7. `common/scorers/country/014_cannibalism_target_scorers.txt`
8. `common/scripted_guis/014_cannibalism_scripted_gui.txt`
9. `history/units/014_cannibalism_dormant.txt`
10. `interface/014_cannibalism_frontline_hunger.gui`

Consolidated section ordering preserves definition identity and the live loader roots remain singular. Current inventories contain 204 focus nodes, 127 unique decision IDs, and 19 unique `chaosx.nr14.*` country-event IDs. The three focus trees contain exactly 108 unified nodes, 68 warlord nodes, and 28 Wendigo nodes.

## Accepted improvement-loop dispositions

No accepted addendum remains only in a plan. The two addenda have the following final dispositions.

| Addendum item | Final disposition | Current implementation evidence |
| --- | --- | --- |
| H-01 reusable target scoring | Accepted, implemented, audited, promoted, closed | Two country scorers, shared score predicates/constants, two MTTH decision weights, six unified targeted-decision consumers, pre-lock Wendigo priorities, and post-lock terminal priorities remain live in the scorer, MTTH, consolidated trigger/effect, decision, and AI surfaces. |
| H-02 paid terminal hunt | Accepted, implemented, audited, promoted, closed | Launch, 120-day maintained mission, paid pressure, and defender-break surfaces share one persistent target and complete success, failure, timeout, route-break, invalidation, capitulation, and cleanup handling. The hunt changes bounded transformation progress and never sets `world_end`. |
| H-03 tuning normalization | Accepted, implemented, audited, promoted, closed | The accepted normalization and narrow semantic/engine exception ledger is reflected in the consolidated constants. Obsolete small/medium reward-ladder identifiers are absent; current focus balance audits report no residual tuning finding. |
| M-01 deeper Wendigo progression | Accepted, implemented, audited, promoted, closed | The existing 28-focus overlay owns the receipt-backed Pack muster, three Pack support stages, three inherited origin-template stages, two commander stages, inherited winter cells, and the terminal hunt without adding filler focuses. |
| Constituent technology union | Accepted, implemented, audited, promoted, closed | `union_compatible_researched_technologies_from_donor` is defined and documented in the shared dynamic effects and is called before annexation for opening CBL creation, later absorption, and the primary donor absorbed into the in-place Wendigo host. |
| Thirty-eight unified decision icons | Accepted, implemented, audited, promoted, closed | The 38 retained unified decisions, 38 GFX sprite names, and 38 final decision DDS paths remain a one-to-one set with independently generated source/processed evidence. |

Optional ideas A-C in `2026-07-12_event014_post_implementation_closure_addendum.md` remain explicitly queued and unaccepted:

- cross-origin joint operations;
- route-aware recovery case files; and
- inspection-access compacts.

Their non-implementation is the recorded design disposition and has no current completion impact. The anti-bloat stop condition remains appropriate: no additional tag family, origin, focus tree, evolution, terminal, achievement set, meter, currency, faction, or scripted GUI is required by the accepted tranche.

## Recursive gameplay audit

### Baseline, routes, and evolutions

- `chaosx.nr14.1` remains the single hidden fire-once entry. It consumes a generation-safe pre-fire host/state transaction and cannot reuse an already consumed generation.
- The opening incident presents open emergency, concealment, and exploitation. Their effects set distinct route flags, meter changes, political consequences, achievement state, and AI preferences. Evolution I and II each add another three-way response rather than collapsing the routes into cosmetic text.
- Evolution I, II, and III have active-runtime and pre-fire handling. The recorded Event Log type, tier, and stage are shared across both entry modes. Evolution III cannot be previewed publicly before `cannibalism_reveal_complete`.
- Evolution scheduling uses qualified actors, MTTH dates, actor generations, convergence entry conditions, and an interruptible convergence window. Failed conditions break convergence and apply the existing rebuild cooldown rather than forcing the reveal.
- The event-owned pulse is ticketed and self-scheduling. Its actor, objective-country, node, recovery, spread, and warlord-release work uses canonical arrays; Event 014 adds no daily, weekly, or monthly all-country on-action.

### Objectives, decisions, spread, victory, and cleanup

- The consolidated decision file retains 127 unique decision IDs and all eight maintained objective families plus paid ordinary, international, unified, warlord, Wendigo, counterwar, achievement-tracker, and aftermath surfaces. The current decision audit proves AI coverage for all 95 selectable non-mission decisions and complete trigger/text coverage for all 94 paid decisions.
- Objective state uses persisted targets, due dates, capped progress, actor/node generations, and explicit full, partial, failure, timeout, and cancellation outcomes. Objective work is registered only for countries that own active Event 014 objectives.
- Foreign spread remains a generation-safe parallel-array queue. It proves physical convoy, conquest, occupation-turnover, volunteer-return, or inherited route state; supports humane and hard screening; invalidates stale country/state lifecycle references; and distinguishes a new external actor from reinfection of an existing actor.
- Country and state lifecycle on-actions invalidate spread entries, rehome the single pulse callback, release reusable slots, and preserve owner-safe cleanup. There is no Event 014 periodic whole-world on-action.
- Local victory requires suppressed meters, no active cell, no warlord on national territory, no inbound route, and a stabilization interval. Global victory requires zero remaining Event 014 residue for its own stabilization interval.
- Final cleanup clears active system, pulse, convergence, unification, target, objective, anchor, spread, and threat state, resizes the live arrays, and preserves Event Log history snapshots. A later manual scenario can prepare a clean runtime only after residue is absent.

### Population, Larder, recovery, and cross-system state

- `cannibalism_consume_current_state` delegates civilian removal to the canonical exact state-population-loss effect, carries a request ID, rejects duplicates, records the Deaths reason once, and derives Larder and recruitment yield only from the returned applied loss.
- Percentage and exact-request modes share the same transaction. Minimum remaining population, state usability, cooldowns, diminishing returns, contamination penalties, and Larder caps remain dynamic.
- Prisoner feeding separates the civilian and military death channels instead of duplicating the civilian entry. The Deaths-disabled route still removes population and does not create recruitable manpower from an unrecorded loss.
- Recovery changes state stage and modifiers but never restores consumed population. Former feeding-state and reconstruction ledgers survive long enough for achievement and aftermath use.
- Nuclear fallout, severe biological and chemical contamination, Death-consumed state, nonhuman ownership, and unusable population exclude Larder use. Famine, locust, disease, disaster supply, camp, relief, air contamination, and shared CBRN state remain read through their canonical integrations.

### Warlord origins and country lifecycle

- CBA-CBH remain eight symmetric, reusable, origin-agnostic country slots. Allocation, validation, quarantine, release, naming, region selection, and player-control handling are identical across the slots.
- Exactly three origins exist: Island Host, Siege Commune, and March Host. No `Prison Host`, `prison_host`, `origin_prison`, `warlord_prison_host`, `lockhouse`, or `lock_house` identifier exists in the live Event 014 runtime/localisation surface.
- The warlord tree contains exactly 68 nodes with one four-focus overlay for each accepted origin. Origin operations, route identity, templates, AI strategy, unification inheritance, and cleanup agree on the same three-origin enumeration.
- Formation and later recruitment pay exact state population before manpower or a zero-filled unit is created. The reusable dormant tags do not carry free divisions, manpower, equipment, templates, route state, or portrait identity between incarnations.
- The live warlord portrait set contains 56 files, seven regions for each of eight slots. Direct hash inspection found 56 unique SHA-256 values. The current visual/provenance audits confirm distinct disturbing HOI4-readable faces and actions with no prison cell, bars, cage, restraints, prisoner uniform, or prison-origin setting.

### Convergence, unification, and inherited state

- Ordinary convergence selects a viable warlord host and creates CBL only after the public reveal flag is set. The source host's actor generation, state, route, Larder, commander, population-loss, template, war, technology, and achievement state are migrated before annexation.
- Later warlords can submit with retained command, surrender the warband, bargain for autonomy, resist, or challenge. Human-player branches prevent silent displacement; dual-human ordinary and Wendigo cases remain protected.
- Technology inheritance is additive. The initial donor, later absorbed donors, and Wendigo primary donor feed the shared technology-union helper before annexation, while mutually exclusive industry branches remain recipient-safe. The recipient retains its own research and research slots.
- If a valid live Event 2 Wendigo exists, the exact original-tag ZZZ survivor is selected and mutated in place. Its country scope, player control, territory, units, technology, ideas, paid recruitment state, and special-project state survive; no replacement Wendigo tag or reconstructed fallback package exists.
- The public characters are `CBL_hannibal` and `ZZZ_hannibal_wendigo`, both localised exactly as `Hannibal Lecter`. Current player-facing source contains no Carthaginian, Punic, ancient-general, or identity-disclaimer wording.

### Unified and Wendigo focus routes

- The unified tree retains exactly 108 manually authored nodes, multiple route families, inherited-origin knowledge, command, Larder, army, naval, air, counterwar, global campaign, operational-package, and ordinary terminal branches. All four Last Table preparation packages and the paid final mobilization remain required.
- The Wendigo overlay retains exactly 28 nodes. It preserves the existing Pack, binds inherited Event 014 units and commanders, opens the Winter Network, counts distinct winter victories, manages anchors, enables paid Pack musters, opens counterwar, starts the countdown, and completes the alternate terminal route.
- H-01 scoring remains consumed by the six specified unified decisions and by pre-lock/post-lock Wendigo strategy effects. Invalid nonhuman, allied, capitulated, unreachable, or unusable-population targets are excluded rather than receiving token scores.
- H-02 terminal-hunt success comes from target capitulation or capital control at full pressure. Failure can come from defender pressure, timeout, route break, invalidation, actor loss, war ending, or anchor loss. A success adds only five progress and a failure removes ten; neither path sets the world end.
- M-01 enemy-death receipts are non-retroactive permission tokens sampled only against current enemies, capped at two per enemy epoch and five held, and reset across inactive enemy periods. A receipt muster still pays one receipt, exact controlled state population, Larder, infantry equipment, and support equipment before it creates a zero-start Pack.
- Three idempotent Pack stages, three inherited origin stages, and two commander stages remain attached to existing focus rewards. The inherited winter-cell operation targets an already existing enemy cell, pays its costs, applies bounded disruption, and cannot create a cell, unit, population, Larder, equipment, or war goal.

### Terminal gates

- `constant:cannibalism_evolution_threshold.world_end_chaos` is exactly `1000`.
- Ordinary focus availability, ordinary terminal execution, the Wendigo countdown gate, Wendigo terminal locking, and achievements 15 and 16 use strict `greater_than` or `>` comparisons. A Chaos value of exactly 1000 is insufficient.
- The separate `constant:cannibalism_delta.world_end_chaos = 80` is an active post-terminal Chaos change consumed by `cannibalism_try_start_ordinary_world_end`; it is not the terminal threshold and is not stale.
- The ordinary terminal additionally requires the unified operational packages, readiness flags, paid mobilization, controlled-state, population, Network Reach, and Larder gates.
- The Wendigo terminal additionally requires the Winter Network, completed route, live anchors, controlled territory, consumed population, distinct winter victories, authority, Larder, countdown progress, and an unbroken transformation. Only `cannibalism_process_wendigo_transformation_pulse` can apply the final lock and set `world_end`.
- Before lock, anchor assault, logistics disruption, recruitment-site destruction, terminal-hunt counterpressure, capitulation, and complete anchor loss remain real counterplay. The locked form is the accepted effectively invincible terminal state.

### Achievements, SCN-010, Event Details, and Event Log

- The achievement registry contains exactly 18 Event 014 definitions. The consolidated trigger file contains 18 matching completion contracts and the decision tracker contains 18 matching read-only entries with staged spoiler-safe visibility.
- SCN-010 remains registry ID 10 and has exactly five types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence. Atomic preflight, four shared intensity levels, cleanup, achievement disqualification, and the exact three-origin destructive setup remain intact.
- Event 014 is still Minor Fire-Once and outside every event cluster. The authoritative workbook keeps Event 014 and SCN-010 at `Fully Functional`, with the baseline, three evolution columns, two terminal descriptions, and five scenario types matching live localisation.
- Event Log actor mapping uses the initial host and then the latest live actor, while recorded history snapshots survive runtime target cleanup. Event Details has separate pre-reveal and revealed descriptions and exposes exactly three evolution previews, with Evolution III and both terminal rows gated behind the public reveal.
- The two terminal registry rows remain independent: `world_is_the_larder` and `no_thaw_will_come`, with separate scenario IDs, super-event IDs, flags, toggles, and details.
- Shared world threat is set and cleared only through `world_threat_source_cannibalism` plus the shared refresh effect. Final cleanup removes the source and refreshes the aggregate threat state.

## Hard asset and presentation constraints

- The Event 014 flag family contains 65 independently image-generated flat source layouts and 195 runtime TGAs across normal, medium, and small sizes. Current provenance records contain 65 distinct built-in image-generation calls, 65 retained source masters, and unique source/final hashes. The CBA-CBH subset has 120 runtime TGAs with 120 unique hashes.
- The flags are front-facing, opaque, mechanically flattened vexillological designs. No fabric scene, pole, perspective mockup, palette-swap substitute, traced emblem, or borrowed sacred motif is accepted in the current production record.
- All 56 live warlord portraits are separate 156x210 DDS files with 56 unique hashes. The two current refresh handoffs preserve independent ImageGen provenance, processed PNGs, contact sheets, and visual review.
- `GFX_portrait_CBL_hannibal` and the ordinary GUI static bind directly to `gfx/leaders/014_cannibalism/hannibal.dds`. `GFX_portrait_ZZZ_hannibal_wendigo` and the transformed GUI static bind directly to `gfx/leaders/014_cannibalism/hannibal_wendigo.dds`.
- The ordinary leader sheet contains 12 genuine frames and the Wendigo sheet contains 16 genuine frames. Frame `000` is the supplied canonical static in each package; the remaining frames are separate image-generated action states rather than transform-only motion. The live declarations play at 12 FPS with the vanilla blend-frames effect.
- Twelve non-portrait animation packages retain planned source frames, sheet DDS files, static fallbacks, preview GIFs, contact sheets, manifests, and GFX/GUI handoffs. Together with the two portrait sheets, Event 014 has exactly 14 semantic animation packages with 142 genuine source and 142 processed frames. They are not single-image move/scale/rotate/filter animations.
- Exactly three GFX files reference Event 014: the dedicated `interface/014_cannibalism.gfx` registry and the shared `interface/chaosx_pictures.gfx` and `interface/chaosx_super_events.gfx` registries. Their 812 references resolve to 598 unique existing Event 014 texture paths with 598 unique hashes and no missing runtime file. The 204 focus icons, 135 decision/category textures, 18 achievement triplets, 21 closure assets, and four distinct action-oriented super-event images remain wired.
- Pre-reveal events, focuses, decisions, GUI, Event Details, evolution previews, achievements, portraits, and audio metadata do not expose Hannibal Lecter. Public reveal and transformed presentation consistently use the exact name without an ancient-general disclaimer.

## Balance and AI findings

No balance or AI repair target remains open.

- Opening and evolution response AI weights distinguish government, integrity, stability, and route state.
- Warlord AI has a common reusable-slot profile plus one self-removing profile for each of the three accepted origins.
- Selectable decisions have current AI coverage, paid actions retain affordability gates and reserve-aware weighting, and maintained missions have defined timeout behavior.
- The shared target scorer excludes invalid targets and then applies population, supply, cell, prison/camp, port, stability, adjacency, route, coalition, enemy, cold-front, and overextension factors. It is consumed rather than existing only as documentation.
- Warlord and unified recruitment are population-backed; Wendigo receipts do not mint resources; complete Pack batches must fit capacity; terminal progress is bounded; and repeated capitulation/state callbacks are deduplicated.
- Focus reward values, stability/war-support totals, timed effects, decision costs, cooldowns, route locks, mission durations, Larder caps, and AI strategy bands remain centralized in the consolidated constants or the documented narrow field-scoped constants.

## Documentation reconciliation performed

This audit changed one existing report in addition to creating this file:

- `docs/plans/014_cannibalism_plans/audits/event014_final_completion_reaudit_2026-07-15.md`
  - corrected the live Hannibal animation declaration from 6 FPS to 12 FPS; and
  - marked that older completion audit as superseded by the consolidation completion authority.

The concurrent localisation/asset consolidation audit owns the same reconciliation in its assigned current asset report. Historical production handoffs remain historical records rather than current runtime authority.

No gameplay file, localisation file, visual/audio asset, workbook, or source specification was edited by this audit. No commit was created.

## Simplifications, omissions, fallbacks, and blockers

No implementation simplification, accepted-item omission, fallback, placeholder, weaker substitute, or unresolved gameplay blocker was found.

The three optional future ideas remain queued by explicit design disposition and are not accepted omissions. The MCP artifact-storage limit prevented a new event-inspection artifact, but it did not prevent direct source inspection or reconciliation against the current specialist audits and therefore is not a completion blocker. This source-level audit does not claim that a live HOI4 runtime session was performed.

## Completion disposition

The improvement loop should stop at the accepted anti-bloat boundary. Event 014's baseline, three evolutions, player routes, maintained objectives, physical spread, local/global victory, recovery and cleanup, three origins, population accounting, convergence, both unification branches, 68/108/28 focus trees, 18 achievements, SCN-010, AI, cross-event integrations, world threat, Event Details, Event Log, asset package, and both strict-greater-than-1000 terminal routes are present in the consolidated implementation. P0/P1/P2/P3 remain zero.

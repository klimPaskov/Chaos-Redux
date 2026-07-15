> **HISTORICAL / SUPERSEDED CHECKPOINT (2026-07-13)**
>
> This audit predates the 2026-07-15 removal of the fourth origin. Its four-origin, 72/108/28 focus, 208-focus-icon, 816-reference, and accepted-P3 statements are preserved below as checkpoint evidence only. Current authority is the 2026-07-15 country-package, decision/mission, focus-tree, improvement-loop, asset, and documentation re-audit set. Do not use this file as current completion proof.

# Event 014 final completion audit — 2026-07-13

## Verdict

**COMPLETION-READY for the frozen Event 014 Cannibalism scope.**

| Severity | Remaining finding groups | Verdict |
| --- | ---: | --- |
| P0 | 0 | No load, data-corruption, player-control, population-accounting, or terminal-path blocker found. |
| P1 | 0 | No missing required route, system, AI path, localisation surface, runtime asset, achievement, or integration found. |
| P2 | 0 | The accepted closure behavior is promoted into the current source specs, matrices, canonical event document, asset manifests, and audit handoffs. |
| P3 | 1 | A pre-lock Wendigo target keeps its first assigned AI score band until the separate post-lock rescore. This is the explicitly accepted, bounded engine limitation in the source contract and is not a completion blocker. |

No fallback, placeholder, omitted route, generic substitute, unapproved simplification, missing AI equivalent, missing localisation, missing runtime texture, or stale accepted-plan disposition remains in the audited scope.

Current catalog note, 2026-07-15: the authoritative workbook and matching helper record `Events!M15` and `Scenarios!F10` as `Fully Functional`. The preserved 2026-07-12 promotion report and older body text below use the catalog vocabulary that was current at that checkpoint; they are historical evidence rather than current status. The canonical event document and current package-status, validation, README, and integration-audit surfaces use the live vocabulary.

## Audit boundary and required references

This was a read-only, definition-level final audit of the live working tree against the complete source package under `docs/specs/014_cannibalism_specs/`, both accepted improvement addenda, the canonical event document, current audit handoffs, asset manifests, workbook re-audit, and all Event 014 gameplay, localisation, interface, graphics, audio, history, focus, decision, achievement, event-log, Event Details, scenario, and integration files. No gameplay or asset file was edited by this audit.

The offline Paradox wiki snapshot was consulted for Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, National focus, Country creation, Achievements, Interface modding, Scripted GUI modding, Graphical assets, Portrait modding, and Sound modding. The corresponding vanilla documentation and live vanilla precedents were consulted, including script concepts and constants, triggers, effects, localisation, focus-tree, decision, achievement, event, AI, country, graphical, and sound definitions. No online Paradox wiki source was used.

The live change surface remains Event 014-scoped. Relative to baseline `ac80683de`, the tracked diff contains 140 files: 22 under `common/`, 96 under `docs/`, one event file, 18 `gfx/` files, one interface file, and two localisation files. Current untracked additions inspected by this audit are likewise Event 014 specs, plans, gameplay packages, or assets; no unrelated subsystem change was attributed to this completion verdict.

## Acceptance evidence

### Classification, entry, and cadence

- Event 014 remains one `Minor Fire-Once` entry with an empty cluster field. `constant:cannibalism_event.id` is registered in `global.fire_once_events`, and the hidden triggered-only root remains `chaosx.nr14.1`.
- The live event file contains 17 Event 014 event definitions: `.1`, `.2`, `.10`, `.20`, `.21`, `.30`, `.60`, `.61`, `.62`, and `.70` through `.77`.
- The system advances through actor-owned pulse scheduling and narrow hooks. Event 014 adds no `on_daily`, `on_weekly`, or `on_monthly` world iteration. The one-time initial-host/scenario selection scans are not recurring world cadence.
- The host is selected dynamically from at-war, non-capitulated, ordinary human countries with fielded divisions. Country pressure and highest-risk state selection are scored from war duration, stability, war support, casualties, manpower, isolation, supply, convoy pressure, occupation, infrastructure, damage, port access, population, and related crisis state rather than a fixed tag or state.

### Core simulation, evolutions, and secrecy

- All seven required values are live: Field Hunger, Command Integrity, Cult Cohesion, Network Reach, Larder Stores, Frenzy, and Network Alignment. Script constants own tuning, while GUI and decision surfaces expose only values appropriate to the current phase.
- The baseline policy routes, local containment and defeat, global containment and defeat, reinfection, spread warning, and counterplay paths are wired to real triggers and cleanup.
- Evolution I, Evolution II, convergence, and Evolution III use actor-generation-safe scheduling and current actor targets. Evolution log records are emitted through the shared event-log contract.
- `cannibalism_reveal_complete` is set before the ordinary unified or Wendigo packages expose country identity, leader, portrait, focus, decision, news, super-event, achievement, or Event Details text. The localisation re-audit found no pre-reveal Hannibal, Wendigo, final portrait, or terminal-route disclosure.
- Event Details has separate post-reveal ordinary and Wendigo terminal rows, each with its own selected title/body, persistent enable state, detail-panel route, and automatic-selection gate.

### Population, Deaths, and recovery

- Every gameplay population-consumption context routes through the canonical exact state-civilian-population-loss transaction. Hunting, feeding, silent-host, recruitment, emergency, battlefield, warlord, and prison contexts establish a request identifier and state/country context before resolution.
- Duplicate request IDs are rejected, unusable states are rejected, a configurable minimum population is preserved, and the requested loss is capped by the currently removable population. Diminishing availability and contamination factors affect actual loss rather than bypassing the transaction.
- Larder gain, global consumed-population totals, state-stage consequences, and country meter changes derive from the actual applied loss. Prisoner feeding records its civilian and prisoner components once rather than double-counting the same death.
- Recovery and reconstruction operate on the state ledger and cannot silently recreate consumed population. No direct parallel population subtraction was found on an Event 014 gameplay path.

### Countries, focus trees, and player preservation

- Eight reusable warlord slots, `CBA` through `CBH`, are registered with history packages, lifecycle cleanup, generation guards, and four authored origin packages: Island Host, Siege Commune, Long March Host, and Prison Republic.
- The regional warlord tree contains exactly 72 focus definitions. The ordinary unified tree contains exactly 108. The Wendigo overlay contains exactly 28. No duplicate focus ID was found in any of the three files.
- Warlord creation, submission, resistance, player switching, retirement, and slot reuse preserve or explicitly route human control. Ordinary unification uses `change_tag_from` before absorption when the selected human host becomes `CBL`.
- Wendigo convergence selects the surviving original `ZZZ` and mutates it in place. Territory, units, technologies, ideas, equipment, Event 2 profile state, and human control are preserved; a human donor is transferred before absorption when the selected `ZZZ` is AI, while conflicting human ownership retains an authored response route.
- The base Wendigo Pack remains a locked 16-battalion template. Normal queue recruitment is closed at merge. Paid two-Pack and receipt-backed one-Pack musters validate the complete requested batch before population or Larder payment and create zero-start formations.

### Decisions, missions, achievements, and AI

- The current decision matrix contains exactly eight maintained mission families and seven added paid-action families. The six newer objective missions have full, partial, failure, timeout, invalid-target, and generation-safe cleanup; the two earlier maintained missions retain their existing complete contracts.
- Wendigo closure adds four terminal-hunt surfaces, one enemy-death receipt muster, and one inherited-winter-cell operation. The hunt has one target lock, a 120-day mission, paid attacker pressure, paid defender counterpressure, success/failure cleanup, and no direct world-end effect.
- Exactly 18 real predicate-based achievements are registered. The separate 18-entry tracker is presentation-only, reads those same completion triggers, has no effects or parallel completion ledger, and reveals late entries only at their proper public stage.
- Exactly two country scorers and two MTTH decision-weight entries implement the shared hard-validity/factor contract. Exactly six unified targeted-decision consumers use `cannibalism_unified_target_decision_weight`.
- Pre-lock Wendigo target priority is idempotent per target through `cannibalism_wendigo_prelock_scored_priority_targets`; repeated focus milestones discover new valid targets without stacking the same target package. The terminal lock applies a separate one-time post-lock scan.
- All 208 focuses have AI weights. Paid Pack, receipt, inherited-cell, terminal-hunt, ordinary unified, counterwar, and terminal paths retain their resource and reserve gates for AI as well as humans.

### Terminal branches, scenarios, and integrations

- The ordinary ending requires its complete route, the independent `world_end_cannibalism_ordinary_scenario_enabled` gate, and Chaos strictly greater than 1000. It cannot start when its Event Details scenario is disabled.
- The Wendigo ending requires the complete countdown/route state, the independent `world_end_cannibalism_wendigo_scenario_enabled` gate, and Chaos strictly greater than 1000. `cannibalism_complete_wendigo_terminal_lock` has one live call site, in the transformation pulse, and its first limit is `cannibalism_wendigo_can_lock_terminal_form`; focuses and terminal hunts cannot set the lock or world end directly.
- Event Details scenario ID 6, **The World Is the Larder**, controls only the ordinary ending and super-event ID 50. ID 7, **No Thaw Will Come**, controls only the Wendigo ending and super-event ID 53. Their disabled states persist independently.
- Triggerable scenario `SCN-010` exposes exactly five types: Discipline Collapse, Ritual Cells, Silent Islands, Warlord States, and Convergence. Intensity scales actor count, state count, warlord count, initial meters, and network state without bypassing source-country, state, evolution, reveal, special-country, or territorial-validity gates. Manual scenario use marks the campaign achievement-ineligible.
- Event 014 uses the shared world-threat and Chaos/Deaths history frameworks. Natural bounded links exist for Event 10, zombies/Wendigo, Fury, famine, plague, camps, chemical and biological warfare, nuclear effects, and air cleanliness; shared special/nonhuman classifiers prevent inappropriate hosts and targets.

### Super-events, assets, localisation, and documents

- Four distinct super-events are wired: reveal `49`, ordinary world end `50`, eligible global defeat `52`, and Wendigo world end `53`. ID 51 is not owned by Event 014. Each ID has unique 44.1 kHz OGG/WAV material, settings-aware registrations, documented rights/provenance, a unique action-scene image, and the required reveal/route gate.
- The final nine-file Event 014 GFX scan records 816 texture references, 598 unique runtime DDS paths, zero missing paths, and 598 unique runtime hashes. Coverage includes 54 achievement textures, 208 focus icons, 56 idea icons, 124 decision icons, 13 category panels, 26 static GUI textures, 22 report images, seven news images, four super-event images, and the leader/animation packages.
- Thirteen flag families supply five ideology variants in three engine sizes, for 195 TGA files. The 56 regional warlord portraits are unique. The final closure package contributes 21 matched assets.
- Fourteen animation packages contain 142 independently rendered source frames and 142 processed frames. Each has the required sheet PNG/DDS, static fallback, preview, contact sheet, manifest, and handoff; the GUI switches all 14 animated/static pairs through the animation-disable and secrecy gates.
- The achievement package now uses the exact required overlay derivation for all 18 not-eligible variants. The live 18 completed/grey/not-eligible triplets total 54 distinct registered DDS files.
- The final localisation audit reports zero P0-P3 findings across events, focuses, decisions, missions, ideas, traits, countries, achievements, tracker stages, Event Details, super-events, dynamic text, terminology, secrecy, missing keys, and duplicate keys.
- `docs/events/014_cannibalism.md`, the package manifest, acceptance criteria, current matrices, final asset manifests, super-event research, audit handoffs, and catalog re-audit agree on the live implementation. Both accepted improvement addenda have dispositions and their accepted behavior has been promoted into the source-of-truth specs.

## Static scenario walkthroughs

These walkthroughs trace the live definitions and their guard order; they are not substitutes for user play.

1. **Initial fire:** the fire-once root prepares candidates, rejects special/nonhuman/ineligible countries, scores eligible wartime countries, scores the selected country's states, initializes the selected actor and state, and schedules the actor pulse without installing a recurring world on-action.
2. **Clean containment:** open emergency policy, successful local objectives, and global cleanup can reach local/global victory while no second country, commune, warlord, or exploitation history exists; the corresponding real achievement trigger reads those ledgers directly.
3. **Evolution chain:** Evolution I and II are scheduled against the current actor generation, choices change real route/meter state, convergence opens counterplay, and Evolution III records only after reveal transaction ordering has made its public identity legal.
4. **Warlord lifecycle:** an eligible origin state allocates a clear `CBA`-`CBH` slot, receives its matching package and 72-focus tree, then submission/resistance/defeat retires or transfers the slot through reference cleanup before reuse.
5. **Ordinary unification:** the selected human host transfers into `CBL` before donor absorption, inherited gameplay state is applied, reveal is set before public surfaces, and the 108-focus package opens with transferred progress and explicit disposition routes.
6. **Ordinary terminal toggle:** with the complete ordinary route and Chaos above 1000, disabling ID 6 prevents only the ordinary automatic terminal. Re-enabling ID 6 permits the ordinary branch while leaving ID 7 unchanged.
7. **Wendigo merge:** the selected original `ZZZ` keeps its live country package and Pack. Queue recruitment closes immediately, the 28-focus overlay loads after reveal, and a capacity-violating paid batch is rejected before population or Larder payment.
8. **Receipt epoch:** the first enemy sample initializes without a retroactive receipt; positive casualty growth issues bounded receipts. Peace/inactive pruning followed by re-war starts a fresh non-retroactive epoch, while counter decrease resets the snapshot without granting backfill.
9. **Terminal hunt:** launch and pressure consume their declared resources; defender break consumes its declared counter-cost. Capitulation/capital control resolves success for +5 progress, while counterpressure/timeout/invalidation/route break resolves failure for -10. Neither result sets world end.
10. **Wendigo terminal toggle:** the transformation pulse can lock only after full countdown and route proof, Chaos above 1000, active countdown, terminal-route completion, maximum progress, and enabled ID 7. Disabling ID 7 blocks the lock without disabling ID 6.
11. **Population request replay:** replaying the same or older consumption request ID fails before applying loss. A valid new request clamps to removable population, applies exact loss once, then derives Deaths, Larder, consumed-population, and state consequences from the result.
12. **Manual scenario launch:** each of the five SCN-010 types validates the selected source, intensity, territory, evolution/reveal rules, and special-country exclusions before dispatch. Successful manual launch marks the campaign ineligible for the 18 achievements and scales rather than cloning one fixed setup.

## Remaining P3 finding

### P3 — Pre-lock target bands are first-assignment bands

The engine exposes `add_ai_strategy` but no matching scripted removal operation suitable for re-banding this package. Event 014 therefore records each target the first time a pre-lock scorer package is applied and does not dynamically remove or reassign that target's band before terminal lock. This prevents repeated focus milestones from stacking duplicate strategy values. The terminal transition performs a separate one-time post-lock scan with the post-lock profile.

This behavior is explicitly accepted in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_12_acceptance_criteria.md`, the promoted AI strategy matrix, the focus closure addendum disposition, the canonical event document, and the focus-tree postclosure re-audit. It is bounded, visible in documentation, does not create a correctness or completion failure, and requires no remediation for this scope.

## Simplifications, omissions, and blockers

None at the historical checkpoint. The single P3 item described in this preserved audit is superseded by the 2026-07-15 improvement-loop reaudit. The authoritative status cells and helper now use `Fully Functional`; current completion disposition belongs to the 2026-07-15 audit set.

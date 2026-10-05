# Event 011 source audit handoff — 2026-10-05

## Status and scope

Read-only source audit of the current Event 011 implementation and latest release repairs; no gameplay source files were changed by this audit.

The current `.1` entry checks the active chain before initialization and reports `already_active`; invalid or missing targets receive failure feedback, and an unstarted context is aborted where a target can still be recovered (`events/011_secret_alliance.txt:12-51`).

Automatic prefire requires a valid target, three selected founders, no active/postwar chain, and drained callbacks (`common/scripted_effects/011_secret_alliance_effects.txt:36-99`). The scenario launch gate and its failure branch assign a reason for already-active, invalid-target, insufficient-roster, or unavailable cases before calling the shared report hook (`common/scripted_effects/011_secret_alliance_effects.txt:8464-8600`).

## Chain, evolutions, terminal outcomes, and presentation

The public root is `chaosx.nr11.1`; it enters the first visible incident at `.3`. The automatic chain contains guarded Evolution II and III notices at `.4` and `.5`, with Evolution III pre-fire staging at `.17`; the evolution type and three stage identifiers are defined in `common/script_constants/011_secret_alliance_constants.txt:9-24` and rendered by the stage-detail localisation selectors in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2441-2462`.

The current event file wires concealed incidents, human invitations, delayed and cleanup callbacks, then terminal reports `.191` through `.198`; the pre-reveal collapse offers a final public, private, innocence-repair, or temporary counterintelligence choice at `.194` (`events/011_secret_alliance.txt:70-598, 616-860`). Public coalition news is `chaosx.nr11.200`; the delayed scenario composition report is `.201`; reveal-presentation cleanup is `.202` (`events/011_secret_alliance.txt:797-840`).

The reveal helper has one news dispatch at `common/scripted_effects/011_secret_alliance_effects.txt:6031`, while the guarded reveal state is committed at `:6213`. The source therefore has one world-news dispatch point for a successful reveal transaction. Hostile-war, pact-controlled, player-forced, fractured, and weakened presentation descriptions remain separate at `localisation/english/011_secret_alliance_l_english.yml:294-298`, with durable presentation state managed around reveal and cleanup.

No Event011-specific `world_end` terminal branch is present; the accepted event boundary explicitly excludes one. The scenario launch trigger and achievement predicates guard against an existing world-end state (`common/scripted_triggers/011_secret_alliance_triggers.txt:1029-1038`; `common/achievements/chaos_redux_achievements.txt:2911-2948`).

## Event Log, Event Details, achievements, and supporting systems

Event 11 actor mapping resolves the fixed target for automatic history (`common/scripted_effects/chaosx_events_log_effects.txt:265-269`). The shared Event Details preview registers all three Event011 evolution stages (`:2437-2451`), and scripted localisation resolves their current and saved-history titles (`common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2441-2462, 3631-3652, 7616-7640`). Player-facing titles are present as `Repeating Methods`, `Coordinated Interference`, and `Approaching Confrontation` (`localisation/english/011_secret_alliance_l_english.yml:321-326`).

Six Event011 achievements have current definitions and qualification checks: The Empty Chair, Every Thread, Their Man in the Room, Divide the Table, Surrounded, Not Buried, and Two Giants, One Grave (`common/achievements/chaos_redux_achievements.txt:2831-2948`). Their run-origin and reveal snapshots, normal/scenario eligibility, disqualifiers, capital control, and outcome predicates are described in `docs/achievements/011_secret_alliance/achievements.md:5-69`; all six normal, grey, and not-eligible sprite registrations remain in `interface/chaosx_achievements.gfx` and their DDS files remain under `gfx/achievements/`.

The dedicated counter-network GUI currently wires its compact one-line status to `GetSecretAllianceGuiStatus`, which selects hidden-state text during Evolution II or an unresolved border conflict and otherwise shows the recent operation (`interface/011_secret_alliance.gui:50`; `common/scripted_localisation/011_secret_alliance_gui_scripted_localisation.txt:5-18`; `localisation/english/011_secret_alliance_gui_l_english.yml:2`). The prior HOI4 MCP inspect/render attempts timed out; current-source MCP visual evidence remains unavailable, and previous handoff renders are not current confirmation.

## Asset runtime inventory and provenance limit

Runtime event, news, interface, decision, idea, achievement, and super-event artwork remains present and wired through `interface/011_secret_alliance.gfx`, `interface/chaosx_achievements.gfx`, and `interface/chaosx_super_events.gfx`. The current asset overview records 57 runtime DDS targets, 38 transparent targets, six achievement triplets, eight warning-animation source/processed frames, and a static warning fallback (`docs/events/011_secret_alliance/overview.md:125-138`). The reveal image is `gfx/super_events/011_secret_alliance/super_event_public_reveal.dds`, registered as `GFX_super_event_011_secret_alliance_public_reveal` (`interface/chaosx_super_events.gfx:168-169`); reveal presentation uses slot 73 and audio ID 43 (`common/script_constants/011_secret_alliance_constants.txt:1246-1253`).

The event-scoped `docs/assets/011_secret_alliance/` workspace and its source/processed PNG manifest are absent. The overview records the former asset-register deletion and retains the runtime paths and prior validator totals, but this source audit cannot independently re-check original artwork provenance, PNG-to-DDS derivation, or the prior binary-validation receipts. Super-event quote/audio research and achievement source notes remain under `docs/super_events/011_secret_alliance/` and `docs/achievements/011_secret_alliance/`.

## Findings and evidence limits

No further source defect was found in the rechecked `.1` guard, scenario failure reasons, one-shot reveal-news dispatch, event-detail/evolution wiring, achievement definitions, or current GUI status binding. Dynamic cost gates and matching payments were separately source-checked for the edited shipment, depot, route seizure, border-conflict, and emergency branches in the parent checkpoint.

The earlier colour audit passed with zero colour-bearing report/news keys, but that run predates the last source edits and should be rerun against the final release bytes. This handoff is a source audit, not engine validation or live-game confirmation.

The shared failure-report hook sets the requester-owned receipt before dispatch, so one request produces at most one plain report (`common/scripted_effects/chaosx_forced_event_feedback_effects.txt:15-30`). Event011 does not add a `.204` report event.

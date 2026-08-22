# Events 003-006 bounded cleanup

Date: 2026-08-22.

## Scope

This tranche applies only high-confidence cleanup findings from the Events 001-010 audit. It removes proven-dead Event 003 helpers, reconciles the Holy Realm documentation and shared scenario localisation with Fallout ownership, removes four explicitly unreferenced Event 005 runtime portrait copies, normalizes one Event 006 localisation file, and repairs or dispositions broken Event 006 evidence links. No interface or GUI layout file was edited.

## Removed Event 003 helpers

The following scripted effects had no source consumer beyond their definitions after repository-wide direct-reference, documentation, scripted-localisation, GUI, GFX, and meta-dispatch review:

- `holy_realm_core_northern_indian_register_states`
- `holy_realm_core_western_chinese_register_states`
- `holy_realm_core_eastern_chinese_register_states`
- `holy_realm_prepare_final_silence`

The current regional coring flows use their focus-owned effects. Current terminal Final Silence calls `holy_realm_complete_terminal_final_silence`, records stable cause memory, and requests `fallout_request_aftermath`; it does not call the removed preparation wrapper.

The legacy strike-wave events, effects, flags, death cause, super-event assets, and compatibility callbacks were retained. They remain reachable from previously queued callbacks or stable cause-memory surfaces and cannot be retired safely without an explicit compatibility-window migration.

## Event 003 documentation and localisation

`docs/events/003_holy_realm/overview.md` now identifies Fallout as the owner of the current public world-end aftermath, terminal contamination, and current terminal presentation. It distinguishes that active route from retained Final Silence compatibility flags, strike waves, death attribution, and terminal assets.

The unconsumed `chaosx.triggerable_scenarios.5.t`, `.d`, and `.a` strings were removed. The stable scenario identity and redirect logic were not renumbered or deleted.

## Event 005 runtime portrait copies

The Event 005 user-supplied runtime manifest records four files as installed but without an active Event 005 consumer. Repository-wide filename and sprite searches confirmed no consumer, so only these runtime copies were removed:

- `gfx/leaders/005_soviet_collapse/LID_leader.dds`
- `gfx/leaders/005_soviet_collapse/RCD_leader.dds`
- `gfx/leaders/005_soviet_collapse/RLD_leader.dds`
- `gfx/leaders/005_soviet_collapse/TRS_leader.dds`

The corresponding durable user-supplied portrait archive, manifest, hashes, and all active runtime portraits were retained.

## Event 006 localisation and evidence links

All 32 keys in `006_independence_wave_evolution_incidents_l_english.yml` were moved to column zero without changing their keys or text. The UTF-8 BOM was preserved.

The Bashkiria portrait handoff now points to the existing portrait GFX file using the correct relative path. Missing Micronesia, Boris Berman, and Altai processed evidence links were not replaced with fabricated artifacts. Their handoffs now state that the temporary or processed evidence is absent and keep each affected package fail-closed. The surviving Altai original source files remain in the durable portrait archive; the missing processed crops and review images are explicitly insufficient for promotion.

## Validation evidence

Post-change `hoi4.event_inspect` lint for `chaosx.nr3.1` completed as `EVENT_INSPECTED_PARTIAL` against revision `2af1fa63424ef325ab938b49e0183b19d58d881a678db801d72f40e94ec2701c`, with no blocking diagnostics in the focused result. The authoritative artifact is `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/acedb45bbaaf90e1d29e353e626fe8e34cab330a583a4a5627f013038c6588f0/921311f140f967b18475072ce3e2edfde14d3210257e9d7fab602486a93914f8/event-lint-2af1fa63424e.json`.

The tool reports that workspace-wide helper projections and lifecycle passes were deferred, so the artifact is partial rather than engine-runtime completion evidence. No focus rewrite, GUI rewrite, weighted-logic change, or in-game validation is claimed.

## Behavior

No intended gameplay behavior changes. Removing the four unreachable helpers and four unreferenced binary copies changes no active call path. The Event 003 and Event 006 text/documentation changes correct ownership and parsing visibility; stable identifiers, active callbacks, and fail-closed package gates remain intact.

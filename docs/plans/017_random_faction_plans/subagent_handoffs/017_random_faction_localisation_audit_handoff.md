# Event 017 Random Faction Localisation Audit Handoff

Date: 2026-07-11
Agent role: `chaosx_localisation_auditor`
Mode: localisation-only patch-capable audit. This agent made no gameplay or workbook edits and created no commit.

## Disposition

Pass. Event 017's player-facing English localisation is complete and aligned with the final implementation, source specifications, catalogue wording, and accepted continuous achievement proofs. No localisation blocker, fallback, simplification, placeholder, missing key, duplicate key, or unexplained orphan remains.

The audit initially found four gameplay/localisation contract gaps: Four Doors accepted any faction at the delayed check, while Frontier Commitment, Liaison Web, and Not Everyone Signed checked only end-state conditions. The parent resolved all four in gameplay before this handoff was finalized. The final achievement text therefore remains faithful to the source specification rather than weakening the wording around an implementation gap.

## Required sources reviewed

- Repository `AGENTS.md` in full.
- Repo skills in full: `chaos-redux-events`, `chaos-redux-subagents`, and `chaos-redux-decisions-missions`.
- Offline wiki pages: Data structures, Triggers, Effects, Modifiers, Localisation, Scopes, On actions, Event modding, Decision modding, Idea modding, AI modding, and Achievement modding.
- Relevant vanilla documentation and precedents, including localisation formatting, localisation objects, script concepts, scripted localisation, decisions, events, and on-action state-control behavior.
- Every file under `docs/specs/017_random_faction_specs/`, including all four specifications, matrices, research, source-review material, prompts, and subagent prompts.
- The Event 017 improvement addendum, architecture report, decision/mission audit handoff, canonical event documentation, and the live Event 017 scripts.

## Audit coverage and findings

### Forced faction choice

- `chaosx.nr17.10` exposes four dynamic option slots backed by `GetFactionName`, with visibility governed by the corresponding saved-option trigger. This correctly represents every one-, two-, three-, and four-option permutation.
- There is no baseline decline or resistance option. `chaosx.nr17.10.f` appears only when every saved option has become invalid and requests fresh terms; it is a recovery path, not a refusal.
- `chaosx.nr17.30.c` is the later pressured-neutral resistance route and is not presented as a baseline Event 017 decline.
- Each join tooltip states the live 150-day Alignment Shock, 20 accession pressure, 50 Neutrality Resilience, 5 leader Cohesion Strain, mutual diplomatic improvement, and regional pressure consequence. The four wartime warnings state the 120-day Emergency Defensive Coordination effect.
- Event Details states that a player receives up to four faction offers and must choose one, matching both the script cap and the catalogue workbook.

### Leader reaction, reports, and news

- `chaosx.nr17.40.a` and `.40.b` are mechanically and textually distinct. Staff support grants a 180-day Faction Liaison Mission, removes 12 pressure, improves mutual relations, and contributes a distinct supported minor. Radio support lasts 240 days, adds 10 pressure and 240-day Bloc Polarization, and contributes a distinct supported minor.
- Both effects and both options revalidate the live leader, target, faction, and stored chosen-leader relationship. `chaosx.nr17.40.c` closes the event without implying that either response occurred when that context has expired.
- Neighbor pressure, the regional cascade report, and `chaosx.news.4` use concrete diplomatic and military consequences rather than map, table, implementation, or update-history language.

### Decisions, missions, ideas, and opinion

- All twelve visible decision/mission identifiers have a name and description: three aligned-minor decisions, four pressured-neutral decisions or missions, and five faction-leader decisions or missions.
- Availability, objective, cost, completion, cancellation, timeout, and conditional-backlash tooltips were checked against the current scripted effects, triggers, and constants. Dynamic stabilization costs, fixed costs, state/division objectives, convoy/train requirements, pressure and resilience changes, durations, relation changes, and route cancellation wording match the live behavior.
- The faction-leader status now identifies the current faction leader rather than incorrectly calling a transferred successor the original accession sponsor.
- Staff-mission and radio text explains distinct-country Liaison Web progress without exposing arrays, flags, tracking implementation, or Event 017 bookkeeping.
- All six ideas and the emergency-accession opinion modifier have their expected visible identifiers. Idea descriptions describe the current world state.

### Achievements

| Achievement | Final player-facing proof | Implementation proof checked |
| --- | --- | --- |
| Four Doors, One Cabinet | Four offered factions, choose one, remain in that faction while independent and uncapitulated for one year | Four-option flag, original chosen-leader/faction memory, leave disqualification, delayed survival and independence check |
| Hold the Neutral Line | Evolution I, council, successful border mission, one year independent and outside factions, capital controlled at the final check | Council and mission proof, lifecycle disqualification, delayed capital check |
| Crowded Border | One small neutral bordered by members of at least three distinct factions | Distinct neighboring-faction count on a non-major neutral |
| The Liaison Web | Three different supported minors remain independent, uncapitulated, and out of direct war with the supporting leader for 180 days | Exactly three snapshotted targets, lifecycle/direct-war broken ledger, faction membership allowed, delayed proof |
| Frontier Commitment | Evolution II, wartime or frontier-pressure accession, remain faction-aligned and independent while continuously holding the capital and every national core border state for 180 days | Launch refusal if any required state is lost, capital plus core-border snapshot, state-control loss cancellation, lifecycle and delayed proof |
| Not Everyone Signed | An original eligible regional survivor remains outside all factions for 180 days after an Evolution III cascade | Original survivor snapshot, permanent removal on faction entry or invalidation, delayed survivor proof |

No achievement wording exposes flags, delayed event IDs, arrays, implementation history, or hidden weight calculations.

### Event Log, Event Details, evolutions, and cluster

- The Event Log and Event Details each have bound-leader, lost-leader, and unresolved-result wording. The bound branches read the secondary actor stored against the exact history sequence, so they do not substitute a country's later faction leader.
- The lost-leader branches say that the country leading the faction at accession no longer exists. The unresolved branches avoid inventing a faction signature.
- Regional Bloc Race, Pressured Neutrality, and Collapse of Neutrality have matching titles and descriptions across the evolution list, selected-history view, Event Details preview, and selected evolution body.
- The unused `chaosx.events_log.window.evolution_details.random_faction.title.event_detail` key was removed. No remaining Event 017 key is orphaned.
- `chaosx.event_name.17`, the event-detail name, evolution type, Diplomatic Panic cluster name, and Diplomatic Panic description are present and consistent.
- The spreadsheet worker confirmed workbook readback after the final `up to four faction offers` Event Details correction. This agent did not edit the workbook.

## Localisation files corrected

- `localisation/english/017_join_faction_l_english.yml`
  - Reworked the visible Event 017 choice, neighbor, faction-leader, cascade-report, and news prose.
  - Added precise join, wartime, resistance, leader-response, decision, mission, and cost wording.
  - Added `chaosx.nr17.40.c`, `random_faction_leader_staff_response_tt`, and `random_faction_leader_radio_response_tt`.
  - Corrected current-leader status, supported-minor language, Event Details, result/history branches, and evolution descriptions.
  - Removed the unused Event Details evolution-title key.
- `localisation/english/chaosx_achievements_l_english.yml`
  - Audited all six Event 017 name/description/tooltip triplets and made their timed, independence, faction, capital, frontier, and survivor requirements explicit.
- `localisation/english/chaosx_gui_l_english.yml`
  - Replaced the Diplomatic Panic description's tuning/system language with in-world diplomatic consequences.

## Validation evidence

- 196 relevant English definitions were found across the Event 017, achievement, Event Log, event-name, and cluster families.
- 121 explicit script or scripted-localisation references resolve; none is missing.
- No relevant definition is duplicated, and no unreferenced definition remains after accounting for engine-derived decision, idea, opinion, category, custom-cost, and achievement keys.
- All 58 expected automatic visible identifiers for Event 017 decisions, missions, ideas, opinion, category, achievements, and event-name mapping are present.
- The baseline event contains four join slots, four matching effect tooltips, four conditional war warnings, one invalid-option recovery path, and zero decline/resistance options.
- Event Details has three result branches; history has three matching result branches; all three evolution titles and all four evolution body variants are dispatched.
- The four audited English files retain UTF-8 BOM encoding. Relevant keys have no `:0`, no leading indentation, no malformed entries, and balanced formatting/localisation brackets.
- Event 017 scripted-localisation files contain no direct `§` or `£` formatting characters.

## Simplifications, omissions, and blockers

None. The parent resolved every gameplay mismatch raised by this audit before final disposition. No fallback wording or weaker substitute was used.

The technical labels for hidden resolver/check events (`chaosx.nr17.20` and `.81` through `.86`) remain intentionally internal and are not player-facing.

## Skills

Used: `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-decisions-missions`.
Created or updated: none.

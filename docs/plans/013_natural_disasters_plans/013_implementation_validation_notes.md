# Event 013 Natural Disasters implementation validation notes

Date: 2026-07-11

This ledger records the final static, data, asset, workbook, balance, and regression checks for the fresh Event 013 implementation. It does not claim that the live HOI4 engine scenarios were executed.

## User-reported firing failure

The hidden root event is intentionally non-popup and every impact must remain delayed. Four concrete defects could therefore make a manual firing appear inert, distort its timing, or prevent the system from loading correctly:

1. a missing `natural_disaster_warning_cost_gate_fixed.local_stability` script-constant reference in the trigger file;
2. random family, sequence-size, gap, report-delay, chain-delay, and exhaustive-retry draws wrote normal scoped variables while the controller read same-named temporary variables;
3. integer random ranges passed their documented inclusive maxima directly into the engine's exclusive `max`, omitting the last family, longest delay, largest sequence count, and highest target tie-break score; and
4. no available decision between scheduling and the later warning/impact.

The missing reference is corrected to `natural_disaster_cost_gate_fixed.warning_stability`. Every scratch random draw now uses the documented `set_temp_variable_to_random`, so the preflight family, exhaustive cursor, planned hit count, pacing gaps, reports, and chains are read from the value that was actually randomized. Each inclusive design maximum is converted to the engine's exclusive upper bound before the draw, preserving every documented family and timing endpoint. An accepted target now sets category visibility and exposes `natural_disaster_forecast_card` immediately. The available state-targeted forecast names the family, state, severity, hazard class, and scheduled date; acknowledging it clears only its alert. The warning and impact remain delayed. Notification cleanup and state-control transfer now treat `natural_disaster_impact_scheduled` as live activity, so another card cannot hide a pending forecast. Abnormal history also prioritizes active warning state over the underlying scheduled-impact flag.

The Event 013 error lines in the supplied 05:25 logs were traced against the current files. The logged unsupported constant tokens in idea/mission modifiers use file-scoped mirrors now; invalid `stability` and `manpower` trigger forms use `has_stability`, `has_manpower`, or `check_variable`; building tests use supported building-level triggers; mission modifiers have `days_remove`; and foreign-relief donor scope is saved as an event target before the opinion effect. Those exact faulty forms are absent from the current Event 013 sources.

## Structural and reference pass

The final audit loaded the workbook and images and parsed the Event 013 script surfaces. It found:

| Check | Result |
| --- | ---: |
| Disaster families | 25 |
| Direct family geography routes | 25 |
| Warning decisions | 75, exactly three per family |
| Family reports | 25, IDs 101-125 |
| Family news events | 25, IDs 201-225 |
| Unique Event 013 English localisation keys | 1,054 |
| Event 013 script-constant references reviewed | 1,152, zero missing |
| Disaster-specific category family mappings | 25, each mutually exclusive |
| Event 013 texture routes opened successfully | 197 |
| Achievement registrations | 10 |
| Super-event slots | 67-72 |
| Super-event playback audio IDs | 37-42 |
| Workbook formulas / cached formula errors | 0 / 0 |

All inspected Event 013 script and GUI files have balanced blocks, defined file-scoped constants, no unsupported `<=` or `>=` tokens, and no missing Event 013 localisation reference. The localisation file retains its UTF-8 BOM. Every family report and every family news description is distinct. No gameplay GFX definition references a GIF.

## Dynamic geography proof

The physical registry contains 175 unique vanilla states mapped to Holocene volcanic vents. The 92-state massive-eruption and 103-state lahar sets are strict subsets. All registry IDs resolve against vanilla or mod state history. Volcanic eruption and massive eruption require their respective registry; ashfall and lahar require a valid volcanic origin context. The same physical predicates are called by primary target selection, delayed execution, neighbor spread, repeated impacts, physical chains, and abnormal path segments.

Heat eligibility is the explicit warm-region registry minus every cold-region match. Its effective overlap with the cold registry is zero. All named Siberian strategic regions are cold-valid and therefore heat-invalid. Dust, drought, wildfire, cyclone, surge, tsunami, slope, basin, and moving-corridor families have separate hard gates before population, infrastructure, buildings, resources, or history can influence scoring.

The source and mapping method are recorded in `subagent_handoffs/2026-07-11_event013_physical_geography_data_handoff.md`. This is a fixed vanilla-map data registry and must be reviewed when the base map changes.

## API, queue, report, and history trace

- `call_natural_disaster` accepts specific family or family group, random family, selected state/country/region, coast, dense state, enemy, caller-provided target, severity, sequence form/count, news, report, aftermath, follow-up, evolution override, scenario context, and independent death/building/supply/recovery/warning scaling.
- Selected target proofs are reset after every request. Invalid enum, stale target, impossible geography, Event 051 heat overlap, unauthorized abnormal bypass, hostile-call authority, and scale errors fail closed.
- A provisional sequence is published only after at least one impact schedules. The only Event 013 history writer is called once on acceptance; internal warnings, impacts, reports, news, chains, reassessments, causal Skyfall segments, and neighbor cards never write another Event 013 row.
- Every job due date enters the global sequence/day reservation ledger and clamps to at least one future day. All 26 aligned job fields have enqueue, processing-removal, transfer-add, and transfer-removal handling.
- Affected controllers always receive a delayed immutable report snapshot. Caller/global distribution and news are independent. News policy no longer inherits a global report request.
- Report snapshots preserve family, severity, deaths, six damage flags, warning, fine route, route target/due date, recovery phase, origin, basin, sequence, and segment across later state mutation or control transfer.

## Decision, mission, AI, and cleanup pass

The category becomes visible at forecast, stays visible through warning and recovery, chooses the highest-priority controlled live state, and maps all 25 families onto existing disaster-specific cosmetics. The overview image is used only when no live display state exists; foreign relief uses its dedicated famine/displacement cosmetic.

All 75 warnings have family identity, a physical availability gate where relevant, visible and executable cost logic, a complete effect, warning protection, expiry behavior, and AI weighting. Recovery exposes four capped rescue slots, three stabilization slots, three reconstruction slots, one typed chain objective, one inbound-relief operation, and one outbound operation per donor. Full, partial, failure, cancel, timeout, cleanup, and state-control transfer paths release their exact slot and refresh the next priority state.

The seven typed chain objectives are tsunami, disease, famine, wildfire spread, supply collapse, lahar, and aftershock. Their deadlines are derived from the reserved arrival and fall one day earlier. Neighbor convoy, port lifeline, engineer column, and medical column variants have distinct equipment, transport, fuel, stability/war-support, legitimacy, arrival, dependency, and AI behavior.

The Event 013 controller uses no periodic whole-world on-action. Evolution II open-card synchronization is event-driven through the bounded open-card state ledger, and state-control changes use the narrow state-control on-action.

## Evolution, cluster, scenario, and GUI pass

The accepted stage mapping is:

| Stage | Name | Tier |
| --- | --- | --- |
| I | Wider Disaster Seasons | Gathering Storm, 1 |
| II | Regional Cascades | Rising Chaos, 2 |
| III | Abnormal Paths | Chaos, 3 |

The constants, stage triggers, event-log previews, cluster logical roles, mechanic docs, and workbook use this mapping. Player-facing titles contain no `Evolution I/II/III` prefix. The Event Details summary contains only chaos tier and evolution stage.

Cluster 5 persists the exact family/target/evolution/severity/policy/scaling context for each of its five logical Event 013 roles before queueing. SCN-007 uses the same API for all five types and four intensities. Low cannot open abnormal Skyfall routes; Maximum can select meteor shower, causal skyfire hail, ocean impact with basin-locked tsunami arrivals, and abnormal ash only after a valid cause. Event 046 remains inert, Event 099 is the narrow dust bridge, and Event 051 is separate and non-stacking.

The abnormal GUI is limited to Evolution III and manual abnormal scenarios. It uses five selectable sequence-scoped markers, six data-driven milestones, state-driven card frames, family-specific motion sheets, a shared normalized route-anchor table, static fallbacks, locate-state, and controlled live-state routing back into normal decisions. History and foreign cards are read-only. All 25 GUI buttons have scripted callbacks; selected-record triggers guard the dormant view.

## Super-event audio and Soviet cleanup

The final minimum-offset Chromaprint pass compared Event 013 audio IDs 37-42 with the registered non-Event-013 catalogue, including later IDs 49, 50, and 52-56. The original ID 37 cue matched Soviet Collapse ID 14 at `0.993730-0.994434`, proving the same recording. ID 37 was replaced with Grieg's *In the Hall of the Mountain King*. Final Event 013 maxima are `0.572875-0.596505`, outside the confirmed reuse cluster. Source, rights, edits, loudness, hashes, slot mapping, and final paths are recorded in `docs/super_events/013_natural_disasters_super_event_audio_production.md`.

Unused Soviet Collapse audio IDs 16 and 19-27 and their OGG/WAV files, asset registrations, localisation, and catalogue rows are absent. IDs 14, 15, 17, and 18 remain because live Soviet super-event routes reference them.

## Balance review

Population loss is proportional to state population and family lethality, then modified by evolution, war, low stability, unresolved aftermath, warning/preparation, resilience, and caller override before severity and hard population caps. Representative unprepared one-million-population outcomes before vulnerability multipliers are:

| Case | Approximate deaths | Damage points / state |
| --- | ---: | ---: |
| Local hailstorm | 1,500 | 3 primary, 2.25 secondary, 1.51 tertiary |
| Local earthquake | 6,900 | 3 primary, 2.25 secondary, 1.51 tertiary |
| Severe earthquake | 20,700 | 6 primary, 4.5 secondary, 3.02 tertiary |
| Evolution II regional earthquake | 53,360 | 9 primary, 6.75 secondary, 4.52 tertiary, plus valid neighbors |
| Evolution II regional earthquake in war at low stability | 76,838 | same damage with stronger supply/recovery pressure |
| Evolution III abnormal rupture | capped at 350,000 | 22 primary, 16.5 secondary, 11.06 tertiary, plus up to five valid neighbors/path segments |

A timely funded population warning multiplies deaths by `0.55 × 0.72 × 0.78`, reducing rather than canceling the disaster. Relevant material preparation multiplies building damage by `0.65 × 0.82 × 0.72`. Evolution II also increases neighbor points, modifier duration, supply loss, chain scaling, recovery-score pressure, famine, disease, refugee, and political consequences. Evolution III doubles the evolved death multiplier again and uses abnormal disruption up to -55% movement, +32% attrition, -60% repair, and -50% resources. These bands match the accepted meaningful-baseline, regional-hundreds-of-thousands-across-sequences, and abnormal-multi-million-aggregate directions without making preparation an immunity button.

## Outstanding validation and archival work

No deterministic headless HOI4 scenario harness exists in the repository, so the live-engine matrix remains queued. It includes same-chain API accept/reject order, far-future/earlier queue insertion, occupied-state transfer, all 75 warning affordability cases, every recovery outcome/cap, overlapping abnormal paths and observers, all ten achievement unlock/disqualifier routes, all six super-event display/audio routes, and aggregate AI balance under concurrent cards. Event 013 and SCN-007 therefore remain `Needs Testing` in the workbook.

The broader concurrent `docs/assets/` cleanup removes the Event 013 binary source-art/audio archive from this working tree. All live DDS/OGG/WAV files, registrations, source URLs, rights, hashes, and production records remain. Restoring the binary source archive is queued pending the repository-wide asset-retention decision; it was not silently reconstructed or treated as present.

No gameplay fallback or accepted gameplay-surface simplification was introduced. The required static animation assets are paired with real frame-sheet motion assets, not substituted for them.

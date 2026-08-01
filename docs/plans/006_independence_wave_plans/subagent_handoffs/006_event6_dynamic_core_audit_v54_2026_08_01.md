# Event 006 SCN-008 and crisis dynamic-core audit v54

Date: 2026-08-01

Scope: bounded read-only audit of SCN-008 mode/intensity selection, ranked candidate attempts, intensity territory/force tuning, type behavior, and the host-facing pre-wave crisis queue/receipt/cleanup contract.

This handoff does not audit package-specific focus, portrait, advisor, icon, formable, or country content.

No gameplay, localisation, interface, asset, workbook, or CSV file was changed by this audit.

## Verdict

SCN-008 shared source contracts are PASS at static source level.

The selector exposes eight player-facing modes from six numeric type families because Universal Belligerence expands into three bounded rules, and each mode accepts four intensity values.

The ranked scenario pass contains exactly 138 current-map-bound package IDs and iterates every one at every intensity without varying candidate admission by intensity.

Low, Medium, High, and Maximum use separate territory and force variables, while Great Partition applies only its documented optional-territory promotion.

Type behavior dispatch is centralized for congress/league formation, former-host wars, Universal Belligerence rules, patron assignment, and partition ambition.

The crisis queue, receipt, Event Log payload, bounded retry, and annexation recovery are source-implemented and delegate ownership changes to the ordinary synchronized planner.

Static runtime limits remain: no live scenario-cell playback, save/load, mission timer, requester-loss, stale-queue, or Event Log rendering was performed.

## Coverage matrix

| Surface | Status | Evidence | Boundary |
| --- | --- | --- | --- |
| Eight selectable SCN-008 modes | PASS, source | `common/script_constants/006_independence_wave_constants.txt:128-142` defines six numeric families. `common/scripted_effects/006_independence_wave_scenario_effects.txt:28-90` makes Universal Belligerence walk its three rules before moving to the next family. `common/scripted_localisation/chaosx_scripted_localisation_scenarios.txt:334-390` provides six-family labels plus Former Hosts, Neighboring Releases, and Nearby Nonleague States. | No live selector playback was run. |
| Four intensities | PASS, source | `common/script_constants/chaosx_triggerable_scenarios_constants.txt:32-42` defines Low, Medium, High, and Maximum. `common/scripted_triggers/006_independence_wave_scenario_triggers.txt:28-34` validates all four values. Generic selector effects are wired at `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:730-778`. | The accepted matrix is 32 mode/intensity cells; playback remains future QA. |
| Launch queue carries the selected cell | PASS, source | `common/scripted_effects/chaosx_triggerable_scenarios_effects.txt:1022-1034` copies type, intensity, and belligerence rule into queued variables before scheduling `chaosx.triggerable_scenarios.8`. `events/006_independence_wave_scenario.txt:10-19` revalidates the queued cell before starting the transaction. | No delayed-event save/load observation. |
| All viable candidate attempts | PASS, source / fail-closed | `common/scripted_effects/006_independence_wave_scenario_effects.txt:94-103` keeps the bound-package target at 138. `:161-300` publishes 138 ranked package IDs. `:379-417` loops the entire ranked array, records unready rows, and sends ready rows through the normal load/reserve API. `:419-460` requires aligned selected metadata and fails closed on an empty or malformed result. | Current content attestation is only 13 packages across 12 compatible groups, so this audit does not claim operational capacity for every automatic band. |
| Candidate attempts do not vary with intensity | PASS, source | `006_independence_wave_scenario_effects.txt:379-417` contains no intensity branch in the ranked loop. The same registry target is established before allocation at `:94-103` and `:429-434`. | Runtime count and reservation order were not observed. |
| Intensity territory/force separation | PASS, source | `006_independence_wave_scenario_effects.txt:94-137` maps Low to anchor/fragile, Medium to compact/viable, High to extended/armed, and Maximum to extended/high-chaos with independent country-value deltas. `:139-156` lets Great Partition promote territory one tier only. `:468-496` applies the five country-value deltas and opens high-chaos/ambition flags only at the documented thresholds. | No balance or live force-materialization claim. |
| League/congress setup | PASS, source | `006_independence_wave_scenario_effects.txt:509-543` marks Common Congress releases and registers Network members/founders. `:598-641` initializes cohesion, common cause, patron capture, confidence, reserve, phase, route, leader, member registry, and member count with intensity-specific reserve/phase tuning. | Package-specific league routes remain outside this audit. |
| Former-host war setup | PASS, source | `006_independence_wave_scenario_effects.txt:545-554` marks Wars of Separation, sets host claim/hostility and security deltas, and `:806-858` validates the living former host, declares the normal war, records danger counters, and falls back to a regional-threat mission when declaration is invalid. | Live war declaration and host-death behavior were not run. |
| Universal Belligerence rules | PASS, source | `006_independence_wave_scenario_effects.txt:556-564` applies hostility/security setup. `:860-906` handles neighboring-release targeting. `:908-964` handles nearby non-league targeting with distance and faction/league exclusion. `:974-998` selects the active Former Hosts, Neighboring Releases, or Nearby Nonleague rule and clears target marks before and after the bounded pass. | No map-distance or diplomatic runtime sweep. |
| Patron Worlds setup | PASS, source | `006_independence_wave_scenario_effects.txt:566-569` marks the Patron Worlds lane. `:643-794` selects a nearby major patron by government, falls back to another nearby major, assigns a channel, registers influence/aid, and applies recognition/capacity deltas; `:796-800` applies it to every released scenario country. | Patron availability and balance remain runtime QA. |
| Great Partition setup | PASS, source | `006_independence_wave_scenario_effects.txt:570-584` marks partition, opens regional ambition when the family ledger exists, promotes host claim/border progress, and applies instability. `:143-156` promotes territory before reservation while preserving the ordinary intensity ladder. | Formable-family admission is outside this audit. |
| Crisis pressure and opening gate | PASS, source | `common/scripted_triggers/006_independence_wave_crisis_triggers.txt:11-33` covers low stability, enemy-controlled owned states, and controlled foreign-owned states above the centralized resistance threshold. `:35-53` rejects world end, pending presentations, a busy coordinator, active/cooldown state, and an occupied crisis queue. | Live category visibility and save/load were not run. |
| Crisis mission cost/time/AI | PASS, source | `common/decisions/006_independence_wave_crisis_decisions.txt:15-38` uses the concrete security cost, a 120-day mission, cancellation/timeout effects, and centralized AI weights. `common/decisions/categories/006_independence_wave_crisis_categories.txt:8-16` keeps the category visible while the mission is active. | No live affordability, timer, cancellation, or AI-choice observation. |
| Crisis queue and ordinary-planner handoff | PASS, source | `common/scripted_effects/006_independence_wave_crisis_effects.txt:204-221` creates one global queue, marks the requester, records the queued cause/resolution, starts cooldown, clears active runtime, and schedules `chaosx.nr6.3`. `events/006_independence_wave.txt:66-98` rechecks the shared barrier, clears the queue before ordinary standalone execution, and records committed or blocked resolution. | No live busy-coordinator retry observation. |
| Bounded retry and failure cleanup | PASS, source | `common/script_constants/006_independence_wave_crisis_constants.txt:23-33` centralizes 120 mission days, 365 cooldown days, one-day retry delay, and a 14-attempt retry limit. `events/006_independence_wave.txt:99-135` retries only while the requester flag and queue remain, then clears queue/retry/requester state and applies the blocked consequence. | The accepted source contract is bounded retry; live timing remains untested. |
| Durable cause/resolution receipt and Event Log | PASS, source | `common/scripted_effects/006_independence_wave_crisis_effects.txt:97-131` stores host id, cause, date, receipt flag, and cause Event Log row. `:133-202` maps queued, blocked, cancelled, committed, requester-lost, and unknown outcomes to distinct resolution rows. `events/006_independence_wave.txt:86-90` sets the committed receipt; blocked/cancelled/requester-loss effects set the failure receipt. `common/scripted_localisation/006_independence_wave_crisis_localisation.txt:9-58` resolves cause and outcome payloads. | No rendered Event Log proof. |
| Requester-loss recovery | PASS, source / runtime HOLD | `common/on_actions/006_independence_wave_crisis_on_actions.txt:9-13` invokes recovery on annexation. `common/scripted_effects/006_independence_wave_crisis_effects.txt:259-296` clears the global queue, sets requester-lost resolution/failure receipt/date, preserves host id, clears requester/runtime flags, writes the requester-lost history payload, and refreshes Event Log views without changing ownership. | Non-annexation removal and live annexation/save-load remain untested. |
| Defensive stale-queue branch | PASS, source after parent follow-up repair | The original audit identified the silent branch at `events/006_independence_wave.txt:132-135`. The parent follow-up now clears the global queue and retry/runtime state, writes an explicit unknown resolution/date/host, sets the failure receipt, and records the resolution Event Log row. | Live corruption/save-load playback remains untested. |

## Cross-system boundaries

- SCN-008 uses the shared Liberations coordinator. `006_independence_wave_scenario_effects.txt:1229-1260` begins the triggerable-scenario plan, enters allocation, allocates the ranked registry, and calls the ordinary standalone frozen-plan executor.
- Scenario commit remains centralized. `006_independence_wave_scenario_effects.txt:1261-1320` applies type behavior only after committed phase, freezes the summary, and rolls back or aborts uncommitted plans on failure.
- Crisis code never changes ownership directly. `events/006_independence_wave.txt:84-95` delegates to the same standalone planner and only records committed or blocked receipts around its result.
- Event 005 separation remains outside this bounded scenario/type audit. The shared transaction source continues to reserve Event 005 anchors before Event 006 anchors, as recorded by the current allocator audit and `006_core_loop_closure_v35_2026_07_29.md`.

## Validation

Ran `python -B .tools/audit_event6_allocator.py`.

The audit passed with 149 publishers, 126 automatic/high-chaos selectable packages, 138 SCN-008 ranked selectable packages, 13 attested packages across 12 compatible reservation groups, RG-RHINE-SAAR pair capacity 2, automatic counts 6/8/10/14/20 with World Collapse 20, the four scenario intensity mappings, the six scenario type families, and Event 005-first joint reservation order.

Ran targeted read-only `rg`/PowerShell source enumeration for mode cardinality, ranked-array cardinality, queue writers/clearers, receipt writers, retry cleanup, and annexation recovery.

No game launch, MCP/live scenario playback, save/load cycle, mission timer observation, Event Log rendering, or package-content audit was performed.

## Changed files

Only this handoff was added by the read-only audit. A parent follow-up subsequently patched the stale-queue branch in `events/006_independence_wave.txt` and added `independence_wave_crisis_resolution.unknown` to `common/script_constants/006_independence_wave_crisis_constants.txt`.

No gameplay file was patched.

## Remaining blockers and unsupported analysis

The current 13-package attestation set and 12 compatible groups do not prove runtime capacity for every automatic 6/8/10/14/20 band.

The 32 SCN-008 mode/intensity cells remain static-source evidence; live selector persistence, map collisions, rollback, and post-commit cleanup are future QA.

The stale queue-without-requester branch is source-repaired; live corruption/save-load playback remains untested.

Package-specific content, focus geometry, formable reachability, assets, AI balance, and whole-event completion are outside this handoff and remain governed by the current Event 006 source-of-truth map.

This handoff does not claim whole-event completion or a blocked goal.

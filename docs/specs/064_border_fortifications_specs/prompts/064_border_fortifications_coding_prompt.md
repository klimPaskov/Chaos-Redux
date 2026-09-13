# Coding Prompt: Implement Event 064 Border Fortifications

Implement Chaos Redux Event 064 from the complete source package under `docs/specs/064_border_fortifications_specs/`.

Use the three-digit `064` prefix for every project-facing event-scoped folder, filename, prompt, asset identifier, achievement identifier, and probability scenario label. Preserve the established Clausewitz namespace `chaosx.nr64.*` and its numeric registry identity. Do not create unpadded project-facing identifiers.

Read every specification, matrix, diagram, research note, and specialist prompt before editing. Follow `AGENTS.md`, `chaos-redux-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets`, `chaos-redux-improvement-loop`, the dynamic trigger and effect references, current event-log and Event Details documentation, current achievement conventions, and current cluster system ownership.

Use project subagents with `fork_context=false`. Pass self-contained tasks and exact paths. Do not rely on inherited chat context.

## Repository starting point

Inspect the current repository before editing.

Preserve the stable identity where compatible:

- namespace `chaosx.nr64`
- canonical entry `chaosx.nr64.1`
- current event family `events/064_border_forts.txt`
- current localisation family `localisation/english/064_border_forts_l_english.yml`
- current report sprite `GFX_report_event_border_fortifications`
- current report texture family `gfx/event_pictures/064_border_forts/`

Replace the current thin two-level border-fort option. Do not create a second Event 064 path that leaves the old effect active.

Spawn `chaosx_repo_explorer` first with the full Event 064 goal, accepted identities, spec paths, current known files, and questions about registry ownership, building and province helpers, evolution integration, history, Event Details, decisions, modifiers, achievements, assets, workbook ownership, and cluster multi-membership. Record its map under `docs/plans/064_border_fortifications_plans/subagent_handoffs/`.

Spawn `chaosx_scripted_system_architect` for the one-token global transaction, bounded targeting, cleanup, persistence, and multi-cluster integration. Resolve its handoff before completing runtime script.

## Event identity

Keep Event 064:

- Minor Repeatable
- Chaos Level 1
- primary Sudden Abundance member at Medium severity
- additional Military Preparation member at Medium severity
- status Needs Testing after complete implementation wiring and before final live acceptance

Keep the event valid as a standalone repeatable event.

## Global transaction

Implement one hidden global root that owns the entire construction wave.

Required sequence:

1. save natural, cluster, manual, and debug context
2. create a unique global wave token
3. snapshot valid country scopes and current map context
4. process each valid country once
5. identify current controlled foreign land-frontier provinces
6. deduplicate province roles
7. apply baseline and enabled evolution packages
8. save local and global result counts
9. record history and first concrete evolution materialization
10. apply mapped direct Chaos with guards
11. send human reports and resolve AI posture choices
12. clear every temporary candidate, score, saved scope, and source-context item

Country report options must never own or repeat the automatic building grant. A report left open cannot delay the world result.

Use a firing-time snapshot. New borders wait for a later Event 064 wave. Completed buildings remain physical and transfer normally.

## Valid frontier rule

A qualifying direct frontier province is:

- controlled by the processed country
- a valid land province with a land-fort slot
- directly adjacent through a passable ordinary land edge to a province controlled by another country

Include peaceful, allied, faction, subject, overlord, hostile, civil-war, occupation, river, enclave, and disconnected land boundaries.

Exclude sea, strait-only, canal-only non-land, lake, impassable, off-map, invalid-slot, and same-controller adjacency.

A province touching several countries receives one baseline grant. Current control, not historical ownership, defines the snapshot.

## Baseline

Every qualifying direct frontier province below the active ordinary cap receives one land-fort level.

Starting baseline cap: level 3.

Preserve existing levels above cap. Add levels to the existing building value. Do not replace that value. Inspect whether the chosen effect repairs damaged forts and prevent an unintended world repair.

Use the shared repeatable weight lifecycle. Add a roughly 365-day natural availability guard or an equivalent safe frequency rule after testing. Keep an active-token and same-incident duplicate guard. Manual and debug routes can bypass natural timing but cannot duplicate one incident and cannot unlock achievements.

## Evolutions

Implement shared evolution eligibility, enablement, maturation, logging, and pre-fire evolved openings.

- Defense in Depth requires 200 or more Chaos.
- Fortress States requires 400 or more Chaos.
- Fortress World requires 600 or more Chaos.

Evolution eligibility and maturation add zero Chaos. Each stage logs and pays its first materialization source only when its package changes valid buildings.

Disabled stages skip cleanly. Higher enabled stages remain functional without disabled lower stages.

### Defense in Depth

Select bounded strategic frontier anchors and bounded second-line positions near real routes or objectives.

Starting caps:

- ordinary frontier 4
- anchor 5
- depth 2

One direct frontier province can receive its baseline level and one evolved bonus. A depth position receives one level.

Use threat, capital, victory point, supply, railway, terrain, river, corridor, industry, port, and geographic-spread factors. Do not fortify random interior provinces. When exact province features are unavailable, use a documented bounded state or maintained-map-role approximation.

### Fortress States

Select about thirty percent of current border states, minimum one when valid, hard cap six as a starting anchor.

Starting caps:

- ordinary frontier 6
- strategic or selected sector 7
- depth 3
- state anti-air 3
- radar 2
- coastal fort 3

Use role-based packages. A selected state can receive stronger direct frontier positions plus a bounded subset of anti-air, radar, supply work, and coastal defense.

Repair or improve existing infrastructure and railway support before creating new supply infrastructure. New supply hubs are exceptional and require separate targeting and balance proof. Do not create hubs in every border state.

Coastal defense requires a state with both a foreign land frontier and a valid coast or port role. Protect ports and bounded landing approaches, not the entire coast.

### Fortress World

Create bounded internal redoubts around capitals, major victory points, supply hubs, railway junctions, industrial centers, major ports, and other verified strategic sites.

Starting caps:

- ordinary frontier 7
- strategic or selected sector 8
- depth 4
- internal redoubt 3
- state anti-air 3
- radar 3
- coastal fort 3

Use the country-size quota and capital-first priority from the tuning matrix, with a hard cap six. Island and isolated countries can receive valid internal redoubts.

Resolve role overlap before construction. No direct frontier province receives more than two automatic Event 064 fort levels in one wave. No interior position receives more than one automatic level in one wave.

## Reports and response postures

After construction, send every human country the correct local report. Use saved local result counts. Countries with no local result receive the observation or foreign-breach version defined by the spec.

Implement three temporary mutually exclusive postures when valid:

- Integrate the Line
- Keep the Roads Open
- Study the Breach

These labels are working labels, not final localisation.

Starting duration: about 180 days.

Use valid current modifiers. Keep defense, logistics, and fort-focused offensive effects distinct. Remove old posture state before applying a new posture. Never stack several Event 064 postures.

## Decision and mission system

Implement the full prompt at `prompts/064_border_fortifications_decision_mission_prompt.md`.

Use a normal decision category with a static picture as the complete player response surface.

Implement all five project families:

1. Reinforce a Priority Sector
2. Connect the New Line
3. Conduct Breach Exercises
4. Harden the Air and Coastal Flank
5. Prepare a National Redoubt

Use targeted decisions, one active Event 064 project per country, visible duration and failure conditions, concrete costs, reserve floors, save-safe timers, one-time completion, target-loss cleanup, annexation cleanup, and wave-use limits.

Use no more than four spendable cost types per action. Use industry, equipment, transport, fuel, experience, manpower, Command Power, and time according to the mapped bundle. Political power is not the default universal price.

Spawn `chaosx_decision_mission_auditor` after the system is substantially implemented and resolve every accepted finding.

## AI

Implement every scenario and target rule in `matrices/ai_probability_scenario_matrix.md`.

AI posture and project behavior must react to:

- capital danger
- defensive or offensive war state
- enemy strength and fort levels
- supply and infrastructure
- country size and frontier length
- stockpile reserve floors
- engineers, doctrine, planning, and experience
- air and coastal threat
- island geography
- subject and civil-war context
- special actor owner contracts
- cluster context
- active project and repeated-wave state

Invalid choices receive zero probability. AI can skip a project.

Spawn `chaosx_ai_probability_auditor` with `fork_context=false`. Use the configured probability inspection, evaluation, sweep, comparison, rendering, simulation, and sequence tools. Save full effective-weight, normalized probability, target-pool, and cluster-arbitration evidence. Do not close AI probability through source inspection alone.

## Chaos impact map

Implement every row in Part 4 and the tuning matrix.

Starting targets:

- first natural global wave about +8, scaled within +5 to +12
- meaningful repeat wave about +2, scaled within +1 to +3, with cooldown and minimum footprint
- first concrete Defense in Depth materialization about +5
- first concrete Fortress States materialization about +10
- first concrete Fortress World materialization about +15
- distinct military-abundance cluster convergence about +3 when another member produced a real relevant gain

Pay zero for no-op, duplicate, debug, eligibility, maturation, posture choice, and trivial waves.

Audit shared Chaos sources for fort, building, military buildup, war, casualty, tension, and related effects. Preserve shared sources and document why Event 064's abnormality premiums are distinct. Do not add a false Chaos refund for local demolition or capture.

## Cluster integration

Implement Event 064 as a Medium member of both accepted clusters.

The current runtime and supplied cluster catalog may not yet support the full accepted map. Reconcile the authoritative cluster registry, constants, member preparation, queue, history, settings, Event Details links, and documentation.

Required multi-cluster behavior:

- one automatic Event 064 selection enters at most one cluster context
- both memberships remain reachable
- manual cluster trigger chooses exact requested cluster
- selected root and queued member cannot execute Event 064 twice
- one cluster incident applies pacing once
- Event 064 applies its own effect, weight, history, and direct Chaos once
- standalone Event 064 remains valid

Sudden Abundance can apply one bounded relevant material-cost benefit and the distinct convergence premium when another member produces a real military-material abundance.

Military Preparation can change strategic target scoring and AI readiness according to current threat and connected strategic sites.

Do not claim cluster completion if the runtime stores only one membership or if one accepted cluster is missing.

## Event connections

Implement only lightweight relevant hooks from Part 4. Do not create new popup chains or duplicate rewards.

Inspect connections with Events 19, 23, 27, 32, 42, 46, 55, 56, 58, 61, 62, 63, and other accepted cluster members. Use actual existing outcome flags and owner APIs. Keep Event 22 interaction neutral and do not reward atrocities.

## Achievements

Implement all four achievements through `prompts/064_border_fortifications_achievement_prompt.md`:

- Continent of Concrete
- The Line Held
- Breach the Unbreachable
- Last Redoubt

Titles are working labels. Write final text. Implement tracking, phases, disqualifiers, save-load, cleanup, icons, documentation, and tests. Suppress manual, debug, console, observer, test, transfer, tag-switch, subject, faction, and third-party shortcuts as mapped.

## Assets

Produce and wire the complete package through `prompts/064_border_fortifications_asset_prompt.md`.

Required families:

- report event image
- decision category picture
- category icon
- three posture icons
- five decision icons
- four achievement completed icons and processed grey and not-eligible variants

Use the existing HOI4 map building visuals for the fortified provinces and state buildings.

Spawn the appropriate generated-event-art and icon specialists with `fork_context=false`. Complete sources, previews, final DDS files, provenance, manifest, hashes, and `.gfx` handoff. Do not use placeholders or temporary runtime paths.

## Final localisation

Spawn `chaosx_localisation_auditor` after final text is written.

Write final player-facing:

- report title, description, and options
- evolution catalog and history
- category and posture text
- decisions, missions, costs, completion, failure, and invalidation
- Event Details and History
- cluster details and member history
- achievements
- debug and settings names
- spreadsheet-facing documentation text

The text must describe an unexplained synchronized manifestation, not a normal government construction order. Remove obsolete current option keys. Keep dynamic singular and plural grammar correct.

## Event log and Event Details

Record one global actorless or otherwise verified non-misleading Event 064 History row per wave. Do not record one row per human report.

Register:

- normal event details
- all three evolution catalog rows
- first concrete evolution history
- normal event history
- cluster member links in both clusters
- debug and settings names

Use saved counts and avoid fake actor, date, or sequence information.

## Catalog and documentation

Update the authoritative workbook through the accepted spreadsheet ownership. Do not edit exported CSV files directly.

Spawn `chaosx_spreadsheet_doc_worker` with Event 064 and both cluster memberships. Correct the stale leader-trait row, fill all three evolution directions, keep Minor Repeatable and Chaos Level 1, record Sudden Abundance and Military Preparation at Medium, and set Needs Testing only after complete implementation wiring.

Run:

`python .tools/export_event_catalog_csv.py`

Regenerate all catalog exports from the authoritative workbook and verify that unrelated rows remain unchanged.

Spawn `chaosx_documentation_curator` for the permanent Event 064 overview, event-system docs, cluster docs, asset references, achievement docs, and completion evidence.

## Validation

Run normal repository validators, syntax checks, localisation checks, asset checks, and targeted static inspection. Do not invoke the dedicated debug-playtest skill unless the user explicitly requests that workflow.

Execute every deterministic scenario in `matrices/acceptance_criteria.md`, including:

- normal, allied, subject, hostile, civil-war, occupation, enclave, and multi-neighbor frontiers
- strait and island exclusions
- tiny and large countries
- high existing forts
- each evolution alone and together
- lower stage disabled with higher stage enabled
- repeat after border change
- both cluster routes and standalone route
- multi-cluster arbitration
- every posture and project
- save-load and target loss
- each achievement phase
- large fragmented late-game world

Prove there is one world pass per incident, bounded candidates, no duplicate province grant, no recurring world scan, clean temporary state, acceptable performance, and no save bloat.

## Mandatory near-completion review

Before claiming the goal near complete, spawn `chaosx_improvement_loop_planner` with `fork_context=false` using the task preserved in:

`docs/plans/064_border_fortifications_plans/subagent_handoffs/064_border_fortifications_improvement_loop_tooling_blocker.md`

Resolve every accepted addendum or save the closure handoff. The planning environment could not execute this mandatory pass, so implementation must close it.

Then spawn `chaosx_event_completion_auditor` with the full spec, implementation paths, probability evidence, assets, localisation, catalogs, documentation, validators, scenario evidence, save-load evidence, performance evidence, and improvement-loop result.

## Completion rule

Keep iterating until the full Event 064 package is implemented to its fullest extent. Do not claim completion while any baseline rule, evolution, response route, AI scenario, probability proof, Chaos source, cluster membership, history surface, achievement, asset, localisation key, catalog field, documentation item, cleanup path, save-load case, performance test, or improvement-loop disposition remains unresolved.

Report every simplification, omission, fallback, blocked tool, unavailable engine hook, and skipped task-specific validation directly.

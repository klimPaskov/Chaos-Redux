# Event 018 Event-Chain Worker Handoff

## Ownership and result

This tranche replaced the two-event prototype with the complete fixed-ordinal Event 018 chain in:

- `events/018_random_resource.txt`
- `localisation/english/018_random_resource_l_english.yml`

The implemented definition set is exactly:

- `.1-.15`
- `.20-.32`
- `.40-.44`
- `.50-.59`
- `.60-.73`
- `.80-.99`

No decision, mission, shared registry, asset, interface, or gameplay-helper file was edited by this worker.

## Runtime contracts implemented

### Discovery and enrichment

- `.1` is the visible fresh-field entry. Prepared execution requires `resources_found_prefire_ready`, exact owner/state targets, matching ROOT ownership and control, and a still-valid new field state. A deliberate direct fire is allowed only when both prepared targets are absent, selects one valid fresh state once, and never rerolls after the package runs.
- `.2` is the visible enrichment entry. It validates and consumes the exact prepared active field, or the country's selected valid enrichment field on a deliberate direct fire. It calls the highest enabled active package: Evolution IV/III all-resource, Evolution II active, Evolution I active, or baseline. Active Evolution I continues into `.40`, Evolution II into `.50`, and Evolution III/IV into `.60`; the opener detects the already-applied active package and never awards it twice.
- Active Evolution IV enrichment also sets the compressed-opening and breach-prone timing state used by the protected incident escalation, matching the Evolution IV pre-fire contract without creating a cave host or bypassing the ordinary incident gates.
- `.1` initializes the persistent state record, applies the highest enabled pre-fire package, and routes to the matching evolved opening notice without selecting another state.

### Baseline, diplomacy, borders, and transfer

- `.3-.15` cover survey, foreign inquiry, bids, contract activation/interruption, nationalization, settlement, smuggling, sabotage, transfer review, occupation, maturity, and exact baseline closure.
- `.20-.32` preserve the competing-survey, road, patrol, mission, border-war, victory, transfer, stalemate, commission, violation, and dissolution stages.
- `.27` transfers the exact persistent field to its stored valid claimant only when the callback has not already received the completed transfer, then invokes the ordinary ownership-transfer helper.

### Evolved incident and closure paths

- Evolution I has separate active `.40` and pre-fire `.41` packages, plus corridor, international rush, and demilitarization callbacks. Both visible stage openers record the field-scoped Evolution I log entry exactly once.
- Evolution II opens through `.50` and escalates through sickness, corrosion, missing workers, knocking, failed ordinary tests, physical evidence, underground attack, exposed casualties, and restricted stabilization.
- `.50` records the field-scoped Evolution II log entry exactly once and distinguishes pre-fire from active enrichment so the active package is not reapplied.
- `.53` and `.57` use `resources_found_apply_incident_civilian_loss` with the matching Event 018 constants. Concealment flags feed later casualty scaling and achievement disqualifiers.
- Evolution III covers the all-resource opening, public breach, settlement and city attacks, transport loss, aid, hunt results, evacuation results, partial sealing, exact full sealing, failed sealing, and the protected final window.
- `.60` records the field-scoped Evolution III log entry exactly once. Evolution IV remains separately recorded by the cave-emergence helper after all its protected gates succeed.
- `.62`, `.64`, `.67`, and `.69` use the same exact population-loss API with incident-specific constants. Cause `constant:chaos_meter_deaths_reason.resource_field_incident` resolves to shared cause 16 and is registered across the shared Deaths views.
- `.71` calls only `resources_found_complete_full_seal`. It adds no retaliation, successor incident, or hidden penalty. Core cleanup removes normal field-status dynamic modifiers.
- `.73` records incident-sequence completion and creates the constant-driven emergency-seal interval. It does not invoke cave emergence itself, preserving a real final response window.

### Cave, terminal, and defeat callbacks

- `.80` gives the human former owner ordinary resistance and aid choices plus the exact vanilla `DHO = { change_tag_from = ROOT }` continuation. Both the former owner and DHO receive `resources_found_cave_player_continuation_chosen`.
- `.81-.89` cover later breaches, neighbor mobilization, battle counterplay, anchor activation/loss, overcapacity, origin danger, regional defeat, and per-state cleanup.
- `.90-.94` cover quarter, half, three-quarter, last-state, and complete-continent milestones.
- `.95` requires `resources_found_cave_world_end_verified`, rechecks the same terminal conditions in the option, and then calls only `resources_found_cave_begin_world_end`.
- `.96-.99` cover distant footholds, global defeat, the conditional defeat presentation, and reconstruction. `.98` requires `resources_found_cave_global_defeat_eligible` before calling `resources_found_emit_global_defeat_super_event`; regional defeat cannot satisfy it.

## Presentation and writing

- All 16 report/news sprite identifiers reserved by the Event 018 asset specification are referenced at their intended narrative families.
- The English file contains final titles, descriptions, option names, and visible consequence tooltips for all 204 options.
- Player-facing text avoids update-history language, implementation labels, semicolons, em dashes, and placeholder prose.
- Localisation is UTF-8 with BOM and uses no `:0` suffixes.

## Validation evidence

- 77 event definitions were found, with no missing or duplicate fixed ordinals.
- 204 options were found; every option has a name, visible consequence tooltip, AI chance, and gameplay effect block.
- All 562 Event 018 localisation references resolve one-to-one; no duplicate or unused chain keys remain.
- All 70 script-constant references in the event file resolve to declared keys.
- All 54 distinct Event 018 scripted effect/trigger calls resolve to current definitions.
- The evolution-log wrapper call counts are exact: two Evolution I opener calls (`.40` and `.41`), one Evolution II opener call (`.50`), and one Evolution III opener call (`.60`).
- Active enrichment continuation was checked across all four enabled stages: Evolution I routes to `.40`, Evolution II to `.50`, Evolution III to `.60`, and Evolution IV to `.60` with compressed timing, while each opener skips the package already awarded by `.2`.
- All six casualty callbacks reference the incident-specific constant pair and the shared exact population-loss effect.
- The event script has balanced blocks and all 16 required picture identifiers are present.

## Parent-owned dependencies and follow-up

1. The generic dispatcher special branch and owner eligibility are complete and were verified together: prepared enrichment fires `.2`, prepared fresh discovery fires `.1`, and an owner with either kind of valid state is eligible for dispatch.
2. The asset tranche must register and provide the 16 referenced sprites. At this worker's last registration scan, all were still absent from `.gfx` files because asset production was running in parallel.
3. The decision/mission layer must fire the matching callbacks with the intended selected field or regular event target, create the real project costs/timers, set `resources_found_full_seal_requirements_met` only after every seal requirement succeeds, and call `resources_found_begin_cave_emergence` only after `.73`'s protected final window and all cave-entry conditions pass.
4. Contract, commission, and border actions must prepare `resources_found_contract_partner_target`, `resources_found_commission_sponsor_target`, and `resources_found_border_claimant_target` before callbacks that consume those scopes.
5. Event-details, spreadsheet, super-event, achievement, and asset-manifest alignment remain parent-owned completion surfaces. The stage-opening evolution-log calls themselves are wired in this tranche.

## Simplifications and blockers

There are no deliberate event-chain or localisation simplifications in this tranche. Full playable completion still depends on the parent-owned decision/mission callbacks, registered art, and shared presentation surfaces listed above.

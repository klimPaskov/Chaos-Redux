# Event 19 Infantry Spawn Planning Package

> **Historical design routing (2026-07-18):** This source specification preserves the accepted design and the bounded 2026-07-18 near-completion tranche. Older closure language remains historical. Exactly two engine-constrained substitutes were approved for that tranche: exact recorded-formation recreate/prove/delete and controlled one-formation combat trials. The 27 fixed technical identity slots are 20 claimant army/muster scenes, 6 fantastical massed-host scenes, and 1 neutral unassigned muster scene, never an individual focal person. Their stable `GFX_portrait_*` names remain engine and UI terminology, not a description of the depicted content.

> **Current implementation extension (2026-08-22):** The accepted design remains the source specification, while the implemented provider bridge covers 19 Event 19 provider IDs (`501-514`, `518`, `520-523`) and all 50 installed custom combat units. Event 016 adds the separate Germany/Mengele-gated Aryan clone provider 522 beside providers 504-510; it never aliases provider 504. Event 014 owns provider 523 for all nine cannibal irregular combat bodies. Custom manifest profiles 130-148 live in the owning provider constants and resolve dynamically to 20 verified local equipment-token identifiers because the clone and Aryan-clone providers share profile 142 while retaining separate provider identities; provider 521 remains combat-only on the CBRN side, and the 43 support-only CBRN, chemical-tank, and Livens definitions remain explicitly parent-owned. Event 19 MCP inspection is partial and normalized dynamic provider-pool odds remain unresolved, so the older `Fully Functional` and no-closure language below is historical for the 2026-07-18 tranche and must not be used as current provider-lifecycle proof.

> Every provider exposes thirteen runtime callbacks. `event19_get_presentation` supplies family-name, request-cost, and sustainment-cost localisation tokens; `event19_get_equipment_token` resolves an obligation profile to its concrete equipment token and specialist policy; and `event19_publish_custom_equipment_tokens` enrolls every custom stockpile touched by payment or refund in the exact snapshot verifier. A future owner adds one registration surface and this complete callback package without editing an Event 19 family or equipment list. The single Event 19 registry-file rule remains unchanged.

> **Current runtime boundary (2026-08-22):** Event 19 is ID `19`, `Minor Repeatable`, unclustered, and nonterminal. The live scenario is `SCN-013` because proposed `SCN-008` is owned by Independence Wave. The player-facing surface is ordinary decisions and decision categories only; no Event 19 scripted GUI is runtime-wired. Former Muster Board GUI designs, prompts, handoffs, and asset rows remain archival provenance and must not be routed as active GUI work. The current provider extension remains subject to unresolved decision/localisation integration, probability-pool, and final cross-surface documentation gates.

This folder is the source planning package for Chaos Redux Event ID `19`, **Infantry Spawn**.

The request label `017# Infantry Spawn` is preserved in the package history, but the catalog and current repository identify the canonical event as ID `19`. All event, file, registry, achievement, scenario, and documentation identifiers in this package therefore use `019` or event ID `19`.

## Package purpose

The current event is a small repeatable global spawn loop. This package redesigns it as a scalable military disruption system whose identity changes through four evolutions:

1. uneven local musters
2. organized and increasingly advanced formations
3. deliberately requested armies with completely random composition and claimant generals
4. registered Chaos unit families whose reckless use can produce independent nonhuman revolt countries

The design keeps the event repeatable, prevents free equipment farming, separates ordinary lifecycle stages from true evolutions, provides AI behavior, maps the decision-category surface, defines derivative country packages, and includes the requested immediate-mutiny triggerable scenario.

## Folder map

- `specs/` contains the sequential source specification.
- `matrices/` contains implementation-facing design maps for templates, decisions, generals, AI, countries, assets, and cleanup.
- `focus_graphs/` contains the route architecture for derivative nonhuman countries.
- `prompts/` contains the historical build contracts for asset production, achievements, decisions and missions, implementation, and the final implementation goal; the work they request is installed and they must not be executed again.
- `research/` records repository findings and historical design anchors.
- `review/` records full source reading, anti-bloat review, manual role-equivalent subagent reviews, uncertainty, and completion auditing.

## Live source-of-truth map

- This folder owns the accepted Event 19 design. Event 19 is ID `19`, `Minor Repeatable`, unclustered, nonterminal, and has no fixed derivative tag.
- `docs/events/019_infantry_spawn/overview.md` owns the canonical implemented-system explanation.
- `docs/events/019_infantry_spawn/systems/triggerable_scenario.md` owns the direct scenario contract. The live identity is `SCN-013` because proposed `SCN-008` collided with Independence Wave.
- `docs/systems/cbrn_warfare/chaos_unit_family_registry.md` owns registry contract version 4. Event 19 has exactly one dedicated registry code file, `common/scripted_effects/019_infantry_spawn_unit_registry_effects.txt`.
- `common/scripted_triggers/chaosx_dynamic_triggers.md` owns the shared special and nonhuman classifier documentation, and `docs/achievements/019_infantry_spawn/achievements.md` owns the eleven achievement proof contracts.
- The accepted near-completion addendum named above owns the disposition of its three findings. Dated implementation and audit evidence lives under `docs/plans/019_infantry_spawn_plans/subagent_handoffs/`.
- `docs/assets/019_infantry_spawn/manifest.md` and `gfx_handoff.md` preserve historical asset evidence. Their former Muster Board rows are archival because the accepted runtime is decisions-only, and the restored package retains their regional raw/master/validation paths as provenance records. The 2026-07-18 remediation PASS is bounded to that asset tranche and does not establish current provider completion.
- `review/decision_only_surface_addendum_2026-08-05.md` is the accepted current UI-surface decision. It supersedes the earlier scripted-GUI implementation handoffs while preserving their source-art provenance as archival evidence.
- `docs/spreadsheets/chaos_redux_events_catalog.xlsx` is the only editable catalog source. The workbook and generated CSVs retain the 2026-07-18 historical `Fully Functional` snapshot for Event 19 and SCN-013, but that snapshot is not current provider-lifecycle proof.

The 2026-07-18 specialist audits are historical tranche evidence. The current provider-extension handoffs record localisation completion, an unresolved decision/localisation integration pass, unresolved normalized provider odds, and bounded MCP event evidence. The final whole-event completion gate is open for the current extension.

The asset manifest and historical remediation handoff retain the 7/18 regional evidence and three accepted engine-constrained exceptions. Their completion statements remain bounded to that asset tranche and do not close the current provider-extension gate. The seven retained GHOST_BASE prompt records and 7/16 superseded composites remain historical provenance.

## Reading order

1. `specs/019_infantry_spawn_spec_part_1_core.md`
2. `specs/019_infantry_spawn_spec_part_2_spawn_engine_and_baseline.md`
3. `specs/019_infantry_spawn_spec_part_3_evolutions_i_and_ii.md`
4. `specs/019_infantry_spawn_spec_part_4_evolution_iii.md`
5. `specs/019_infantry_spawn_spec_part_5_evolution_iv.md`
6. `specs/019_infantry_spawn_spec_part_6_derivative_countries.md`
7. `specs/019_infantry_spawn_spec_part_7_decisions_ui_ai_balance.md`
8. `specs/019_infantry_spawn_spec_part_8_scenario_interactions_acceptance.md`

The matrices and prompts should be read after the sequential specification.
Part 7 holds the live decision mapping from each design label to its installed identifier and disposition.

## Deliberate boundaries

The event has no terminal world-end outcome. The derivative countries are dangerous regional actors, not substitutes for the Zombie Outbreak, Death, golem, or future parent event endgames. No super-event is planned because the normal event, its evolutions, and its requested triggerable scenario do not meet the project threshold for a campaign-defining presentation moment. A later globally dominant derivative revolt could justify a separate improvement proposal, but it is outside this source design.

The planning text distinguishes working labels from stable script identifiers.
Final in-world English wording is owned by `localisation/english/019_infrantry_spawn_l_english.yml` and its aligned Event 19 documentation and catalog fields.

## Process disclosure

All 30 supplied project files were read in full before this package was drafted.
Their hashes and line counts are recorded in `review/source_reading_manifest.md`.

The planning environment initially lacked the custom project-agent runtime, so its early role-equivalent reviews are preserved as historical design evidence.
Implementation subsequently used project agents with no inherited parent context. A later required near-completion planner pass produced the routed addendum named above; its findings were implemented. Dated specialist handoffs live under `docs/plans/019_infantry_spawn_plans/`.

Implementation also inspected the full local repository, required offline Paradox wiki snapshot, installed vanilla documentation and source precedents, and approved reference mods where needed. Current engine limitations, transaction invariants, and remaining audit gates are recorded in `review/blockers_and_uncertainty.md`.

## Open questions

All entries are proposed (spec audit 2026-10-10) and need a user or parent decision before any implementation.

- Design-only decision rows with no live decision.
  - Part 7 maps every design label to its live identifier; ten rows have none: Trace the Equipment Ledgers, Recombine Random Battalions (with Break It Into Cadres for ordinary lots), Relocate an Impossible Lot, Clear the Training Grounds, Disarm a Claimant District, Reassign Loyal Formations, Limit the Command, Break the Claimant Network, Contain Anomalous Saturation, and Negotiate Retirement.
  - Proposal: retire the first nine as design rows, because settlement, training-cycle, rail, counter-command, discrediting, arrest, the Event 67 demands, and the family decisions already carry their purpose, and a recomposition decision sits too close to the no-reroll rule in Part 1.
  - Proposal: build Negotiate Retirement as the one new decision, because arrest, discrediting, counter-command, takeover, and revolt are today the only ways a claimant crisis ends, and Part 4 promises a peaceful co-option path.
  - Sketch: visible while a claimant exists below the revolt band, paid in political power plus a status concession, success absorbs the claimant's loyal lots into ordinary command and closes the file, and failure raises influence by the shared failure rule; it needs a Black Friday price key and an AI weight beside the other claimant responses.
  - Retiring rows is a reduction of requested functionality, so it stays unresolved until the user approves it.
- Lot and family cursors.
  - Four cursor decisions (`infantry_spawn_select_next_ordinary_lot`, `infantry_spawn_select_next_unaccounted_lot`, `infantry_spawn_cycle_anomalous_family_decision`, `infantry_spawn_cycle_claimant_file`) plus the review decision exist only to move a selection.
  - Proposal: advance the cursor to the next unresolved lot automatically after a lot decision completes, and merge the ordinary and unaccounted lot cursors, so a player rarely spends a click on selection.
  - The current selection rule must be read in `common/scripted_effects/019_infantry_spawn_management_effects.txt` before this is specified further.
- Claimant takeover and the Chaos Meter.
  - A takeover applied with `set_politics` reaches the meter only if the ruling party actually changes; it never calls `chaos_meter_on_coup_succeeded`.
  - Proposal: leave it as is, because a second contribution would duplicate the ideology-change amount; add a direct amount only for a takeover that keeps the ruling party.
- Anomalous Saturation display: Part 5 now asks for the band and the main contributor instead of a component list; confirm that this matches the intended decision-only surface.
- Event document drift (owner outside this package): `docs/events/019_infantry_spawn/overview.md` says Evolution II offers an unrestricted draw and still describes a Muster Board refresh and six board markers in its Black Friday and asset sections, while the installed decisions give Evolution II four lane-split requests and Evolution III the unrestricted draw, and the board has no runtime consumer.

## Changelog

- 2026-10-10 specification audit.
  - Adopted the earlier same-day audit pass that was left uncommitted in Parts 4 and 7: the live decision mapping table, the Group E request-lane note, the Part 4 lot-disposition mapping, and the condensed archived scripted-GUI section; each identifier in the table was checked against `common/decisions/019_infantry_spawn_*.txt`.
  - Added the mapping rows for integration staff, the emergency reserve, the training cycle, the prototype trial, lot cursors, request modes, the request-cooldown mission, and the four combat trials, and stated the live status under each design-only decision and mission heading.
  - Part 3 records that the evolutions are timed by a multi-signal score with no calendar date gate, and that Evolution II requests are lane-split while the unrestricted draw is an Evolution III feature.
  - Part 5 replaces the saturation component breakdown with a band plus main contributor, and Part 7 adds a proposed surface budget so no Event 19 tooltip lists many values.
  - Part 8 now reflects the installed state: Event 19 is in the default-enabled allowlist, the golem body is `coal_golem`, the Event 67 and Event 96 bridges are live, Events 127 and 131 have no package yet, Event 19 writes no Chaos Meter amount of its own, and Famine and Migration receive nothing from Event 19 except through shared state-level owners.
  - The decision and asset matrices mark unresolved rows and condense the archived scripted-GUI tables; the three non-GUI prompts are marked as historical build contracts that must not be executed again.
  - `review/blockers_and_uncertainty.md` condenses its two superseded gate step lists into one disposition line.
  - No gameplay source, localisation, plan, event document, or spreadsheet was edited; the Open questions above hold every unresolved proposal.

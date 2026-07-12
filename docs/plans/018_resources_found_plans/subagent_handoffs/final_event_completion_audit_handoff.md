# Event 018 final completion audit handoff

## Gate result

**FAIL — Event 018 is not complete.**

The final live gameplay re-audit passes the named ledger, achievement, closure, cave-country, target-selection, World-End, registry, and foreign-scoring scenarios after the parent-owned repairs made during this audit. The completion gate still fails because the source package's field-detail UI, visible Closed state, super-event duration, asset-provenance, combined super-event research, and audio-rights requirements are not all satisfied. A documented audio checksum is also wrong.

The Event completion-auditor checkbox in `docs/specs/018_resources_found_specs/matrices/acceptance_criteria.md` remains unchecked. This audit does not authorize that checkbox to be marked complete while the findings below remain unresolved.

## Audit snapshot and boundary

- Audit date: 2026-07-12, Europe/Kyiv.
- Git HEAD at the audit snapshot: `dedb30ed`.
- The live worktree was heavily dirty with concurrent work. This audit evaluated the live Event 018 files, including parent-owned repairs made while the audit was running, and did not treat unrelated changes as part of Event 018 evidence.
- The user explicitly waived launching Hearts of Iron IV. No live-engine, combat, GUI-scale, audio-playback, or campaign-AI result is claimed.
- No logs were requested. The existing historical `error.log` was inspected only as older negative evidence: last write `2026-07-11T16:58:09.7659249+03:00`, 6,077 bytes, with zero `018_resources_found`, `chaosx.nr18`, `DHO`, `Oth-Kesh`, or `Vhorruk` hits. It predates the final live repairs and cannot prove current runtime behavior.
- This final auditor changed no gameplay, localisation, asset, specification, spreadsheet, acceptance-checkbox, staging, or commit surface. Its only authored file is this handoff.

## Required references consulted

The main audit read the complete instructions for `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, `chaos-redux-super-events`, `hoi4-focus-trees`, `hoi4-decisions-missions`, `chaos-redux-subagents`, `chaos-redux-improvement-loop`, and the relevant event-planning guidance before adjudicating their surfaces.

The required offline wiki snapshot was consulted, including:

- `Data structures - Hearts of Iron 4 Wiki.md`
- `Triggers - Hearts of Iron 4 Wiki.md`
- `Effects - Hearts of Iron 4 Wiki.md`
- `Modifiers - Hearts of Iron 4 Wiki.md`
- `Localisation - Hearts of Iron 4 Wiki.md`
- `Scopes - Hearts of Iron 4 Wiki.md`
- `On actions - Hearts of Iron 4 Wiki.md`
- `Event modding - Hearts of Iron 4 Wiki.md`
- `Decision modding - Hearts of Iron 4 Wiki.md`
- `Idea modding - Hearts of Iron 4 Wiki.md`
- `AI modding - Hearts of Iron 4 Wiki.md`
- `National focus modding - Hearts of Iron 4 Wiki.md`
- `Country creation - Hearts of Iron 4 Wiki.md`

Vanilla documentation and live vanilla precedents were consulted in parallel, including `effects_documentation.md`, `triggers_documentation.md`, `modifiers_documentation.md`, `script_concept_documentation.md`, `dynamic_variables_documentation.md`, and `common/script_constants/documentation.md`. Current dynamic-resource semantics were checked against `dynamic_variables_documentation.md`; Event 018's six-resource deficit/import/production scoring was not adjudicated from memory.

The complete Event 018 source package was treated as authoritative: all eight sequential specs, all six matrices, the focus architecture, the six specialist prompts, the research notes, the accepted improvement-loop disposition, the static acceptance report, prior specialist handoffs, asset manifests, super-event research, and spreadsheet rows were reviewed.

## Unresolved completion blockers

### 1. The required field-detail UI is incomplete

Requirement:

- `docs/specs/018_resources_found_specs/specs/018_resources_found_spec_part_1_core_and_baseline.md:365-378` requires a field detail view showing current owner and controller, state name, discovered resource composition, discovery count, administration posture, lifecycle stage, the five value bands, contract or commission status, and closure or suspension status.

Live evidence:

- `interface/018_resources_found.gui` exposes selected state, the six-resource ledger, Developed Yield, Excavation Depth, Workforce Safety, Foreign Pressure, revealed Disturbance, revealed Breach Pressure, condition art, and navigation controls.
- `localisation/english/018_resources_found_system_l_english.yml:69-79` supplies only those fields.
- Repository-wide searches found no second live field-detail surface displaying owner, controller, discovery count, posture, lifecycle stage, contract or commission status, or explicit closure/suspension status.
- The compact-header checklist at `matrices/acceptance_criteria.md:62-79` is narrower than the sequential source spec and does not supersede it.

Repair contract:

1. Extend the live field-detail GUI and its scripted localisation with every omitted durable fact.
2. Keep values attached to the exact selected field record, not inferred from unrelated country state.
3. Preserve reveal gates for Disturbance and Breach Pressure.
4. Show owner and controller independently when occupied.
5. Show contract, commission, suspension, closing, and permanent-closure states without implementation-history wording.
6. Re-audit layout and visibility statically; runtime visual scale remains outside this waived pass.

### 2. The required Closed visual state is registered but never visible

Requirement:

- `specs/018_resources_found_spec_part_8_ai_text_assets_and_acceptance.md:350-357` includes a closed state in the field UI state family.
- `prompts/resources_found_asset_prompt.md:470-476` names `GFX_018_resource_field_closed` as the permanent sealed-work state.

Live evidence:

- `interface/018_resources_found.gfx:85` registers `GFX_018_resource_field_closed`.
- The source PNG, processed PNG, DDS, dimensions, and hash are complete in `docs/assets/018_resources_found/animations/selected_field_ui/manifest.md`.
- `interface/018_resources_found.gui` has no Closed `iconType`.
- `common/scripted_guis/018_resources_found_scripted_gui.txt` has no Closed visibility path.
- The asset manifest explicitly says the sprite was intentionally left out because exact closure removes the field from the active registry. That lifecycle concern is valid, but it is an unapproved specification omission, not proof that the visible state exists.

Repair contract:

1. Wire the existing sprite to a real visible history, last-closed-record, closure-confirmation, or other spec-compliant GUI state.
2. Do not keep a permanently closed field in the active discovery registry and do not make it rediscoverable merely to show the art.
3. Gate active-field condition sprites and Closed presentation so they cannot overlap.
4. If the intended design is to remove Closed from all live UI, obtain explicit user approval and update the source spec and asset prompt rather than silently treating the omission as complete.

### 3. All three final super-event tracks are too short

Requirement:

- `prompts/resources_found_super_event_prompt.md:100-112` requires roughly one to two minutes for the emergence track.
- The same prompt requires one to two minutes after trim for the World-End track at lines `177-186` and one to two minutes for the defeat track at lines `247-256`.

Live evidence from `ffprobe`:

| Audio ID | Runtime file | Duration |
| --- | --- | ---: |
| 54 | `music/018_resources_found/super_event_54_oth_kesh_emergence.ogg` | 34.000 seconds |
| 55 | `music/018_resources_found/super_event_55_deep_war_crosses_seas.ogg` | 34.000 seconds |
| 56 | `music/018_resources_found/super_event_56_last_depth_sealed.ogg` | 34.000 seconds |

All are unique, real-music Vorbis tracks at 44.1 kHz stereo, but none satisfies the specified duration and no approved exception exists.

Repair contract:

1. Produce unique, licensed, musically structured 60-to-120-second final cuts for IDs 54, 55, and 56.
2. Replace both OGG runtime files and preserved WAV mirrors.
3. Keep the tracks distinct and preserve the no-generated-tone, no-drone, no-placeholder requirements.
4. Re-run duration, codec, channel, sample-rate, loudness, peak, and uniqueness checks.
5. Update every hash, edit ledger, source attribution, and final-path reference.

### 4. The Event 018 icon provenance package is incomplete

Requirement:

- `prompts/resources_found_asset_prompt.md:659-679` requires every asset to record its source mode, generation prompt, inspected reference folder, source and processed paths, final path, dimensions, sprite, target GFX file, related live surface, status, and uncertainty.

Live evidence:

- Physical and live-wiring checks pass for 65 focus icons, 36 idea/state icons, 44 decision/category icons, and 5 category pictures.
- Existing inventories and GFX maps do not supply a per-asset generation prompt, source-mode record, and reference-inspection record for these 150 assets.
- The selected-field animation and achievement packages do have strong prompt/provenance ledgers; that evidence does not cover the other icon families.

Repair contract:

1. Create a complete per-asset provenance ledger for all 150 affected assets.
2. Record actual prompts and source history; do not reconstruct fictitious provenance after the fact.
3. If the original generation/source record is unrecoverable, regenerate or resource the affected art through an approved workflow, or obtain an explicit user disposition. A silent provenance fallback is forbidden.
4. Cross-check every ledger row against the physical source, processed output, runtime file, sprite, and live reference.

### 5. The mandated combined super-event research note is absent

Requirement:

- `prompts/resources_found_super_event_prompt.md:27-35` mandates `docs/super_events/018_resources_found_super_event_research.md`, containing considered candidates, selected sources, confidence, licensing, final paths, implementation IDs, and open blockers.

Live evidence:

- `Test-Path` for the mandated file returns false.
- Substantive text and audio research exists in separate Event 018 notes, but the exact required source-of-truth deliverable does not.

Repair contract:

1. Create the mandated combined research file.
2. Reconcile, rather than merely link, the three roles' text, quotation, image, audio, licensing, IDs, paths, rejected candidates, and open issues.
3. Make the combined note agree with the final live audio durations, hashes, and rights disposition.

### 6. The WAV 56 checksum is stale in two source-of-truth documents

Live file:

- `sound/018_resources_found/super_event_56_last_depth_sealed.wav`
- Actual SHA-256: `199de5830ce1444b4405cdecdc46acf510af474667998437a57f3e6e9d62a0e5`

Incorrect documentation:

- `docs/assets/018_resources_found/audio_manifest.md:43`
- `docs/super_events/018_resources_found_super_event_audio_research.md:185`

Both documented hashes omit the `f` in `...46acf510...`.

Repair contract: correct both records after the final audio replacement. If the audio is replaced to satisfy duration, record the replacement hash rather than the current one.

### 7. Audio ID 55 retains a material distribution-rights caveat

The audio research correctly discloses that ID 55's recording is supported as U.S. public domain, not by a worldwide CC0 or equivalent grant. Documentation exists, but the selected basis is not a clean worldwide distribution grant. This matters for a distributable mod and is not removed by accurate attribution.

Repair contract:

1. Replace ID 55 with a recording whose composition and recording rights support the intended distribution, or obtain an explicit user decision accepting the jurisdiction-limited risk.
2. Preserve the selected source page, rights statement, author/performer credit, edit history, and final attribution in the combined research note and audio manifest.

## Named gameplay scenario verdicts

| Scenario | Result | Evidence and adjudication |
| --- | --- | --- |
| Baseline discovery and field ledger | PASS | One uniformly selected standard resource receives an 80-to-120 inclusive deposit centered on 100; six event-owned resource ledgers remain separate from state totals; repeat enrichment updates the existing field instead of duplicating initialization. |
| Exact full seal | PASS | The inverse subtracts only the six recorded Event 018 additions, protects unrelated state resources, clears active-field registration, and permanently blocks rediscovery and Evolution IV for that field. |
| Closure project lifecycle | PASS after live repair | Event `.57.c` and `.61.b` now use the same paid partial-closure launcher as the decision; `.73.a` uses the paid emergency launcher. `.59.b`, `.70.b`, and `.72.a` record nonblocking intent. Canonical launchers at `common/scripted_effects/018_resources_found_decision_effects.txt:583-688` pay once, bind one field, set physical closure flags only after valid project preparation, and activate one containment mission. |
| Closure cancellation and owner/control loss | PASS after live repair | `resources_found_fail_selected_field_project` at `common/scripted_effects/018_resources_found_decision_effects.txt:1360-1398` clears partial, full-seal, emergency-seal, requirements, project-active, and field-closing flags on the locked field even when the original country no longer owns or controls it. No missionless closing state remains in the static cancellation paths. |
| Suspension and Maximum Shifts accounting | PASS | `resources_found_suspend_field` finalizes extraction tracking before suspension dates are written, and resume starts a fresh interval only while Maximum Shifts remains the durable posture. Suspended days cannot enter the extraction-achievement ledger. |
| Mutually exclusive field stages | PASS | All six output-stage modifiers are cleared and rebuilt only through `resources_found_normalize_field_output_stage` and the common field refresh path at `common/scripted_effects/018_resources_found_effects.txt:345-417`. |
| Contract of the Century | PASS | The immutable 365-day review is bound to one field, owner, partner, active long-term contract, exact yield/safety/pressure thresholds, sovereignty, and disqualifiers. Restoring a failed condition does not repair a disqualified term. |
| Resolve a Field Dispute | PASS | The 180-day settlement is bound to the exact field, claimant, owner, severe claimant-specific history, and live settlement mode; transfer, renewed coercion, border war, occupation, or actor invalidation cancels it. |
| Thirty From Below | PASS | Owner/controller eligibility is snapshotted before transfer, cave strength is frozen before release, exactly 30 starting divisions is required, and the original capital, independence, survival, and regional-defeat gates are rechecked. |
| Last Shaft Closed | PASS | Only mature, ordinary, non-origin anchors count, once per state and contributor; at least three are required; regional defeat, zero residual anchor/cleanup state, and cleared world-threat source are rechecked. |
| Burrow War objective | PASS | The target must be a defended enemy capital/supply/fort state adjacent to an active anchor; the exact target pointer, start-defense fact, 90-day mission, control-change success hook, World-End exclusion, and cancel/timeout cleanup agree. |
| Hills Begin to Move | PASS | Only deployed Scree Packs count; per-attempt state and defeated-country ledgers deduplicate exact identities; completion requires at least five distinct states, two distinct countries, three live Scree Packs, sufficient capacity, the route capstone, and no World End. |
| Ground Is Quiet Again | PASS | Completion requires the actual Event 018 World-End super-event history, eligible global defeat, ordinary-country contribution, completed reconstruction, zero surviving DHO territory, zero residual anchors/cleanup, and cleared threat source. The player-facing tooltip names `THE DEEP WAR CROSSES THE SEAS` rather than an internal flag. |
| Route evidence | PASS after live repair | Moving Mountain, Front Has a Floor, and Hills Begin to Move route flags are set only at their named capstones (`focus_tree.txt:660`, `:760`, `:860`). |
| Richest reachable state | PASS after live repair | `resources_found_cave_mark_richest_reachable_state` at `common/scripted_effects/018_resources_found_cave_effects.txt:1609-1642` now computes the exact standard-resource total for every eligible reachable enemy state and retains the deterministic maximum with a stable first-state tie rule. |
| Later breach registry | PASS | A later valid Evolution IV breach reinforces the one existing DHO tag, removes the converted field from the former owner's registry, repairs the selected-field pointer, transfers and cores the state, creates its anchor, and refreshes capacity/wars without spawning a contradictory cave country. |
| World-End capstone | PASS after live repair | The DHO daily pulse now completes delayed verification and emits notice `.95` only. Event `.95` is notice-only at `events/018_random_resource.txt:3230-3251`. Repository-wide caller scan finds exactly one call to `resources_found_cave_begin_world_end`: final focus `DHO_the_world_opens_below` at `common/national_focus/018_resources_found_cave_focus_tree.txt:1159-1171`; the shared effect rechecks the exact gates. |
| Foreign interest scoring | PASS | One Invite Strategic Bids entry point performs one deterministic country scan. Six resource-specific deficit/import/consumption/production gates combine with field/owner factors, route, relations, claims, rivalry, war, major status, factories, overextension, and a minimum threshold. No random fallback selects a foreign partner. |

## Achievement completion matrix

All fifteen achievements are defined at `common/achievements/chaos_redux_achievements.txt:2613-2760`, localized, and have distinct available, greyed, and unavailable artwork. Their final predicates live in `common/scripted_triggers/018_resources_found_achievement_triggers.txt`.

| Achievement | Result | Core proof |
| --- | --- | --- |
| One Vein Market | PASS | Ordinary eligible owner controls an active field with one Event-owned resource at or above the required single-resource threshold. |
| All Resources, One State | PASS | One active controlled non-origin field has positive Event-owned oil, aluminium, rubber, tungsten, steel, and chromium ledgers. |
| Every Worker Home | PASS | The dedicated evacuation/safety history flag is awarded only by the qualifying field path and requires ordinary-country eligibility. |
| Full Seal at Evolution III | PASS | A successful eligible Evolution III exact seal records the dedicated outcome and excludes cave-player continuation. |
| Contract of the Century | PASS | Uses the immutable field/owner/partner 365-day evidence described above. |
| Resolve a Field Dispute | PASS | Uses the immutable claimant-specific severe-history and 180-day settlement evidence described above. |
| Thirty From Below | PASS | Requires exact maximum starting strength, original owner/controller eligibility, capital recovery, independence, survival, and regional defeat. |
| Last Shaft Closed | PASS | Requires three distinct mature-anchor cleanups and the complete regional cleanup state. |
| Ten From One State | PASS | Cave-player route uses the exact single-state capacity/output history rather than a country-wide total. |
| No Men, No Guns | PASS | Cave player reaches the required brood and anchor totals before World End while remaining on the no-manpower/no-equipment system. |
| Moving Mountain | PASS | Exact route capstone, prepared-major victory, origin retention through the qualifying war, and pre-World-End state are required. |
| Front Has a Floor | PASS | Exact Burrow route plus the pointer-bound 90-day defended-objective capture is required. |
| Hills Begin to Move | PASS | Exact route plus the distinct state/country/Scree/capacity ledger is required. |
| Continental Appetite | PASS | Cave player consumes the origin continent, completes verification, fires the actual Event 018 World End and super-event, and creates at least one valid distant foothold. |
| The Ground Is Quiet Again | PASS | Uses the immutable global World-End/global-defeat/reconstruction and complete cleanup predicate described above. |

## Other passing implementation surfaces

### Event, decision, and integration wiring

- Entry root remains `chaosx.nr18.1`.
- The Event 018 script defines 77 unique `.nr18` events; all 77 referenced numeric IDs are defined.
- Six Event 018 news events (`chaosx.news.84` through `.89`) are defined and routed.
- Six decision categories, 134 decisions/missions, and 21 timed mission definitions are present; every referenced Event 018 decision/mission identifier is defined.
- Event category registration, settings gate, auto-fire path, event-log actor mapping, event details, evolution log chronology, news, and super-event dispatch are wired.
- The only periodic country hook is the explicitly narrow `on_daily_DHO`; no new world-iterating daily/weekly/monthly on-action was introduced.

### Cave country and focus tree

- `DHO` is uniquely registered; the Oth-Kesh/World Below identities, Vhorruk, three commanders, portraits, parties, traits, history, and cosmetic forms are present.
- Five brood templates are locked and non-recruitable. Brood battalions use no ordinary manpower/equipment economy, have no recruitable production loop, and DHO receives no ordinary air/navy/convoy/faction/market route.
- The focus tree has exactly 65 unique focus IDs and 65 unique coordinates, no missing prerequisite, a completion reward and AI weight for every focus, and complete title/description/tooltip/icon coverage.
- The three doctrine roots are mutually exclusive and have distinct capstones and spawn-preference effects.
- Captured-state capacity sums the six standard resources, uses `floor(total/10)`, caps a state at 10, gives the origin zero, removes capacity after the control-loss grace period, and keeps automatic spawning under live capacity.
- Defeat and cleanup remove DHO threat state, arrays, targets, objectives, terminal ideas, cosmetic identity, cores, anchors, footholds, and cleanup flags through the annexation/capitulation/puppet hooks.

### Localisation, GFX, animation, and documents

- Event 018's dedicated English localisation has UTF-8 BOM, no `:0` keys, no leading-space keys, no replacement characters, and no duplicate keys.
- All 65 focuses have title and description localisation; all 15 achievements have name, description, and tooltip localisation.
- A static key-reference audit found no missing key among 562 explicit Event 018 event-localisation references or 418 explicit tooltip references.
- The nine hidden evolution-clock mission keys are intentionally absent because those missions are permanently non-rendered.
- All 153 unique Event 018 GFX references resolve to a unique sprite definition and existing runtime file.
- All 235 runtime DDS files exist and are pixel-identical to their processed PNG sources; all 18 DHO flag TGAs match their processed sources.
- Report, news, portrait, super-event, focus, idea/state, decision/category, achievement, and flag families are physically complete. No placeholder or duplicated runtime art was found.
- All selected-field animation families and Vhorruk's animated portrait use genuinely distinct planned frames, with source frames, sheets, previews, contact sheets, static fallbacks, and frame-zero parity. They are not transform-only animations.
- Super-event slots 82-84 and audio IDs 54-56 are registered and dispatched; quotation provenance matches the live Job, Aeschylus, and Herodotus text.
- Workbook `docs/spreadsheets/chaos_redux_events_catalog.xlsx` has aligned Events and Clusters rows, no formula errors, automatic calculation, and premise/evolution/cluster wording matching the live game text.

## Focused static validation after the live repairs

- 36 dedicated Event 018 script, GUI, and GFX files were checked after the final gameplay repairs: zero brace-count mismatches and zero literal unsupported `<=`/`>=` operators.
- Unique custom-call scan: 401 `resources_found_* = yes` calls, 410 custom effect/trigger definitions, zero unresolved calls.
- Event scan: 77 unique `.nr18` definitions, 77 referenced `.nr18` IDs, zero undefined IDs.
- Direct physical closure call scan: only the canonical containment-project launcher calls `resources_found_begin_partial_closure` or `resources_found_begin_full_seal`.
- World-End call scan: exactly one caller, final focus `DHO_the_world_opens_below`.
- Route setter scan: one setter each for Moving Mountain, Front Has a Floor, and Hills Begin to Move, all at their named capstones.
- Audio duration and SHA-256 checks produced the exact unresolved findings above.

These checks are task-specific evidence, not a substitute for the waived live-engine run.

## Simplifications, omissions, and blockers

No fallback or simplification was accepted by this auditor. The implementation is incomplete because the seven unresolved items above remain. In particular:

- the full field-detail presentation is omitted;
- the Closed asset is not visible on a live surface;
- all three final tracks use a shorter unapproved duration;
- 150 icon/category assets lack the required individual provenance record;
- the combined super-event research deliverable is omitted;
- one audio hash is stale in two documents;
- one selected recording retains a material jurisdiction-limited rights caveat.

The static-only test boundary is an explicit user waiver and is reported as a limitation, not disguised as observed gameplay. No completion claim, acceptance-checkbox change, stage, or commit should be made until the remaining requirements are repaired or explicitly dispositioned by the user.


# Event 006 localisation audit handoff — 2026-07-26

## Bounded verdict

PASS for the bounded localisation scope after one narrow player-facing wording repair.

The whole Event 006 implementation remains HOLD for the unrelated runtime, shared-layout, package, portrait, asset, and live presentation blockers recorded by the parent audit set.

No fallback content or gameplay change was introduced.

## Scope and source surfaces checked

- All 34 `localisation/english/006_independence_wave*_l_english.yml` files were parsed as one Event 006 namespace set.
- The ten Event 006 scripted-localisation files were checked: `006_independence_wave_decision_scripted_localisation.txt`, `006_independence_wave_focus_scripted_localisation.txt`, `006_independence_wave_form03_scripted_localisation.txt`, `006_independence_wave_form05_scripted_localisation.txt`, `006_independence_wave_formable_registry_scripted_localisation.txt`, `006_independence_wave_gui_scripted_localisation.txt`, `006_independence_wave_iw005_flanders_scripted_localisation.txt`, `006_independence_wave_rival_bloc_scripted_localisation.txt`, `006_independence_wave_scenario_scripted_localisation.txt`, and `006_independence_wave_scripted_localisation.txt`.
- Shared event-log and super-event localisation references were checked in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt`, `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt`, and `common/scripted_localisation/chaosx_scripted_localisation_debug.txt`.
- Event source references were checked across the nine `events/006_*.txt` files, including `chaosx.nr6.1`, `chaosx.nr6.2`, `chaosx.nr006.*`, option names, event descriptions, and custom effect tooltips.
- Focus source was checked across the four `common/national_focus/006_*.txt` files, including the shared tree and the AGX overlay.
- Decision source was checked across the Event 006 decision files and the vanilla formable compatibility decision; decision category IDs and descriptions were checked across the 18 Event 006 category files.
- Achievement IDs and tooltip references were checked in `common/achievements/chaos_redux_achievements.txt` and `localisation/english/006_independence_wave_achievements_l_english.yml`.
- Event-log evolution, cluster, event-details, scenario, and super-event surfaces were checked against their shared localisation and scripted-localisation consumers.

## Required audit output

### Missing key list

- None in the Event 006 scoped localisation set.
- The compatibility decision references vanilla `form_idel_uralic_republic` and `form_idel_uralic_republic_desc`; those are intentional external vanilla localisation dependencies, not missing Chaos Redux keys.
- The shared focus tree has no consumed `independence_wave_focus_tree_desc`; `independence_wave_focus_tree` is the actual tree key and is present.
- Event-log scripted localisation resolves all 15 Event 006-specific event/evolution/history keys, including `chaosx.events_log.window.event_details.independence_wave`, all five evolution titles, all five evolution bodies, the evolution type, summary, and the 6002 history title/description.

### Duplicate key list

- None across the 34 Event 006 English localisation files.
- The scoped parse found 5,602 key rows after excluding `l_english` headers, with zero duplicate IDs and zero `:0` keys.

### Scripted localisation issue list

- None unresolved.
- The ten Event 006 scripted-localisation files contain 337 `localization_key` references, 331 unique targets, and all targets resolve against the English localisation set.
- Event-log and evolution selectors use `independence_wave.evolution.*` keys that are present in `006_independence_wave_evolutions_l_english.yml`.
- `GetIndependenceWaveLeaguePhase` is already wired to named phase localisation and is consumed by the GUI; no raw numeric phase text remains in that surface.

### Dynamic text opportunities

- Existing dynamic localisation is sufficient for the checked surfaces: scenario counts, package IDs, rejection reasons, phase names, event-log dates and actors, evolution stages, and decision/focus constants are all displayed through scripted or variable-backed text.
- The AGX focus overlay has eight title/description/custom-effect-tooltip triplets, with explicit route-dependent outcomes and current constants in the displayed values.
- The AGX conference decision still has a low-priority gameplay-owned opportunity for a dedicated custom trigger tooltip that groups its five prerequisites and separates them from the strategic cost. Its description already names secure waterline, recognition, network membership, water-board mandate, and Low Countries candidacy, and its cost triplet is explicit, so no localisation-only key was invented.

### Cross-surface mismatch notes

- AGX overlay: all eight focus IDs have title, `_desc`, and `_tt` keys in `006_independence_wave_wallonia_frisia_l_english.yml`.
- AGX conference decision: `independence_wave_agx_convene_north_sea_coastal_conference_desc` names all five visible prerequisites; `independence_wave_cost_agx_coastal_conference`, `_tooltip`, and `_blocked` all use the major civilian-factory constant and therefore match the three-factory reservation.
- AGX mandate and dossier text correctly distinguish authorization from federation consent and ratification; no hidden route name is revealed before the relevant overlay stage.
- The shared Liberations cluster resolves to `chaosx.event_cluster.liberations.name`, and the Event Details window resolves to `chaosx.events_log.window.event_details.independence_wave`.
- Achievement surface: all 16 `chaosx_006_*` IDs have `_NAME` and `_DESC` strings, and all 17 source tooltip references resolve.
- Super-event 6002 has all four presentation strings (`chaosx_super_event.24.t`, `.d`, `.a`, `.q`) plus its Event 006 history title/description. Super-event 6001 remains intentionally absent because the approved rights/audio gate is blocked; this is a non-localisation blocker, not a missing-key defect.
- No Event 006 player-facing string exposes portrait, asset-pipeline, provenance, rights, attestation, or visual-audit gates. The remaining `asset ledger` wording is in-world public-property language, not an implementation leak.
- The SCN-008 scenario ledger intentionally exposes its frozen-plan rejection categories, but the former package-unready wording leaked implementation terms and was repaired below.

### File encoding concerns

- All 34 Event 006 English localisation files begin with UTF-8 BOM bytes and parse as UTF-8.
- The patched scenario file retained its BOM.
- No Event 006 localisation file uses a `:0` key suffix.

## Patch made

Changed file: `localisation/english/006_independence_wave_scenario_l_english.yml`.

Changed key: `independence_wave_scenario_reject_package_unready`.

Before: `Rejected because its researched playable package or exact force mapping is not ready. Registry membership alone does not authorize shallow release content.`

After: `Rejected because the proposed state lacks a complete institutional and military foundation for a safe release. It remains closed until its government and opening defenses are ready.`

The before text exposed registry, force-mapping, and shallow-content implementation language in a player-facing rejection ledger. The after text preserves the same blocked outcome while describing the state’s institutional and defensive readiness in-world.

## Validation evidence

- Scoped BOM, duplicate, and key-shape parse: 34 files, 5,602 keys, zero BOM failures, zero duplicates, zero `:0` keys.
- Scripted-localisation target scan: 10 files, 337 references, 331 unique targets, zero missing targets.
- Event source reference scan: all Event 006 event title/description/option/custom-effect references resolved; no missing Event 006 localisation targets.
- Decision cost scan: 321 custom-cost references, 101 unique cost bases, and zero missing `_tooltip` or `_blocked` triplets.
- Focus scan: four source files and the AGX eight-focus overlay resolved; zero missing custom-effect tooltip keys.
- Achievement scan: 16 Event 006 achievement IDs, zero missing `_NAME`/`_DESC` pairs, and zero missing tooltip targets.
- Event-log/evolution scan: 15 Event 006-specific scripted-localisation targets, zero missing.
- No HOI4 process, live save, GUI render, or in-game playback was run, per repository policy; those checks belong to the parent/user validation boundary.

## Unresolved wording decisions and blockers

- The optional AGX custom trigger tooltip would require a gameplay decision-file edit and is therefore left with the owning decision agent.
- SCN-008 still contains intentionally technical ledger terms such as package, registry row, frozen plan, and transaction proof in its diagnostics; no further wording change was made because that surface is explicitly a launch/readiness ledger and its values correspond to the current planner vocabulary.
- Portrait and asset admission gates remain runtime/docs concerns and are correctly absent from player-facing localisation.
- Super-event 6001 remains rights-blocked, and 6002 live playback remains unproved; neither is a localisation key gap.

## Handoff path

This audit and the narrow wording repair are recorded at `docs/plans/006_independence_wave_plans/subagent_handoffs/006_localisation_audit_2026_07_26.md` for parent review.

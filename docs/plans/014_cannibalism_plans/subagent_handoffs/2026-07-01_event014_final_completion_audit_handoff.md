# Event 014 Cannibalism Final Completion Audit Handoff

Audit mode: read-only completion audit. No gameplay, localisation, interface, asset, sound, or spreadsheet files were patched.

Overall status: partial. Event 014 has a large working implementation, but it is blocked for no-simplification completion. The blockers are not load-only syntax issues; they are spec-role, asset-workflow, mission-depth, AI-depth, and documented-validation gaps against the accepted specs and plans.

## Completion Status By Surface

| Surface | Status | Evidence |
| --- | --- | --- |
| Minor Fire-Once registration | Implemented | `common/scripted_effects/chaosx_logic_effects.txt:160` registers `global.fire_once_events = 14`; `common/scripted_effects/chaosx_logic_effects.txt:526-527` blocks the pool if no valid origin exists. |
| Entry and outbreak chain | Partial | `events/014_cannibalism.txt` defines `chaosx.nr14.1`, `.2`, `.4`, `.5`, `.6`, `.7`, `.8`, `.9`, `.10`, `.13`, `.14`. Spec roles for `.3`, `.11`, and `.12` are absent, and `.4` is used as spread exposure rather than public leak news. |
| Opening war-horror discipline/supply collapse | Implemented | `events/014_cannibalism.txt:30-72` opens with discipline, logistics, and secrecy postures; `common/scripted_effects/014_cannibalism_effects.txt:167-236` initializes country outbreak variables and posture effects. |
| Local containment and spread-country response | Implemented with simplifications | `events/014_cannibalism.txt:74-122` gives spread, containment success, and containment failure events; `common/scripted_effects/014_cannibalism_effects.txt:580-619` performs local cleanup and success achievements. Mission target geography remains abstract. |
| Evolutions I-III | Implemented mechanically | `common/scripted_effects/014_cannibalism_effects.txt:730-834` records ritual hunger, silent islands, and global table evolutions; event-log localisation exists in `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:2031-2054` and `:5099-5172`. |
| World-end gate | Implemented | `common/scripted_triggers/014_cannibalism_triggers.txt:387-409` requires global table, Hannibal or accepted unifier, chaos threshold, network strength, cult nodes, and communes; `common/scripted_effects/014_cannibalism_effects.txt:1229-1241` launches world-end only through that trigger. |
| Decisions and missions | Implemented with unresolved depth gaps | `common/decisions/014_cannibalism_decisions.txt` contains concrete costs and timed missions using Command Power, Army XP, equipment, trains, convoys, fuel, manpower, stability, war support, supplied commitment, controlled-state access, naval access, and deadlines. Prior audit still records abstract mission geography and missing outbreak-country production/supply AI strategy. |
| Political power store | Not present | No Event 014 decision store was found; costs are direct resource gates/spends. |
| Exploitation danger | Implemented | `common/scripted_effects/014_cannibalism_effects.txt:510-515` increases deaths/network/resonance and flags exploitation; `:1414-1431` makes dismantle/failure interact with Hannibal resonance. |
| CBL country package | Mostly implemented | `common/country_tags/chaosx_countries.txt:6`, `common/countries/Cannibal Commune.txt`, `history/countries/CBL - Cannibal Commune.txt`, `history/units/CBL_1936.txt`, `common/characters/CBL.txt`, `common/national_focus/014_cannibalism_focus_tree.txt`, `common/ai_strategy/014_cannibalism.txt`, and `common/countries/cosmetic.txt:41` exist. Creation/reinforcement lives in `common/scripted_effects/014_cannibalism_effects.txt:840-909`. |
| CBL 36-focus tree and Last Table | Implemented | `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md` records the 36-focus implementation as folded in; `common/national_focus/014_cannibalism_focus_tree.txt:646-663` gates `cbl_proclaim_the_last_table` behind map validation and sets `CBL_LAST_TABLE`. |
| CBL cleanup | Partial | `common/scripted_effects/014_cannibalism_effects.txt:664-721` cleans CBL flags, ideas, and missions. Prior handoff still records an edge case if creation is reached without a valid owned/controlled state and stale state-pressure cleanup if control changes before cleanup. |
| Super-event text/audio | Mostly implemented | Text/audio research handoffs exist; localisation keys `chaosx_super_event.141-144.*` exist in `localisation/english/014_cannibalism_l_english.yml:361-376`; images are mapped in `common/scripted_localisation/chaosx_scripted_localisation_super_events.txt:218-236`; sound effects for 141-144 exist in `sound/chaosx_sound.asset:2213-2239`. |
| Static assets | Partial/blocking | Final DDS files and sprite definitions exist in `interface/014_cannibalism.gfx`, but the asset package was produced by `docs/assets/014_cannibalism/generate_assets.py` and the handoff says "Generated deterministic fictional horror assets" rather than documenting imagegen/source-research provenance per the asset prompt. |
| Animated assets | Partial/blocking | `interface/014_cannibalism.gfx:104-130` defines three `frameAnimatedSpriteType` assets. The spec requested six animated pieces with real source frames, preview GIFs, manifest entries, and GUI handoff; no `.gif` preview or `docs/assets/014_cannibalism/manifest.md` was found, and the animated sprite names are only referenced in GFX/docs, not a GUI surface. |
| Achievements matrix | Partial | Thirteen achievements are registered in `common/achievements/chaos_redux_achievements.txt:1805-1947`, localised in `localisation/english/014_cannibalism_l_english.yml:389-428`, and sprite-registered in `interface/chaosx_achievements.gfx:1267-1305`. However every Event 014 achievement has `possible = always`, and several matrix disqualifiers are only implicit through whether a flag is set. |
| Event docs/log/evolutions | Implemented with caveats | `docs/events/014_cannibalism.md` documents the implemented system, and event/evolution detail localisation is present. It does not disclose all current simplifications, especially event-map role collapse and asset workflow deviations. |
| Spreadsheet/catalog | Implemented as current-implementation catalog | `docs/spreadsheets/chaos_redux_events_catalog.xlsx` row 15 directly contains Event ID 14, `Cannibalism`, the implementation summary, Evolutions I-III, world-end summary, `Minor Fire-Once`, and status `Implemented`. This reflects current docs, not no-simplification completion. |

## Blocking Missing Or Simplified Requirements

1. Event-map roles are not fully implemented.

Evidence: `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_5_event_map_acceptance.md:15-24` lists roles for `chaosx.nr14.3` first command investigation, `chaosx.nr14.4` public leak minor news, `chaosx.nr14.11` Evolution III global network reveal, and `chaosx.nr14.12` Hannibal connection reveal. `events/014_cannibalism.txt` has no `.3`, `.11`, or `.12`; `.4` is a spread-country event. `events/_chaosx_news.txt:145-154` defines `chaosx.news.17`, but `rg "chaosx.news.17"` found no call site outside the news definition, localisation, and old repo-explorer handoff.

2. Public leak/news gateway is defined but unwired.

Evidence: `localisation/english/014_cannibalism_l_english.yml:36-38` localises `chaosx.news.17`, and `interface/014_cannibalism.gfx:2` defines `GFX_news_cannibalism`, but no implementation effect/event calls `chaosx.news.17`. This leaves the spec's public leak/news role unfulfilled.

3. Decision and mission mechanics are concrete but mission geography is abstract.

Evidence: `docs/plans/014_cannibalism_plans/subagent_handoffs/2026-07-01_event014_decision_mission_audit_handoff.md` records the remaining gap: rail, prison, island, commune, and hospital missions do not persist target state/event-target geography. `common/scripted_triggers/014_cannibalism_triggers.txt:163-197` checks generic division count, supply-vehicle shortfall, any controlled state, or any coastal controlled state rather than named mission targets.

4. Outbreak-country AI remains per-decision, not a systemic response package.

Evidence: the same decision/mission audit records no dedicated outbreak-country AI strategy for production, trains, convoys, support equipment, or supply posture. `common/ai_strategy/014_cannibalism.txt` is CBL-oriented, while outbreak countries rely on `ai_will_do` blocks in `common/decisions/014_cannibalism_decisions.txt`.

5. Asset production does not meet the accepted Event 014 asset prompt.

Evidence: `docs/specs/014_cannibalism_specs/prompts/014_cannibalism_asset_prompt.md:16-18` requires generated fictional gore and period-authentic assets, and `:166-188` requires real animation source frames, sheet PNG/DDS, static fallback DDS, preview GIF, manifest entries, and per-entry metadata. The implemented package has `docs/assets/014_cannibalism/generate_assets.py`, whose code procedurally draws all sources and frames with PIL, and `docs/assets/014_cannibalism/gfx_handoff.md` only describes "Generated deterministic fictional horror assets." No `docs/assets/014_cannibalism/manifest.md` was found.

6. Animated asset scope is reduced and not visibly wired to a GUI.

Evidence: the spec asks for decision category seal, cult pressure warning, island signal card, Hannibal resonance seal, council portrait overlay, and world-end progress border. `interface/014_cannibalism.gfx:104-130` defines only three animated sprites: table pulse, warning larder, and signal map. `rg` found these names only in `interface/014_cannibalism.gfx`, `docs/events/014_cannibalism.md`, `docs/assets/014_cannibalism/gfx_handoff.md`, and the generator script, not in scripted GUI or other UI surfaces. `rg --files docs/assets/014_cannibalism ...` found PNG contacts/statics/sheets but no GIF previews.

7. Achievement eligibility/disqualification is simplified.

Evidence: `common/achievements/chaos_redux_achievements.txt:1805-1947` gives every Event 014 achievement `possible = { ... always = yes }`. Some matrix disqualifiers are represented indirectly by not setting flags, for example clean containment excludes spread/secrecy/exploitation in `common/scripted_effects/014_cannibalism_effects.txt:589-595`, but the matrix's disqualifier model is not consistently encoded as achievement eligibility.

8. CBL creation has an acknowledged edge-case risk.

Evidence: `common/scripted_triggers/014_cannibalism_triggers.txt:232-245` allows commune formation based on stage/cult/containment and source flags, but does not require a valid owned/controlled state before `common/scripted_effects/014_cannibalism_effects.txt:848-890` sets `cannibalism_commune_spawn_source` and tries `random_owned_controlled_state`. Prior country-package handoff records the same risk.

9. Cleanup can miss state pressure after control changes.

Evidence: `common/scripted_effects/014_cannibalism_effects.txt:643-662` cleans only currently controlled states for the resolving country. The prior decision/mission audit notes stale Event 014 state pressure can remain if contaminated states changed controller before cleanup.

## Accepted Plans And Disposition

| Plan or handoff | Disposition |
| --- | --- |
| `docs/plans/014_cannibalism_plans/cbl_focus_tree_depth_followup.md` | Marked implemented and largely reflected in CBL focus/decision/effect/AI files. No unresolved tree-depth addendum remains for the 36-focus CBL pass. |
| `2026-07-01_cbl_focus_tree_depth_pass_audit_handoff.md` | Reports no missing route from the depth follow-up, but records no in-game/parser/visual render validation and only local focus AI weighting rather than a separate ordered focus strategy plan. |
| `2026-07-01_event014_decision_mission_audit_handoff.md` | Applied cost/deadline/localisation fixes. Leaves abstract mission target geography, missing outbreak-country AI strategy, static cost localisation, no in-game validation, and state-pressure cleanup risk. |
| `2026-07-01_cbl_country_package_audit_handoff.md` | Applied creation/reinforcement fixes and documents CBL runtime creation. Leaves edge-case risk if a source country reaches creation without a valid owned/controlled state. |
| `2026-07-01_cbl_country_package_depth_audit_handoff.md` and `2026-07-01_cbl_depth_decision_mission_audit_handoff.md` | Depth and CBL mission fixes were incorporated into current CBL files, but the broader abstract targeting and validation caveats remain. |
| `014_cannibalism_super_event_text_handoff.md` | Text research was promoted into localisation for super-events 141-144. Its caution that the Hannibal package itself is a future dependency still applies; current Event 014 only gates hooks against `hannibal_exists` or accepted unifier flags. |
| `014_cannibalism_audio_handoff.md` | Audio files and sound effects are now wired for super-events 141-144. The handoff's CC BY-SA attribution note for the islands cue remains a documentation/licensing obligation. |
| `2026-07-01_event014_catalog_workbook_handoff.md` | Workbook row 15 is updated and was directly inspected during this audit. It reflects the current implementation summary, but should not be used as proof that spec deviations are resolved. |

## Meaningful Validation Performed

- Compared event-map IDs and roles in `docs/specs/014_cannibalism_specs/specs/014_cannibalism_spec_part_5_event_map_acceptance.md` against `events/014_cannibalism.txt` and repo-wide references.
- Searched for `chaosx.news.17` call sites; none were found outside definition/localisation/docs.
- Checked fire-once registration and valid-origin pool gating in `chaosx_logic_effects.txt`.
- Checked world-end trigger gates and launch effect for chaos threshold plus Hannibal/accepted unifier requirements.
- Checked CBL package registration, runtime creation, focus tree, AI strategy, Last Table cosmetic tag, and special-chaos-country registration.
- Checked super-event image/audio/scripted-localisation wiring for 141-144 and final audio/source files under `music/super_events/014_cannibalism/` and `sound/`.
- Checked achievement registration/localisation/sprites and searched where achievement flags are set.
- Inspected the xlsx row 15 XML directly enough to confirm the Event 014 catalog row content.

Validation not performed: no in-game run, no error-log validation, no parser run, no focus-tree visual render, no audio playback test, and no visual QA of the generated/procedural images beyond file/source inspection.

## Asset And Documentation Gaps

- `docs/assets/014_cannibalism/manifest.md` is missing even though the asset prompt requires it.
- Animated previews are contact/static PNGs only; no preview GIFs were found.
- Only three animated sprites are present, not the six requested animated pieces.
- Animated sprites appear defined but not consumed by a GUI/scripted GUI surface.
- Asset source files are procedural PIL outputs, not documented generated-art/source-research deliverables with source mode, uncertainty, and per-asset metadata.
- `docs/events/014_cannibalism.md` documents current implementation but does not clearly disclose event-role collapse, the unwired public news event, mission geography simplification, outbreak AI gap, asset workflow deviation, or unresolved cleanup risks.
- The workbook row says `Implemented`; this is true for the current implementation catalog but misleading if read as no-simplification completion.

## Remaining Blockers

- Missing event roles: `chaosx.nr14.3`, `chaosx.nr14.11`, `chaosx.nr14.12`.
- Public leak/news role: `chaosx.news.17` is defined but not called.
- Mission target geography: no target-state/event-target registry for rail, prison, island, hospital, commune, and global-network missions.
- Outbreak-country AI strategy: no systemic production/supply/transport AI package.
- Asset compliance: procedural generator package, missing required manifest, missing GIF previews, incomplete animated asset scope, and animated assets not visibly used in GUI.
- Achievement disqualifier depth: achievement `possible` blocks are all `always = yes`; matrix disqualifiers are not fully modeled as eligibility.
- CBL creation edge case and stale state-pressure cleanup risk remain documented but unresolved.

## Recommended Next Actions

1. Add or explicitly supersede the missing event-map roles. Either implement `chaosx.nr14.3`, `.11`, `.12` and a public leak/news call, or update the source spec with a reasoned role mapping that proves the roles are covered elsewhere.
2. Wire `chaosx.news.17` behind public fear/secrecy leak conditions, or remove the stale news surface and document the replacement.
3. Add target-state/event-target selection for the mission families that currently use abstract `any_controlled_state`, coastal access, or generic supplied-division gates.
4. Add an outbreak-country AI strategy pass for supply vehicles, support equipment, trains, convoys, and response decisions if AI countries are expected to fight their own outbreaks at spec depth.
5. Rework the asset package through `chaos-redux-event-assets` and `chaos-redux-frame-animation`: produce or source compliant final art, create `manifest.md`, add preview GIFs, finish the six requested animated pieces, and wire animations into a real UI surface or explicitly queue/reject that requirement.
6. Tighten achievement eligibility/disqualifiers or document which matrix disqualifiers are intentionally represented only by success-flag setting.
7. Add a CBL creation precheck for valid owned/controlled states before setting `cannibalism_commune_spawn_source`.
8. Add state-pressure cleanup coverage for controller changes or a target registry, if stale modifiers are not acceptable.

## Improvement Loop Recommendation

Use `chaosx_improvement_loop_planner` for a focused Event 014 addendum only if the parent does not want to patch the above directly. The useful planner scope would be: mission geography and UI/animation integration for named rail, prison, island, hospital, commune, and global-network targets. Do not spawn another broad CBL focus-tree planner now; the existing CBL depth addendum is marked implemented, and the remaining blockers are narrower implementation/spec-disposition gaps rather than a new focus-tree concept gap.

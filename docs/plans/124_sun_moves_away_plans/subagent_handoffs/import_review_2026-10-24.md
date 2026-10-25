# Import consistency review: Sun Moves Away 124

Date: 2026-10-24 import; reviewed 2026-10-25.

## Scope and authority

The user asked for one Chaos Redux event planning package to be imported, reviewed and made ready for use: Event 124 "Sun moves away", extracted from `124_sun_moves_away_planning_package.zip`.
The parent decided that package ID 124 is the canonical identity and that the catalog migration from former catalog ID 136 is the parent's work, outside this package.
This review edits documentation only.
It changes no gameplay, localisation, GFX, asset, workbook or CSV file.
Gameplay design acceptance is not granted here.
The package's expanded mechanics, numeric tuning, achievements, presentation and AI remain unresolved proposals, as recorded in the disposition table below.
The archive carries 22 members, not the 38 mentioned in the brief; every archive entry is accounted for below.

## Source-of-truth map and disposition

- **Identity:** `docs/specs/shared_identifier_registry.md` line 192 lists `124 | Sun moves away | 136`, and `docs/spreadsheets/chaos_redux_events_catalog.csv` now carries the row `124,Sun moves away`.
  The package states 124 as the catalog identity with former catalog ID 136, and Demilitarization at 114.
  Disposition: **implemented by the parent** for identity; the catalog row description is still wrong (see unresolved items).
- **Design:** the eight spec parts, the acceptance matrix and the README describe the event as an **unresolved proposal**, with the brief's required behaviours carried as requirements.
  Disposition: **unresolved**.
  The two central engine mechanisms, reversible whole-map daytime darkness and normal native night combat at every hour, remain **unproven** and keep explicit status in parts 1, 2 and 3.
- **Implementation:** none. The runtime event root `chaosx.nr124.1` does not exist. Disposition: **unresolved** until the parent accepts a queued implementation plan.
- **Prompts:** coding, goal, asset, achievement, super-event and decision/mission prompts are future aids governed by the specs.
  They require acceptance of the design before implementation; they are not instructions to execute during this review.
- **Usage maps:** the subagent and MCP usage maps guide future implementation.
  They are kept in the spec folder as active companions and now use canonical role names and current MCP tool names.
- **Historical evidence:** the source coverage ledger, the package manifest and the closed design review are historical.
  They sit in `docs/plans/124_sun_moves_away_plans/imported_review/` and remain unchanged, including the hashes and the 3,966-character goal count they record.

## Member disposition table

SHA-256 values are for the extracted originals, which match the archive entry sizes.
Destinations are relative to the mod root.

| Member | Bytes | SHA-256 (original) | Destination | What changed |
| --- | ---: | --- | --- | --- |
| 124_sun_moves_away_acceptance_matrix.md | 17557 | CA0F36986052093B83ACAAC4E6083F55C9E8827DA2515DA6E80DF5AFE978D515 | docs/specs/124_sun_moves_away_specs/ | CORE-01 identity row now states catalog identity 124 (former 136) and Demilitarization at 114. |
| 124_sun_moves_away_achievement_prompt.md | 4239 | 79922895B2847197B3A3786D50BCAB184890E0E93FC9910AB6F9AECF4DF5E72A | docs/specs/124_sun_moves_away_specs/ | Added the gptimage route with live-schema read and transparent request; alpha verification on saved PNGs. |
| 124_sun_moves_away_asset_prompt.md | 4445 | FD793ECDD2B4E2CB52B9D5286E0EFDAB4BD1D99AFDA3F55BA77103652045CA59 | docs/specs/124_sun_moves_away_specs/ | Replaced the unnamed "Project Source protocol" with current CLAUDE.md and the event-assets skill; named the gptimage route; added portrait and 3D routing and the RunPod boundary. |
| 124_sun_moves_away_coding_prompt.md | 7721 | 111CD49D53CF7A87D741B37A21BF98D10B75D2901FEAD66E019061D274BF454A | docs/specs/124_sun_moves_away_specs/ | Identity rewritten to 124 (former 136); design implementation gated on a recorded acceptance basis; CSV regeneration named as the export command; collisions reported, not chosen silently; current reads and inputs named. |
| 124_sun_moves_away_decision_mission_prompt.md | 5085 | C18E1E6C78C0D457DBAB5E17C66F0334CDA48FBFFFF4353B5E4FEE7FE686D8A2 | docs/specs/124_sun_moves_away_specs/ | Added the player-meaningful requirement tooltip rule and complete effect-description requirement. |
| 124_sun_moves_away_design_review.md | 6944 | BE59C2CA51AF6F138DF6D06B935AAD4E139FC1208C0B70C5A1C91664C778BE7E | docs/plans/124_sun_moves_away_plans/imported_review/ | Moved as historical evidence; content unchanged. |
| 124_sun_moves_away_goal_prompt.md | 3966 | FA24C1E3C205D9157C28B090070C1FB2F0536CB185D4A72BFDCF2EB9025966AE | docs/specs/124_sun_moves_away_specs/ | Identity rewritten; acceptance gate added; CLAUDE.md and moved review files named; length is now 4,085 characters and bytes (the README row is updated). |
| 124_sun_moves_away_mcp_usage_map.md | 8929 | DDA0004785E9E6875659462A53A777F1C760F40F7A4B534F91D8198326DAF2F5 | docs/specs/124_sun_moves_away_specs/ | Pinned GitHub links replaced by local links to docs/systems and docs/runtimes.md; pinned commit kept as a dated fact. |
| 124_sun_moves_away_research_and_sources.md | 18430 | E5939B28393AE96A1B5699EF2F3D2E0564232EA0884601B0A2363674A432E705 | docs/specs/124_sun_moves_away_specs/ | Source ledger link moved to the plans folder; identity paragraph and conflict-table row rewritten as the 124 identity decision with the historical 136 snapshot kept. |
| 124_sun_moves_away_source_coverage.csv | 58400 | 3621AE1C6B44161FC014902AC46A66C251B6EECC80699EC8C798FFD3FF1E4666 | docs/plans/124_sun_moves_away_plans/imported_review/ | Moved as historical evidence; content unchanged. 152 rows verified. |
| 124_sun_moves_away_spec_part_1_core.md | 19718 | 218D871C4A11003BD2BB9E09B3E36275EE6B6E4059F254BE47BAD062B29D406B | docs/specs/124_sun_moves_away_specs/ | Identity table and paragraph rewritten; status sentences added (unresolved proposal; two mechanisms unproven); "Intended design" header changed to "Proposed design"; namespace note added. |
| 124_sun_moves_away_spec_part_2_evolutions_and_return.md | 21787 | 15EBD925E9C8D8E83055AB7E74A9988FF13FD11F97A14972B608544142DDA9FA | docs/specs/124_sun_moves_away_specs/ | Status opener added: unresolved design proposal, proposed tuning, Return depends on the two unproven mechanisms. |
| 124_sun_moves_away_spec_part_3_incidents_and_countries.md | 17387 | 64E3B9BF5310D9AA3CA49990ACBED51BD8C5D19EF5CD1E09B0CEAE605B4AA83A | docs/specs/124_sun_moves_away_specs/ | One sentence added: the continental night-combat disposition depends on the unproven all-hour night-combat behaviour. |
| 124_sun_moves_away_spec_part_4_decisions_missions.md | 28555 | 080BCCCE1483095495A52D2F7222DF758B3C5AC9FEDDABB2465DFFCD99402DF0 | docs/specs/124_sun_moves_away_specs/ | Unchanged. Counts (20 actions, A01 to A20) verified; the A02 worked example recomputed. Items for the parent are listed below. |
| 124_sun_moves_away_spec_part_5_ai_balance.md | 16173 | F66AB5F9EA20EA30240548F75B2611FF0AB4F34BA27E5F33B75B24E8946AFBE3 | docs/specs/124_sun_moves_away_specs/ | Unchanged. Arithmetic recomputed (coverage, Lifeline Reliability, priority rows, opening totals, stage activation, Return table, Chaos ceiling); no errors found. |
| 124_sun_moves_away_spec_part_6_integrations_and_chaos.md | 21060 | 34FCC43C3F56789A60DD9E74C3568FBF7BDEF163F00E8C7597AE968FDD32EF83 | docs/specs/124_sun_moves_away_specs/ | Unchanged. Owner identifiers verified: `famine_request_event_pressure`, `migration_accept_famine_survivor_request`, the Heat Wave event and the humanitarian validation triggers. |
| 124_sun_moves_away_spec_part_7_presentation.md | 25395 | E8D58A90221B0382703259B659E61759FF5D3320E2D467EA2F560F28172F619C | docs/specs/124_sun_moves_away_specs/ | Registry link added for presentation and audio checks; SE124 prefix clarified as not claiming slot or audio 124; researcher names canonical; CSV export command named; UI and asset route ownership made proposal-level. |
| 124_sun_moves_away_spec_part_8_achievements.md | 19641 | 23E6BDDC278230D8996AD12ECC0ED8A2330FD328751D42FDDD9684FEEE5A514A | docs/specs/124_sun_moves_away_specs/ | Icon route routed to chaosx_icon_artist under chaos-redux-event-assets; filename convention tied to common/achievements/chaos_redux_achievements.txt and gfx/achievements. |
| 124_sun_moves_away_subagent_usage_map.md | 13310 | F1C9168E4C4D7373F2D4BD2C6719FA5B097850993584FE45F0C218D59AD67C4A | docs/specs/124_sun_moves_away_specs/ | Identity wording rewritten; D5 gate reworded; real or archival images route to chaosx_asset_source_researcher; portraits and 3D routes restated. |
| 124_sun_moves_away_super_event_prompt.md | 4234 | FA45F606B383B0076FF4E11665DF2042ED37B7C243F144A27633E44CDA64B62E | docs/specs/124_sun_moves_away_specs/ | Licence recording requirement; generated audio never presented as sourced; SE124 handles checked against registry reservations. |
| README.md | 8907 | 04A6977D84E58D120FC25345165EB6F3AE3FE7309597627F2CF806A24146F173 | docs/specs/124_sun_moves_away_specs/ | Links to moved files repointed; placement section rewritten to the installed state; identity sentence rewritten; goal count now 4,085; coding row wording aligned. |
| package_manifest.json | 4756 | 8047DB0979DFF94B6637E22D30AFA0A63C7F5BFF608B9108B4FFAE3DB661DDDB | docs/plans/124_sun_moves_away_plans/imported_review/ | Moved as historical evidence; content unchanged. Its recorded hashes and goal count describe the original planning pass, not the edited files. |

## Checks performed

- Archive listing: 22 entries, matching the 22 extracted files in size. No member was omitted.
- Relative Markdown links in both 124 folders: 78 checked, 0 broken.
- Hard-wrap heuristic over the spec folder: no mid-sentence wrap found.
- Forbidden-pattern scan over the spec folder: no `<=`, `>=`, whole-world `on_daily`, `on_weekly` or `on_monthly` script, co-author line, RunPod instruction, or unconditional live-test gate. Remaining "do not launch / wait for user live testing" statements are prohibitions or conditional.
- Identity scan: every remaining "136" is historical or states the migration.
- Subagent role names: all named `chaosx_*` roles exist in `.claude/agents/`.
- Acceptance matrix: 59 scenario rows (48 P0, 11 P1), matching the README.
- Source coverage ledger: 152 rows, 3,213,650 bytes, 260 aliases, matching the research record.
- Pinned commit 41bc4e5045a7b5c131be69dda2f08079d478634c exists in the repository.
- Goal prompt: trimmed by the parent to 3,984 characters (under the 4,000 limit).
- Repository identifiers checked by Grep in `common/`, `events/`, `docs/systems/`, `localisation/` and `gfx/`: `famine_request_event_pressure`, `migration_accept_famine_survivor_request`, `events/051_heat_wave.txt`, `common/achievements/chaos_redux_achievements.txt`, the super-event music and GUI names, and the achievement filename pattern.
- Not run: no HOI4 MCP check, script validation, game launch, live test, probability analysis or render. The package's own MCP and acceptance cases remain planned and unrun.

## Unresolved items for the parent

1. **Catalog row description.** `docs/spreadsheets/chaos_redux_events_catalog.csv` line 255 reads `124,Sun moves away,A research surge focuses each country on one field.`
   That text belongs to another concept, and the package's research record (`124_sun_moves_away_research_and_sources.md` line 38) already records it as incorrect.
   Fix the workbook row and rerun `python .tools/export_event_catalog_csv.py`. The description has not been changed here.
2. **Mission duration versus the mission rule.** Part 4 line 138 gives strategic projects 45 to 90 days.
   Mission-bearing cards A05 (45 days), A10, A17 and A20 (60 days) and A13 (30 days) are shorter than the 90-day easy-mission band in `.claude/skills/chaos-redux-decisions-missions/SKILL.md` section 9.
   A18 and the 15 to 30-day rescues may be justified emergencies. The design choice is the parent's: keep or retune. Nothing was changed.
3. **Tuning constants.** Part 4 line 9 calls the costs "authored tuning anchors," but no specification or prompt says the implementation must place them in `common/script_constants/` as `constant:category.key`.
   This is not a clear violation of the text as written. The coding and decision prompts should carry that direction when the parent accepts the design.
4. **Delegated Famine mission slot.** Part 4 line 132 allows a delegated Famine mission to occupy a slot, while line 144 omits A03 from the mission-bearing list. The parent should confirm whether A03 counts toward the three-mission limit.
5. **Achievement visibility and grant API.** Part 8 lines 10 to 20 say "visible after first Event 124 encounter," but the registry and `docs/systems/custom_achievements.md` have only `possible` and `happened` triggers and no hidden-visibility field. Part 8 lines 22 and 37 assume an achievement-mode predicate, registry allocator, persistent storage and grant API that were not verified. Part 8 line 220 requires the parent to review registry uniqueness, grant idempotence and persistent proof before these claims are relied on; they remain open.
6. **Heat Wave exclusion.** `events/051_heat_wave.txt` gives every country a two-year `heat_wave` idea and has no Sun guard. No current "active Heat Wave" scripted trigger was found. The two-way exclusion is design-required gameplay work and is not implemented.
7. **Remaining "accepted" wording.** Part 7 (lines 5, 122, 136, 142, 144, 153), part 8 line 7, the asset prompt line 3, the super-event prompt line 3 and the decision prompt ("Preserve the accepted action set") use "accepted" in the package's design sense.
   They do not claim implementation, but the parent should confirm that this wording is not read as acceptance under the disposition rules.
8. **Core engine mechanisms.** Reversible whole-map daytime darkness and normal native night combat at every hour remain unproven. They must not be marked implemented or validated until the owner review in the research record and MCP map is complete.
9. **Presentation and audio numbers.** The package proposes no presentation slot or audio ID. Slot 124 and audio ID 124 belong to Event 103 in the shared registry. Any future allocation must be checked against registry lines 117 to 127 and the audio ledger.
10. **Permanent documentation.** `docs/events/124_sun_moves_away.md` does not exist. It will be created at closure under catalog identity 124.

## Work for the parent outside this package

- Fix the catalog row description and re-export the CSVs (item 1).
- Add Sun Moves Away to `docs/specs/README.md` with the package link, and keep the registry entry at identity 124 with former ID 136.
- Decide items 2 to 5 and 7 before any implementation prompt is used.
- Allocate any presentation, audio or scenario identifier only after a registry check.

## Disposition and limitations

Import, instruction correction, moves to the plans folder, and the identity wording are complete in the documentation.
The gameplay design, achievements, presentation and AI remain unresolved proposals.
No design simplification was made, no archive member was omitted, and no runtime asset, localisation or workbook was changed.
No game launch, live test or MCP validation was run; source review and link checks support only the documentation claims above.

Skills and sources used: `chaos-redux-event-planning`, `chaos-redux-events`, `chaos-redux-subagents`, `chaos-redux-super-events`, `chaos-redux-decisions-missions`, `chaos-redux-event-assets` routing, and the 121 and 122 import records as format references.
No skill was created or changed.

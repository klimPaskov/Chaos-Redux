# Event 019 Localisation and Asset Independent Reaudit

Date: 2026-07-16  
Mode: independent read-only audit  
Scope: Event 019 English localisation, Event Log/history/evolution/details text, SCN-013 text, achievement text and icon triplets, fixed identity scenes, animation packages, manifests, contact sheets, runtime formats, and sprite consumers  
Gameplay edits: none

## Closure verdict

**Not closed for the audited localisation-and-asset scope.** No P0 finding was found, but two P1 findings and one P2 finding remain:

- Event 019's selected evolution panel actively resolves to the shared `GFX_portrait_unknown` fallback because its portrait selector has no Event 019 branch.
- Several visible achievement and controlled-trial strings expose implementation vocabulary instead of describing the world state and the player's military choices in-world.
- The fourth evolution body uses the game-design phrase "revolt paths."

The produced asset package itself is structurally and visually healthy. The fixed 27-scene identity package, three real frame-sheet animations, achievement triplets, report pictures, icons, GUI background, base flags, and regional flag matrix passed the checks described below. The scoped closure blockers are the active shared portrait consumer and player-facing wording, not missing or malformed art.

This report does **not** claim whole-event completion.

## Findings

### P0

None.

### P1-01 - Event 019 evolution details actively display an unknown-person portrait

Evidence:

- `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:7034-7165` defines `GetEventsLogSelectedEvolutionPortrait`.
- The complete selector contains no check for `constant:infantry_spawn_event.id` or `constant:infantry_spawn_event.evolution_type`.
- Its unconditional branch at `common/scripted_localisation/chaosx_scripted_localisation_events_log.txt:7161-7163` returns `GFX_portrait_unknown`.
- `common/scripted_guis/chaosx_scripted_gui_events_log.txt:1563-1564` actively binds `events_log_evolution_details_portrait` to `[GetEventsLogSelectedEvolutionPortrait]`.

Impact:

- Selecting any Event 019 evolution row in the Event Log displays generic unknown-person art.
- This violates the explicit ban on active generic human/unknown portrait references and bypasses the otherwise compliant Event 019 army/host scene package.
- `docs/assets/019_infantry_spawn/manifest.md` and `docs/assets/019_infantry_spawn/gfx_handoff.md` do not record this shared Event Log consumer, so their current wiring account is incomplete.

Required closure:

1. Add deliberate Event 019 stage branches to `GetEventsLogSelectedEvolutionPortrait` before the unconditional fallback.
2. Use approved 156 by 210 Event 019 army/muster or massed-host scene sprites; do not use a generic person or unknown portrait.
3. Record the Event Log portrait consumer in the asset manifest/GFX handoff.
4. Recheck all four selected evolution stages against the live selector.

### P1-02 - Achievement and controlled-trial UI exposes implementation language

Representative visible strings:

- `localisation/english/chaosx_achievements_l_english.yml:625` says "human-controlled country."
- `localisation/english/chaosx_achievements_l_english.yml:628` says "scenario menu."
- `localisation/english/019_infrantry_spawn_l_english.yml:433` says "exact generated unit" and "ledger proof."
- `localisation/english/019_infrantry_spawn_l_english.yml:434` calls it an "Event 19 formation."
- `localisation/english/019_infrantry_spawn_l_english.yml:439` again says "exact generated unit."
- `localisation/english/019_infrantry_spawn_l_english.yml:446` calls it an "Event 19 formation."
- `localisation/english/019_infrantry_spawn_l_english.yml:451` says "exact generated formation."
- `localisation/english/019_infrantry_spawn_l_english.yml:455` refers to an "Event 19 trial," "Event 19 management," and "ledger checks."
- `localisation/english/019_infrantry_spawn_l_english.yml:457` says "frozen identity."
- `localisation/english/019_infrantry_spawn_l_english.yml:458-459` says "No achievement proof is recorded."

Impact:

- The 11 achievement names and short descriptions are in-world, but parts of the eligibility, criteria, decision, mission, cancellation, and timeout copy are not.
- Terms such as event number, human control, menu, generated unit, frozen identity, and achievement proof expose implementation/verification concepts instead of the military record, formation identity, command decision, and trial result as the country experiences them.
- The wording therefore fails the repository rule and this audit's explicit requirement that achievement text remain in-world, even though the described mechanical gates appear aligned with the achievement implementation.

Required closure:

1. Rewrite the cited strings without changing their mechanical meaning or thresholds.
2. Prefer world-facing concepts such as the same recorded formation, muster rolls, sealed certification, command records, a deliberately invoked muster, and a trial being voided.
3. Recheck the entire Event 019 achievement/trial key family together so the criteria tooltips, decision tooltips, mission description, cancel text, and timeout text use one vocabulary.

### P2-01 - Evolution IV body uses branch-design wording

`localisation/english/019_infrantry_spawn_l_english.yml:185` ends with "revolt paths." The rest of the evolution and history copy describes an observed world state. "Paths" reads as route-design terminology in that context.

Required closure: replace it with an in-world consequence such as the risk of armed secession or the prospect of an independent host, while preserving the anomalous-host meaning.

## Passing localisation evidence

### Encoding and key coverage

The four English files carrying Event 019 or its shared UI/achievement surfaces all begin with the UTF-8 BOM:

- `localisation/english/019_infrantry_spawn_l_english.yml`
- `localisation/english/chaosx_achievements_l_english.yml`
- `localisation/english/chaosx_chaos_meter_l_english.yml`
- `localisation/english/chaosx_gui_l_english.yml`

A source-to-localisation scan across 60 Event 019-bearing source files found:

- 1,948 unique player-facing references;
- 2,926 Event 019-relevant English definitions across the four files;
- zero missing English keys;
- zero duplicate definitions among referenced keys;
- zero parser failures;
- zero referenced cosmetic-tag gaps across 13 base identities and 91 regional identities;
- no `:0` key versions or leading indentation on the relevant definitions.

The reference set included event titles/descriptions/options, scripted localisation results, decision/category names and descriptions, focus and idea names/descriptions, custom effect tooltips, GUI text/button/tooltip fields, country/cosmetic identity keys, leader names, scenario keys, Event Log keys, and achievement keys.

### Event Log, history, details, scenario, and achievements

- The only four Event 019 evolution title/body pairs are present and wired as `Organized Muster`, `Arsenal Lottery`, `Command Fracture`, and `Anomalous Muster`.
- Claimant appearance/takeover/failed-coup/revolt, anomalous family revolt/defeat, claimant defeat, scenario launch, and first-family reception outcomes are maintained as history payloads rather than additional evolution stages.
- Eighteen Event 019 history payload constants have matching title and description keys and matching history-title/history-detail selector branches.
- `chaosx.events_log.window.event_details.infantry_spawn` is an in-world premise summary and contains no fabricated date or achievement spoiler.
- SCN-013 is labelled `The Unbidden Muster`; all four type labels/descriptions, all four intensity impacts, confirmation/setup/failure reports, and institutional government names are present.
- All 11 Event 019 achievements have NAME/DESC pairs and criteria tooltips. Their thresholds and route conditions align with the achievement documentation; P1-02 concerns presentation vocabulary, not a missing key or evident rules mismatch.

## Passing identity-scene evidence

### Fixed 27-slot package

| Slot group | Source PNG | Processed PNG | Runtime DDS | Visual result |
| --- | ---: | ---: | ---: | --- |
| Human claimant identities | 20 | 20 | 20 | Twenty distinct massed army/muster scenes; no focal individual |
| Derivative identities | 6 | 6 | 6 | Six distinct fantastical massed hosts; no focal individual |
| Neutral/unassigned identity | 1 | 1 | 1 | Identity-neutral army/muster scene; no focal individual |

Structural results:

- All 27 source files exist, are RGB, and have 27 distinct SHA-256 hashes. Source sizes are 1080 by 1456, 1085 by 1450, 1086 by 1448, or 1086 by 1449.
- All 27 processed files exist, are RGB, are 156 by 210, and have 27 distinct SHA-256 hashes.
- All 27 runtime DDS files exist, decode as 156 by 210 RGBA, have 27 distinct SHA-256 hashes, and use the required legacy uncompressed 32-bit BGRA contract.
- Every processed PNG is decoded-pixel-identical to its paired DDS.
- Every declared source/processed/runtime path and SHA-256 in `notes/claimant_portrait_asset_crosswalk_2026_07_16.md` matches the current file.
- The eight identity review-sheet hashes declared in the crosswalk also match the current files. The synchronized legacy derivative sheet is byte-identical to the processed derivative review sheet as documented.

Visual review at source detail and processed size confirmed:

- all 20 claimant slots are army/muster identities rather than portraits of a commander;
- the zombie commander is a massed wall, and the zombie council shows exactly three separated masses;
- the ghost commander is a massed spearhead, and the ghost council shows exactly three separated formations;
- the golem master-builder is a collective host/worksite, and the golem council shows exactly three separated cohorts;
- the neutral slot is an anonymous radial muster with no individual identity;
- no Event 019 identity slot contains an individual focal human/person.

The comparison contact sheet contains five explicitly labelled vanilla leader portraits only as scale/style references. They are not Event 019 slots or runtime Event 019 assets.

### Gender and direct portrait references

- `common/scripted_effects/019_infantry_spawn_claimant_identity_effects.txt:196-207` creates every claimant commander with `female = no`; the later identity proof also requires `is_female = no` at line 311.
- The three named derivative commander effects set `female = no` at `common/scripted_effects/019_infantry_spawn_derivative_package_effects.txt:389`, `:398`, and `:407`.
- The zombie, ghost, and golem councils use institutional names, people-free massed-host scenes, and no gendered localisation or pronouns. They therefore read as councils rather than individual people.
- No Event 019 source directly references `GFX_portrait_communist_rebels`, `GFX_portrait_unknown`, or another generic human portrait. P1-01 is the shared Event Log selector that Event 019 currently reaches.

## Passing animation evidence

| Package | Source frames | Processed frames | Runtime frames/FPS | Sheet | Static fallback | GIF |
| --- | ---: | ---: | --- | --- | --- | --- |
| Muster Seal Pulse | 8 unique | 8 unique at 64 by 64 | 8 at 8 FPS | 512 by 64 | 64 by 64 | 8 frames, 120 ms each |
| Critical Command Border | 8 unique | 8 unique at 156 by 210 | 8 at 6 FPS | 1248 by 210 | 156 by 210 | 8 frames, 160 ms each |
| Anomalous Registry Emblem | 10 unique | 10 unique at 64 by 64 | 10 at 5 FPS | 640 by 64 | 64 by 64 | 10 frames, 200 ms each |

For all three packages:

- source-frame, keyed-frame, and processed-frame counts are complete;
- all source and processed frame hashes are distinct within the sequence;
- frame-plan hashes, atlas hashes, sheet hashes, static hashes, preview hashes, and contact-sheet hashes match current files;
- each horizontal sheet is exactly the ordered concatenation of its processed frames;
- each static fallback is exactly processed frame 000;
- runtime DDS pixels match the sheet/static PNG pixels;
- GIF frame counts and timing match the intended package speed;
- source atlases and processed contacts show substantive crack propagation, seam/hardware movement, and changing relief/light state rather than translation, scale, rotation, recolour, blur, or filter changes applied to one still image.

`interface/019_infantry_spawn.gfx` declares the exact 8/8/10 `frameAnimatedSpriteType` frame counts and 8/6/5 FPS rates plus three static siblings. `interface/019_infantry_spawn_muster_board.gui` consumes all six sprites, and the scripted GUI exposes mutually exclusive animated/static states through the animation preference plus the critical/anomalous state gates.

## Passing achievement-asset evidence

- Eleven retained achievement source PNGs exist, all are 1254 by 1254 RGB, and all have distinct SHA-256 hashes.
- Eleven completed, eleven grey, and eleven not-eligible processed PNGs exist. All 33 are 64 by 64 RGBA and all 33 hashes are distinct.
- Every grey icon is the exact grayscale derivative of its completed icon with alpha preserved.
- Every not-eligible icon is the exact completed icon composited with the canonical skill-provided not-eligible overlay; the overlay hash matches the documented source.
- All 33 runtime achievement DDS files are 64 by 64, use the correct legacy uncompressed BGRA contract, and decode pixel-identically to their PNG counterpart.
- All 11 registry IDs have matching completed/grey/not-eligible naming triplets and matching NAME/DESC localisation pairs.
- Completed and not-eligible contact sheets show 11 distinct, legible concepts with the expected state treatment.

## Passing broader asset-package evidence

The retained read-only Event 019 package validator completed successfully against the current workspace and reported:

- 11 distinct report-event images, each processed/runtime pair 210 by 176;
- 45 distinct focus icons at 100 by 88;
- 47 distinct decision icons at 33 by 32;
- 9 distinct idea icons at 64 by 64;
- 9 distinct category/UI icons at their declared 50 by 40 or 32 by 32 size;
- one 1120 by 760 muster-board background;
- 13 distinct base identity flag sets at normal, medium, and small size;
- three complete animation packages and 11 achievement triplets as detailed above.

An independent read of `regional_flag_validation_2026_07_16.json` and the files it declares found 273 current records for 91 regional tags across 82 by 52, 41 by 26, and 10 by 7 sizes. All recorded PNG and TGA hashes match, all PNG/TGA pairs decode pixel-identically, each size has 91 unique processed hashes, and all 273 lines in `regional_flag_checksums_2026_07_16.sha256` match the runtime records.

`interface/019_infantry_spawn.gfx` contains 203 uniquely named sprite declarations and 203 texture declarations pointing to 155 unique runtime files; every texture path exists. All concrete custom Event 019 gameplay/UI references for reports, identity scenes, focuses, decisions, ideas, and muster-board sprites resolve to declarations. Aliases intentionally share some texture paths.

The report, focus, decision, idea, UI, GUI, base-flag, regional-flag, identity-scene, achievement, and animation review sheets were inspected. They agree with the retained source/processed/runtime package; no stale Event 019 focal-person slot was found.

## Reference and tooling record

Consulted before and during the audit:

- `AGENTS.md`;
- the complete `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-frame-animation`, and `chaos-redux-subagents` skills;
- the complete Event 019 specification package, prompts, matrices, and current Event 019 docs/manifests/handoffs;
- the required offline wiki pages for data structures, triggers, effects, modifiers, localisation, scopes, on actions, events, decisions, ideas, AI, interface, scripted GUI, graphical assets, and characters;
- relevant installed vanilla documentation, including script concepts, localisation formatter/collection documentation, effects/triggers documentation, and vanilla animated-sprite precedents.

The HOI4 MCP event inspection could not return `chaosx.nr19.1` because the tool reported `ARTIFACT_STORAGE_LIMIT`; scripted-GUI inspection could not return the muster board because the tool reported `SCAN_BYTE_LIMIT`. Those tool-capacity failures are not content findings. The audit replaced them with direct source, selector, runtime-format, hash, pixel, and visual inspection.

## Files changed by this subagent

- `docs/plans/019_infantry_spawn_plans/subagent_handoffs/019_localisation_asset_independent_reaudit_2026_07_16.md`

No gameplay, localisation, interface, asset, manifest, workbook, or export file was changed.

## Simplifications, omissions, and blockers

- No audit requirement was intentionally simplified or omitted.
- The two MCP capacity limits are recorded above; they did not prevent a source-backed scoped verdict.
- No fallback was introduced or approved.
- Whole-event completion was not evaluated or claimed.

## Skills used

- `chaos-redux-events`
- `chaos-redux-event-assets`
- `chaos-redux-frame-animation`
- `chaos-redux-subagents`

No skill was created or updated.

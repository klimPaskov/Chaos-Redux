# Event 32 localisation and visual-wiring audit

Disposition: implemented and superseded by the parent asset/GFX wiring pass. The localisation findings remain current for the text surfaces; the statement that no GFX reference change was necessary applies only to this audit's 2026-09-01 snapshot. Current visual consumers and final asset wiring are authoritative in `docs/events/032_missiles/asset_audit.md`.

Date: 2026-09-01

Scope: Event 32 English localisation, scripted localisation, event and news text, Event Log and Event Details text, decisions, missions, achievements, ideas, state modifiers, opinion modifiers, texticons, guidance and retaliation-posture indicators, sprite aliases, runtime DDS files, encoding, and the current `docs/events/032_missiles/asset_audit.md`.

Applied repository skills: `chaos-redux-events`, `chaos-redux-event-assets`, `chaos-redux-decisions-missions`, and `chaos-redux-subagents`. Required offline wiki pages and relevant vanilla documentation, technology definitions, sprite registries, and decision precedents were consulted. No skill was created or updated.

## Outcome

The audit found and fixed six duplicate event-description keys, 44 missing decision and tooltip keys, eight missing blocked-cost variants, 16 missing idea and state-modifier keys, two missing opinion-modifier keys, one achievement eligibility namespace mismatch, 34 indented achievement keys, one static target label, one misleading retaliation summary, and widespread implementation-facing Event Details and evolution prose.

Post-patch static coverage is complete for the inspected Event 32 surfaces. All 50 event title, description, and option references resolve. All 240 expected decision, mission, tooltip, cost, and blocked-cost references resolve. All eight achievements have name, description, completion tooltip, and the shared eligibility tooltip. The three edited localisation files remain UTF-8 with BOM and have no duplicate keys.

No gameplay costs, triggers, effects, probabilities, variables, formatting tokens, or asset files were changed. No GFX reference change was necessary.

## Changed files

- `events/032_missile_crisis.txt`
- `common/scripted_localisation/032_missiles_localisation.txt`
- `localisation/english/032_missile_crisis_l_english.yml`
- `localisation/english/032_missiles_decisions_l_english.yml`
- `localisation/english/032_missiles_achievements_l_english.yml`
- `docs/plans/032_missiles_plans/subagent_handoffs/2026-09-01_event32_localisation_visual_wiring_audit.md`

`common/scripted_localisation/032_missiles_localisation.txt` was already an untracked working-tree file before this audit. The other Event 32 source files also contained pre-existing edits. This patch changed only the identifiers and player-facing text listed below.

## Missing-key audit and fixes

### Parent-listed missing keys

All 20 parent-listed missing keys were added:

- `missiles_accelerate_recovery_effect_tt`
- `missiles_allow_rogue_launch_effect_tt`
- `missiles_cost_accelerate_recovery`
- `missiles_cost_deny_responsibility`
- `missiles_cost_emergency_recalibration`
- `missiles_cost_guard_captured_site`
- `missiles_cost_integrate_captured_site`
- `missiles_cost_investigate_debris`
- `missiles_cost_scuttle_captured_site`
- `missiles_cost_study_captured_site`
- `missiles_deny_responsibility_effect_tt`
- `missiles_emergency_recalibration_effect_tt`
- `missiles_guard_captured_site_effect_tt`
- `missiles_integrate_captured_site_effect_tt`
- `missiles_investigate_debris_effect_tt`
- `missiles_scuttle_captured_site_effect_tt`
- `missiles_select_payload_effect_tt`
- `missiles_set_payload_policy_effect_tt`
- `missiles_set_posture_effect_tt`
- `missiles_study_captured_site_effect_tt`

### Additional missing decision titles and descriptions

Static comparison against all 43 decision definitions found 24 additional missing keys. They were added as title and description pairs for:

- `missiles_guard_captured_site`
- `missiles_study_captured_site`
- `missiles_integrate_captured_site`
- `missiles_scuttle_captured_site`
- `missiles_select_special_payload`
- `missiles_set_special_payload_policy`
- `missiles_set_retaliation_posture`
- `missiles_accelerate_incident_recovery`
- `missiles_deny_incident_responsibility`
- `missiles_emergency_guidance_recalibration`
- `missiles_investigate_debris`
- `missiles_allow_rogue_launch`

The eight newly added custom-cost keys also received the engine-facing `_blocked` variants with identical values and red formatting:

- `missiles_cost_guard_captured_site_blocked`
- `missiles_cost_study_captured_site_blocked`
- `missiles_cost_integrate_captured_site_blocked`
- `missiles_cost_scuttle_captured_site_blocked`
- `missiles_cost_accelerate_recovery_blocked`
- `missiles_cost_deny_responsibility_blocked`
- `missiles_cost_emergency_recalibration_blocked`
- `missiles_cost_investigate_debris_blocked`

### Additional visible modifier and opinion keys

The following visible source identifiers had no English localisation and now have names and descriptions where the consumer supports them:

- `missiles_program_experimental`
- `missiles_program_operational`
- `missiles_program_compromised`
- `missiles_launch_site_active`
- `missiles_launch_site_hardened`
- `missiles_launch_site_damaged`
- `missiles_launch_site_compromised`
- `missiles_launch_site_rogue`
- `missiles_neutral_accident_compensation`
- `missiles_neutral_accident_denial`

### Achievement namespace mismatch

`common/achievements/chaos_redux_achievements.txt` requests `chaos_redux_032_achievement_eligible_tooltip`, while the localisation file defined `chaosx_032_achievement_eligible_tooltip`. The localisation key was renamed to the requested `chaos_redux_032_achievement_eligible_tooltip`. The eight achievement eligibility consumers now resolve.

Post-patch missing-key list for the inspected scope: none.

## Duplicate-key audit and fixes

Before the patch, six event descriptions reused the same key as option D, causing the later option text to overwrite the event description:

- `chaosx.nr32.30.d`
- `chaosx.nr32.31.d`
- `chaosx.nr32.32.d`
- `chaosx.nr32.40.d`
- `chaosx.nr32.60.d`
- `chaosx.nr32.80.d`

Each event description now uses a distinct `.desc` key in both `events/032_missile_crisis.txt` and `localisation/english/032_missile_crisis_l_english.yml`. The `.d` keys remain the fourth option labels.

Post-patch duplicate-key list in the three Event 32 localisation files: none.

## Scripted-localisation audit

### Fixed issues

- `GetMissilesCategoryTargetName` previously returned the static phrase `Selected country` whenever `missiles_selected_target` existed. It now requires `missiles_selected_target_is_valid = yes` and resolves `missiles_category_target_selected` as `[?missiles_selected_target.GetName]`.
- `GetMissilesCategoryRetaliationLine` previously displayed only `Armed` or `Inactive` based on whether the automatic-retaliation evolution existed. It now displays the actual `Off`, `Supervised`, `Delegated`, or `Automatic` posture, including the corresponding posture icon.
- No direct `§` or `£` formatting character was added to scripted-localisation source.

### Remaining dynamic-text opportunities

- Event 32 cost strings still repeat file-scoped `@m32_*` values as static localisation numbers. They currently match the source values, but a later gameplay-owner change could drift. Converting those tuning values to shared script constants or synchronised display variables would remove that risk. This audit did not change tuning ownership.
- Several state-targeted decision descriptions could name `[FROM.GetName]`. Their existing generic wording is mechanically correct, and changing every target scope without a production decision-view render would add avoidable uncertainty.
- The Event Log history row already uses the dynamic processed-programme count. No actor is stored for the global row, so no country name was invented.

The ordinary category currently exposes nine live fields: reserve, readiness, command control, technology, site count, guidance, target, retaliation posture, and crisis. The accepted Event 32 specification requests these fields, but the decisions/missions presentation guidance normally permits one primary value, two supporting values, and four visible values as a hard ceiling. Resolving that contradiction requires an owner-level presentation choice about which fields remain in the header and which move to concise tooltips or decision states. The minimal localisation patch shortened the surrounding prose but did not hide specification-required information.

Post-patch scripted-localisation issue list: no unresolved broken reference found in the inspected Event 32 file.

## Prose-quality changes

### Vagueness

- The Missile Command category opening now identifies launch sites, operational weapons, crews, and codes instead of describing a “reserve of symbols on a ledger.”
- The scenario descriptions now state which countries receive programmes, sites, reserves, warheads, or warning networks.
- The missing decision descriptions now state the concrete action and object for captured sites, debris, guidance recalibration, incident recovery, payload policy, and rogue launch authority.

### Bloat

- Event descriptions for `.30`, `.31`, `.32`, `.40`, `.60`, and `.80` were shortened and moved the actionable choice to the front.
- The Event Details passage now explains the premise and visible systems without listing internal adapters, ledgers, queue bounds, or implementation safeguards.

### Obvious explanation

- `missiles_survey_effect_tt` now states the state-control and suitability condition instead of saying only that the selected state must remain valid.
- `missiles_accept_retaliation_effect_tt` now describes accepting the order and beginning preparation instead of explaining that the code avoids recursion.

### Repetition

- The five evolution bodies and summary no longer repeat that the system is bounded, registered, or unable to create payloads.
- Scenario intensity text retains the required immediate-launch warning but removes repeated internal profile terminology.

### Overcomplication

- Long noun stacks such as “physical site ledger, normalized technology, operational reserve” were replaced with direct descriptions of programmes, launch sites, missiles, guidance, crews, and codes.
- The saturation mission description was split into two sentences and its semicolon removed.

### Style-rule repair

- Removed the em dash from `missiles.event_log.history.row`.
- Removed sentence semicolons and implementation-facing terms such as `bounded`, `normalized`, `recursive launch path`, `incident root`, `generation bounds`, and `disabled-safe behavior` from the edited player-facing text.
- Removed leading indentation from all 34 achievement localisation keys.
- Rewrote the `No Second Sun` locked line to remove fake-profound wording.
- Clarified that `Long Reach` requires fighting a major power, not merely existing while a major is at war.
- Split the `Break the Chain` requirement so “no retaliatory launch or special payload” cannot be read as an either-or condition.

## Cross-surface consistency

- The event description keys now match their event consumers and no longer collide with option D.
- The decision category target line now agrees with the persisted variable-scope target used by operation missions and triggers.
- The retaliation line now agrees with `GetMissilesRetaliationPostureName` and the four posture icons instead of showing an evolution-level armed state.
- The eight achievement script IDs, localisation IDs, and completed/grey/not-eligible sprite aliases agree.
- The accepted specification excludes a dedicated scripted GUI, super-event, 3D model, and animation package. No such surface was found or invented.
- Working achievement display names omit some articles used in early specification labels. The IDs, mechanics, descriptions, and icon aliases are internally consistent, so this was treated as accepted final wording rather than a runtime mismatch.

Unresolved wording decision: the repository uses both British `programme` and American `program` across Event 32. Existing event and decision prose was not globally normalised because both forms predated this audit and changing clear text solely for house voice would exceed the bounded patch.

## Encoding validation

- `localisation/english/032_missile_crisis_l_english.yml`: UTF-8 BOM present after patch.
- `localisation/english/032_missiles_decisions_l_english.yml`: UTF-8 BOM present after patch.
- `localisation/english/032_missiles_achievements_l_english.yml`: UTF-8 BOM present after patch.
- No `:0` version suffix was introduced.
- No localisation key in the achievement file retains leading indentation.

File-encoding concerns after patch: none in the three Event 32 English files.

## Visual and sprite-wiring audit

### Runtime aliases and files

Source inspection found 82 Event 32 runtime aliases and 82 corresponding DDS files:

- 1 at 114x101
- 1 at 210x176
- 3 at 24x24
- 14 at 32x32
- 34 at 33x32
- 1 at 397x153
- 1 at 52x40
- 3 at 60x68
- 24 at 64x64

All 82 paths exist, begin with a valid DDS header, and report the expected dimensions. No duplicate Event 32 sprite alias was found.

The 59 directly referenced aliases in events, decisions, missions, category, ideas, state modifiers, and localisation all resolve to registered runtime textures. `GFX_train_texticon` is the only reference not defined by the mod registries; it is a vanilla texticon and is not an Event 32 missing alias.

Specific family checks:

- Three texticons resolve exactly: operational reserve, launch readiness, and command control.
- Five guidance icons resolve exactly: poor, uncertain, serviceable, accurate, and precise.
- Four retaliation-posture icons resolve exactly: off, supervised, delegated, and automatic.
- Twenty-seven ordinary decision icons and seven mission icon files are registered. Shared use of the strike-preparation mission icon is intentional.
- Three programme ideas and five launch-site state modifiers point to Event 32 aliases.
- Eight achievements each have completed, grey, and not-eligible aliases and files.
- Event report, news, category picture, and category button aliases resolve from their intended shared or Event 32 registries.

The following contact sheets were opened at original resolution:

- `docs/assets/032_missiles/contact_sheets/032_missiles_contact_sheet.png`
- `docs/assets/032_missiles/contact_sheets/runtime_final/runtime_status.png`
- `docs/assets/032_missiles/contact_sheets/runtime_final/runtime_decisions.png`
- `docs/assets/032_missiles/contact_sheets/runtime_final/runtime_missions.png`
- `docs/assets/032_missiles/contact_sheets/runtime_final/runtime_achievements.png`

No obvious subject crop, transparent-edge defect, or family mismatch was visible in those review artifacts. These contact sheets are asset review evidence, not a production decision-window render.

### Current `asset_audit.md`

The 58 non-achievement table rows in `docs/events/032_missiles/asset_audit.md` still match the current runtime files by SHA-256. No listed path is missing and no listed hash changed.

The document says that all 82 files were audited, but its itemised table contains only the 58 non-achievement assets. The 24 achievement DDS files are asserted in prose and appear in the contact sheet, but they do not have per-file paths, dimensions, and hashes in the table. The final runtime-directory bullet also says `gfx/achievements/032_missiles_*.dds`, while the actual files are `gfx/achievements/chaos_redux_032_*.dds`. This is a documentation-evidence gap, not a runtime wiring defect. It was not edited because the parent authorised only minimal localisation and GFX-reference fixes.

The audit also records the missile-delivery raid icon as blocked because no exact Event 32 consumer exists in the native raid namespace. Source inspection found no unresolved Event 32 sprite reference for such an icon, so no fallback alias should be added.

### Overflow and production-render limits

Event 32 uses the vanilla decision UI and introduces no dedicated `.gui` layout. There is therefore no Event 32 scripted-GUI source for the HOI4 GUI inspector or renderer. The installed tool package exposes no ordinary vanilla decision-category production render accepting this category as a target. Texticon, guidance, and posture overflow in the final vanilla decision view could not be proved by a one-to-one production render. The status assets are at their intended native dimensions and the category description was shortened, but live consumer proof remains with the user.

The separate Technology Tree Viewer is absent from the installed package, as expected by the localisation-agent contract.

## MCP evidence and exact blockers

### Successful pre-patch event evidence

`hoi4.event_inspect` returned `EVENT_INSPECTED_PARTIAL` with status `ok` for namespace `chaosx.nr32` before the localisation patch. Useful artifact:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/6b86346891498f8bb22c51c278645ab32bf471e0585b4a961db68a4039125670/bd9c26c9d136702d19e1fb880badb41ba7dfc1234f6e079e8b24287349c99f4c/event-lint-3d4d1503eea1.json`

`hoi4.event_render` returned `EVENT_RENDERED_PARTIAL` with status `ok` for the `chaosx.nr32.30` options view. Useful artifacts:

- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/56c85c16ab7c64fb2c47431302ea629a228cde7e0aac45d70793a1f8f07a9f19/95b74666cfa6ccf2fd151f500dc607fffc86ef6f78f96f64bb5ece6b2c02d4e3/event-options-3d4d1503eea1-manifest.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/c2edc69823dc4a2abd34fa9e33ab06ef87edf401a940a6e9f5a606cefe7a2ad9/07a45447a8e6dbf817d85aff11e43e57dbc05442e11d93de825c4ca178be77c7/event-options-3d4d1503eea1.json`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/0905c9cfc1d77706182fa6359fe95973db795b205d7afc064db46c5800354c6e/3913ede3806e8618d603f4d4e8a058a1c25872069ef6e9a1331dd085dd912934/event-options-3d4d1503eea1.svg`
- `hoi4-agent://workspace/mod_chaos_redux_ea3b2d67c2c0/artifact/af26b8ec48ed8f6198a5da5167549da9d8d239904c12b9ef8474852a452a368f/be9b72f3d9fba26c40313102c34a4cb06c2e50cd923d856e5c024783e3a6e315/event-options-3d4d1503eea1.png`

The render retained the Event 32 payload event and its five options. It was generated before the `.desc` key correction, so it is not post-patch proof.

### Post-patch event blocker

A post-patch `hoi4.event_inspect` lint refresh for namespace `chaosx.nr32` did not return after approximately 93 seconds and was terminated. No post-patch event artifact or diagnostic was produced. Static source validation therefore cannot be represented as equivalent MCP evidence.

### Technology asset blockers

- `hoi4.tech_inspect`, mode `trace`, technology `experimental_rockets`, descendants, refresh enabled, did not return after approximately 155 seconds and was terminated. No artifact or diagnostic was produced.
- `hoi4.tech_render`, view `assets`, technology `experimental_rockets`, refresh disabled, did not return after approximately 62 seconds and was terminated. No artifact or diagnostic was produced.

Offline source inspection confirms that `experimental_rockets`, `rocket_engines`, `improved_rocket_engines`, and `advanced_rocket_engines` exist in vanilla `common/technologies/electronic_mechanical_engineering.txt`. Their `_medium` aliases and four 64x64 DDS textures exist in vanilla `interface/Technologies.gfx` and `gfx/interface/technologies/`. This source evidence does not replace the unavailable MCP technology graph and asset render.

## Meaningful validation

- Compared all 43 Event 32 decision IDs and 10 mission IDs with English title and description keys.
- Compared every referenced custom effect tooltip, trigger tooltip, custom cost key, and custom blocked-cost key with the combined English localisation key set. Result: 240 expected keys, zero missing.
- Compared all Event 32 event title, description, and option references. Result: 50 references, zero missing.
- Compared the eight achievement IDs with name, description, completion-tooltip, and shared eligibility keys. Result: zero missing.
- Re-ran duplicate-key and BOM checks on the three edited Event 32 localisation files. Result: zero duplicates and BOM present in all three.
- Verified 82 Event 32 DDS aliases, paths, headers, and dimensions. Result: zero missing or malformed files.
- Compared the 58 itemised `asset_audit.md` hashes with current runtime files. Result: zero missing and zero hash mismatches.
- Opened the main, status, decision, mission, and achievement contact sheets at original resolution.
- Confirmed vanilla source and sprite registrations for the four technology IDs used by Event 32.

Skipped meaningful validation:

- HOI4 was not launched, as required.
- No live decision-category or event-window render was available.
- Post-patch event MCP refresh and both technology MCP calls timed out as documented above.
- No Technology Tree Viewer exists in the installed package.

## Sourced quotations and preserved tokens

No sourced or attributed quotation appears on the inspected Event 32 player-facing surfaces. No quotation was altered.

All existing dynamic value tokens, colour codes, texticon tokens, country/state scope tokens, and gameplay numbers outside the newly supplied missing cost strings were preserved. The new missing cost strings reproduce the current `@m32_*` source values exactly. The target label intentionally changed from static prose to `[?missiles_selected_target.GetName]`.

## Recommended parent follow-up

1. Re-run post-patch `hoi4.event_inspect` and `hoi4.event_render` when the server responds, focusing on `chaosx.nr32.30` and the full namespace.
2. Re-run `hoi4.tech_inspect` and `hoi4.tech_render` for `experimental_rockets` and its descendants. Do not mark the technology graph or asset route as MCP-verified until those calls return.
3. Extend `docs/events/032_missiles/asset_audit.md` with the 24 achievement rows and correct its final achievement glob to `gfx/achievements/chaos_redux_032_*.dds`.
4. Confirm text wrapping and icon placement in the ordinary Missile Command decision category during the user's normal live validation.
5. If cost tuning is moved out of file-scoped `@m32_*` constants, update or replace the static cost localisation in the same change.
6. Reconcile the category's nine live fields with the decision presentation value budget before calling the category visually final.

No new mechanic gap was identified, so no separate improvement-loop plan handoff was written.

## Simplifications, omissions, and blockers

- No visual asset, GFX alias, gameplay effect, or tuning value was changed.
- The production decision-view overflow check remains blocked by the absence of a supported one-to-one ordinary decision-category render route.
- Post-patch event MCP and technology MCP evidence remains blocked by the exact timeouts above.
- `asset_audit.md` was audited but not edited because the parent limited patches to localisation and GFX-reference fixes.
- No Git commit was created. The repository contained broad pre-existing staged, modified, and untracked work, including Event 32 files, so an isolated truthful commit could not be guaranteed without capturing unrelated ownership.

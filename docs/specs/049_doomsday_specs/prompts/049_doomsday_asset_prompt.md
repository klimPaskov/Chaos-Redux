# Event 049 Doomsday Asset Production Prompt

## Role

Create the complete final visual asset package for Event 049, **Doomsday**, using `chaos-redux-event-assets` and the narrow asset subagents defined by `chaos-redux-subagents`.

Read the full specification under `docs/specs/049_doomsday_specs/`, with special attention to:

- `specs/049_doomsday_spec_part_3_societies_and_responses.md`
- `specs/049_doomsday_spec_part_7_focus_content.md`
- `specs/049_doomsday_spec_part_8_final_vigil.md`
- `specs/049_doomsday_spec_part_11_presentation_and_assets.md`
- `specs/049_doomsday_spec_part_12_achievements_and_acceptance.md`
- `prompts/049_doomsday_super_event_prompt.md`
- `prompts/049_doomsday_achievement_prompt.md`

Follow `AGENTS.md`, `chaos-redux-event-assets`, `chaos-redux-frame-animation` only when animation is explicitly authorized, `chaos-redux-super-events`, and `chaos-redux-subagents`. Character portraits follow the `chaos-redux-event-assets` portrait-production reference.

## Boundaries

- Produce static final assets for the accepted package.
- Do not create a full scripted GUI.
- Do not create a 3D model, unit, vehicle, building, creature, aircraft, ship, or skeletal animation package.
- Do not create a national flag set for every Doomsday administration.
- Do not invent a real person for a grounded country.
- Do not use primitive local drawings, copied icons, resized cross-family icons, placeholders, or opaque square backgrounds where alpha is required.
- Do not create final super-event quotes, button text, or audio. Coordinate with the super-event research handoff.
- Do not edit gameplay, localisation, event, decision, focus, GUI, scripted effect, scripted trigger, country, or spreadsheet files unless the parent explicitly expands scope.

## Required reference inspection

Before production, inspect the matching canonical reference folder and its `contact_sheet.png` under the event-assets skill.

At minimum inspect:

- `assets/vanilla_reference/event_art/report/`
- `assets/vanilla_reference/event_art/news/`
- `assets/vanilla_reference/event_art/super_event/`
- `assets/vanilla_reference/icons/decisions/`
- `assets/vanilla_reference/icons/decision_categories/`
- `assets/vanilla_reference/icons/decision_categories/pictures/`
- `assets/vanilla_reference/icons/ideas/`
- `assets/vanilla_reference/icons/national_focus/`
- `assets/vanilla_reference/icons/achievements/`
- `assets/vanilla_reference/portraits/leaders/` for any leader-sized institutional portrait consumer

If a required contact sheet is missing, build and document it before production according to the skill. Reference assets remain review material and cannot be traced, recolored, or shipped.

## Visual direction

The visual identity is a 1936 to 1945 world reorganizing daily life around an expected ending.

Strong subjects include:

- Mass public gatherings.
- Calendars and public schedules with unreadable print.
- Pacifist marches.
- Abandoned schools, universities, shipyards, and long projects.
- Communal kitchens and shelters.
- Trains, ports, and family movement.
- Prisoner release and suppression raids.
- Soldiers refusing offensive deployment.
- Civic, religious, municipal, and relief councils.
- Archives, seed, medicine, and public records.
- Ordinary dawn after the date fails.

Avoid:

- One scientist or prophet as the sole cause.
- Modern digital displays, modern tactical equipment, or modern clothing.
- Readable generated text.
- Cinematic science-fiction treatment.
- An exploding planet or confirmed supernatural cause.
- Generic maps as the main visual.
- Caricature, mockery, gore, or religious stereotype.

Generated event scenes should resemble period documentary photography or period news imagery. Keep composition clear at the final crop.

## Event art inventory

### Report images

Create final report-event art for these working basenames:

1. `doomsday_university_exodus`
2. `doomsday_shipyard_abandonment`
3. `doomsday_pacifist_march`
4. `doomsday_communal_kitchen`
5. `doomsday_survival_settlement`
6. `doomsday_suppression_raid`
7. `doomsday_shelter_construction`
8. `doomsday_soldiers_refuse`
9. `doomsday_final_vigil_local`
10. `doomsday_failed_date_dawn`
11. `doomsday_archives_preserved`
12. `doomsday_schools_reopen`

Use the inspected report consumer, normally `210x176`. Each image needs its own source, crop, processed PNG, DDS, manifest row, and contact-sheet entry.

### News images

Create final black-and-white news art for:

1. `doomsday_last_calendar_news`
2. `doomsday_parallel_governments_news`
3. `doomsday_final_assembly_news`
4. `doomsday_last_day_passes_news`

Use the inspected news consumer, normally `397x153`.

### Super-event images

Create or coordinate final image production for:

1. `doomsday_opening_super_event`
2. `doomsday_final_vigil_super_event`

Use the inspected super-event consumer, normally `457x328`.

Opening image role:

Show public convergence through a large gathering, public calendars, prayer or civic assembly, altered schedules, and social diversity. Do not confirm a cause.

Final Vigil image role:

Show a large public assembly, relief distribution, surrendered or stored weapons, extinguished military activity, shelters, and a common vigil. Do not depict physical planetary destruction.

## Decision-category picture family

Create five static stage variants. Do not paint buttons, values, meters, or fake controls into the art.

Working basenames:

1. `doomsday_category_convergence`
2. `doomsday_category_societies`
3. `doomsday_category_last_calendar`
4. `doomsday_category_parallel_government`
5. `doomsday_category_failed_date`

Use the exact inspected decision-category picture consumer. The current reference family is commonly `114x101`, but the live sprite and GUI consumer decide the final size.

The variants should retain one coherent visual language while showing distinct state. They do not need to be the same scene or a transformed single image.

No animation is required. Do not manufacture animation by shifting, scaling, recoloring, glowing, or filtering one still.

## Decision-category icon

Create one dedicated category icon:

- `doomsday_category_icon`

It should combine a calendar, horizon, gathered public, or watch motif without readable text. Design it for the actual category-button consumer, not by shrinking a focus icon.

## Decision icon family

Create distinct decision icons for these working basenames:

1. `doomsday_civic_continuity`
2. `doomsday_concordat`
3. `doomsday_emergency_order`
4. `doomsday_national_preparation`
5. `doomsday_peace_negotiations`
6. `doomsday_final_offensive`
7. `doomsday_keep_schools_open`
8. `doomsday_technical_institutes`
9. `doomsday_rail_food_network`
10. `doomsday_muster_rolls`
11. `doomsday_archives`
12. `doomsday_hospitals`
13. `doomsday_shelters`
14. `doomsday_reserves`
15. `doomsday_debt_settlement`
16. `doomsday_prisoner_release`
17. `doomsday_open_borders`
18. `doomsday_society_representation`
19. `doomsday_authority_transfer`
20. `doomsday_final_assembly_petition`
21. `doomsday_reconstruction`
22. `doomsday_investigate_suppression`

Design each for the inspected decision icon consumer, normally `32x32`. Use strong silhouettes and limited interior detail.

## Idea and national-spirit icon family

Create separate idea art for the staged ideas that remain after implementation review.

Initial working basenames:

1. `doomsday_global_conviction`
2. `doomsday_administration`
3. `doomsday_hollowed_institutions`
4. `doomsday_last_muster`
5. `doomsday_common_relief_network`
6. `doomsday_suppression_reckoning`
7. `doomsday_preserved_continuity`
8. `doomsday_scattered_arms`
9. `doomsday_last_days_debt`
10. `doomsday_shelters_remain`
11. `doomsday_calendar_skepticism`
12. `doomsday_permanent_millenarian_minority`

The implementation agent may merge or rename staged ideas. Lock the final stable list with the parent before final production. Do not create unused assets for ideas that were removed.

Design idea icons for the inspected `64x64` idea consumer. Do not resize focus art.

## Focus icon family

Create one coordinated focus icon family after the focus implementation locks final focus IDs and roles.

The family must cover every implemented focus in the 18 to 24 focus emergency branch, including these route concepts:

- Government transfer and custodial mandate.
- National inventory.
- Peace and demobilization.
- Defensive-only service.
- Prisoner and objector policy.
- Food and reserves.
- Shelters.
- Archives.
- Railways and ports.
- Hospitals and relief.
- Public observance.
- Reconciliation.
- Communal devolution.
- Custodial administration.
- Final Assembly delegation and membership.
- Hidden Avenging Witnesses content where valid.

Every focus icon requires an asset-specific source and prompt. Shared symbols and palette are allowed. Resizing one icon to fill several focuses is not allowed.

Use the inspected focus consumer, normally `94x86`.

## Final Assembly emblem

Create one flat emblem:

- `doomsday_final_assembly_emblem`

The emblem should communicate watchfulness, gathered humanity, peace, shelter, and a shared horizon. Avoid readable text and direct use of one religion’s sacred symbol as the universal identity.

Create transparent PNG and DDS variants for the actual consumers, with preserved native alpha.

## Institutional council portraits

Route all portrait production to `chaosx_portrait_creator`.

Create five fictional people-free or clearly collective institutional portrait packages only if the implementation needs them:

1. `doomsday_civic_relief_council`
2. `doomsday_religious_civic_synod`
3. `doomsday_communal_delegates_council`
4. `doomsday_defensive_service_committee`
5. `doomsday_revolutionary_witness_assembly`

These are institutional identities. They must not present one invented person as a grounded national leader.

Use full HOI4 leader framing if the consumer is a country leader portrait. Confirm the exact consumer, basename, role, and dimensions before production.

If any country route selects a named grounded individual, stop and use attributed source research and the source-placeholder or user-supplied styled-final workflow. Never generate that person’s identity.

## Achievement icon family

Create completed icons and all required achievement state variants for:

1. `049_doomsday_a_future_worth_planning`
2. `049_doomsday_the_last_recruit`
3. `049_doomsday_no_one_dies_for_tomorrow`
4. `049_doomsday_the_calendar_was_wrong`
5. `049_doomsday_the_final_assembly`
6. `049_doomsday_no_future_no_masters`
7. `049_doomsday_prepare_for_everything`
8. `049_doomsday_the_state_outlived_the_prophecy`
9. `049_doomsday_still_waiting`
10. `049_doomsday_every_bell_at_midnight`

Achievement files remain directly under `gfx/achievements/` according to the root-only exception. Filenames must match final achievement IDs.

Use the canonical achievement reference family and its overlay workflow. Do not treat a simple grayscale conversion as the complete not-eligible state unless the existing project workflow specifically requires it.

## Source mode

Use generated period-authentic art for fictional event scenes and symbolic icons.

Use `chaosx_generated_event_art` for report, news, super-event, category-picture, and emblem scenes that are fictional or symbolic.

Use `chaosx_icon_artist` for decision, category, idea, focus, emblem-small-consumer, and achievement icons.

Use `chaosx_portrait_creator` for all institutional portraits and any grounded portrait work.

Use `chaosx_asset_source_researcher` only when a final asset must depict real historical material or use an attested symbol.

## Transparency

Request genuine native transparency in the first ImageGen call for every alpha-backed icon, emblem, overlay, and portrait layer whose consumer uses transparent unused canvas.

Preserve alpha through processing and DDS conversion.

Validate unused corners, silhouette edges, internal opacity, and absence of white matte, halo, checkerboard, or opaque square background.

Background removal is fallback-only after native transparency fails or when an inherited source begins opaque. Preserve the original and document the fallback.

## Final placement

Use event-scoped runtime folders where the consumer accepts explicit paths:

- `gfx/event_pictures/049_doomsday/`
- `gfx/super_events/049_doomsday/`
- `gfx/interface/decisions/049_doomsday/`
- `gfx/interface/ideas/049_doomsday/`
- `gfx/interface/goals/049_doomsday/`
- an inspected event-owned interface folder for the Final Assembly emblem
- the correct inspected portrait path for institutional councils
- `gfx/achievements/` for achievement triplets

Confirm every path against the active consumer and project convention before final placement.

## Working evidence and cleanup

Use `docs/assets/049_doomsday/` as the temporary evidence workspace while production is active.

Preserve:

- Source PNGs.
- Prompts and source-mode notes.
- Processed previews.
- DDS files before runtime copy.
- Contact sheets.
- Provenance and licensing.
- Dimension and alpha checks.
- Manifest rows.
- GFX handoff notes.
- Portrait-specific evidence under the durable portrait archive where required.

Before the Event 049 goal is declared complete:

- Move final runtime assets into engine-facing folders.
- Verify no runtime reference points into `docs/assets/`.
- Promote durable provenance, coverage, and review facts into permanent event or super-event documentation.
- Delete the completed temporary event workspace.
- Retain the workspace when any asset remains blocked or awaiting review.

## Handoff

Return a handoff that lists:

- Every required asset and status.
- Source mode and producer.
- Source and final paths.
- Native dimensions and final dimensions.
- Sprite names or proposed stable names.
- Alpha and edge verdict.
- Contact sheets.
- Source and final checksums.
- Grounded portrait provenance where applicable.
- Assets blocked or awaiting parent lock.
- Files the parent must wire.
- Any asset that was merged or removed because implementation changed the consumer list.

Do not claim the event asset package complete while any required visible asset is placeholder, missing, unwired, unreviewed, or undocumented.

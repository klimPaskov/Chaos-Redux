# Event 032 Missiles icon artist handoff

Disposition: implemented for all authorized icon families and superseded by the parent wiring pass. The exact conventional/saturation raid-consumer blocker remains intentionally unresolved because no matching installed runtime entity exists; it is tracked in `docs/events/032_missiles/asset_audit.md`.

Status: complete for the authorized transparent icon package, with parent-owned runtime wiring and two explicit review items.

## Ownership and changed surfaces

This worker produced only asset evidence under `docs/assets/032_missiles/icon_artist/` and this handoff. It did not edit gameplay, localisation, interface, GFX definitions, decisions, missions, events, achievements, spreadsheets, or the existing parent-owned Event 032 full-canvas art.

The parent owns copying approved DDS files into engine-facing `gfx/` folders, registering sprite aliases, selecting the final category-button alias, mapping mission families to runtime decisions, and validating the consumers in-game.

## Completed package

The sidecar contains the following complete static evidence packages.

- One 52×40 transparent category button icon.
- Three 60×68 transparent program-idea variants.
- Five 32×32 transparent launch-site modifier icons using the existing sprite names.
- Three 24×24 transparent texticons following the installed Event 031 texticon precedent.
- Twenty-seven 33×32 transparent requested decision icons.
- Seven 33×32 transparent mission-family icons.
- Five 32×32 guidance-state icons and four 32×32 retaliation-posture icons retained from the pre-existing Event 032 source batch and processed as supplemental visible state evidence.
- Eight achievement triplets, each with completed, grey, and not-eligible 64×64 DDS outputs.

The four strike-preparation mission consumers share `mission_032_missiles_strike_preparation.dds`: precision strike, strategic barrage, saturation barrage, and counterforce strike preparation. This is the seven-family mapping defined by the asset prompt.

The category button evidence is `dds/decision_category/032_missiles_program_category_icon.dds` and the current category consumer is `GFX_decision_category_032_missiles`. The separate full-canvas category picture and its `GFX_decision_cat_picture_032_missiles` consumer remain parent-owned and untouched.

The current launch-site modifier consumers use the existing `GFX_idea_032_missiles_launch_site_*` names, including the `GFX_idea_` prefix. Those names were preserved exactly.

The eight exact achievement IDs are `chaos_redux_032_exact_distance`, `chaos_redux_032_still_on_the_line`, `chaos_redux_032_break_the_chain`, `chaos_redux_032_keys_returned`, `chaos_redux_032_no_second_sun`, `chaos_redux_032_empty_the_silos`, `chaos_redux_032_sky_full_of_steel`, and `chaos_redux_032_long_reach`.

## Source provenance

The three retaliation-network decision gaps, the category button, seven mission-family sources, and twenty-four achievement state sources were generated with the official ImageGen skill using genuine transparent-background prompts.

The other twenty-four decision sources, three ideas, five state modifiers, three texticons, five guidance states, and four posture states were already present under `docs/assets/032_missiles/icons/source_png/`. They were copied byte-for-byte into this worker workspace and independently alpha-audited before processing. Their predecessor prompt records were not present, so the prompt ledger records them as `retained_native_alpha_imagegen_batch` rather than claiming new generation provenance.

One initial `long_reach_grey` generation was fully transparent and was rejected. A replacement was generated, inspected, and used for the final triplet. The rejected source was not copied into the package.

## Reference evidence

The matching canonical contact sheets were inspected before individual references under `.agents/skills/chaos-redux-event-assets/assets/vanilla_reference/icons/`. The inspected families were decision categories, ideas, decisions, missions, achievements, state modifiers, modifiers, and military raids.

The visual review sheets are `docs/assets/032_missiles/icon_artist/review/preexisting_source_contact_sheet.png`, `achievement_source_contact_sheet.png`, `processed_decisions_contact_sheet.png`, `processed_missions_contact_sheet.png`, and `achievement_final_contact_sheet.png`.

The full prompt and ImageGen output ledger is `docs/assets/032_missiles/icon_artist/prompts/032_missiles_icon_prompt_set.md`.

The complete asset inventory, target dimensions, sprite proposals, runtime copy roots, and blocker notes are `docs/assets/032_missiles/icon_artist/manifest.md`.

The copy/register mapping is `docs/assets/032_missiles/icon_artist/gfx_handoff.md`.

## Validation evidence

All processed non-achievement PNGs have exact target dimensions and alpha extrema 0–255. All 27 decision DDS files decode as 33×32. All seven mission DDS files decode as 33×32. The category DDS decodes as 52×40. Ideas decode as 60×68. State modifiers, guidance, and postures decode as 32×32. Texticons decode as 24×24.

The eight achievement triplets were written with `process_achievement_icons.py` and each passed its strict audit for 64×64 BGRA structure and source-layer equality. The canonical achievement plaque makes decoded alpha 254–255, which matches the opaque achievement reference family.

No animation, transform-only fake motion, recolour-only state variant, portrait, flag, focus art, 3D model, GUI art, or primitive-drawn substitute was used.

## Blockers and parent review

The category-button prompt contained an illustrative alias `GFX_decision_category_icon_032_missiles_program`, while the installed category consumer uses `GFX_decision_category_032_missiles`. The handoff preserves the installed consumer name and leaves the alias decision to the parent.

No conventional or saturation operation icon was generated or reused. The installed raid namespace contains chemical and biological raid subjects but no exact Event 032 missile-delivery adapter or consumer. An unrelated CBRN or nuclear raid icon would violate the exact consumer-and-subject reuse rule. The operation-icon surface is blocked pending parent confirmation that a real consumer exists.

Guidance and posture assets are complete art evidence, but their exact parent consumers and sprite names were not present in the prompt or current GFX registry. They remain parent-review items for naming and wiring.

No other simplification or omission was made within the authorized icon package.

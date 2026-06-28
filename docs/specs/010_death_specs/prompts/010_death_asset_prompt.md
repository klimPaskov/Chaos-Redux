# Asset Prompt: Event 010 Death

Create the final visual asset package for Event 010 `Death` according to the specs in `docs/specs/010_death_specs/specs/`.

Follow `chaos-redux-event-assets` and `chaos-redux-frame-animation`. Inspect the relevant reference folders before creating assets:

- ideas: `.agents/skills/chaos-redux-event-assets/assets/ideas`
- decisions: `.agents/skills/chaos-redux-event-assets/assets/decisions`
- focuses: `.agents/skills/chaos-redux-event-assets/assets/focuses`
- achievements: `.agents/skills/chaos-redux-event-assets/assets/achievements`
- report images: `.agents/skills/chaos-redux-event-assets/assets/report_event_images`
- news images: `.agents/skills/chaos-redux-event-assets/assets/news_event_images`
- super-event images: `.agents/skills/chaos-redux-event-assets/assets/super_event_images`
- flags: `.agents/skills/chaos-redux-event-assets/assets/flags`

Use generated art for fictional, symbolic, supernatural, and alternate-history assets. Do not use real historical leader sourcing for Zol because Zol is fictional/nonhuman. Do not use a generated portrait for any real person if future implementation adds real advisers.

## Required country assets

1. `DTH` flag set: normal 82x52, medium 41x26, small 10x7. Fictional near-black/void flag, no text. Map color remains complete black.
2. `leader_zol`: 156x210 generated nonhuman HOI4-style portrait, static fallback.
3. `leader_zol_world_end_animated`: optional animated portrait package with real generated source frames, static fallback, frame sheet DDS, preview GIF for review only. Use only if animation quality is strong.
4. Optional route flags if Herald/Black Apostolate route is implemented: `herald_of_zol` and `black_apostolate` normal/medium/small flags.

## Required report/news images

- `report_event_death_mail_boat`, 210x176 report-card treatment, generated period-documentary empty pier/mail boat.
- `report_event_death_lighthouse`, 210x176 report-card treatment, generated period-documentary lighthouse/empty island settlement.
- `report_event_death_census`, 210x176 report-card treatment, generated period-documentary census office with blank papers and no readable text.
- `news_event_death_mainland_reveal`, 397x153 black-and-white generated period-news image of emptied mainland coastal state.
- `news_event_death_defeated`, 397x153 black-and-white generated period-news image of troops/surveyors entering empty wasteland.

## Required super-event images

- `super_event_death_reveal`, 457x328, generated: black coastline, empty mainland settlement, official observers dwarfed by absence.
- `super_event_death_world_end`, 457x328, generated: black tide/shoreline world-end image.
- `super_event_death_defeat_aftermath`, 457x328, generated: soldiers or surveyors in dead land, victory without restoration.
- `super_event_death_world_consumed`, 457x328, generated: ruined coastal capital consumed by a vast black tide, dramatic exterior end-state, no office, no map table, no readable text.
- Optional `super_event_death_black_oath`, 457x328, generated if Herald route implemented.

## Required icons

Create each icon type as its own asset. Do not resize focus icons into ideas or decisions.

Ideas/national spirits 64x64:

- `idea_country_without_breath`
- `idea_first_silence`
- `idea_public_death`
- `idea_last_shores`
- `idea_black_census`
- optional `idea_black_oath`
- optional `idea_black_book_offices`

Decision category/icons:

- `decision_category_death_country`
- `decision_death_survey_boat`
- `decision_death_coastal_watch`
- `decision_death_quarantine_line`
- `decision_death_wasteland_gear`
- `decision_death_black_book`
- `decision_death_black_oath`
- `decision_death_living_compact`
- `decision_death_dead_zone_outpost`

Focus icons 94x86:

- Shroud lane motifs: empty mail, weather record, island pattern.
- Hunger lane motifs: low names, silent ports, mainland smell.
- Census lane motifs: black census, no graves, ghost muster.
- Wasteland lane motifs: roads slow, empty supply, state without state.
- Host lane motifs: mourning host, ruin host, orders without breath.
- World-end and whole-world-consumed motifs. Do not infer final super-event titles from asset filenames.

Achievement icons 64x64:

Create completed achievement icons for every achievement in `010_death_achievement_prompt.md`. Grey and not-eligible variants can be generated/processed later if the achievement system requires them.

## Custom UI/animation assets

If the Black Atlas scripted GUI is implemented, create:

- `death_black_atlas_background` static panel.
- `death_black_atlas_header_animated` plus static fallback. Slow dark fog/shroud frames.
- `death_coastal_risk_pulse_animated` plus static fallback.
- `death_wither_target_frame_animated` plus static fallback.
- `death_compact_warning_animated` plus static fallback.

For each animated asset, write an animation brief and frame plan, use real generated source frames, build a horizontal frame sheet, convert to DDS, and include manifest/gfx handoff. Do not create final animation by moving, scaling, filtering, recoloring, or pulsing one still image.

## Output package

Write the asset manifest to `docs/assets/010_death/manifest.md` and gfx handoff to `docs/assets/010_death/gfx_handoff.md`. Final DDS/TGA files must be placed in the correct mod asset folders, not left only under docs. Every asset should be `complete`, `blocked`, or `needs_user_review` with source mode, prompt/source notes, target size, final path, sprite name, and related gameplay use.

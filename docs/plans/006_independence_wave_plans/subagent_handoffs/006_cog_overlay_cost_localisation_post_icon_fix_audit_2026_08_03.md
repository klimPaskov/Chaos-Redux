# Event 006 COG overlay cost localisation post-icon-fix audit

Date: 2026-08-03.

Scope: parent-owned source audit of the two Event 006 overlay localisation families after commit `a6f123a86` normalized the equipment text-icon tokens. The obsolete pasted flag log was excluded.

## Verdict

**PASS for the requested post-fix surface.** Both COG overlay cost families retain centralized constant references, UTF-8 BOM encoding, unique keys, and canonical installed equipment icon tokens. No gameplay cost, decision availability, route, advisor icon, or runtime claim changed.

## Audited files

- `localisation/english/006_independence_wave_iw101_iw102_iw105_cog_overlays_l_english.yml`
- `localisation/english/006_independence_wave_iw156_iw196_iw197_iw204_overlays_l_english.yml`

## Checks

- Both files begin with the UTF-8 BOM and parse as `l_english` localisation.
- The COG family contains 90 unique parsed keys and the sibling reusable-region family contains 116 unique parsed keys, with no duplicate key in either file.
- The twelve COG base, blocked, and tooltip strings continue to use `constant:independence_wave_iw_cog_overlay_cost` fields, and the sibling family continues to use `constant:independence_wave_iw_region_overlay_cost` fields.
- No bare `£train_equipment`, `£support_equipment`, or `£infantry_equipment` token remains on these surfaces; installed canonical references are `£GFX_train_texticon`, `£support_equipment_text_icon`, and `£infantry_equipment_text_icon`.
- No `cog_cog` key or token is present in either file.
- The earlier re-audit's bare-token observation is superseded for current routing by this post-fix audit; its dated findings remain historical evidence only.

## Boundaries

This audit does not promote any COG overlay identity to a full country package, add a guard-mission cost family, create or wire advisor icons, or claim live UI, save/load, or runtime localisation evidence.

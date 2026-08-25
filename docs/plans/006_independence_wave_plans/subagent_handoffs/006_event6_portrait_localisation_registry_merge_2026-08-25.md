# Event 006 portrait localisation registry merge — 2026-08-25

## Scope

This source-only consolidation removes two tiny package-specific localisation files whose keys belong to the existing Montenegro and Kosovo package registries. It does not rename a localisation key, change a character, alter a portrait consumer, or change gameplay.

## Consolidated files

- `localisation/english/006_independence_wave_montenegro_portraits_l_english.yml` was folded into `localisation/english/006_independence_wave_montenegro_l_english.yml`.
- `localisation/english/006_independence_wave_kosovo_portraits_l_english.yml` was folded into `localisation/english/006_independence_wave_kosovo_l_english.yml`.
- The two portrait-only source files were then removed.

The preserved keys are `MNT_independence_wave_mitar_martinovic` and its description, plus `KOS_independence_wave_ferhat_draga`, `KOS_independence_wave_miladin_popovic`, and `KOS_independence_wave_shaban_polluzha` with their descriptions. All character identifiers and player-facing text are byte-for-byte unchanged.

## Validation

- Confirmed each preserved key occurs exactly once in its package localisation file.
- Confirmed both receiving localisation files retain their UTF-8 BOM.
- Confirmed no current source or package documentation reference points to either removed filename; historical handoffs retain their original provenance references.
- Confirmed the portrait `.gfx`, character, country, event, decision, and focus files were not changed.

## Boundary

This reduces file count only. It does not promote any country package, change portrait provenance, add an advisor or dossier portrait, restore any pre-event Independence Wave category, or claim live localisation rendering.

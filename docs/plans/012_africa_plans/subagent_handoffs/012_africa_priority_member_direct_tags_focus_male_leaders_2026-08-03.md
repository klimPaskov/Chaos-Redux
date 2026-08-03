# Event 012 direct-tag, focus-loading, and male sovereign handoff

Scope: patch the existing Event 012 Africa priority-member package so the seven niche identities work directly on their registered country tags without a live Event 006 receipt, every accepted carrier receives the Event 012 focus tree, and all sixteen sovereign character definitions use male metadata. No country tag, map state, model, or new asset was created.

## Package coverage

The package matrix remains sixteen rows: DOX/Asante, DSX/Oyo, SOK/Sokoto, DUX/Kanem-Bornu, MLI/Manden, COG/Kongo, UGA/Buganda, TIG/Aksum, HAR/Harar, EMX/Kilwa, SUD/Nubia, DYX/Luba, DZX/Lunda, ZIM/Great Zimbabwe, MAD/Merina, and EQX/Zulu. The seven niche rows are Asante, Oyo, Kanem-Bornu, Kilwa, Luba, Lunda, and Zulu; their existing carrier identities remain in place.

All sixteen sovereign characters retain their existing character ids and GFX sprite ids. `common/characters/012_africa_priority_member_characters.txt` now explicitly sets `gender = male` for every row. The Aksum, Nubia, and Merina localisations in `localisation/english/012_africa_priority_member_characters_l_english.yml` use the historical male names Ezana of Aksum, Taharqa of Kush, and Radama II of Merina.

## Changed gameplay surfaces

- `common/scripted_triggers/012_africa_priority_member_triggers.txt`: all sixteen origin and carrier predicates now use direct existing tags and Event 012 origin flags; no Independence Wave registry, Event 006 receipt, or Soviet-origin predicate is read. `africa_priority_member_portrait_runtime_is_approved` admits all sixteen because all sixteen stable source-locked runtime DDS files exist.
- `common/scripted_effects/012_africa_priority_member_effects.txt`: `africa_priority_member_record_direct_tag_origin` resolves the accepted carrier tags directly and no longer reads an Event 006 or Independence Wave receipt. `africa_priority_member_ensure_focus_tree_loaded` now clears stale bookkeeping, preserves an already-loaded Event 012 tree, or directly calls `load_focus_tree = { tree = africa_priority_member_focus_tree keep_completed = yes }`; no Event 006, Soviet, or generic-tree branch can skip the package tree.
- `common/scripted_effects/012_africa_priority_member_character_effects.txt`: updated the package contract comment so all sixteen accepted rows install their sovereign role when settlement completes; source provenance and actor review are no longer a gameplay loading gate.
- `common/characters/012_africa_priority_member_characters.txt`: explicit male metadata on all sixteen sovereign character ids.
- `localisation/english/012_africa_priority_member_characters_l_english.yml`: male Aksum, Nubia, and Merina sovereign names and descriptions replace the former female-only entries.

The historical source masters and direct-crop placeholders are retained under `docs/assets/portraits/012_africa/`, with the complete runtime map in `source_locked_runtime_mapping.md`. Artifact/map identity rows are explicitly labelled and never presented as fabricated human likenesses. Fictional external package stewards remain a separate portrait family.

## Validation

Focused static checks returned: sixteen package predicates in the portrait-admission trigger; sixteen `gender = male` character rows; zero `gender = female` rows; sixteen source-locked runtime DDS files and sixteen `.gfx` sprite references; no missing sovereign localisation keys; zero Independence Wave/Event 006 registry calls in Event 012 origin/effect code; valid source mapping; and no focus-loader skip assignment or Soviet-origin condition. The loader still clears the old `africa_priority_member_focus_tree_overlay_skipped` flag as cleanup, but never sets it.

No live HOI4 launch or consumer validation was run because the parent owns live-game testing. No map/state, politics, military, technology, industry, supply, advisor, or AI changes were required by this narrow package-loading task.

## Remaining risks and blockers

The durable source/rights crosswalk still records archival attribution and permission notes for individual rows. The current runtime choice is deliberately a direct source placeholder, as requested, so no generated face or unsupported regalia is introduced. The all-sixteen runtime admission is therefore backed by an actual source-locked DDS path for every identity while deeper rights review remains documented rather than silently substituted.

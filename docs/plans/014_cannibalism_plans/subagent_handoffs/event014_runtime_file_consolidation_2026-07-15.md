# Event 014 runtime file consolidation handoff

Date: 2026-07-15

Status: implemented; final cross-surface audits remain responsible for confirming the consolidated loaders after the visual refresh.

## Result

Event 014 dedicated runtime files were reduced from 93 tracked files to 23 current files. Seventy loader files were eliminated without renaming gameplay identifiers, localisation keys, sprite names, event IDs, focus IDs, decision IDs, effects, triggers, constants, traits, ideas, or modifiers.

The consolidation keeps one Event 014 file per merge-safe loader folder. Section comments preserve the former source-file boundaries and order inside each merged file.

## Consolidated loader files

| Loader family | Current file | Former dedicated files folded into it |
| --- | --- | ---: |
| Leader traits | `common/country_leader/014_cannibalism_traits.txt` | 2 |
| Decisions | `common/decisions/014_cannibalism_decisions.txt` | 8 |
| Decision categories | `common/decisions/categories/014_cannibalism_categories.txt` | 2 |
| Dynamic modifiers | `common/dynamic_modifiers/014_cannibalism_dynamic_modifiers.txt` | 4 |
| Ideas | `common/ideas/014_cannibalism_ideas.txt` | 2 |
| National focuses | `common/national_focus/014_cannibalism_focus.txt` | 3 tree files; all three `focus_tree` roots retained |
| Script constants | `common/script_constants/014_cannibalism_constants.txt` | 14 |
| Scripted effects | `common/scripted_effects/014_cannibalism_effects.txt` | 20 |
| Scripted localisation | `common/scripted_localisation/014_cannibalism_scripted_localisation.txt` | 2 |
| Scripted triggers | `common/scripted_triggers/014_cannibalism_triggers.txt` | 14 |
| Events | `events/014_cannibalism.txt` | 2 event files; one namespace retained |
| Sprite registration | `interface/014_cannibalism.gfx` | 7 GFX files; one `spriteTypes` root retained |
| English localisation | `localisation/english/014_cannibalism_l_english.yml` | 3 UTF-8 BOM files |

The ten already-singleton loader files remain separate because they belong to different HOI4 loader folders or file grammars: AI strategy, characters, country tags, MTTH, on actions, opinion modifiers, country scorers, scripted GUI logic, dormant unit history, and the `.gui` layout.

## Structural evidence

- Current dedicated runtime count: 23.
- Removed dedicated runtime count: 70.
- The consolidated focus file retains three `focus_tree` roots.
- The consolidated GFX file retains one `spriteTypes` root.
- The consolidated idea and leader-trait files each retain one required wrapper root.
- The consolidated event file retains one `add_namespace = chaosx.nr14` declaration.
- The consolidated localisation file retains its UTF-8 BOM.
- Every consolidated file has balanced braces at the file level.

## Asset-source boundary

Animation source frames, processed frames, sheets, static fallbacks, preview GIFs, contact sheets, and manifests remain separate assets. They are not redundant runtime loader fragments: the Event 014 animation contract requires genuine source-frame evidence and exact frame handoff. Runtime sprite declarations for those assets are consolidated in `interface/014_cannibalism.gfx`.

No gameplay or presentation fallback was introduced by this consolidation.
